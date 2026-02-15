"""Main CLI command group for invenio-testrig."""

import functools
import json
import logging
import subprocess
from collections.abc import Callable
from pathlib import Path
from typing import Any

import click

from invenio_testrig.commands.dependencies import collect_dependencies, filter_packages
from invenio_testrig.commands.initialization import initialize_config
from invenio_testrig.commands.report import (
    generate_report,
    generate_reports_index,
    load_test_artifacts,
)
from invenio_testrig.commands.repository import clone_repositories, select_patches
from invenio_testrig.commands.testing import (
    disable_codestyle_checks,
    install_package_for_testing,
    run_tests,
)
from invenio_testrig.config import Config
from invenio_testrig.github import GitCache
from invenio_testrig.types import Progress, TestedPackageInfo


class ClickProgress(Progress):
    """Click-based progress reporter with emoticons and colors."""

    def start(self, message: str, icon: str | None = None) -> None:
        """Report the start of a new step in the testing process."""
        icon = icon or "🔄"
        click.secho(f"{icon} {message}", fg="cyan", bold=True)

    def info(self, message: str, icon: str | None = None) -> None:
        """Report informational messages about the testing process."""
        icon = icon or "ℹ️"
        click.secho(f"{icon}  {message}", fg="blue")

    def success(self, message: str, icon: str | None = None) -> None:
        """Report successful completion of a step in the testing process."""
        icon = icon or "✅"
        click.secho(f"{icon} {message}", fg="green", bold=True)

    def warning(self, message: str, icon: str | None = None) -> None:
        """Report a warning during the testing process."""
        icon = icon or "⚠️"
        click.secho(f"{icon}  {message}", fg="yellow", bold=True, err=True)

    def error(self, message: str, icon: str | None = None) -> None:
        """Report an error during the testing process."""
        icon = icon or "❌"
        click.secho(f"{icon} {message}", fg="red", bold=True, err=True)


progress = ClickProgress()


def with_debug(func: Callable[..., Any]) -> Callable[..., Any]:
    """Decorator that adds debug option and handles exceptions."""

    @functools.wraps(func)
    def wrapper(*args: Any, config: Config, **kwargs: Any) -> Any:
        try:
            return func(*args, config=config, **kwargs)
        except Exception as e:
            if config.debug:
                raise
            progress.error(f"Error: {e}")
            raise click.Abort()

    return wrapper


def with_verbose(func: Callable[..., Any]) -> Callable[..., Any]:
    """Decorator that adds verbose option and configures logging."""

    @functools.wraps(func)
    def wrapper(*args: Any, config: Config, **kwargs: Any) -> Any:
        if config.verbose:
            logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
        return func(*args, config=config, **kwargs)

    return wrapper


def with_config(func: Callable[..., Any]) -> Callable[..., Any]:
    """Decorator that loads config and passes it as config parameter."""

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        # Try to get config path from either config_json_path or config_path
        workdir = kwargs.pop("workdir", None)

        if workdir is None:
            progress.error("workdir is required but was not provided")
            raise click.Abort()

        return func(*args, config=Config.load(workdir / "config.json"), **kwargs)

    click_arg = click.argument(
        "workdir",
        type=click.Path(exists=True, path_type=Path, resolve_path=True),
    )

    return click_arg(wrapper)


@click.group()
def cli():
    """Workflow commands for testing invenio packages."""
    pass


