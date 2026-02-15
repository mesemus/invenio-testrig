"""Report generation functionality for test results.

This module generates HTML reports from test execution artifacts,
showing test results for both patched and unpatched versions of packages.
"""

import json
from collections import defaultdict
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from invenio_testrig.config import (
    Config,
    load_execution_status,
)
from invenio_testrig.types import ExecutionStatus, Progress, ReportPackageData


def collect_warnings_by_log_type(
    artifacts_path: Path, progress: Progress
) -> dict[str, dict[str, dict[str, tuple[int, str]]]]:
    """Collect warnings from all package warnings JSON files, organized by log type.

    Args:
        artifacts_path: Path to the artifacts directory containing package subdirectories

    Returns:
        Dict mapping log_type to warning text to package data (count and artifact link).
        Structure: {log_type: {warning_text: {package_name: (count, artifact_link)}}}
    """
    warnings_by_type: dict[str, dict[str, dict[str, tuple[int, str]]]] = defaultdict(
        lambda: defaultdict(dict)
    )

    if not artifacts_path.exists():
        return {}

    # Find all warnings JSON files
    for warnings_file in artifacts_path.glob("*/warnings_*.json"):
        try:
            package_name = warnings_file.parent.name
            log_type = "patched" if "patched" in warnings_file.name else "original"

            # Construct link to the simplified log file
            artifact_link = f"artifacts/{package_name}/{log_type}_simplified_log.log"

            with warnings_file.open("r") as f:
                warnings_data = json.load(f)

            if isinstance(warnings_data, dict):
                for warning_text, count in warnings_data.items():
                    warnings_by_type[log_type][warning_text][package_name] = (
                        count,
                        artifact_link,
                    )

        except (json.JSONDecodeError, IOError) as e:
            progress.error(f"Failed to process {warnings_file}: {e}")
            continue

    return {k: dict(v) for k, v in warnings_by_type.items()}


def calculate_total_occurrences(package_data: dict[str, tuple[int, str]]) -> int:
    """Calculate total occurrences of a warning across all packages."""
    return sum(count for count, _ in package_data.values())


def create_warnings_report(
    config: Config,
    artifacts_path: Path,
    report_output_path: Path,
    progress: Progress,
) -> None:
    """Collect all warnings and create a warnings report in HTML format.

    Args:
        config: Configuration object
        artifacts_path: Path to the artifacts directory
        report_output_path: Path where the report should be saved
    """
    progress.info("Generating warnings report")

    # Collect warnings from all packages
    warnings_by_type = collect_warnings_by_log_type(artifacts_path, progress)

    # Calculate statistics
    total_unique_warnings = sum(len(warnings) for warnings in warnings_by_type.values())
    total_packages_with_warnings: set[str] = set()
    total_warning_occurrences = 0

    for log_type, warnings_data in warnings_by_type.items():
        for warning_text, package_data in warnings_data.items():
            total_packages_with_warnings.update(package_data.keys())
            total_warning_occurrences += calculate_total_occurrences(package_data)

    progress.info(
        f"Found {total_unique_warnings} unique warning(s) from {len(total_packages_with_warnings)} package(s)"
    )

    # Prepare data for template
    warnings_by_type_sorted = {}
    for log_type in sorted(
        warnings_by_type.keys(), reverse=True
    ):  # patched, then original
        warnings_data = warnings_by_type[log_type]

        # Sort warnings by total count (descending) then by text (ascending)
        sorted_warnings = sorted(
            warnings_data.items(),
            key=lambda x: (-calculate_total_occurrences(x[1]), x[0]),
        )

        warnings_list = []
        for warning_text, package_data in sorted_warnings:
            total_count = calculate_total_occurrences(package_data)
            # Sort packages by count descending, build list with name, count, and link
            package_list = [
                {
                    "name": pkg_name,
                    "count": count,
                    "link": artifact_link,
                }
                for pkg_name, (count, artifact_link) in sorted(
                    package_data.items(), key=lambda x: (-x[1][0], x[0])
                )
            ]

            warnings_list.append(
                {
                    "text": warning_text,
                    "total_count": total_count,
                    "packages": package_list,
                }
            )

        warnings_by_type_sorted[log_type] = warnings_list

    jinja_context = {
        "config_name": config.name,
        "config_mode": config.mode,
        "last_updated": datetime.now(UTC).strftime("%Y-%m-%d %H:%M:%S UTC"),
        "total_unique_warnings": total_unique_warnings,
        "total_packages_with_warnings": len(total_packages_with_warnings),
        "total_warning_occurrences": total_warning_occurrences,
        "warnings_by_type": warnings_by_type_sorted,
    }

    # Render the template
    from jinja2 import Environment, FileSystemLoader

    env = Environment(
        loader=FileSystemLoader(searchpath=Path(__file__).parent / "templates")
    )
    template = env.get_template("warnings.html")
    report_content = template.render(**jinja_context)

    # Save the report
    report_output_path.mkdir(parents=True, exist_ok=True)
    warnings_report_file = report_output_path / "warnings.html"
    warnings_report_file.write_text(report_content)

    progress.success(f"Warnings report written to: {warnings_report_file}")


