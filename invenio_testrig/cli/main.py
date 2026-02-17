"""Main CLI command group for invenio-testrig."""

import functools
import json
import logging
import shutil
import subprocess
import zipfile
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
from invenio_testrig.github.api import GitApi
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


@cli.command("setup")
@click.argument("config_yaml_path_or_url", required=False)
@click.option(
    "--workdir",
    type=click.Path(path_type=Path, resolve_path=True),
    default=Path("workdir"),
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
@click.option("--patch-mode", help="Patch mode to use for patching packages")
@click.option(
    "--patch",
    "patches",
    multiple=True,
    help="Add a patch to the configuration (can be used multiple times)",
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
    type=click.Choice(["patched-only", "stop-on-success", "run-all"]),
    default="stop-on-success",
    help="Test mode: 'patched-only' (only test primary version), 'stop-on-success' (test original only on failure), 'run-all' (always test both versions)",
)
@click.option(
    "--repository",
    "repository_git",
    default=None,
    help="Override repository.git configuration (e.g., 'org/repo@branch' or GitHub URL)",
)
@click.option(
    "--e2e",
    "repository_e2e",
    default=None,
    help="Override repository.e2e configuration (e.g., 'org/repo@branch' or GitHub URL)",
)
@click.option(
    "--name",
    "name",
)
def setup_cmd(
    config_yaml_path_or_url: str | None,
    workdir: Path,
    python_version: str,
    uv_executable: str,
    disable_codestyle_checks: bool,
    test_scope: str,
    test_mode: str,
    repository_git: str | None,
    repository_e2e: str | None,
    name: str | None,
    debug: bool,
    verbose: bool,
    patch_mode: str | None,
    patches: list[str],
):
    """Complete setup: init, collect, filter, select-patches, and clone.

    This command combines the following steps:
    1. Initialize configuration (init)
    2. Collect dependencies (collect)
    3. Filter packages (filter)
    4. Select patches (select-patches)
    5. Clone repositories (clone)

    This is a convenience command that runs all preparation steps before testing.

    Example: invenio-testrig setup config.yaml --workdir ./workdir
    """
    # Step 1: Initialize
    progress.start("Step 1/5: Initializing configuration", icon="🔧")
    Path(workdir).mkdir(parents=True, exist_ok=True)
    config = initialize_config(
        config_yaml_path_or_url,
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

    # Override repository configurations if provided
    api = GitApi(GitCache(workdir / "git_cache"))
    if repository_git:
        config.repository.git = api.parse_reference(repository_git)
    if repository_e2e:
        config.repository.e2e = api.parse_reference(repository_e2e)
    if name:
        config.name = name
    if patch_mode:
        config.patch_mode = patch_mode  # type: ignore[assignment]
    if patches:
        config.patches = [api.parse_reference(patch) for patch in patches]

    config.save(workdir / "config.json")

    # Step 2: Collect dependencies
    progress.start("Step 2/5: Collecting dependencies", icon="📦")
    try:
        collect_dependencies(
            config, config.uv_executable, config.python_version, progress
        )
    except Exception as e:
        if debug:
            raise
        progress.error(f"Error collecting dependencies: {e}")
        raise click.Abort()

    # Step 3: Filter packages
    progress.start("Step 3/5: Filtering packages", icon="🔍")
    try:
        filter_packages(config, progress)
    except Exception as e:
        if debug:
            raise
        progress.error(f"Error filtering packages: {e}")
        raise click.Abort()

    # Step 4: Select patches
    progress.start("Step 4/5: Selecting patches", icon="🏷️")
    try:
        select_patches(config, progress)
    except Exception as e:
        if debug:
            raise
        progress.error(f"Error selecting patches: {e}")
        raise click.Abort()

    # Step 5: Clone repositories
    progress.start("Step 5/5: Cloning repositories", icon="📥")
    clone_path = config.workdir_path("cloned_repos")
    try:
        clone_repositories(config, clone_path, progress)
    except ValueError as e:
        progress.error(str(e))
        raise click.Abort()
    except Exception as e:
        if debug:
            raise
        progress.error(f"Error cloning repositories: {e}")
        raise click.Abort()

    progress.success("Setup complete! Ready for testing.", icon="🎉")


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


@cli.command("archive-report")
@click.argument(
    "report_directory", type=click.Path(exists=True, path_type=Path, resolve_path=True)
)
def archive_report_cmd(
    report_directory: Path,
):
    """9/ Archive a report directory by zipping its contents.

    Creates a report.zip file containing all files from the report directory,
    then removes all files except the zip and data.json (if present).

    This is useful for reducing storage space for older reports while keeping
    them accessible in archived form.

    Arguments:
        report_directory: Path to the report directory to archive
    """
    if not report_directory.is_dir():
        progress.error(f"Not a directory: {report_directory}")
        raise click.Abort()

    progress.start(f"Archiving report directory: {report_directory}", icon="📦")

    # Check if already archived
    zip_file = report_directory / "report.zip"
    if zip_file.exists():
        # Check if there are other files besides the zip and data.json
        files = list(report_directory.iterdir())
        non_archive_files = [
            f for f in files if f.name not in ("report.zip", "data.json")
        ]
        if not non_archive_files:
            progress.warning("Report is already archived")
            return

    # Create the zip file
    progress.info("Creating report.zip...")
    with zipfile.ZipFile(zip_file, "w", zipfile.ZIP_DEFLATED) as zipf:
        for item in report_directory.rglob("*"):
            if item.is_file() and item != zip_file:
                # Add file to zip with path relative to report_directory
                arcname = item.relative_to(report_directory)
                zipf.write(item, arcname)
                progress.info(f"  Added: {arcname}")

    # Count files before cleanup
    files_before = len(list(report_directory.iterdir()))

    # Remove all files and directories except report.zip and data.json
    progress.info("Removing unarchived files...")
    for item in report_directory.iterdir():
        if item.name in ("report.zip", "data.json"):
            continue

        if item.is_file():
            item.unlink()
        elif item.is_dir():
            shutil.rmtree(item)

    # Count files after cleanup
    files_after = len(list(report_directory.iterdir()))
    removed_count = files_before - files_after

    progress.success(
        f"Report archived successfully. Removed {removed_count} items, kept {files_after} item(s)"
    )
    progress.info(f"Archive: {zip_file}")
    progress.info(f"Archive size: {zip_file.stat().st_size / 1024 / 1024:.2f} MB")


if __name__ == "__main__":
    cli()
