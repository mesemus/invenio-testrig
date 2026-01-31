#!/usr/bin/env python3
"""
Resolve pull request URLs in config.json5 to git+branch format.

This script reads a config.json5 file, identifies patches specified as GitHub PR URLs,
resolves them to git+branch format by fetching PR information from GitHub API,
and saves the modified configuration.
"""

import json
import re
import sys
from pathlib import Path
from urllib.request import Request, urlopen

import json5


def load_config(config_path):
    """Load config.json5 file."""
    with config_path.open("r") as f:
        return json5.load(f)


def output_config(config, output_path):
    """Output config to file or stdout."""
    if output_path == "-":
        # Print to stdout
        json.dump(config, sys.stdout, indent=4)
        sys.stdout.write("\n")
    else:
        # Save to file
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


def resolve_pull_requests(config):
    """Resolve all PR URLs in patches to git+branch format."""
    patches = config.get("patches", {})
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


def main():
    """Main entry point."""
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print(
            "Usage: resolve_pull_requests.py <config.json5> [output_file]",
            file=sys.stderr,
        )
        print(
            "  If output_file is not provided, the output will be print to stdout",
            file=sys.stderr,
        )
        sys.exit(1)

    config_path = Path(sys.argv[1])
    output_path = sys.argv[2] if len(sys.argv) == 3 else None

    if not config_path.exists():
        print(f"Error: Config file not found: {config_path}", file=sys.stderr)
        sys.exit(1)

    print(f"Loading config from: {config_path}", file=sys.stderr)
    config = load_config(config_path)

    print("\nResolving pull requests...", file=sys.stderr)
    modified = resolve_pull_requests(config)

    if not modified:
        print("\nNo pull request references found to resolve", file=sys.stderr)

    print(
        f"\nSaving config to: {output_path if output_path else '-'}",
        file=sys.stderr,
    )
    output_config(config, output_path if output_path else "-")

    print("✓ Config saved successfully", file=sys.stderr)


if __name__ == "__main__":
    main()
