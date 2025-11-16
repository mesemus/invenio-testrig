#!/usr/bin/env python3
"""
Add a new summary line to reports.md after the table header.

Usage: add_summary_line.py <reports_md_path> <test_name> <report_dir> <status>

Inserts a new row into the reports table after the separator line.
The report_dir should be the directory name (e.g., "2025-11-15_20-49-34").
The test_name is an optional description of the test run.
"""

import re
import sys
from pathlib import Path


def add_summary_line(
    reports_md_path: Path, test_name: str, report_dir: str, status: str
) -> None:
    """Add a new summary line to reports.md."""

    if not reports_md_path.exists():
        print(f"Error: {reports_md_path} does not exist", file=sys.stderr)
        sys.exit(1)

    # Read the file
    with reports_md_path.open("r", encoding="utf-8") as f:
        lines = f.readlines()

    # Find the table separator line using regex
    # Matches lines like |---|---| or |-----|------|
    separator_pattern = re.compile(r"^\|[\|\-]+\|$")
    separator_index = None

    for i, line in enumerate(lines):
        if separator_pattern.match(line):
            separator_index = i
            break

    if separator_index is None:
        print("Error: Could not find table separator line", file=sys.stderr)
        sys.exit(1)

    # Create markdown link from report directory name
    # Convert underscores to spaces for display
    display_name = report_dir.replace("_", " ")
    report_link = f"[{display_name}](./results/{report_dir}/report.md)"

    # Use test_name if provided, otherwise use empty string
    test_name_display = test_name if test_name else ""

    # Create new row with test name as first column
    new_row = f"| {test_name_display} | {report_link} | {status} |\n"

    # Insert after separator
    lines.insert(separator_index + 1, new_row)

    # Write back
    with reports_md_path.open("w", encoding="utf-8") as f:
        f.writelines(lines)


def main() -> None:
    """Main entry point."""
    if len(sys.argv) != 5:
        print(
            "Usage: add_summary_line.py <reports_md_path> <test_name> <report_dir> <status>",
            file=sys.stderr,
        )
        sys.exit(1)

    reports_md_path = Path(sys.argv[1])
    test_name = sys.argv[2]
    report_dir = sys.argv[3]
    status = sys.argv[4]

    try:
        add_summary_line(reports_md_path, test_name, report_dir, status)
        print(f"✓ Updated {reports_md_path}")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
