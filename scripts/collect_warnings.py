#!/usr/bin/env python3
"""
Collect warnings from all package test results and generate a summary report.

Usage: collect_warnings.py <artifacts_dir> <output_file>

Aggregates warnings from all package result-summary.json files and generates
a markdown report with warnings sorted by total occurrence count.
"""

import json
import sys
from collections import defaultdict
from pathlib import Path


def collect_warnings_by_log_type(
    artifacts_dir: Path,
) -> dict[str, dict[str, dict[str, int]]]:
    """
    Collect warnings from all package result-summary.json files, organized by log type.

    Returns:
        Dict mapping log_type to warning text to package counts.
        Structure: {log_type: {warning_text: {package_name: count}}}
    """
    warnings_by_type: dict[str, dict[str, dict[str, int]]] = defaultdict(
        lambda: defaultdict(lambda: defaultdict(int))
    )

    # Find all result-summary.json files
    for result_file in artifacts_dir.glob("*/result-summary.json"):
        try:
            with result_file.open("r") as f:
                data = json.load(f)

            package_name = data.get("package", "unknown")
            warnings = data.get("warnings", {})

            # Process warnings for each log type (original, patched)
            for log_type, warning_dict in warnings.items():
                if isinstance(warning_dict, dict):
                    for warning_text, count in warning_dict.items():
                        warnings_by_type[log_type][warning_text][package_name] = count
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: Failed to process {result_file}: {e}", file=sys.stderr)
            continue

    return {k: dict(v) for k, v in warnings_by_type.items()}


def calculate_total_occurrences(package_counts: dict[str, int]) -> int:
    """Calculate total occurrences of a warning across all packages."""
    return sum(package_counts.values())


def generate_warnings_report(
    warnings_by_type: dict[str, dict[str, dict[str, int]]], output_file: Path
) -> None:
    """Generate markdown report with collected warnings organized by log type."""

    if not warnings_by_type:
        with output_file.open("w", encoding="utf-8") as f:
            f.write("## Collected Warnings\n\n")
            f.write("No warnings found in any package.\n")
        return

    with output_file.open("w", encoding="utf-8") as f:
        f.write("## Collected Warnings\n\n")

        # Process each log type (original, patched)
        for log_type in sorted(warnings_by_type.keys(), reverse=True):
            warnings_data = warnings_by_type[log_type]

            if not warnings_data:
                continue

            f.write(f"### {log_type.capitalize()}\n\n")

            # Sort warnings by total count (descending) then by text (ascending)
            sorted_warnings = sorted(
                warnings_data.items(),
                key=lambda x: (-calculate_total_occurrences(x[1]), x[0]),
            )

            for idx, (warning_text, package_counts) in enumerate(sorted_warnings, 1):
                total_count = calculate_total_occurrences(package_counts)
                f.write(
                    f"#### Warning {idx} - {total_count} occurrence{'s' if total_count > 1 else ''}\n\n"
                )
                f.write(f"{warning_text}\n\n")

                # Create table of packages
                f.write("| Package | Count |\n")
                f.write("|---------|-------|\n")

                # Sort packages by count descending
                package_list = sorted(
                    package_counts.items(), key=lambda x: (-x[1], x[0])
                )

                for pkg, count in package_list:
                    f.write(f"| `{pkg}` | {count} |\n")

                f.write("\n")

            f.write("\n")


def main() -> None:
    """Main entry point."""
    if len(sys.argv) != 3:
        print(
            "Usage: collect_warnings.py <artifacts_dir> <output_file>",
            file=sys.stderr,
        )
        sys.exit(1)

    artifacts_dir = Path(sys.argv[1])
    output_file = Path(sys.argv[2])

    if not artifacts_dir.exists() or not artifacts_dir.is_dir():
        print(f"Error: {artifacts_dir} is not a valid directory", file=sys.stderr)
        sys.exit(1)

    try:
        # Collect warnings from all packages
        warnings_data = collect_warnings_by_log_type(artifacts_dir)

        total_warnings = sum(len(warnings) for warnings in warnings_data.values())
        print(f"Collected {total_warnings} unique warning(s) from all packages")

        # Generate report
        generate_warnings_report(warnings_data, output_file)
        print(f"✓ Generated {output_file}")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
