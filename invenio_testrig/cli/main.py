"""Main CLI command group for invenio-testrig."""

import functools
import json
import logging
import re
import subprocess
import tempfile
from collections.abc import Callable
from pathlib import Path
from typing import Any, cast

import click
import yaml

from invenio_testrig.config import ConfigDict, ConfigSchema, load_config, save_config
from invenio_testrig.git_api import git_api
from invenio_testrig.hooks import run_hook
from invenio_testrig.patchers import patchers_by_mode
from invenio_testrig.python_api import PythonAPI


def with_debug(func: Callable[..., Any]) -> Callable[..., Any]:
    """Decorator that adds debug option and handles exceptions."""

    @click.option("--debug", is_flag=True, help="Enable debug mode with full traceback")
    @functools.wraps(func)
    def wrapper(*args: Any, debug: bool = False, **kwargs: Any) -> Any:
        try:
            return func(*args, **kwargs)
        except Exception as e:
            if debug:
                raise
            click.secho(f"❌ Error: {e}", fg="red", bold=True, err=True)
            raise click.Abort()

    return wrapper


def with_verbose(func: Callable[..., Any]) -> Callable[..., Any]:
    """Decorator that adds verbose option and configures logging."""

    @click.option("--verbose", is_flag=True, help="Enable verbose output")
    @functools.wraps(func)
    def wrapper(*args: Any, verbose: bool = False, **kwargs: Any) -> Any:
        if verbose:
            logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
        return func(*args, **kwargs)

    return wrapper


@click.group()
def cli():
    """Workflow commands for testing invenio packages."""
    pass


@cli.command("init")
@click.argument(
    "config_yaml_path", type=click.Path(exists=True, path_type=Path, resolve_path=True)
)
@click.argument("config_json_path", type=click.Path(path_type=Path, resolve_path=True))
@with_verbose
@with_debug
def init(config_yaml_path: Path, config_json_path: Path):
    """1/ Initialize workflow by preparing configuration.

    Resolves all git references in the YAML configuration and outputs JSON.

    Example: invenio-testrig init config.yaml config.json
    """
    # Read the yaml config file
    with open(config_yaml_path, "r") as f:
        config_data = yaml.safe_load(f)
        config_dict = cast(ConfigDict, ConfigSchema().load(config_data))

    # Resolve all git references
    resolve_config(config_dict)

    # Write the resolved config to the output file
    save_config(config_json_path, config_dict)
    click.secho(
        f"✅ Configuration prepared and written to {config_json_path}",
        fg="green",
        bold=True,
    )

    # Run after-config-preprocessing hook if it exists
    config_dict = run_hook(
        config_dict,
        config_json_path,
        "after-config-preprocessing",
        env={"CONFIG_PATH": str(config_json_path)},
    )


@cli.command("collect")
@click.argument(
    "config_json_path", type=click.Path(exists=True, path_type=Path, resolve_path=True)
)
@click.option(
    "--uv",
    "uv_executable",
    default="uv",
    help="Path to uv executable",
)
@click.option(
    "--python",
    "python_version",
    default="python3",
    help="Python version to use",
)
@with_verbose
@with_debug
def collect(config_json_path: Path, uv_executable: str, python_version: str):
    """2/ Collect dependencies/libraries for the repository.

    Clones the repository, installs it (if uv.lock is not found),
    and collects dependencies. Updates the config JSON with a "packages" key
    containing all detected dependencies and their versions.

    Example: invenio-testrig collect config.json
    """
    # Read the config JSON
    config_dict = load_config(config_json_path)

    git_ref = config_dict["repository"]["git"]

    # Clone the repository to a temporary directory
    with tempfile.TemporaryDirectory() as tmpdir:
        repo_path = Path(tmpdir) / "repo"
        click.secho("🔄 Cloning invenio repository...", fg="cyan")
        git_api.clone_git_reference(git_ref, repo_path)

        config_dict = run_hook(
            config_dict,
            config_json_path,
            "after_invenio_repo_clone",
            env={
                "INVENIO_REPOSITORY_PATH": str(repo_path),
                "CONFIG_PATH": str(config_json_path),
            },
            cwd=repo_path,
        )
        # Install and get dependencies
        click.secho(
            "📦 Collecting dependencies (might take a while as the repository might be installed)...",
            fg="cyan",
        )
        python_api = PythonAPI(uv_executable, python_version)
        dependencies = python_api.get_dependencies(repo_path)

    # Add dependencies to the config
    config_dict["packages"] = dependencies

    # Write back to the JSON file
    save_config(config_json_path, config_dict)

    config_dict = run_hook(
        config_dict,
        config_json_path,
        "after_dependencies_collected",
        env={"CONFIG_PATH": str(config_json_path)},
    )
    click.secho(
        f"✅ Collected {len(dependencies)} dependencies and updated {config_json_path}",
        fg="green",
        bold=True,
    )


