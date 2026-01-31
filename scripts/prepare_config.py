#!/usr/bin/env python3
"""
Prepare configuration: resolve pull request URLs and load test configuration.

This script reads a config.yaml file, resolves GitHub PR URLs to git+branch format,
saves the resolved configuration, and outputs test configuration values for GitHub Actions.

Usage: prepare_config.py <input_config.yaml> <output_config.json>

Outputs key=value pairs for GitHub Actions to stdout.
"""

import json
import re
import sys
from pathlib import Path
from urllib.request import Request, urlopen

import yaml


def load_config(config_path):
    """Load config.yaml file."""
    with config_path.open("r") as f:
        return yaml.safe_load(f)


def save_config(config, output_path):
    """Save config to JSON file."""
    output_file = Path(output_path)
    with output_file.open("w") as f:
        json.dump(config, f, indent=4)
        f.write("\n")


def is_github_pr_reference(ref):
    """Check if the ref is a GitHub pull request reference (URL or org/repo#prno format)."""
    if not isinstance(ref, str):
        return False
    # Check for full URL format
    url_pattern = r"^https://github\.com/([^/]+)/([^/]+)/pull/(\d+)$"
    if re.match(url_pattern, ref):
        return True
    # Check for org/repo#prno format
    short_pattern = r"^([^/]+)/([^/#]+)#(\d+)$"
    return re.match(short_pattern, ref) is not None


def parse_github_pr_reference(ref):
    """Parse GitHub PR reference (URL or org/repo#prno) and return owner, repo, pr_number."""
    # Try full URL format first
    url_pattern = r"^https://github\.com/([^/]+)/([^/]+)/pull/(\d+)$"
    match = re.match(url_pattern, ref)
    if match:
        return match.group(1), match.group(2), match.group(3)

    # Try org/repo#prno format
    short_pattern = r"^([^/]+)/([^/#]+)#(\d+)$"
    match = re.match(short_pattern, ref)
    if match:
        return match.group(1), match.group(2), match.group(3)

    return None, None, None


def get_pr_info(owner, repo, pr_number):
    """Fetch PR information from GitHub API.

    Returns:
        tuple: (git_url, branch, is_merged, is_closed) or (None, None, None, None) on error
    """
    api_url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}"

    try:
        # Create request with User-Agent header (required by GitHub API)
        request = Request(api_url)
        request.add_header("User-Agent", "invenio-testrig-resolve-pr")
        request.add_header("Accept", "application/vnd.github.v3+json")

        with urlopen(request, timeout=10) as response:
            data = json.loads(response.read().decode("utf-8"))

            # Get PR state information
            is_merged = data.get("merged", False)
            is_closed = data["state"] == "closed"

            # If merged, use the base branch; otherwise use head branch
            if is_merged:
                target = data["base"]
            else:
                target = data["head"]

            git_url = target["repo"]["clone_url"]
            branch = target["ref"]

            return git_url, branch, is_merged, is_closed
    except Exception as e:
        print(f"Error fetching PR info: {e}", file=sys.stderr)
        return None, None, None, None


def resolve_branches(config):
    """Resolve branch string references (org/repo@branch) to git+branch format."""
    patches = config.get("patches") or {}

    for package_name, patch_info in list(patches.items()):
        # PR references have already been handled at this point
        if isinstance(patch_info, str):
            # Check if it matches org/repo@branch pattern
            branch_pattern = r"^([^/]+)/([^/@]+)@(.+)$"
            match = re.match(branch_pattern, patch_info)

            if match:
                owner, repo, branch = match.groups()
                git_url = f"https://github.com/{owner}/{repo}.git"
                patches[package_name] = {"git": git_url, "branch": branch}
                print(
                    f"Resolved {package_name}: {patch_info} -> {git_url} @ {branch}",
                    file=sys.stderr,
                )
            else:
                print(
                    f"Error: Invalid patch format for {package_name}: '{patch_info}'",
                    file=sys.stderr,
                )
                print(
                    "  Expected format: org/repo@branch or org/repo#prno",
                    file=sys.stderr,
                )
                sys.exit(1)


def resolve_pull_requests(config):
    """Resolve all PR URLs in patches to git+branch format."""
    patches = config.get("patches") or {}
    modified = False

    for package_name, patch_info in list(patches.items()):
        if is_github_pr_reference(patch_info):
            print(
                f"Resolving PR reference for {package_name}: {patch_info}",
                file=sys.stderr,
            )

            owner, repo, pr_number = parse_github_pr_reference(patch_info)
            if owner and repo and pr_number:
                git_url, branch, is_merged, is_closed = get_pr_info(
                    owner, repo, pr_number
                )

                if git_url and branch:
                    # Skip cancelled/closed PRs that were not merged
                    if is_closed and not is_merged:
                        print(
                            "  ⊗ PR is closed without being merged, removing from patches",
                            file=sys.stderr,
                        )
                        del patches[package_name]
                        modified = True
                    else:
                        status = "merged" if is_merged else "open"
                        patches[package_name] = {"git": git_url, "branch": branch}
                        print(
                            f"  ✓ Resolved to: {git_url} @ {branch} (PR {status})",
                            file=sys.stderr,
                        )
                        modified = True
                else:
                    print("  ✗ Failed to resolve PR reference", file=sys.stderr)
            else:
                print("  ✗ Invalid PR reference format", file=sys.stderr)

    return modified


def output_test_config(config):
    """Output test configuration values for GitHub Actions."""
    # Extract values with defaults
    test_name = config.get("name", "")
    test_timeout = config.get("test_timeout", 90)
    packages = config.get("packages", [])

    # Convert packages list to space-separated string
    packages_str = " ".join(packages) if packages else ""

    # Output to stdout for parsing by GitHub Actions
    print(f"test_name={test_name}")
    print(f"test_timeout={test_timeout}")
    print(f"packages={packages_str}")


def main():
    """Main entry point."""
    if len(sys.argv) != 3:
        print(
            "Usage: prepare_config.py <input_config.yaml> <output_config.json>",
            file=sys.stderr,
        )
        sys.exit(1)

    config_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])

    if not config_path.exists():
        print(f"Error: Config file not found: {config_path}", file=sys.stderr)
        sys.exit(1)

    try:
        print(f"Loading config from: {config_path}", file=sys.stderr)
        config = load_config(config_path)

        print("\nResolving pull requests...", file=sys.stderr)
        modified = resolve_pull_requests(config)

        if not modified:
            print("No pull request references found to resolve", file=sys.stderr)

        resolve_branches(config)

        print(f"\nSaving resolved config to: {output_path}", file=sys.stderr)
        save_config(config, output_path)
        print("✓ Config saved successfully", file=sys.stderr)

        print("\nOutputting test configuration...", file=sys.stderr)
        output_test_config(config)

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        import traceback

        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
