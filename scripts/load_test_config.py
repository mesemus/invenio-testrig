#!/usr/bin/env python3
"""
Load test configuration from config.json5 and output with defaults.

Usage: load_test_config.py <config.json5>

Outputs key=value pairs for GitHub Actions, one per line.
"""

import sys
from pathlib import Path

import json5


def load_test_config(config_file: Path) -> None:
    """Load configuration and output with defaults."""
    if not config_file.exists():
        print(f"Error: Config file {config_file} not found", file=sys.stderr)
        sys.exit(1)

    try:
        with config_file.open("r") as f:
            config = json5.load(f)

        # Extract values with defaults
        test_name = config.get("name", "")
        run_original_tests = config.get("run_original_tests", True)
        test_timeout = config.get("test_timeout", 90)
        packages = config.get("packages", [])

        # Convert packages list to space-separated string
        packages_str = " ".join(packages) if packages else ""

        # Output to stdout for parsing
        print(f"test_name={test_name}")
        print(f"run_original_tests={'true' if run_original_tests else 'false'}")
        print(f"test_timeout={test_timeout}")
        print(f"packages={packages_str}")

    except Exception as e:
        print(f"Error loading config: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: load_test_config.py <config.json5>", file=sys.stderr)
        sys.exit(1)

    config_file = Path(sys.argv[1])
    load_test_config(config_file)