@cli.command("filter")
@click.argument(
    "config_json_path", type=click.Path(exists=True, path_type=Path, resolve_path=True)
)
@with_verbose
@with_debug
def filter_cmd(config_json_path: Path):
    """3/ Filter dependencies based on GitHub include/exclude patterns.

    Reads packages and filters entries based on github.include and
    github.exclude patterns inside the config file. Creates a new
    "tested_packages" key with matching entries.

    Example: invenio-testrig filter config.json
    """
    # Read the config JSON
    config_dict = load_config(config_json_path)

    config_dict = run_hook(
        config_dict,
        config_json_path,
        "before_filtering_packages",
        env={"CONFIG_PATH": str(config_json_path)},
    )

    # Check if packages exists
    if "packages" not in config_dict:
        click.secho("❌ Error: No packages in config", fg="red", bold=True, err=True)
        raise click.Abort()

    packages_map = config_dict["packages"]
    github_configs = config_dict["github"]

    # Filter dependencies based on github patterns
    tested_packages: dict[str, dict[str, str | list[str]]] = {}

    for package_name, version in packages_map.items():
        # Check each github config entry
        for github_entry in github_configs:
            include_patterns = github_entry.get("include", [])
            exclude_patterns = github_entry.get("exclude", [])
            branch = github_entry.get("branch", "")
            test_command = github_entry.get("test", [])
            extras = github_entry.get("extras", [])

            # Check if package matches any include pattern
            included = False
            for pattern in include_patterns:
                if re.match(pattern, package_name, re.IGNORECASE):
                    included = True
                    break

            if not included:
                continue

            # Check if package matches any exclude pattern
            excluded = False
            for pattern in exclude_patterns:
                if re.match(pattern, package_name, re.IGNORECASE):
                    excluded = True
                    break

            if excluded:
                continue

            # Package matches this github config
            tested_packages[package_name] = {
                "version": version,
                "repo-branch": branch if branch else "",
                "org": github_entry.get("org", ""),
                "repo": package_name,
                "test": test_command,
                "extras": extras,
            }
            break  # Stop checking other github configs once matched

    # Add tested packages to the config
    config_dict["tested_packages"] = tested_packages

    # Write back to the JSON file
    save_config(config_json_path, config_dict)

    config_dict = run_hook(
        config_dict,
        config_json_path,
        "after_filtering_packages",
        env={"CONFIG_PATH": str(config_json_path)},
    )

    click.secho(
        f"✅ Filtered {len(tested_packages)} packages from {len(packages_map)} "
        f"total dependencies and updated {config_json_path}",
        fg="green",
        bold=True,
    )


