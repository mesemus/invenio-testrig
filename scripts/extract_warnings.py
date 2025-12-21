#!/usr/bin/env python3
"""
Extract warnings from test logs and add them to result-summary.json.

Usage: extract_warnings.py <log_path> <log_type> <result_summary_path> <warnings_file>

Extracts Python warnings (e.g., DeprecationWarning, RuntimeWarning, etc.) from test logs
by matching lines containing '*Warning:' patterns. The extracted warnings include only
the warning type and message, with file paths and line numbers removed.
Warnings are deduplicated with counts and added to result-summary.json.
Also generates a markdown file with warnings sorted by occurrence count.
"""

import json
import re
import sys
from collections import defaultdict
from pathlib import Path


def extract_warnings(log_path: Path) -> dict[str, int]:
    """Extract and count warnings from a log file."""
    warnings: dict[str, int] = defaultdict(int)
    # Match lines containing "Warning:" and extract from the warning type onwards
    # Pattern captures the warning type (e.g., DeprecationWarning) and the message
    warning_pattern = re.compile(r"(\w+Warning:.*?)$")

    if not log_path.exists():
        return {}

    with log_path.open("r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            match = warning_pattern.search(line)
            if match:
                warning_text = match.group(1).strip()
                warnings[warning_text] += 1

    return dict(warnings)


def generate_warnings_markdown(
    warnings: dict[str, int], warnings_file: Path, log_type: str
) -> None:
    """Generate markdown file with warnings sorted by occurrence count."""
    if not warnings:
        return

    # Sort warnings by count (descending) then by text (ascending)
    sorted_warnings = sorted(warnings.items(), key=lambda x: (-x[1], x[0]))

    with warnings_file.open("w", encoding="utf-8") as f:
        f.write(f"# Warnings ({log_type})\n\n")
        for idx, (warning_text, count) in enumerate(sorted_warnings, 1):
            f.write(
                f"## Warning {idx} - {count} occurrence{'s' if count > 1 else ''}\n\n"
            )
            f.write(f"{warning_text}\n\n")


def update_result_summary(
    result_summary_path: Path, log_type: str, warnings: dict[str, int]
) -> None:
    """Update result-summary.json with warning information."""

    # Load existing result summary
    if result_summary_path.exists():
        with result_summary_path.open("r") as f:
            result_summary = json.load(f)
    else:
        result_summary = {}

    # Initialize warnings structure if it doesn't exist
    if "warnings" not in result_summary:
        result_summary["warnings"] = {}

    if "warnings_count" not in result_summary:
        result_summary["warnings_count"] = {}

    # Add warnings for this log type
    result_summary["warnings"][log_type] = warnings

    # Calculate and add cumulative warning count
    total_count = sum(warnings.values())
    result_summary["warnings_count"][log_type] = total_count

    # Write updated result summary
    with result_summary_path.open("w") as f:
        json.dump(result_summary, f, indent=2)


def main() -> None:
    """Main entry point."""
    if len(sys.argv) != 5:
        print(
            "Usage: extract_warnings.py <log_path> <log_type> <result_summary_path> <warnings_file>",
            file=sys.stderr,
        )
        sys.exit(1)

    log_path = Path(sys.argv[1])
    log_type = sys.argv[2]
    result_summary_path = Path(sys.argv[3])
    warnings_file = Path(sys.argv[4])

    try:
        # Extract warnings from log
        warnings = extract_warnings(log_path)

        if warnings:
            print(f"Found {len(warnings)} unique warning(s) in {log_type} log:")
            for warning_text, count in warnings.items():
                print(f"  [{count}x] {warning_text}")
        else:
            print(f"No warnings found in {log_type} log")

        # Update result summary
        update_result_summary(result_summary_path, log_type, warnings)
        print(f"✓ Updated {result_summary_path}")

        # Generate warnings markdown file
        if warnings:
            generate_warnings_markdown(warnings, warnings_file, log_type)
            print(f"✓ Generated {warnings_file}")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