def generate_report(
    config: Config,
    completed: bool,
    test_results: list[ReportPackageData],
    report_output_path: Path,
    progress: Progress,
) -> None:
    """Generate a report based on the execution status of the tested packages."""
    progress.info(f"Generating report with {len(test_results)} test results")
    progress.info(f"Report output path: {report_output_path}")
    progress.info(f"Completed: {completed}")

    # Filter out packages that are still pending (both patched and original are pending)
    test_results = [
        p
        for p in test_results
        if not (p.patched.status == "pending" and p.original.status == "pending")
    ]
    progress.info(f"After filtering pending: {len(test_results)} test results")

    # Debug: Show summary of test results
    patched_not_skipped = sum(
        1 for p in test_results if p.patched.status not in ("skipped", "pending")
    )
    original_not_skipped = sum(
        1 for p in test_results if p.original.status not in ("skipped", "pending")
    )
    progress.info(f"Patched results (not skipped): {patched_not_skipped}")
    progress.info(f"Original results (not skipped): {original_not_skipped}")

    # Calculate error totals
    regression_count = sum(
        1
        for p in test_results
        if p.patched.status == "failed" and p.original.status == "success"
    )
    still_failing_count = sum(
        1
        for p in test_results
        if p.original.status == "failed" and p.patched.status != "success"
    )
    total_errors = regression_count + still_failing_count
    has_errors = total_errors > 0

    # Determine status and badge styling
    if completed:
        if has_errors:
            status = "Complete with Errors"
            status_class = "complete-errors"
            status_icon = "❌"
        else:
            status = "Complete"
            status_class = "complete"
            status_icon = "✅"
    else:
        if has_errors:
            status = "In Progress with Errors"
            status_class = "in-progress-errors"
            status_icon = "⚠️"
        else:
            status = "In Progress"
            status_class = "in-progress"
            status_icon = "🔄"

    # Convert started_at from ISO format to human-readable format
    started_at_formatted = None
    if config.started_at:
        try:
            started_at_dt = datetime.fromisoformat(config.started_at)
            started_at_formatted = started_at_dt.strftime("%Y-%m-%d %H:%M:%S UTC")
        except (ValueError, AttributeError):
            started_at_formatted = config.started_at

    jinja_context: dict[str, Any] = {
        "config_name": config.name,
        "config_mode": config.mode,
        "started_at": started_at_formatted,
        "status": status,
        "status_class": status_class,
        "status_icon": status_icon,
        "completed": completed,
        "has_errors": has_errors,
        "last_updated": datetime.now(UTC).strftime("%Y-%m-%d %H:%M:%S UTC"),
        "total_packages_count": len(test_results),
        "patched_packages_count": sum(
            1
            for p in test_results
            if p.patched.status not in ("skipped", "pending")
            or p.original.status not in ("skipped", "pending")
        ),
        "unpatched_packages_count": sum(
            1
            for p in test_results
            if p.patched.status in ("skipped", "pending")
            and p.original.status in ("skipped", "pending")
        ),
        "ok_count": sum(
            1
            for p in test_results
            if p.patched.status == "success"
            or (
                p.original.status == "success"
                and p.patched.status in ("skipped", "pending")
            )
        ),
        "regression_count": regression_count,
        "still_failing_count": still_failing_count,
        "packages": test_results,
        "packages_without_patches": [
            p
            for p in test_results
            if p.patched.status in ("skipped", "pending")
            and p.original.status not in ("pending",)
        ],
        "patched_packages": [
            p
            for p in test_results
            if p.patched.status not in ("skipped", "pending") and p.info.patches
        ],
        "packages_with_patched_dependencies": [
            p
            for p in test_results
            if p.patched.status not in ("skipped", "pending") and not p.info.patches
        ],
    }

    # Debug: Show calculated counts
    progress.info("Report statistics:")
    progress.info(f"   - Total packages: {jinja_context['total_packages_count']}")
    progress.info(f"   - Patched packages: {jinja_context['patched_packages_count']}")
    progress.info(
        f"   - Unpatched packages: {jinja_context['unpatched_packages_count']}"
    )
    progress.info(f"   - OK count: {jinja_context['ok_count']}")
    progress.info(f"   - Regression count: {jinja_context['regression_count']}")
    progress.info(f"   - Still failing count: {jinja_context['still_failing_count']}")
    progress.info(
        f"   - Packages without patches: {len(jinja_context['packages_without_patches'])}"
    )
    progress.info(f"   - Patched packages: {len(jinja_context['patched_packages'])}")
    progress.info(
        f"   - Packages with patched deps: {len(jinja_context['packages_with_patched_dependencies'])}"
    )

    # render the invenio-testrig/templates/report.html template with the collected data and save to report_output_path/report.html
    from jinja2 import Environment, FileSystemLoader

    env = Environment(
        loader=FileSystemLoader(searchpath=Path(__file__).parent / "templates")
    )
    template = env.get_template("report.html")
    report_content = template.render(**jinja_context)

    report_output_path.mkdir(parents=True, exist_ok=True)
    report_file = report_output_path / "index.html"
    report_file.write_text(report_content)

    # Debug: Confirm report was written
    progress.info(f"Report file written to: {report_file}")
    progress.info(f"Report file size: {report_file.stat().st_size} bytes")
    progress.info(f"Report content length: {len(report_content)} characters")

    # Generate warnings report
    artifacts_path = config.workdir_path("artifacts")
    create_warnings_report(config, artifacts_path, report_output_path, progress)


