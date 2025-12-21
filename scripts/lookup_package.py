#!/usr/bin/env python3
"""
Lookup package repository information from config.json5.

Usage: lookup_package.py <config.json5> <package-name>

Outputs bash-compatible environment variable assignments:
  original_repository_url="..."
  original_repository_branch="..."
  patched_repository_url="..."
  patched_repository_branch="..."
"""

import re
import sys
from pathlib import Path

import json5


def package_matches(package_name: str, regexes: list[str]) -> bool:
    """Check if package name matches any of the given regex patterns."""
    for pattern in regexes:
        # Add anchors to ensure full string match
        full_pattern = f"^{pattern}$"
        if re.fullmatch(full_pattern, package_name):
            return True
    return False


def lookup_package(config_path: Path, package_name: str) -> None:
    """Look up package information and return repository URLs and branches."""

    # Load config.json5 with json5
    with config_path.open("r") as f:
        config = json5.load(f)

    # Get patches from config
    patches = config.get("patches", {})

    # Find matching repository configuration
    original_url = None
    original_branch = ""

    for repo in config.get("repositories", []):
        base_url = repo.get("base_url", "")
        branch = repo.get("branch", "")
        package_regexes = repo.get("package-regexes", [])
        exclude_package_regexes = repo.get("exclude-package-regexes", [])

        # Check if package matches any include regex
        if not package_matches(package_name, package_regexes):
            continue

        # Check if package matches any exclude regex
        if package_matches(package_name, exclude_package_regexes):
            continue

        original_url = f"{base_url}/{package_name}"
        original_branch = branch
        break

    # Default to inveniosoftware if no match found
    if not original_url:
        raise ValueError(f"Package '{package_name}' not found in configuration.")

    # Look up patch information
    patched_url = ""
    patched_branch = ""

    if package_name in patches:
        patch_info = patches[package_name]
        patched_url = patch_info.get("git", "")
        patched_branch = patch_info.get("branch", "")

    # Output bash-compatible variable assignments
    print(f'original_repository_url="{original_url}"')
    print(f'original_repository_branch="{original_branch}"')
    print(f'patched_repository_url="{patched_url}"')
    print(f'patched_repository_branch="{patched_branch}"')


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(
            "Usage: lookup_package.py <config.json5> <package-name>",
            file=sys.stderr,
        )
        sys.exit(1)

    config_path = Path(sys.argv[1])
    package_name = sys.argv[2]

    try:
        lookup_package(config_path, package_name)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
