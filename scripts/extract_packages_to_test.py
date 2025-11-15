#!/usr/bin/env python3
"""
Extract packages to test from uv.lock file based on config.json rules.

Usage: extract_packages_to_test.py <uv_lock_path> <config.json> <variables.sh>

Extracts package names from uv.lock that match the regex patterns in config.json
and don't match exclude patterns, then outputs them to variables.sh.
"""

import json
import re
import sys
from pathlib import Path


def package_matches(package_name: str, regexes: list[str]) -> bool:
    """Check if package name matches any of the given regex patterns."""
    for pattern in regexes:
        # Add anchors to ensure full string match
        full_pattern = f"^{pattern}$"
        if re.fullmatch(full_pattern, package_name):
            return True
    return False


def extract_packages_from_uv_lock(uv_lock_path: Path) -> list[str]:
    """Extract all package names from uv.lock file."""
    packages: list[str] = []

    with uv_lock_path.open("r") as f:
        for line in f:
            line = line.strip()
            if line.startswith('name = "'):
                # Extract package name from: name = "package-name"
                package_name = line[8:-1]  # Remove 'name = "' and trailing '"'
                packages.append(package_name)

    return packages


def filter_packages(packages: list[str], config_path: Path) -> list[str]:
    """Filter packages based on config.json rules."""

    # Load config
    with config_path.open("r") as f:
        config = json.load(f)

    filtered_packages: list[str] = []

    for package_name in packages:
        matched = False

        # Check each repository configuration
        for repo in config.get("repositories", []):
            package_regexes = repo.get("package-regexes", [])
            exclude_package_regexes = repo.get("exclude-package-regexes", [])

            # Check if package matches any include regex
            if not package_matches(package_name, package_regexes):
                continue

            # Check if package matches any exclude regex
            if package_matches(package_name, exclude_package_regexes):
                print(f"⏭️  Excluding {package_name} (matches exclude pattern)")
                matched = False
                break

            matched = True
            break

        if matched:
            filtered_packages.append(package_name)

    return filtered_packages


def extract_packages(uv_lock_path: Path, config_path: Path, output_path: Path) -> None:
    """Extract and filter packages, then write to variables.sh."""

    # Extract all packages from uv.lock
    all_packages = extract_packages_from_uv_lock(uv_lock_path)
    print(f"Found {len(all_packages)} packages in uv.lock")

    # Filter based on config
    filtered_packages = filter_packages(all_packages, config_path)
    print(f"Filtered to {len(filtered_packages)} packages")

    # Sort for consistency
    filtered_packages.sort()

    # Write to variables.sh as JSON array
    packages_json = json.dumps(filtered_packages)

    with output_path.open("w") as f:
        f.write(f"packages='{packages_json}'\n")

    print(f"\n✓ Extracted {len(filtered_packages)} packages to test")
    if filtered_packages:
        print(f"Packages: {', '.join(filtered_packages)}")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(
            "Usage: extract_packages_to_test.py <uv_lock_path> <config.json> <variables.sh>",
            file=sys.stderr,
        )
        sys.exit(1)

    uv_lock_path = Path(sys.argv[1])
    config_path = Path(sys.argv[2])
    output_path = Path(sys.argv[3])

    try:
        extract_packages(uv_lock_path, config_path, output_path)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