@cli.command("matrix")
@click.argument(
    "config_json_path", type=click.Path(exists=True, path_type=Path, resolve_path=True)
)
@click.argument(
    "github_output_file", type=click.Path(path_type=Path, resolve_path=True)
)
def matrix_cmd(config_json_path: Path, github_output_file: Path):
    config = load_config(config_json_path)
    tested_packages = config.get("tested_packages", {})
    matrix = [package for package in tested_packages.keys()]
    with open(github_output_file, "a") as f:
        f.write("\n")
        f.write(f"matrix_tested_packages={json.dumps(matrix)}\n")
    click.secho(
        f"✅ Generated test matrix for {len(tested_packages)} packages and "
        f"written to {github_output_file}",
        fg="green",
        bold=True,
    )


@cli.command("clone")
@click.argument(
    "config_json_path", type=click.Path(exists=True, path_type=Path, resolve_path=True)
)
@click.argument("clone_path", type=click.Path(path_type=Path, resolve_path=True))
@with_verbose
@with_debug
def clone_cmd(config_json_path: Path, clone_path: Path):
    """4/ Clone packages from configuration.

    Clone repository.git and repository.e2e (if configured) to the output directory.
    Then clone all packages specified in "tested_packages" into the packages/ subdirectory.
    If a package has patches, also clone it into the patched/ subdirectory and apply patches.
    The patching behavior depends on the mode specified in the config (as-is, upstream, or custom).

    Layout of the output directory:
        clone_path/
        ├── repo/                # Cloned repository.git
        ├── invenio-e2e/         # Cloned repository.e2e (if configured)
        ├── packages/            # Cloned dependencies without patches
        |     └── package_name/     # Cloned dependency repository with pinned version
        └── patched/             # Cloned dependencies with patches applied
              └── package_name/     # Cloned dependency repository with patches applied

    The command fails if the clone_path already exists to prevent accidental overwriting.

    Example: invenio-testrig clone config.json ./repos
    """
    # Check if output directory exists
    if clone_path.exists():
        click.secho(
            f"❌ Error: Output directory {clone_path} already exists",
            fg="red",
            bold=True,
            err=True,
        )
        raise click.Abort()

    # Read the config JSON
    config_dict = load_config(config_json_path)
    config_dict = run_hook(
        config_dict,
        config_json_path,
        "before_cloning_packages",
        env={"CONFIG_PATH": str(config_json_path), "CLONE_PATH": str(clone_path)},
    )

    # Create output directory
    clone_path.mkdir(parents=True, exist_ok=False)

    # Clone repository.git
    repo_git = config_dict["repository"]["git"]
    repo_dir = clone_path / "repo"
    click.secho(
        f"🔄 Cloning {repo_git['org']}/{repo_git['repo']} to {repo_dir}", fg="cyan"
    )
    git_api.clone_git_reference(repo_git, repo_dir)

    config_dict = run_hook(
        config_dict,
        config_json_path,
        "after_cloning_repository",
        env={
            "CONFIG_PATH": str(config_json_path),
            "REPOSITORY_PATH": str(repo_dir),
            "CLONE_PATH": str(clone_path),
        },
        cwd=repo_dir,
    )

    # Clone repository.e2e if it exists
    if "e2e" in config_dict["repository"] and config_dict["repository"]["e2e"]:
        e2e_ref = config_dict["repository"]["e2e"]
        e2e_dir = clone_path / "invenio-e2e"
        click.secho(
            f"🔄 Cloning {e2e_ref['org']}/{e2e_ref['repo']} to {e2e_dir}", fg="cyan"
        )
        git_api.clone_git_reference(e2e_ref, e2e_dir)

        config_dict = run_hook(
            config_dict,
            config_json_path,
            "after_cloning_e2e_repository",
            env={
                "CONFIG_PATH": str(config_json_path),
                "E2E_REPOSITORY_PATH": str(e2e_dir),
                "CLONE_PATH": str(clone_path),
            },
            cwd=e2e_dir,
        )

    # Clone dependencies using appropriate patcher mode
    tested_packages = config_dict.get("tested_packages", {})
    mode = config_dict.get("mode", "as-is")
    patcher_cls = patchers_by_mode.get(mode)

    if patcher_cls is None:
        click.secho(
            f"❌ Error: Unsupported mode '{mode}'", fg="red", bold=True, err=True
        )
        raise click.Abort()

    if tested_packages:
        packages_dir = clone_path / "packages"
        packages_dir.mkdir(parents=True, exist_ok=True)
        patched_packages_dir = clone_path / "patched"
        patched_packages_dir.mkdir(parents=True, exist_ok=True)

        patcher = patcher_cls(config_dict, packages_dir, patched_packages_dir)

        for package_name in tested_packages.keys():
            click.secho(
                f"📦 Cloning dependency {package_name} using '{mode}' mode",
                fg="cyan",
            )
            patcher.clone(package_name)
            config_dict = run_hook(
                config_dict,
                config_json_path,
                "after_cloning_dependency",
                env={
                    "CONFIG_PATH": str(config_json_path),
                    "CLONE_PATH": str(clone_path),
                    "PACKAGE_NAME": package_name,
                    "PACKAGE_CLONE_PATH": str(packages_dir / package_name),
                    "PATCHED_PACKAGE_CLONE_PATH": str(
                        patched_packages_dir / package_name
                    ),
                },
                cwd=clone_path,
            )

    config_dict = run_hook(
        config_dict,
        config_json_path,
        "after_cloning_packages",
        env={"CONFIG_PATH": str(config_json_path), "CLONE_PATH": str(clone_path)},
    )

    click.secho(
        f"✅ Successfully cloned repositories to {clone_path}",
        fg="green",
        bold=True,
    )


