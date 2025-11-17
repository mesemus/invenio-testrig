#!/usr/bin/env python3
"""
Generate markdown report from test artifacts.

Usage: generate_report.py <artifacts_dir> <report_dir> <report_file>

Processes test result artifacts and generates a comprehensive markdown report
using Jinja2 templates.
"""

import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from jinja2 import Environment, FileSystemLoader


def artefact_iterator(artefact_dir: Path):
    """Iterate over artifact directories containing result-summary.json."""
    for d in artefact_dir.glob("*"):
        if not d.is_dir():
            continue
        if not (d / "result-summary.json").exists():
            continue
        yield d


def get_status_emoji(outcome: str) -> str:
    """Get status emoji and text for test outcome."""
    status_map = {
        "success": "✅ Pass",
        "failed": "❌ Fail",
        "skipped": "⏭️  Skip",
    }
    return status_map.get(outcome, "❓ Unknown")


def get_build_status_emoji(outcome: str) -> str:
    """Get build status emoji and text."""
    status_map = {
        "success": "✅ Success",
        "failed": "❌ Failed",
        "skipped": "⏭️  Skipped",
    }
    return status_map.get(outcome, "❓ Unknown")


def create_package_links(report_dir: Path, package: str) -> str:
    """Create links for package test outputs."""
    package_dir = report_dir / "packages" / package
    links = []

    link_files = [
        ("test-output-original.txt", "original"),
        ("test-output-patched.txt", "patched"),
        ("test-diff.txt", "diff"),
        ("warnings-original.md", "warnings-original"),
        ("warnings-patched.md", "warnings-patched"),
    ]

    for filename, link_text in link_files:
        if (package_dir / filename).exists():
            links.append(f"[{link_text}](packages/{package}/{filename})")

    return " ".join(links) if links else ""


def process_package(
    result_summary: dict[str, Any], report_dir: Path, package: str
) -> dict[str, Any]:
    """Process a single package result summary."""
    patched_pkgs = result_summary.get("patched_packages", "")
    if isinstance(patched_pkgs, str) and "\n" in patched_pkgs:
        patched_pkgs = patched_pkgs.replace("\n", " ")

    original_outcome = result_summary.get("original_tests_outcome", "skipped")
    patched_outcome = result_summary.get("patched_tests_outcome", "skipped")

    result_icon = result_summary.get("result_icon", "")
    result_text = result_summary.get("result_text", "")
    result_status = (
        f"{result_icon} {result_text}"
        if result_icon and result_icon != "null"
        else "❓ Unknown"
    )

    links = create_package_links(report_dir, package)
    display = f"`{package}` <br/> {links}" if links else f"`{package}`"

    return {
        "name": package,
        "display": display,
        "patched_pkgs": patched_pkgs,
        "original_status": get_status_emoji(original_outcome),
        "patched_status": get_status_emoji(patched_outcome),
        "result_status": result_status,
        "status": get_build_status_emoji(original_outcome),
    }


def calculate_statistics(artifacts_dir: Path) -> dict[str, int]:
    """Calculate overall statistics from artifacts."""
    stats = {
        "total": 0,
        "patched": 0,
        "unpatched": 0,
        "fixed": 0,
        "regression": 0,
        "no_change": 0,
        "still_failing": 0,
    }

    for result_dir in artefact_iterator(artifacts_dir):
        summary_file = result_dir / "result-summary.json"
        if not summary_file.exists():
            continue

        with summary_file.open("r") as f:
            summary = json.load(f)

        stats["total"] += 1
        applies = summary.get("patch_applies", False)

        if applies:
            stats["patched"] += 1
            result = summary.get("result", "")
            if result == "fixed":
                stats["fixed"] += 1
            elif result == "regression":
                stats["regression"] += 1
            elif result == "still-failing":
                stats["still_failing"] += 1
            else:
                stats["no_change"] += 1
        else:
            stats["unpatched"] += 1

    return stats


def load_configured_patches(patches_json_path: Path) -> list[dict[str, str]]:
    """Load configured patches from patches.json."""
    if not patches_json_path.exists():
        return []

    try:
        with patches_json_path.open("r") as f:
            patches_data = json.load(f)

        configured_patches = []
        for package, info in patches_data.items():
            repo_url = info.get("url", "").rstrip(".git")
            branch = info.get("branch", "")

            # Create tree URL only if branch is provided
            if branch:
                repo_tree_url = f"{repo_url}/tree/{branch}"
            else:
                repo_tree_url = repo_url

            configured_patches.append(
                {
                    "package": package,
                    "repo_url": repo_url,
                    "branch": branch,
                    "repo_tree_url": repo_tree_url,
                }
            )

        return configured_patches
    except Exception as e:
        print(f"Warning: Could not read patches.json: {e}", file=sys.stderr)
        return []


def generate_report(artifacts_dir: Path, report_dir: Path, report_file: Path) -> None:
    """Generate the markdown report."""

    # Calculate statistics
    stats = calculate_statistics(artifacts_dir)

    # Collect packages by category
    patched_packages: list[dict[str, Any]] = []
    unpatched_packages: list[dict[str, Any]] = []
    dependency_packages: list[dict[str, Any]] = []

    for result_dir in artefact_iterator(artifacts_dir):
        summary_file = result_dir / "result-summary.json"
        if not summary_file.exists():
            continue

        with summary_file.open("r") as f:
            summary = json.load(f)

        package = summary.get("package")
        has_patch = summary.get("has_patch", False)
        applies = summary.get("patch_applies", False)
        if package is None:
            package = result_dir.name.replace("test-results-", "")

        package_data = process_package(summary, report_dir, package)

        if has_patch:
            patched_packages.append(package_data)
        elif applies:
            dependency_packages.append(package_data)
        else:
            unpatched_packages.append(package_data)

    # Load warnings if available
    warnings_file = report_dir / "collected-warnings.md"
    warnings_content = ""
    if warnings_file.exists():
        warnings_content = warnings_file.read_text()

    # Load configured patches from patches.json
    patches_json_path = Path(__file__).parent.parent / "patches.json"
    configured_patches = load_configured_patches(patches_json_path)

    # Setup Jinja2 environment
    template_dir = Path(__file__).parent / "templates"
    env = Environment(
        loader=FileSystemLoader(template_dir), trim_blocks=True, lstrip_blocks=True
    )
    template = env.get_template("report.md.jinja")

    # Render template
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    content = template.render(
        timestamp=timestamp,
        stats=stats,
        configured_patches=configured_patches,
        patched_packages=patched_packages,
        unpatched_packages=unpatched_packages,
        dependency_packages=dependency_packages,
        warnings_content=warnings_content,
    )

    # Write report
    report_file.parent.mkdir(parents=True, exist_ok=True)
    report_file.write_text(content)
    print(f"✓ Generated report: {report_file}")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(
            "Usage: generate_report.py <artifacts_dir> <report_dir> <report_file>",
            file=sys.stderr,
        )
        sys.exit(1)

    artifacts_dir = Path(sys.argv[1])
    report_dir = Path(sys.argv[2])
    report_file = Path(sys.argv[3])

    try:
        generate_report(artifacts_dir, report_dir, report_file)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        import traceback

        traceback.print_exc()
        sys.exit(1)
