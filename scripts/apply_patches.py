#!/usr/bin/env python3
"""
Apply patches from config.json5 to packages in a virtual environment.

Usage: apply_patches.py <package_name> <venv_path> <config.json5> <variables.sh>

Checks which packages from config (patches key) are installed in the virtual environment,
installs patched versions (excluding the package being tested), and outputs results to variables.sh.
"""

import json
import subprocess
import sys
from pathlib import Path

import json5


def get_venv_python(venv_path: Path) -> Path:
    """Get the path to the Python executable in the virtual environment."""
    python_path = venv_path / "bin" / "python"
    if not python_path.exists():
        raise FileNotFoundError(f"Python executable not found at {python_path}")
    return python_path


def list_installed_packages(venv_python: Path) -> set[str]:
    """List all packages installed in the virtual environment."""
    result = subprocess.run(
        ["uv", "pip", "list", "--python", str(venv_python), "--format", "json"],
        capture_output=True,
        text=True,
        check=True,
    )
    packages = json.loads(result.stdout)
    return {pkg["name"] for pkg in packages}


def apply_patches(
    current_package: str, venv_path: Path, config_path: Path, output_path: Path
) -> None:
    """Apply patches to installed packages and write results to variables.sh."""

    # Load config and get patches
    with config_path.open("r") as f:
        config = json5.load(f)
    patches = config.get("patches", {})

    # Get Python executable and installed packages
    venv_python = get_venv_python(venv_path)
    installed_packages = list_installed_packages(venv_python)

    # Find which patches apply
    patched_packages: list[str] = []
    for package_name, patch_info in patches.items():
        # Skip if this is the package being tested
        if package_name == current_package:
            print(f"⏭️  Skipping {package_name} (current package being tested)")
            continue

        if package_name in installed_packages:
            patched_packages.append(package_name)
            patch_url = patch_info.get("git", "")
            patch_branch = patch_info.get("branch", "")

            if patch_url:
                print(
                    f"📥 Applying patch for {package_name} from {patch_url} @ {patch_branch}"
                )

                # Construct git+https URL with branch
                if patch_branch:
                    git_url = f"git+{patch_url}@{patch_branch}"
                else:
                    git_url = f"git+{patch_url}"

                # Install the patched version
                try:
                    subprocess.run(
                        [
                            "uv",
                            "pip",
                            "install",
                            "--python",
                            str(venv_python),
                            git_url,
                            "--force-reinstall",
                            "--no-deps",
                        ],
                        check=True,
                        capture_output=True,
                        text=True,
                    )
                    print(f"✓ Patch applied for {package_name}")
                except subprocess.CalledProcessError as e:
                    print(
                        f"❌ Failed to apply patch for {package_name}: {e.stderr}",
                        file=sys.stderr,
                    )
                    raise

    # Write output variables
    applies = "true" if patched_packages else "false"
    patched_list = " ".join(patched_packages)

    with output_path.open("w") as f:
        f.write(f'applies="{applies}"\n')
        f.write(f'patched_packages="{patched_list}"\n')

    print(f"\nPatches applied: {applies}")
    if patched_packages:
        print(f"Patched packages: {patched_list}")


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print(
            "Usage: apply_patches.py <package_name> <venv_path> <config.json5> <variables.sh>",
            file=sys.stderr,
        )
        sys.exit(1)

    package_name = sys.argv[1]
    venv_path = Path(sys.argv[2])
    config_path = Path(sys.argv[3])
    output_path = Path(sys.argv[4])

    try:
        apply_patches(package_name, venv_path, config_path, output_path)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