def store_status(
    status_file: Path | None,
    status: str,
    package_name: str,
    package_patches: dict[str, Any],
    library_patches: dict[str, Any],
) -> None:
    """Store test status in a JSON file.

    Args:
        status_file: Path to the status file
        status: Test status ("success" or "failed")
        package_name: Name of the tested package
        package_patches: Patch information for the package
        library_patches: Patch information for the libraries
    """
    if status_file is None:
        return
    status_data: dict[str, Any] = {
        "status": status,
        "package": package_name,
        "package_patches": package_patches,
        "library_patches": library_patches,
    }
    with open(status_file, "w") as f:
        json.dump(status_data, f, indent=2)


@cli.command("test")
@click.argument(
    "config_path", type=click.Path(exists=True, path_type=Path, resolve_path=True)
)
@click.argument(
    "clone_path", type=click.Path(exists=True, path_type=Path, resolve_path=True)
)
@click.argument("package_name")
@click.argument(
    "working_dir", type=click.Path(path_type=Path, resolve_path=True), default=None
)
@click.option(
    "--python",
    "python_version",
    required=True,
    help="Python version to use",
)
@click.option(
    "--apply-patches",
    "apply_patches",
    is_flag=True,
    help="Reinstall dependencies from local patches",
)
@click.option(
    "--log-dir",
    "log_dir",
    type=click.Path(path_type=Path, resolve_path=True),
    default=None,
    help="Path to save test output log and the status file",
)
@with_verbose
@with_debug
def test_cmd(
    config_path: Path,
    clone_path: Path,
    package_name: str,
    working_dir: Path | None,
    python_version: str,
    apply_patches: bool,
    log_dir: Path | None,
):
    """Test a package in an isolated uv environment."""
    config = load_config(config_path)

    if log_dir:
        log_dir.mkdir(parents=True, exist_ok=True)
        log_file = log_dir / f"{'patched' if apply_patches else 'original'}_log.log"
        status_file = (
            log_dir / f"{'patched' if apply_patches else 'original'}_status.json"
        )
    else:
        log_file = None
        status_file = None

    with tempfile.TemporaryDirectory() as tmpdir:

        if working_dir is None:
            working_dir = Path(tmpdir).resolve()

        if working_dir.exists():
            click.secho(
                f"❌ Error: Working directory {working_dir} already exists",
                fg="red",
                bold=True,
                err=True,
            )
            raise click.Abort()

        package_name = package_name.lower()
        api = PythonAPI("uv", python_version)

        if package_name not in config.get("tested_packages", {}):
            click.secho(
                f"❌ Error: Package '{package_name}' not found in tested_packages",
                fg="red",
                bold=True,
                err=True,
            )
            raise click.Abort()

        package_config = config["tested_packages"][package_name]

        def patch_installation_progress(message: str) -> None:
            click.secho(f"📦 {message}", fg="cyan")

        click.echo(f"::group::📦 Installing package '{package_name}'")
        package_patches, library_patches = api.install_with_patches(
            repositories_root=clone_path,
            package_name=package_name,
            target_dir=working_dir,
            install_patched_dependencies=apply_patches,
            extras=package_config.get("extras", []),
            progress=patch_installation_progress,
        )

        click.secho(
            f"✅ Successfully installed package '{package_name}' in {working_dir}",
            fg="green",
            bold=True,
        )
        click.echo("::endgroup::")

        patched = bool(package_patches.get("patches")) or any(
            bool(x.get("patches")) for x in library_patches.values()
        )

        if apply_patches and not patched:
            # skip the test execution if patches were requested but not applied (e.g. no patches found)
            click.secho(
                f"⚠️  No patches applied for package '{package_name}', skipping test execution",
                fg="green",
                bold=True,
            )
            store_status(
                status_file=status_file,
                status="skipped",
                package_name=package_name,
                package_patches=package_patches,
                library_patches=library_patches,
            )
            return

        # Print a summary of the version of the package and applied patches before running the tests
        click.echo("::group::📋 Test Configuration Summary")
        click.secho("\n" + "=" * 80, fg="blue")
        click.secho("📋 Test Configuration Summary", fg="blue", bold=True)
        click.secho("=" * 80, fg="blue")

        # Print patch mode
        mode = config.get("mode", "as-is")
        click.secho(f"Patch mode: {mode}", fg="cyan")

        # Print package information
        click.secho(f"\n📦 Package: {package_name}", fg="green", bold=True)
        if package_patches:
            base_ref = package_patches.get("base", {})
            if base_ref:
                base_info = f"{base_ref.get('org', '')}/{base_ref.get('repo', '')} @ {base_ref.get('commit', '')[:8]}"
                if base_ref.get("branch"):
                    base_info += f" (branch: {base_ref.get('branch')})"
                click.secho(f"  Base: {base_info}", fg="white")

            patches = package_patches.get("patches", [])
            if patches:
                click.secho(f"  Applied patches ({len(patches)}):", fg="yellow")
                for patch in patches:
                    patch_info = f"{patch.get('org', '')}/{patch.get('repo', '')}"
                    if patch.get("pr"):
                        patch_info += f" PR#{patch.get('pr')}"
                    elif patch.get("branch"):
                        patch_info += f" branch:{patch.get('branch')}"
                    if patch.get("commit"):
                        patch_info += f" @ {patch.get('commit')[:8]}"
                    click.secho(f"    - {patch_info}", fg="white")
            else:
                click.secho("  No patches applied", fg="white", dim=True)
        else:
            click.secho(
                "  Using PyPI version (no patch info available)", fg="white", dim=True
            )

        # Print library dependencies with patches
        if library_patches:
            patched_libs = [
                lib for lib, info in library_patches.items() if info.get("patches")
            ]
            if patched_libs:
                click.secho(
                    f"\n📚 Patched dependencies ({len(patched_libs)}):",
                    fg="green",
                    bold=True,
                )
                for lib_name in patched_libs:
                    lib_info = library_patches[lib_name]
                    click.secho(f"  {lib_name}:", fg="cyan")

                    base_ref = lib_info.get("base", {})
                    if base_ref:
                        base_info = f"{base_ref.get('org', '')}/{base_ref.get('repo', '')} @ {base_ref.get('commit', '')[:8]}"
                        if base_ref.get("branch"):
                            base_info += f" (branch: {base_ref.get('branch')})"
                        click.secho(f"    Base: {base_info}", fg="white")

                    patches = lib_info.get("patches", [])
                    if patches:
                        click.secho(f"    Patches ({len(patches)}):", fg="yellow")
                        for patch in patches:
                            patch_info = (
                                f"{patch.get('org', '')}/{patch.get('repo', '')}"
                            )
                            if patch.get("pr"):
                                patch_info += f" PR#{patch.get('pr')}"
                            elif patch.get("branch"):
                                patch_info += f" branch:{patch.get('branch')}"
                            if patch.get("commit"):
                                patch_info += f" @ {patch.get('commit')[:8]}"
                            click.secho(f"      - {patch_info}", fg="white")

            # Show unpatched but locally installed libraries
            unpatched_libs = [
                lib for lib, info in library_patches.items() if not info.get("patches")
            ]
            if unpatched_libs:
                click.secho(
                    f"\n📚 Locally installed dependencies without patches ({len(unpatched_libs)}):",
                    fg="white",
                    dim=True,
                )
                for lib_name in unpatched_libs:
                    lib_info = library_patches[lib_name]
                    base_ref = lib_info.get("base", {})
                    if base_ref:
                        base_info = f"{base_ref.get('commit', '')[:8]}"
                        if base_ref.get("branch"):
                            base_info += f" (branch: {base_ref.get('branch')})"
                        click.secho(f"  {lib_name} @ {base_info}", fg="white", dim=True)

        click.secho("=" * 80 + "\n", fg="blue")
        click.echo("::endgroup::")

        # save the actual uv pip freeze into the logs if logging
        if log_dir:
            freeze_file = (
                log_dir / f"{'patched' if apply_patches else 'original'}_freeze.txt"
            )
            with open(freeze_file, "w") as f:
                subprocess.call(
                    ["uv", "run", "pip", "freeze"], cwd=working_dir, stdout=f
                )

        click.echo(f"::group::🚀 Running tests for package '{package_name}'")
        click.secho(
            f"🚀 Running tests for package '{package_name}' with command: "
            f"{package_config['test']}",
            fg="cyan",
        )

        try:
            api.run_in_venv(
                working_dir,
                package_config["test"],
                log_file,
            )
            click.secho(
                f"✅ Tests completed successfully for package '{package_name}'",
                fg="green",
                bold=True,
            )
            click.echo("::endgroup::")
            # Write status file on success
            store_status(
                status_file=status_file,
                status="success",
                package_name=package_name,
                package_patches=package_patches,
                library_patches=library_patches,
            )

        except subprocess.CalledProcessError as e:
            click.echo("::endgroup::")
            click.echo("::error::Tests failed")
            click.secho(
                f"❌ Tests failed for package '{package_name}' with exit code {e.returncode}",
                fg="red",
                bold=True,
                err=True,
            )
            click.secho(
                f"💡 Check the output log at: {log_file}",
                fg="yellow",
            )
            # Write status file on failure
            store_status(
                status_file=status_file,
                status="failed",
                package_name=package_name,
                package_patches=package_patches,
                library_patches=library_patches,
            )
            raise


def resolve_config(config: ConfigDict) -> None:
    """Resolve all git references in the configuration.

    Fills in missing information like PR details by querying the GitHub API.

    Args:
        config: The configuration dictionary to resolve
    """
    config["patches"] = [
        git_api.resolve_git(git_ref) for git_ref in config.get("patches", [])
    ]
    if "repository" in config:
        config["repository"]["git"] = git_api.resolve_git(config["repository"]["git"])
        if e2e := config["repository"].get("e2e"):
            config["repository"]["e2e"] = git_api.resolve_git(e2e)


if __name__ == "__main__":
    cli()