def load_test_artifacts(
    config: Config, artefacts_path: Path, progress: Progress
) -> list[ReportPackageData]:
    """Load test artifacts from the artifacts directory.

    Scans the artifacts directory for test execution status files and loads
    them into ReportPackageData structures for report generation.

    Args:
        config: Configuration containing tested packages information
        artefacts_path: Path to the directory containing test artifacts

    Returns:
        List of ReportPackageData with test execution status for each package
    """
    progress.info(f"Loading test artifacts from: {artefacts_path}")
    progress.info(f"Artifacts path exists: {artefacts_path.exists()}")
    progress.info(f"Number of tested packages in config: {len(config.tested_packages)}")

    package_data: dict[str, ReportPackageData] = {
        package_name: ReportPackageData(
            info=package_info,
            artefact_dir=f"artifacts/{package_name}",
            patched=ExecutionStatus(status="pending", package=package_info),
            original=ExecutionStatus(status="pending", package=package_info),
        )
        for package_name, package_info in config.tested_packages.items()
    }

    progress.info(f"Initialized package_data dict with {len(package_data)} entries")

    if not artefacts_path.exists():
        progress.warning(f"Artifacts path does not exist: {artefacts_path}")
        return sorted(
            package_data.values(), key=lambda p: (4, p.info.reference.package)
        )

    dir_items = list(artefacts_path.iterdir())
    progress.info(f"Found {len(dir_items)} items in artifacts directory")

    for package_dir in dir_items:
        package_name = package_dir.name
        progress.info(f"Checking item: {package_name} (is_dir: {package_dir.is_dir()})")

        if package_name not in package_data:
            progress.warning(
                f"Found artefacts for package '{package_name}' which is not in the config, skipping"
            )
            continue
        if package_dir.is_dir():
            status_files = list(package_dir.glob("*_status.json"))
            progress.info(
                f"Package '{package_name}': Found {len(status_files)} status files"
            )
            # the directory is present, thus the package is not pending
            package_data[package_name].patched.status = "skipped"
            package_data[package_name].original.status = "skipped"

            # now overwrite with actual status if status files are present
            for status_file in status_files:
                progress.info(f"   Loading: {status_file.name}")
                loaded_status = load_execution_status(status_file)
                match status_file.stem:
                    case "patched_status":
                        package_data[package_name].patched = loaded_status
                    case "original_status":
                        package_data[package_name].original = loaded_status
                    case _:
                        progress.warning(
                            f"Found unexpected status file '{status_file.name}' for package '{package_name}', skipping"
                        )

    # Sort results: failed first, then success, then skipped; within each group, sort by package name
    def sort_key(pkg: ReportPackageData) -> tuple[int, str]:
        """Generate sort key: (priority, package_name)."""
        status = pkg.patched.status
        if status == "failed":
            priority = 0  # Failed packages first
        elif status == "success":
            priority = 1  # Success packages second
        else:  # skipped or any other status
            status = pkg.original.status
            if status == "failed":
                priority = 2  # Failed packages first (even if patched was skipped)
            elif status == "success":
                priority = 3  # Success packages second (even if patched was skipped)
            else:
                priority = 4  # Skipped/other packages last
        return (priority, pkg.info.reference.package)

    return sorted(package_data.values(), key=sort_key)