@cli.command("init")
@click.argument(
    "config_yaml_path", type=click.Path(exists=True, path_type=Path, resolve_path=True)
)
@click.argument(
    "workdir",
    type=click.Path(path_type=Path, resolve_path=True),
    default=Path("./testrig_workdir"),
)
@click.option("--verbose", is_flag=True, help="Enable verbose output")
@click.option("--debug", is_flag=True, help="Enable debug mode with full traceback")
@click.option(
    "--python",
    "python_version",
    default="python3",
    help="Python version to use for testing",
)
@click.option(
    "--uv",
    "uv_executable",
    default="uv",
    help="Path to uv executable",
)
@click.option(
    "--disable-codestyle-checks",
    "disable_codestyle_checks",
    is_flag=True,
    help="Disable codestyle checks (black, isort, pydocstyle) in test configuration",
)
@click.option(
    "--test-scope",
    "test_scope",
    type=click.Choice(["affected", "all"]),
    default="affected",
    help="Test scope: 'affected' (only packages with patches), 'all' (all packages)",
)
@click.option(
    "--test-mode",
    "test_mode",
    type=click.Choice(["first-only", "stop-on-success", "run-all"]),
    default="stop-on-success",
    help="Test mode: 'first-only' (only test primary version), 'stop-on-success' (test original only on failure), 'run-all' (always test both versions)",
)
def init_cmd(
    config_yaml_path: Path,
    workdir: Path,
    python_version: str,
    uv_executable: str,
    disable_codestyle_checks: bool,
    test_scope: str,
    test_mode: str,
    debug: bool,
    verbose: bool,
):
    """1/ Initialize workflow by preparing configuration.

    Resolves all git references in the YAML configuration and outputs JSON.

    Example: invenio-testrig init config.yaml config.json
    """
    Path(workdir).mkdir(parents=True, exist_ok=True)
    config = initialize_config(
        config_yaml_path,
        workdir,
        progress,
    )
    config.python_version = python_version
    config.uv_executable = uv_executable
    config.disable_codestyle_checks = disable_codestyle_checks
    config.test_scope = test_scope  # type: ignore[assignment]
    config.test_mode = test_mode  # type: ignore[assignment]
    config.verbose = verbose
    config.debug = debug
    config.save(workdir / "config.json")


@cli.command("collect")
@with_config
@with_verbose
@with_debug
def collect_cmd(
    config: Config,
):
    """2/ Collect dependencies/libraries for the repository.

    Clones the repository, installs it (if uv.lock is not found),
    and collects dependencies. Updates the config JSON with a "packages" key
    containing all detected dependencies and their versions.

    Example: invenio-testrig collect config.json
    """
    collect_dependencies(config, config.uv_executable, config.python_version, progress)


@cli.command("filter")
@with_config
@with_verbose
@with_debug
def filter_cmd(config: Config):
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
    filter_packages(config, progress)


@cli.command("matrix")
@with_config
@click.argument(
    "github_output_file", type=click.Path(path_type=Path, resolve_path=True)
)
@with_verbose
@with_debug
def matrix_cmd(config: Config, github_output_file: Path):
    """Generate GitHub Actions test matrix for tested packages.

    Reads the tested packages from config and writes a JSON matrix to the
    GitHub Actions output file for workflow matrix strategy.

    Example: invenio-testrig matrix config.json $GITHUB_OUTPUT
    """
    tested_packages = config.tested_packages or {}
    matrix = [package for package in tested_packages.keys()]
    with open(github_output_file, "a") as f:
        f.write("\n")
        f.write(f"matrix_tested_packages={json.dumps(matrix)}\n")
    progress.success(
        f"Generated test matrix for {len(tested_packages)} packages and "
        f"written to {github_output_file}"
    )


@cli.command("select-patches")
@with_config
@with_verbose
@with_debug
def select_patches_cmd(config: Config):
    """4/ Select patches for the filtered out packages.

    Reads tested_packages and for each package, checks if there are any patches
    that match the package name. If there are, adds them to the config under a new
    "patches" key for each package. This will be used in the cloning step to determine
    which packages need to be cloned with patches applied.

    Example: invenio-testrig select-patches config.json
    """
    select_patches(config, progress)


@cli.command("clear-cache")
@with_config
@with_verbose
@with_debug
def clear_cache_cmd(config: Config):
    """Clear git cache.

    This is useful to force re-cloning repositories and re-resolving git references
    in the next run. It removes the local cache directory used for storing cloned
    repositories and resolved references.

    Example: invenio-testrig clear-cache
    """
    git_cache = GitCache(config.workdir_path("git_cache"))
    git_cache.clear_cache()
    progress.success("Git cache cleared successfully")


