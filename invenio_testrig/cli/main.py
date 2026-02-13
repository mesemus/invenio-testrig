"""Main CLI command group for invenio-testrig."""

import functools
import json
import logging
import re
import shutil
import subprocess
import tempfile
from collections.abc import Callable
from pathlib import Path
from typing import Any, cast

import click
import marshmallow as ma
import yaml

from invenio_testrig.config import (
    Config,
    ConfigSchema,
    TestedPackageInfo,
    load_config,
    save_config,
)
from invenio_testrig.github import GitReference, GitReferenceSchema, parse_reference
from invenio_testrig.github.api import git_api
from invenio_testrig.github.cache import git_cache
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
def init_cmd(config_yaml_path: Path, config_json_path: Path):
    """1/ Initialize workflow by preparing configuration.

    Resolves all git references in the YAML configuration and outputs JSON.

    Example: invenio-testrig init config.yaml config.json
    """
    # Read the yaml config file
    schema = GitReferenceSchema()
    with open(config_yaml_path, "r") as f:
        config_data = yaml.safe_load(f)
        # resolve all references before loading
        config_data["patches"] = [
            schema.dump(parse_reference(x)) for x in (config_data.get("patches") or [])
        ]
        repository = config_data.get("repository", {})
        if "git" in repository and repository["git"]:
            repository["git"] = schema.dump(parse_reference(repository["git"]))
        if "e2e" in repository and repository["e2e"]:
            repository["e2e"] = schema.dump(parse_reference(repository["e2e"]))
        config_data["hooks"] = config_data.get("hooks", {}) or {}

        config = cast(Config, ConfigSchema().load(config_data, unknown=ma.INCLUDE))

    # Write the resolved config to the output file
    save_config(config_json_path, config)
    click.secho(
        f"✅ Configuration prepared and written to {config_json_path}",
        fg="green",
        bold=True,
    )

    # Run after-config-preprocessing hook if it exists
    config = run_hook(
        config,
        config_json_path,
        "after_config_preprocessing",
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
def collect_cmd(config_json_path: Path, uv_executable: str, python_version: str):
    """2/ Collect dependencies/libraries for the repository.

    Clones the repository, installs it (if uv.lock is not found),
    and collects dependencies. Updates the config JSON with a "packages" key
    containing all detected dependencies and their versions.

    Example: invenio-testrig collect config.json
    """
    # Read the config JSON
    config = load_config(config_json_path)

    git_ref = config.repository.git

    # Clone the repository to a temporary directory
    with tempfile.TemporaryDirectory() as tmpdir:
        repo_path = Path(tmpdir) / "repo"
        click.secho("🔄 Cloning invenio repository...", fg="cyan")
        git_api.clone_git_reference(git_ref, repo_path)

        config = run_hook(
            config,
            config_json_path,
            "after_invenio_repo_clone",
            repository_path=repo_path,
        )
        # Install and get dependencies
        click.secho(
            "📦 Collecting dependencies (might take a while as the repository might be installed)...",
            fg="cyan",
        )
        python_api = PythonAPI(uv_executable, python_version)
        dependencies = python_api.get_dependencies(repo_path)

    # Add dependencies to the config
    config.packages = dependencies

    # Write back to the JSON file
    save_config(config_json_path, config)

    config = run_hook(
        config,
        config_json_path,
        "after_dependencies_collected",
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
    "tested_packages" key with matching entries. For each matched package,
    get the branch name and potential commit.

    The version might be:
    - semver version (e.g. 1.2.3). The branch name is v<version> (e.g. v1.2.3)
    - full github url (e.g.https://github.com/inveniosoftware/invenio-swh?rev=v0.13.4#<hash> or https://github.com/inveniosoftware/invenio-records-resources?branch=fix-read-many#<hash>)

    Example: invenio-testrig filter config.json
    """
    # Read the config JSON
    config = load_config(config_json_path)

    config = run_hook(
        config,
        config_json_path,
        "before_filtering_packages",
    )

    # Check if packages exists
    if not config.packages:
        click.secho("❌ Error: No packages in config", fg="red", bold=True, err=True)
        raise click.Abort()

    packages_map = config.packages

    # Filter dependencies based on github patterns
    tested_packages: dict[str, TestedPackageInfo] = {}

    for package_name, version in packages_map.items():
        # Check each github config entry
        github_entry = find_git_repository_config(config, package_name)
        if not github_entry:
            continue
        click.secho(
            f"🔍 Adding package {package_name} to a set of tested packages ...",
            fg="cyan",
        )

        if version.startswith("https://"):
            # If the version is a full github url, parse it to get the branch and potential commit
            reference = parse_reference(version)
        else:
            reference = GitReference(
                org=github_entry.org or "",
                repo=package_name,
                package=package_name,
                branch=f"v{version}",
            )
        reference = git_api.resolve_reference(reference)

        # Package matches this github config
        tested_packages[package_name] = TestedPackageInfo(
            reference=reference,
            test=github_entry.test,
            extras=github_entry.extras or [],
            freeze=github_entry.freeze or [],
        )

    # Add tested packages to the config
    config.tested_packages = tested_packages

    # Write back to the JSON file
    save_config(config_json_path, config)

    config = run_hook(
        config,
        config_json_path,
        "after_filtering_packages",
    )

    click.secho(
        f"✅ Filtered {len(tested_packages)} packages from {len(packages_map)} "
        f"total dependencies and updated {config_json_path}",
        fg="green",
        bold=True,
    )


def find_git_repository_config(config: Config, package_name: str):
    for github_entry in config.github or []:
        exclude_patterns = github_entry.exclude or []

        # Check if package matches any include pattern
        for pattern in github_entry.include or []:
            if re.match(pattern, package_name, re.IGNORECASE):
                break
        else:
            return None

        # Check if package matches any exclude pattern
        if any(
            re.match(pattern, package_name, re.IGNORECASE)
            for pattern in exclude_patterns
        ):
            continue
        return github_entry


@cli.command("matrix")
@click.argument(
    "config_json_path", type=click.Path(exists=True, path_type=Path, resolve_path=True)
)
@click.argument(
    "github_output_file", type=click.Path(path_type=Path, resolve_path=True)
)
def matrix_cmd(config_json_path: Path, github_output_file: Path):
    config = load_config(config_json_path)
    tested_packages = config.tested_packages or {}
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


@cli.command("select-patches")
@click.argument(
    "config_json_path", type=click.Path(exists=True, path_type=Path, resolve_path=True)
)
@with_verbose
@with_debug
def select_patches_cmd(config_json_path: Path):
    """4/ Select patches for the filtered out packages.

    Reads tested_packages and for each package, checks if there are any patches
    that match the package name. If there are, adds them to the config under a new
    "patches" key for each package. This will be used in the cloning step to determine
    which packages need to be cloned with patches applied.

    Example: invenio-testrig select-patches config.json
    """
    # Read the config JSON
    config = load_config(config_json_path)

    config = run_hook(
        config,
        config_json_path,
        "before_selecting_patches",
    )

    # Check if patches exists
    if not config.patches:
        click.secho(
            "✅ Warning: No patches in config, will skip patch selection",
            fg="yellow",
            bold=True,
            err=True,
        )
        return

    applied_patches_count = 0
    applied_packages_count = 0
    for tested_package_name, tested_package_info in (
        config.tested_packages or {}
    ).items():
        matching_patches = [
            patch for patch in config.patches if patch.package == tested_package_name
        ]

        run_hook(
            config,
            config_json_path,
            "selecting_package_patch",
            package_name=tested_package_name,
            package_info=tested_package_info,
            matching_patches=matching_patches,
        )
        tested_package_info.patches = matching_patches
        if matching_patches:
            applied_packages_count += 1
            applied_patches_count += len(matching_patches)
            click.secho(
                f"📌 Selected {', '.join(str(patch) for patch in matching_patches)} for package {tested_package_name}",
                fg="cyan",
                bold=True,
            )

    # Write back to the JSON file
    save_config(config_json_path, config)

    config = run_hook(
        config,
        config_json_path,
        "after_selecting_patches",
    )

    click.secho(
        f"✅ Selected {applied_patches_count} patches to apply to {applied_packages_count} packages",
        fg="green",
        bold=True,
    )


@cli.command("clone")
@click.argument(
    "config_json_path", type=click.Path(exists=True, path_type=Path, resolve_path=True)
)
@click.argument("clone_path", type=click.Path(path_type=Path, resolve_path=True))
@click.option(
    "--package",
    "package_name",
    default=None,
    help="Only clone this package instead of all",
)
@click.option("--clear-cache", is_flag=True, help="Clear git cache before cloning")
@with_verbose
@with_debug
def clone_cmd(
    config_json_path: Path,
    clone_path: Path,
    package_name: str | None,
    clear_cache: bool,
):
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

    if clear_cache:
        git_cache.clear_cache()  # Clear git cache before cloning to ensure we get the latest data for PRs and branches

    # Read the config JSON
    config = load_config(config_json_path)
    config = run_hook(
        config,
        config_json_path,
        "before_cloning_packages",
        clone_path=clone_path,
        package_name=package_name,
    )

    # Create output directory
    clone_path.mkdir(parents=True, exist_ok=False)

    if not package_name:
        # Clone repository.git
        repo_git = config.repository.git
        repo_dir = clone_path / "repo"
        click.secho(
            f"🔄 Cloning {repo_git.org}/{repo_git.repo} to {repo_dir}", fg="cyan"
        )
        git_api.clone_git_reference(repo_git, repo_dir)

        config = run_hook(
            config,
            config_json_path,
            "after_cloning_repository",
            repository_path=repo_dir,
            clone_path=clone_path,
        )

        # Clone repository.e2e if it exists
        if config.repository.e2e:
            e2e_ref = config.repository.e2e
            e2e_dir = clone_path / "invenio-e2e"
            click.secho(
                f"🔄 Cloning {e2e_ref.org}/{e2e_ref.repo} to {e2e_dir}", fg="cyan"
            )
            git_api.clone_git_reference(e2e_ref, e2e_dir)

            config = run_hook(
                config,
                config_json_path,
                "after_cloning_e2e_repository",
                e2e_repository_path=e2e_dir,
                clone_path=clone_path,
            )

    # Clone dependencies using appropriate patcher mode
    tested_packages = config.tested_packages or {}
    mode = config.mode
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

        patcher = patcher_cls(config, packages_dir, patched_packages_dir)

        for tested_package_name in tested_packages.keys():
            if package_name and package_name != tested_package_name:
                continue

            click.secho(
                f"📦 Cloning dependency {tested_package_name} using '{mode}' mode",
                fg="cyan",
            )
            patcher.clone(tested_package_name)
            config = run_hook(
                config,
                config_json_path,
                "after_cloning_dependency",
                clone_path=clone_path,
                package_name=tested_package_name,
                package_clone_path=packages_dir / tested_package_name,
                patched_package_clone_path=patched_packages_dir / tested_package_name,
            )

    config = run_hook(
        config,
        config_json_path,
        "after_cloning_packages",
        clone_path=clone_path,
        package_name=package_name,
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


def prepare_working_directory(func: Callable[..., Any]) -> Callable[..., Any]:
    """Decorator to prepare the working directory for testing."""

    @functools.wraps(func)
    def wrapper(*args: Any, working_dir: Path | None = None, **kwargs: Any) -> Any:
        # Set up the working directory. If not provided, use a temporary directory that will be cleaned up after the test.
        if working_dir is None:
            with tempfile.TemporaryDirectory() as tmpdir:
                # the temporary directory must not exist, otherwise clone will fail
                # so we just note the path and let tempfile remove it.
                working_dir = tmpdir_path = Path(tmpdir)
        else:
            tmpdir_path = None

        working_dir = working_dir.resolve()
        if working_dir.exists():
            click.secho(
                f"❌ Error: Working directory {working_dir} already exists",
                fg="red",
                bold=True,
                err=True,
            )
            raise click.Abort()
        try:
            return func(*args, working_dir=working_dir, **kwargs)
        finally:
            if tmpdir_path and tmpdir_path.exists():
                shutil.rmtree(tmpdir_path)

    return wrapper


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
@prepare_working_directory
def test_cmd(
    config_path: Path,
    clone_path: Path,
    package_name: str,
    working_dir: Path,  # resolved by the prepare_working_directory decorator
    python_version: str,
    apply_patches: bool,
    log_dir: Path | None,
):
    """5/ Test the package.

    Arguments:
        config_path: Path to the config JSON file
        clone_path: Path to the cloned repositories (output of the clone command)
        package_name: Name of the package to test
        working_dir: Path to the working directory where the package will
          be installed and tested. Must not exist.
          If not provided, a temporary directory will be used.
        python_version: Python version to use for testing
        apply_patches: Whether to install dependencies from the patched directory
                (if patches were applied) or from the packages directory
        log_dir: Directory to save test logs and status. If not provided, logs and status will not be saved,
            just printed to the console.
    """
    config = load_config(config_path)
    python_api = PythonAPI("uv", python_version)

    # prepare log and status file paths if log_dir is provided, otherwise skip logging and status saving
    if log_dir:
        log_dir.mkdir(parents=True, exist_ok=True)
        log_file = log_dir / f"{'patched' if apply_patches else 'original'}_log.log"
        status_file = (
            log_dir / f"{'patched' if apply_patches else 'original'}_status.json"
        )
    else:
        log_file = None
        status_file = None

    package_name = package_name.lower()
    api = PythonAPI(python_version=python_version)

    if package_name not in config.tested_packages:
        click.secho(
            f"❌ Error: Package '{package_name}' not found in tested_packages",
            fg="red",
            bold=True,
            err=True,
        )
        raise click.Abort()

    package_config = config.tested_packages[package_name]

    def patch_installation_progress(message: str) -> None:
        click.secho(f"📦 {message}", fg="cyan")

    click.echo(f"::group::📦 Installing package '{package_name}'")
    package_patches, library_patches = api.install_with_patches(
        repositories_root=clone_path,
        package_name=package_name,
        target_dir=working_dir,
        install_patched_dependencies=apply_patches,
        extras=package_config.extras,
        freeze=package_config.freeze,
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

    print_patch_summary(config, package_name, package_patches, library_patches)

    # save the actual uv pip freeze into the logs if logging
    if log_dir:
        freeze_file = (
            log_dir / f"{'patched' if apply_patches else 'original'}_freeze.txt"
        )
        python_api.run_in_venv(
            working_dir,
            ["uv", "pip", "freeze"],
            capture_to_file=freeze_file,
            tee_output=False,  # don't print the freeze output to the console
        )

    click.echo(f"::group::🚀 Running tests for package '{package_name}'")
    click.secho(
        f"🚀 Running tests for package '{package_name}' with command: "
        f"{package_config.test}",
        fg="cyan",
    )

    try:
        api.run_in_venv(
            working_dir,
            package_config.test,
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


def print_patch_summary(
    config: Config,
    package_name: str,
    package_patches: dict[str, Any],
    library_patches: dict[str, Any],
) -> None:

    # Print a summary of the version of the package and applied patches before running the tests
    click.echo("::group::📋 Test Configuration Summary")
    click.secho("\n" + "=" * 80, fg="blue")
    click.secho("📋 Test Configuration Summary", fg="blue", bold=True)
    click.secho("=" * 80, fg="blue")

    # Print patch mode
    mode = config.mode
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
                        patch_info = f"{patch.get('org', '')}/{patch.get('repo', '')}"
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
                else:
                    click.secho(f"  {lib_name}", fg="white", dim=True)

    click.secho("=" * 80 + "\n", fg="blue")
    click.echo("::endgroup::")


@cli.command("report")
@click.argument(
    "config_json_path", type=click.Path(exists=True, path_type=Path, resolve_path=True)
)
@click.argument(
    "artefacts_path", type=click.Path(exists=True, path_type=Path, resolve_path=True)
)
@click.argument(
    "report_output_path", type=click.Path(path_type=Path, resolve_path=True)
)
def report_cmd(config_json_path: Path, artefacts_path: Path, report_output_path: Path):
    """5/ Generate a test report based on the test artefacts.

    Reads the test status files and logs from the artefacts_path and creates
    a report summarizing the test results, applied patches, etc.

    The report format is always a HTML file saved to report_output_path.

    Arguments:
    - config_json_path: Path to the config JSON file used for the test run
    - artefacts_path: Path to the directory containing test artefacts. This directory
        contains subdirectories for each tested package, and within those,
        status files and logs for both the original and patched test runs.
    - report_output_path: Path to save the generated report. This is a directory,
        and the report file will be named "report.html" within that directory.
        All artifacts will be copied directly into this directory as well for easy access from the report.
    """
    # This is a placeholder implementation. The actual implementation would depend on the desired report format and content.
    click.secho(
        f"📊 Generating test report based on artefacts in {artefacts_path} and configuration in {config_json_path}",
        fg="cyan",
    )
    # Load config to correlate with artefacts
    config = load_config(config_json_path)

    package_data: dict[str, Any] = {
        package_name: {
            "info": package_info,
            "patched": {},
            "original": {},
        }
        for package_name, package_info in config.tested_packages.items()
    }

    for package_dir in artefacts_path.iterdir():
        package_name = package_dir.name
        if package_name not in package_data:
            click.secho(
                f"⚠️  Found artefacts for package '{package_name}' which is not in the config, skipping",
                fg="yellow",
                err=True,
            )
            continue
        if package_dir.is_dir():
            status_files = list(package_dir.glob("*_status.json"))
            for status_file in status_files:
                package_data[package_name][status_file.stem.replace("_status", "")] = (
                    json.loads(status_file.read_text())
                )

    # render the invenio-testrig/templates/report.html template with the collected data and save to report_output_path/report.html
    from jinja2 import Environment, FileSystemLoader

    env = Environment(
        loader=FileSystemLoader(searchpath=Path(__file__).parent / "templates")
    )
    template = env.get_template("report.html")
    report_content = template.render(packages=package_data)

    report_output_path.mkdir(parents=True, exist_ok=True)
    (report_output_path / "report.html").write_text(report_content)


if __name__ == "__main__":
    cli()
