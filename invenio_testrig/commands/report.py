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
    click.secho(
        f"🔍 Generating report with {len(test_results)} test results", fg="cyan"
    )
    click.secho(f"🔍 Report output path: {report_output_path}", fg="cyan")
    click.secho(f"🔍 Completed: {completed}", fg="cyan")

    # Filter out packages that are still pending (both patched and original are pending)
    test_results = [
        p
        for p in test_results
        if not (p.patched.status == "pending" and p.original.status == "pending")
    ]
    click.secho(
        f"🔍 After filtering pending: {len(test_results)} test results", fg="cyan"
    )

    # Debug: Show summary of test results
    patched_not_skipped = sum(
        1 for p in test_results if p.patched.status not in ("skipped", "pending")
    )
    original_not_skipped = sum(
        1 for p in test_results if p.original.status not in ("skipped", "pending")
    )
    click.secho(f"🔍 Patched results (not skipped): {patched_not_skipped}", fg="cyan")
    click.secho(f"🔍 Original results (not skipped): {original_not_skipped}", fg="cyan")

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
    click.secho("🔍 Report statistics:", fg="cyan")
    click.secho(
        f"   - Total packages: {jinja_context['total_packages_count']}", fg="cyan"
    )
    click.secho(
        f"   - Patched packages: {jinja_context['patched_packages_count']}", fg="cyan"
    )
    click.secho(
        f"   - Unpatched packages: {jinja_context['unpatched_packages_count']}",
        fg="cyan",
    )
    click.secho(f"   - OK count: {jinja_context['ok_count']}", fg="cyan")
    click.secho(
        f"   - Regression count: {jinja_context['regression_count']}", fg="cyan"
    )
    click.secho(
        f"   - Still failing count: {jinja_context['still_failing_count']}", fg="cyan"
    )
    click.secho(
        f"   - Packages without patches: {len(jinja_context['packages_without_patches'])}",
        fg="cyan",
    )
    click.secho(
        f"   - Patched packages: {len(jinja_context['patched_packages'])}", fg="cyan"
    )
    click.secho(
        f"   - Packages with patched deps: {len(jinja_context['packages_with_patched_dependencies'])}",
        fg="cyan",
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
    click.secho(f"🔍 Report file written to: {report_file}", fg="cyan")
    click.secho(f"🔍 Report file size: {report_file.stat().st_size} bytes", fg="cyan")
    click.secho(
        f"🔍 Report content length: {len(report_content)} characters", fg="cyan"
    )


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
    click.secho(f"🔍 Loading test artifacts from: {artefacts_path}", fg="cyan")
    click.secho(f"🔍 Artifacts path exists: {artefacts_path.exists()}", fg="cyan")
    click.secho(
        f"🔍 Number of tested packages in config: {len(config.tested_packages)}",
        fg="cyan",
    )

    package_data: dict[str, ReportPackageData] = {
        package_name: ReportPackageData(
            info=package_info,
            artefact_dir=f"artifacts/{package_name}",
            patched=ExecutionStatus(status="pending", package=package_info),
            original=ExecutionStatus(status="pending", package=package_info),
        )
        for package_name, package_info in config.tested_packages.items()
    }

    click.secho(
        f"🔍 Initialized package_data dict with {len(package_data)} entries", fg="cyan"
    )

    if not artefacts_path.exists():
        click.secho(
            f"⚠️  Artifacts path does not exist: {artefacts_path}", fg="yellow", err=True
        )
        return sorted(
            package_data.values(), key=lambda p: (4, p.info.reference.package)
        )

    dir_items = list(artefacts_path.iterdir())
    click.secho(f"🔍 Found {len(dir_items)} items in artifacts directory", fg="cyan")

    for package_dir in dir_items:
        package_name = package_dir.name
        click.secho(
            f"🔍 Checking item: {package_name} (is_dir: {package_dir.is_dir()})",
            fg="cyan",
        )

        if package_name not in package_data:
            click.secho(
                f"⚠️  Found artefacts for package '{package_name}' which is not in the config, skipping",
                fg="yellow",
                err=True,
            )
            continue
        if package_dir.is_dir():
            status_files = list(package_dir.glob("*_status.json"))
            click.secho(
                f"🔍 Package '{package_name}': Found {len(status_files)} status files",
                fg="cyan",
            )
            # the directory is present, thus the package is not pending
            package_data[package_name].patched.status = "skipped"
            package_data[package_name].original.status = "skipped"

            # now overwrite with actual status if status files are present
            for status_file in status_files:
                click.secho(f"🔍   Loading: {status_file.name}", fg="cyan")
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