def generate_reports_index(
    reports_directory: Path,
    output_file: Path,
    progress: Progress,
) -> None:
    """Generate an index page listing all reports in the reports directory.

    Args:
        reports_directory: Path to the directory containing report subdirectories
        output_file: Path where the index HTML file should be saved
        progress: Progress reporter for status updates
    """
    progress.start("Generating reports index", icon="📑")

    if not reports_directory.exists():
        progress.error(f"Reports directory does not exist: {reports_directory}")
        return

    # Find all directories in the reports directory that have an index.html
    report_dirs: list[dict[str, Any]] = []
    for item in reports_directory.iterdir():
        if item.is_dir():
            # Check if index.html exists in the directory
            index_file = item / "index.html"
            if not index_file.exists():
                continue

            # Get the last modification time
            mtime = item.stat().st_mtime

            # Add report directory info
            report_dirs.append(
                {
                    "name": item.name,
                    "path": item.name,  # Relative path from the index
                    "mtime": mtime,
                    "mtime_formatted": datetime.fromtimestamp(mtime).strftime(
                        "%Y-%m-%d %H:%M:%S"
                    ),
                }
            )

    # Sort by modification time, most recent first
    report_dirs.sort(key=lambda x: float(x["mtime"]), reverse=True)

    progress.info(f"Found {len(report_dirs)} report directories")

    jinja_context = {
        "last_updated": datetime.now(UTC).strftime("%Y-%m-%d %H:%M:%S UTC"),
        "total_reports": len(report_dirs),
        "reports": report_dirs,
    }

    # Render the template
    from jinja2 import Environment, FileSystemLoader

    env = Environment(
        loader=FileSystemLoader(searchpath=Path(__file__).parent / "templates")
    )
    template = env.get_template("reports_index.html")
    report_content = template.render(**jinja_context)

    # Save the report
    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(report_content)

    progress.success(f"Reports index written to: {output_file}")