@cli.command("clone")
@with_config
@with_verbose
@with_debug
def clone_cmd(
    config: Config,
):
    """5/ Clone packages from configuration.

    Clone repository.git and repository.e2e (if configured) to the output directory.
    Then clone all packages specified in "tested_packages" into the packages/ subdirectory.
    If a package has patches, also clone it into the patched/ subdirectory and apply patches.
    The patching behavior depends on the patch_mode specified in the config (as-is, upstream, or custom).

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
    clone_path = config.workdir_path("cloned_repos")
    try:
        clone_repositories(config, clone_path, progress)
    except ValueError as e:
        progress.error(str(e))
        raise click.Abort()


@cli.command("test")
@with_config
@click.argument("package_name")
@click.option(
    "--apply-patches",
    "apply_patches",
    is_flag=True,
    help="Reinstall dependencies from local patches",
)
@with_verbose
@with_debug
def test_cmd(
    config: Config,
    package_name: str,
    apply_patches: bool,
):
    """6/ Test the package.

    Arguments:
        config: Configuration object containing paths and settings
        package_name: Name of the package to test
        apply_patches: Whether to install dependencies from the patched directory
                (if patches were applied) or from the packages directory
    """
    log_dir = config.workdir_path("artifacts") / package_name
    package_name = package_name.lower()

    if package_name not in config.tested_packages:
        progress.error(f"Package '{package_name}' not found in tested_packages")
        raise click.Abort()

    # Prepare log directory
    log_dir.mkdir(parents=True, exist_ok=True)

    # Install the package
    click.echo(f"::group::📦 Installing package '{package_name}'")
    try:
        package_dir, package_config, library_patches, patched = (
            install_package_for_testing(
                config,
                package_name,
                apply_patches,
                progress,
            )
        )
    except ValueError as e:
        click.echo("::endgroup::")
        progress.error(str(e))
        raise click.Abort()

    click.echo("::endgroup::")

    # Print test configuration summary
    print_patch_summary(config, package_name, package_config, library_patches)

    # Disable codestyle checks if requested
    if config.disable_codestyle_checks:
        progress.info(
            "Disabling codestyle checks (black, isort, pydocstyle)",
            icon="🔧",
        )
        disable_codestyle_checks(package_dir)

    # Run the tests
    click.echo(f"::group::🚀 Running tests for package '{package_name}'")
    try:
        run_tests(
            config,
            package_dir,
            package_name,
            package_config,
            library_patches,
            apply_patches,
            patched,
            progress,
        )
        click.echo("::endgroup::")

    except subprocess.CalledProcessError:
        click.echo("::endgroup::")
        click.echo("::error::Tests failed")
        raise


def print_patch_summary(
    config: Config,
    package_name: str,
    package_config: TestedPackageInfo,
    library_patches: list[TestedPackageInfo],
) -> None:
    """Print a summary of package configuration and applied patches.

    Args:
        config: Configuration object containing patch_mode information
        package_name: Name of the package being tested
        package_config: Configuration for the tested package
        library_patches: List of dependency packages with configuration
    """

    # Print a summary of the version of the package and applied patches before running the tests
    click.echo("::group::📋 Test Configuration Summary")
    click.secho("\n" + "=" * 80, fg="blue")
    click.secho("📋 Test Configuration Summary", fg="blue", bold=True)
    click.secho("=" * 80, fg="blue")

    # Print patch mode
    mode = config.patch_mode
    click.secho(f"Patch mode: {mode}", fg="cyan")

    # Print package information
    click.secho(f"\n📦 Package: {package_name}", fg="green", bold=True)
    if package_config.patches:
        for patch in package_config.patches:
            click.secho(f"  Patch: {str(patch)}", fg="yellow")
    else:
        click.secho("  No patches applied", fg="white", dim=True)

    # Print library dependencies with patches
    if library_patches:
        patched_libs = [lib for lib in library_patches if lib.patches]
        unpatched_libs = [lib for lib in library_patches if not lib.patches]

        if patched_libs:
            click.secho(
                f"\n📚 Patched dependencies ({len(patched_libs)}):",
                fg="green",
                bold=True,
            )
            for lib_info in patched_libs:
                click.secho(f"  {lib_info.reference.package}:", fg="cyan")
                for patch in lib_info.patches:
                    click.secho(f"    Patch: {str(patch)}", fg="yellow")

        # Show unpatched but locally installed libraries
        if unpatched_libs:
            click.secho(
                f"\n📚 Locally installed dependencies without patches ({len(unpatched_libs)}):",
                fg="white",
                dim=True,
            )
            for lib_info in unpatched_libs:
                click.secho(f"  {lib_info.reference.package}", fg="white", dim=True)

    click.secho("=" * 80 + "\n", fg="blue")
    click.echo("::endgroup::")


@cli.command("report")
@with_config
@click.argument(
    "report_output_path", type=click.Path(path_type=Path, resolve_path=True)
)
@click.option(
    "--completed",
    is_flag=True,
    help="Whether to mark the report as completed (e.g. all tests finished)",
)
@with_verbose
@with_debug
def report_cmd(
    config: Config,
    report_output_path: Path,
    completed: bool,
):
    """7/ Generate a test report based on the test artefacts.

    Reads the test status files and logs from the artefacts directory and creates
    a report summarizing the test results, applied patches, etc.

    The report format is always a HTML file saved to report_output_path.

    Arguments:
        config: Configuration object containing paths and settings
        report_output_path: Path to save the generated report. This is a directory,
            and the report file will be named "report.html" within that directory.
            All artifacts will be copied directly into this directory as well for easy access from the report.
        completed: Whether to mark the report as completed (e.g. all tests finished)
    """
    artefacts_path = config.workdir_path("artifacts")

    progress.start(
        f"Generating test report based on artefacts in {artefacts_path} and configuration in {config.config_path}",
        icon="📊",
    )

    # Debug: Check if artifacts directory exists and what's in it
    progress.info(f"Checking artifacts directory: {artefacts_path}")
    if not artefacts_path.exists():
        progress.error(f"Artifacts directory does not exist: {artefacts_path}")
    else:
        progress.info(f"Artifacts directory exists: {artefacts_path}")
        items = list(artefacts_path.iterdir())
        progress.info(f"Found {len(items)} items in artifacts directory")
        for item in items:
            if item.is_dir():
                progress.info(f"  - Directory: {item.name}")
                status_files = list(item.glob("*_status.json"))
                progress.info(
                    f"    Found {len(status_files)} status files: {[f.name for f in status_files]}"
                )
            else:
                progress.info(f"  - File: {item.name}")

    # Debug: Check tested packages in config
    progress.info(f"Config contains {len(config.tested_packages)} tested packages")
    for pkg_name in list(config.tested_packages.keys())[:5]:  # Show first 5
        progress.info(f"  - {pkg_name}")
    if len(config.tested_packages) > 5:
        progress.info(f"  ... and {len(config.tested_packages) - 5} more")

    test_result_data = load_test_artifacts(config, artefacts_path, progress=progress)

    # Debug: Check loaded test results
    progress.info(f"Loaded {len(test_result_data)} test result entries")
    for pkg in test_result_data[:5]:  # Show first 5
        progress.info(
            f"  - {pkg.info.reference.package}: patched={pkg.patched.status}, original={pkg.original.status}"
        )
    if len(test_result_data) > 5:
        progress.info(f"  ... and {len(test_result_data) - 5} more")

    generate_report(
        config,
        completed,
        test_result_data,
        report_output_path=report_output_path,
        progress=progress,
    )


@cli.command("reports-index")
@click.argument(
    "reports_directory", type=click.Path(exists=True, path_type=Path, resolve_path=True)
)
@click.argument("output_file", type=click.Path(path_type=Path, resolve_path=True))
def reports_index_cmd(
    reports_directory: Path,
    output_file: Path,
):
    """8/ Generate an index page listing all reports in a directory.

    Scans the reports directory for subdirectories and creates an index.html
    file listing all available reports, sorted by last modification time.

    Arguments:
        reports_directory: Path to the directory containing report subdirectories
        output_file: Path where the index HTML file should be saved
    """
    progress.start(
        f"Generating reports index from {reports_directory}",
        icon="📑",
    )

    generate_reports_index(
        reports_directory=reports_directory,
        output_file=output_file,
        progress=progress,
    )


if __name__ == "__main__":
    cli()
