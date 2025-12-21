#!/usr/bin/env python3
"""
Extract Invenio packages to test from uv.lock file.

This script extracts package names from a uv.lock file, filters them based on
configuration, and outputs them as a JSON array for GitHub Actions matrix.
"""

import argparse
import json
import re
import sys
from pathlib import Path

import json5


def parse_uv_lock(lock_file_path):
    """Parse uv.lock file and extract package names."""
    packages = set()

    with open(lock_file_path, "r") as f:
        content = f.read()

    # Extract package names from [[package]] sections
    # Looking for lines like: name = "package-name"
    pattern = r'name\s*=\s*"([^"]+)"'
    matches = re.findall(pattern, content)
    packages.update(matches)

    return packages


def load_config(config_path):
    """Load repository configuration from JSON5."""
    with open(config_path, "r") as f:
        return json5.load(f)


def filter_packages(packages, config):
    """Filter packages based on configuration rules."""
    filtered = set()

    for repo_config in config.get("repositories", []):
        include_patterns = [
            re.compile(pattern) for pattern in repo_config.get("package-regexes", [])
        ]
        exclude_patterns = [
            re.compile(pattern)
            for pattern in repo_config.get("exclude-package-regexes", [])
        ]

        for package in packages:
            # Check if package matches include patterns
            if any(pattern.match(package) for pattern in include_patterns):
                # Check if package doesn't match exclude patterns
                if not any(pattern.match(package) for pattern in exclude_patterns):
                    filtered.add(package)

    return sorted(filtered)


def get_already_tested_packages(previous_report_path):
    """Get list of packages that were already tested in a previous run."""
    if not previous_report_path:
        return []

    packages_dir = Path(previous_report_path) / "packages"
    if not packages_dir.exists():
        return []

    # List all subdirectories in the packages directory
    tested = [d.name for d in packages_dir.iterdir() if d.is_dir()]
    return sorted(tested)


def filter_by_package_list(packages, filter_list):
    """Filter packages to only include those in the filter list."""
    if not filter_list:
        return packages

    # Parse the filter list (can be comma or space separated)
    filter_packages = set()
    for item in filter_list:
        # Split by comma and/or spaces
        parts = re.split(r"[,\s]+", item.strip())
        filter_packages.update(p.strip() for p in parts if p.strip())

    # Only keep packages that are in the filter list
    return sorted([pkg for pkg in packages if pkg in filter_packages])


def main():
    parser = argparse.ArgumentParser(
        description="Extract Invenio packages to test from uv.lock"
    )
    parser.add_argument("lock_file", help="Path to uv.lock file")
    parser.add_argument("config_file", help="Path to config.json5 file")
    parser.add_argument("output_file", help="Path to output shell script file")
    parser.add_argument(
        "--previous-report", help="Path to previous report directory to continue from"
    )
    parser.add_argument(
        "--filter-packages",
        nargs="*",
        help="Space or comma separated list of packages to test",
    )

    args = parser.parse_args()

    # Extract packages from lock file
    all_packages = parse_uv_lock(args.lock_file)

    # Load configuration and filter packages
    config = load_config(args.config_file)
    filtered_packages = filter_packages(all_packages, config)

    # Apply package filter if provided
    if args.filter_packages:
        filtered_packages = filter_by_package_list(
            filtered_packages, args.filter_packages
        )

    # Get already tested packages if continuing from previous run
    already_tested = get_already_tested_packages(args.previous_report)

    # Determine which packages to test
    packages_to_test = [pkg for pkg in filtered_packages if pkg not in already_tested]
    # Output as JSON arrays
    packages_json = json.dumps(packages_to_test)
    done_packages_json = json.dumps(already_tested)

    # Write to shell script file
    with open(args.output_file, "w") as f:
        f.write(f"packages='{packages_json}'\n")
        f.write(f"done_packages='{done_packages_json}'\n")

    print(f"Total packages found: {len(all_packages)}")
    print(f"Filtered packages: {len(filtered_packages)}")
    print(f"Already tested: {len(already_tested)}")
    print(f"To test: {len(packages_to_test)}")

    if args.filter_packages:
        print(f"Package filter applied: {args.filter_packages}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
