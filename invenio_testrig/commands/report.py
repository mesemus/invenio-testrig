"""Report generation functionality for test results.

This module generates HTML reports from test execution artifacts,
showing test results for both patched and unpatched versions of packages.
"""

from datetime import UTC, datetime
from pathlib import Path
from typing import Any

# TODO: should use progress here instead of click.secho
import click

from invenio_testrig.config import (
    Config,
    load_execution_status,
)
from invenio_testrig.types import ExecutionStatus, ReportPackageData


def generate_report(
    config: Config,
    completed: bool,
    test_results: list[ReportPackageData],
    report_output_path: Path,
) -> None:
    """Generate a report based on the execution status of the tested packages."""

    jinja_context: dict[str, Any] = {
        "status": "Complete" if completed else "In Progress",
        "last_updated": datetime.now(UTC).strftime("%Y-%m-%d %H:%M:%S UTC"),
        "total_packages_count": len(test_results),
        "patched_packages_count": sum(
            1
            for p in test_results
            if p.patched.status != "skipped" or p.original.status != "skipped"
        ),
        "unpatched_packages_count": sum(
            1
            for p in test_results
            if p.patched.status == "skipped" and p.original.status == "skipped"
        ),
        "ok_count": sum(
            1
            for p in test_results
            if p.patched.status == "success"
            or (p.original.status == "success" and p.patched.status == "skipped")
        ),
        "regression_count": sum(
            1
            for p in test_results
            if p.patched.status == "failed" and p.original.status == "success"
        ),
        "still_failing_count": sum(
            1
            for p in test_results
            if p.original.status == "failed" and p.patched.status != "success"
        ),
        "packages": test_results,
        "packages_without_patches": [
            p
            for p in test_results
            if p.patched.status == "skipped" and p.original.status != "skipped"
        ],
        "patched_packages": [
            p for p in test_results if p.patched.status != "skipped" and p.info.patches
        ],
        "packages_with_patched_dependencies": [
            p
            for p in test_results
            if p.patched.status != "skipped" and not p.info.patches
        ],
    }
    # render the invenio-testrig/templates/report.html template with the collected data and save to report_output_path/report.html
    from jinja2 import Environment, FileSystemLoader

    env = Environment(
        loader=FileSystemLoader(searchpath=Path(__file__).parent / "templates")
    )
    template = env.get_template("report.html")
    report_content = template.render(**jinja_context)

    report_output_path.mkdir(parents=True, exist_ok=True)
    (report_output_path / "index.html").write_text(report_content)


def load_test_artifacts(
    config: Config, artefacts_path: Path
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
    package_data: dict[str, ReportPackageData] = {
        package_name: ReportPackageData(
            info=package_info,
            artefact_dir=package_name,
            patched=ExecutionStatus(status="skipped", package=package_info),
            original=ExecutionStatus(status="skipped", package=package_info),
        )
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
                loaded_status = load_execution_status(status_file)
                match status_file.stem:
                    case "patched_status":
                        package_data[package_name].patched = loaded_status
                    case "original_status":
                        package_data[package_name].original = loaded_status
                    case _:
                        click.secho(
                            f"⚠️  Found unexpected status file '{status_file.name}' for package '{package_name}', skipping",
                            fg="yellow",
                            err=True,
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
