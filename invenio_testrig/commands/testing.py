"""Testing command implementation."""

import json
import re
import shutil
import subprocess
from collections import defaultdict
from pathlib import Path

from invenio_testrig.config import (
    Config,
    save_execution_status,
)
from invenio_testrig.python_api import PythonAPI
from invenio_testrig.types import ExecutionStatus, Progress, TestedPackageInfo


def testing_directory(config: Config, package_name: str, apply_patches: bool) -> Path:
    return (
        config.workdir_path("tests")
        / package_name
        / ("patched" if apply_patches else "original")
    )


def process_warnings(
    input_log_path: Path, warnings_json_path: Path, output_log_path: Path
) -> None:
    """Extract warnings from log file and create a filtered version without warnings.

    This function:
    1. Extracts Python warnings from the log file (e.g., DeprecationWarning, RuntimeWarning)
    2. Normalizes and counts occurrences of each warning
    3. Saves warnings to a JSON file
    4. Creates a filtered log file with warnings and other noise removed

    Args:
        input_log_path: Path to the input log file
        warnings_json_path: Path where warnings JSON should be saved
        output_log_path: Path where filtered log (without warnings) should be saved
    """
    if not input_log_path.exists():
        # If input log doesn't exist, create empty output files
        warnings_json_path.write_text("{}")
        output_log_path.write_text("")
        return

    # Extract warnings
    warnings: dict[str, int] = defaultdict(int)
    warning_pattern = re.compile(r"(\w+Warning:.*?)$")

    with input_log_path.open("r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
        for line in content.splitlines():
            match = warning_pattern.search(line)
            if match:
                warning_text = match.group(1).strip()
                # Normalize by replacing memory addresses with [id]
                warning_text = re.sub(r"0x[0-9a-fA-F]+", "[id]", warning_text)
                warnings[warning_text] += 1

    # Save warnings to JSON
    warnings_json_path.parent.mkdir(parents=True, exist_ok=True)
    warnings_json_path.write_text(json.dumps(dict(warnings), indent=2))

    # Create filtered log without warnings
    output_log_path.parent.mkdir(parents=True, exist_ok=True)

    # Read the original content
    with input_log_path.open("r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()

    # Filter out unwanted lines
    filtered_lines = []
    for line in lines:
        # Skip GitHub Actions warning annotations
        if line.strip().startswith("::warning file="):
            continue
        # Remove ::warning from within lines
        line = re.sub(r"::warning file=.*", "", line)

        # Skip Python warning lines
        if re.search(
            r"DeprecationWarning|PendingDeprecationWarning|ResourceWarning|"
            r"UserWarning|FutureWarning|ImportWarning|RuntimeWarning",
            line,
        ):
            continue

        # Skip pytest warning summary lines
        if re.match(r"^\s*warnings summary", line):
            continue
        if re.match(r"^\s*--.*warnings", line):
            continue
        if re.search(r"[0-9]+ warnings?$", line):
            continue

        # Skip Docker pull output lines
        if re.match(
            r"^\s*[0-9a-f]{12}\s+(Waiting|Pulling|Downloading|Verifying|Download|Extracting|Pull complete)",
            line,
        ):
            continue

        # Skip separator lines
        if re.match(r"^[=\-]{10,}$", line.strip()):
            continue

        # Remove test progress indicators (dots) from beginning and end of lines
        line = re.sub(r"^\.+", "", line)
        line = re.sub(r"\.+$", "", line)

        # Skip empty lines
        if not line.strip():
            continue

        filtered_lines.append(line)

    # Write filtered output
    output_log_path.write_text("".join(filtered_lines))


def install_package_for_testing(
    config: Config,
    package_name: str,
    apply_patches: bool,
    progress: Progress,
) -> tuple[Path, TestedPackageInfo, list[TestedPackageInfo], bool]:
    """Install a package for testing.

    Args:
        config: Config object
        package_name: Name of the package to test
        apply_patches: Whether to install dependencies from the patched directory
        progress: Progress reporter for status updates

    Returns:
        Tuple of (package_config, library_patches, has_patches)

    Raises:
        ValueError: If the package is not found in tested_packages
    """
    python_api = PythonAPI("uv", config.python_version)

    package_name = package_name.lower()

    if package_name not in config.tested_packages:
        raise ValueError(f"Package '{package_name}' not found in tested_packages")

    package_config = config.tested_packages[package_name]

    working_dir = testing_directory(config, package_name, apply_patches)
    if working_dir.exists():
        progress.info(
            f"Working directory {working_dir} already exists, removing it before installation",
            icon="⚠️",
        )
        shutil.rmtree(working_dir)

    dependencies = python_api.install_with_patches(
        repositories_root=config.workdir_path("cloned_repos"),
        package_name=package_name,
        target_dir=working_dir,
        install_patched_dependencies=apply_patches,
        extras=package_config.extras,
        freeze=package_config.freeze,
        progress=progress,
    )

    progress.success(
        f"Successfully installed package '{package_name}' in {working_dir}"
    )

    library_patches = [
        config.tested_packages[x] for x in dependencies if x in config.tested_packages
    ]

    patched = bool(config.tested_packages[package_name].patches) or any(
        bool(config.tested_packages[x].patches)
        for x in dependencies
        if x in config.tested_packages
    )

    # save the actual uv pip freeze into the logs if logging
    log_dir = config.workdir_path("artifacts") / package_name
    freeze_file = log_dir / f"{'patched' if apply_patches else 'original'}_freeze.txt"
    python_api.run_in_venv(
        working_dir,
        ["uv", "pip", "freeze"],
        capture_to_file=freeze_file,
        tee_output=False,  # don't print the freeze output to the console
    )

    return working_dir, package_config, library_patches, patched


def disable_codestyle_checks(package_path: Path) -> None:
    """Remove codestyle check flags from package configuration files.

    This function removes --black, --isort, and --pydocstyle flags from
    setup.cfg and pyproject.toml files in the specified package directory.

    Args:
        package_path: Path to the package directory
    """
    flags_to_remove = ["--black ", "--isort ", "--pydocstyle "]

    def fix_file(file_path: Path) -> None:
        """Remove codestyle flags from a single file."""
        if not file_path.exists():
            return
        content = file_path.read_text()
        original_content = content

        for flag in flags_to_remove:
            content = content.replace(flag, "")

        if content != original_content:
            file_path.write_text(content)
            print(f"Removed codestyle checks from {file_path}")

    fix_file(package_path / "setup.cfg")
    fix_file(package_path / "pyproject.toml")


def run_tests(
    config: Config,
    working_dir: Path,
    package_name: str,
    package_config: TestedPackageInfo,
    library_patches: list[TestedPackageInfo],
    apply_patches: bool,
    patched: bool,
    progress: Progress,
) -> str:
    """Run tests for an installed package.

    Args:
        config: Config object
        working_dir: Directory where the package is installed (either patched or original)
        package_name: Name of the package to test
        package_config: Package configuration
        library_patches: List of dependency packages with configuration
        apply_patches: Whether patches were applied
        patched: Whether any patches were applied to package or dependencies
        progress: Progress reporter for status updates

    Returns:
        Test status ("success", "failed", or "skipped")

    Raises:
        subprocess.CalledProcessError: If the tests fail
    """
    log_dir = config.workdir_path("artifacts") / package_name
    log_file = log_dir / f"{'patched' if apply_patches else 'original'}_log.log"
    status_file = log_dir / f"{'patched' if apply_patches else 'original'}_status.json"
    warnings_file = (
        log_dir / f"warnings_{'patched' if apply_patches else 'original'}.json"
    )
    simplified_log_file = (
        log_dir / f"{'patched' if apply_patches else 'original'}_simplified_log.log"
    )

    if apply_patches and not patched:
        # skip the test execution if patches were requested but not applied
        progress.warning(
            f"No patches applied for package '{package_name}', skipping test execution"
        )
        status = "skipped"
        save_execution_status(
            status_file,
            ExecutionStatus(
                status=status, package=package_config, dependencies=library_patches
            ),
        )
        return status

    api = PythonAPI(
        uv_executable=config.uv_executable, python_version=config.python_version
    )

    progress.start(
        f"Running tests for package '{package_name}' with command: "
        f"{package_config.test}",
        icon="🚀",
    )

    try:
        api.run_in_venv(
            working_dir,
            package_config.test,
            log_file,
        )
        progress.success(f"Tests completed successfully for package '{package_name}'")

        # Process warnings from log file
        process_warnings(log_file, warnings_file, simplified_log_file)

        status = "success"
        save_execution_status(
            status_file,
            ExecutionStatus(
                status=status, package=package_config, dependencies=library_patches
            ),
        )
        return status

    except subprocess.CalledProcessError as e:
        progress.error(
            f"Tests failed for package '{package_name}' with exit code {e.returncode}"
        )
        if log_file:
            progress.info(f"Check the output log at: {log_file}", icon="💡")

        # Process warnings from log file even on failure
        process_warnings(log_file, warnings_file, simplified_log_file)

        save_execution_status(
            status_file,
            ExecutionStatus(
                status="failed", package=package_config, dependencies=library_patches
            ),
        )
        raise
