import json
import logging
import os
import shutil
import subprocess
from collections.abc import Callable
from pathlib import Path
from typing import Any

log = logging.getLogger(__name__)


class PythonAPI:
    def __init__(
        self, uv_executable: str = "uv", python_version: str = "python3"
    ) -> None:
        self.uv_executable = uv_executable
        self.python_version = python_version

    def install_project(
        self, project_path: Path, extras: list[str] | None = None
    ) -> None:
        """
        Create a virtual environment in the project directory and install the package.

        Strategy:
        1. If uv.lock exists, run `uv sync --locked` - it is a repository
        2. If pyproject.toml exists with [project] table, run `uv sync` - a new library
        3. Otherwise, run `uv venv` + `uv pip install -e .` - an older library without correct pyproject.toml

        Args:
            project_path: Path to the directory containing the package to install

        Raises:
            subprocess.CalledProcessError: If venv creation or package installation fails
        """
        import tomllib

        project_path = project_path.resolve()
        pyproject_path = project_path / "pyproject.toml"
        lock_path = project_path / "uv.lock"

        # Strategy 1: If uv.lock exists, use uv sync --locked
        if lock_path.exists():
            subprocess.run(
                [
                    self.uv_executable,
                    "sync",
                    "--locked",
                    "--python",
                    self.python_version,
                ],
                cwd=project_path,
                env=self.build_environment(project_path),
                check=True,
            )
            return

        # Strategy 2: If pyproject.toml has [project] table, use uv sync
        if pyproject_path.exists():
            try:
                with open(pyproject_path, "rb") as f:
                    pyproject_data = tomllib.load(f)

                if "project" in pyproject_data:
                    subprocess.run(
                        [
                            self.uv_executable,
                            "sync",
                            "--python",
                            self.python_version,
                        ],
                        cwd=project_path,
                        env=self.build_environment(project_path),
                        check=True,
                    )
                    return
            except Exception:
                log.exception("Failed to parse pyproject.toml")
                # If parsing fails, fall through to strategy 3
                pass

        # Strategy 3: Use uv venv + uv pip install -e .
        # First, create the venv with a clean environment
        clean_env = os.environ.copy()
        # Clear virtualenv variables to avoid conflicts during venv creation
        clean_env.pop("VIRTUAL_ENV", None)
        clean_env.pop("PYTHONHOME", None)

        subprocess.run(
            [
                self.uv_executable,
                "venv",
                "--python",
                self.python_version,
            ],
            check=True,
            cwd=project_path,
            env=clean_env,
        )

        # Then install using the new venv's environment
        extras_str = f"[{','.join(extras)}]" if extras else ""
        project_spec = f".{extras_str}"
        subprocess.run(
            [self.uv_executable, "pip", "install", "-e", project_spec],
            cwd=project_path,
            env=self.build_environment(project_path),
            check=True,
        )

    def get_dependencies(self, project_path: Path) -> dict[str, str]:
        """
        Get dependencies from uv.lock file or installed packages.

        Strategy:
        1. If no lock file exists, run install_directory first
        2. If lock file exists, extract dependencies from it
        3. If no lock file (even after install), use uv pip list

        Args:
            project_path: Path to the directory containing the package

        Returns:
            Dictionary mapping package names to their version strings.
            Versions can be standard version numbers or git references.

        Raises:
            subprocess.CalledProcessError: If commands fail
        """
        import tomllib

        project_path = project_path.resolve()
        lock_path = project_path / "uv.lock"

        # If no lock file exists, run install_directory first
        if not lock_path.exists():
            self.install_project(project_path)

        # If lock file exists, extract dependencies from it
        if lock_path.exists():
            try:
                with open(lock_path, "rb") as f:
                    lock_data = tomllib.load(f)

                # Extract dependencies from lock file
                dependencies: dict[str, str] = {}
                if "package" in lock_data:
                    for package in lock_data["package"]:
                        name = package.get("name")
                        if not name:
                            continue
                        name = name.lower()

                        # Check if package is installed from git
                        source = package.get("source")
                        if source and isinstance(source, dict) and "git" in source:
                            # Return git URL for git-based installations
                            dependencies[name] = source["git"]
                        else:
                            # Return version for regular packages
                            version = package.get("version")
                            if version:
                                dependencies[name] = version

                return dependencies
            except Exception:
                # If parsing fails, fall through to pip list
                log.exception("Failed to parse uv.lock file")
                pass

        # If no lock file (even after install), get installed dependencies directly
        return self.get_installed_dependencies(project_path)

    def get_installed_dependencies(self, project_path: Path) -> dict[str, str]:
        """Get installed dependencies using uv pip list."""
        result = subprocess.run(
            [self.uv_executable, "pip", "list", "--format", "json"],
            cwd=project_path,
            env=self.build_environment(project_path),
            check=True,
            capture_output=True,
            text=True,
        )

        # Parse JSON output
        packages_list = json.loads(result.stdout)

        # Convert to dict of package -> version
        dependencies = {pkg["name"]: pkg["version"] for pkg in packages_list}

        return dependencies

    def build_environment(self, project_path: Path) -> dict[str, str]:
        """Prepare environment variables for commands executed inside the venv.

        This clears any active virtualenv settings and points to the project's venv.
        """
        venv_path = project_path / ".venv"
        env = os.environ.copy()

        # Clear any existing virtualenv variables to avoid conflicts
        env.pop("VIRTUAL_ENV", None)
        env.pop("PYTHONHOME", None)

        # Set the new virtualenv
        env["VIRTUAL_ENV"] = str(venv_path)
        bin_dir = venv_path / "bin"

        # Prepend venv bin directory to PATH, removing any old venv paths
        path_value = env.get("PATH", "")
        # Filter out paths from other virtualenvs
        path_parts = path_value.split(os.pathsep) if path_value else []
        filtered_paths = [
            p for p in path_parts if "/.venv/" not in p and "/venv/" not in p
        ]
        env["PATH"] = os.pathsep.join([str(bin_dir)] + filtered_paths)

        return env

    def install_patched_dependencies(
        self,
        *,
        project_path: Path,
        packages_root: Path,
        patched_packages_root: Path,
        progress: Callable[[str], None] = (lambda _msg: None),
    ) -> dict[str, dict[str, Any]]:
        """Reinstall dependencies with local patches when available.

        Returns:
            Dictionary mapping package names to patch info:
            {
                package_name: {
                    'base': GitReference of the base package,
                    'patches': list of patches
                }
            }
        """
        dependencies = self.get_installed_dependencies(project_path)
        patch_info_dict: dict[str, dict[str, Any]] = {}

        for library_package in dependencies.keys():
            library_path = None

            if (patched_packages_root / library_package).exists():
                progress(f"Installing patched dependency '{library_package}'")
                library_path = patched_packages_root / library_package
            elif (packages_root / library_package).exists():
                progress(f"Installing dependency '{library_package}' from local clone")
                library_path = packages_root / library_package

            # If we installed from a local library, get patch info
            if library_path:
                self.install_external_library(project_path, library_path)
                patch_info_dict[library_package] = self._get_patch_info(library_path)

        return patch_info_dict

    def _get_patch_info(self, package_path: Path) -> dict[str, Any]:
        """Get patch info from the library's patch_info.py file."""
        patch_info_file = package_path / "patch_info.py"
        if patch_info_file.exists():
            try:
                result = subprocess.run(
                    ["python3", str(patch_info_file)],
                    cwd=package_path,
                    capture_output=True,
                    text=True,
                    check=True,
                )
                patch_data = json.loads(result.stdout)
                return {
                    "base": patch_data.get("reference"),
                    "patches": patch_data.get("applied_patches", []),
                }
            except (
                subprocess.CalledProcessError,
                json.JSONDecodeError,
                KeyError,
            ):
                log.warning(f"Failed to read patch info for {package_path}")
        return {}

    def install_external_library(self, project_path: Path, library_path: Path) -> None:
        """Install a project directory using uv pip install."""

        args = [self.uv_executable, "pip", "install"]
        args.extend(["--no-deps", "--force-reinstall"])
        args.append(str(library_path))

        subprocess.run(
            args,
            cwd=project_path,
            env=self.build_environment(project_path),
            check=True,
        )

    def install_with_patches(
        self,
        repositories_root: Path,
        package_name: str,
        target_dir: Path,
        install_patched_dependencies: bool = True,
        extras: list[str] | None = None,
        progress: Callable[[str], None] = (lambda _msg: None),
    ) -> tuple[dict[str, Any], dict[str, Any]]:
        """Install a package with patches applied.

        Args:
            repositories_root: Root directory containing both patched and regular packages
            package_name: Name of the package to install
            target_dir: Directory where the package should be installed

        Returns:
            A dictionary containing patch information for the package and its libraries.

        Strategy:
        1. Check if patched version of the package exists in patched_packages_root
        2. If not, check if the package exists in packages_root
        3. Copy the source code to the target directory
        4. Install the package in the target directory
        5. Install patched dependencies if any
        """

        source_path = repositories_root / "patched" / package_name
        if not source_path.exists() or not install_patched_dependencies:
            source_path = repositories_root / "packages" / package_name
            if not source_path.exists():
                raise FileNotFoundError(
                    f"Package '{package_name}' not found in patched or regular packages directories"
                )
        # copy source to target directory
        if target_dir.exists():
            raise FileExistsError(f"Target directory '{target_dir}' already exists")

        progress(f"Copying package '{package_name}' from {source_path} to {target_dir}")

        shutil.copytree(source_path, target_dir)

        progress(f"Installing package '{package_name}' in {target_dir}")
        # install the package in the target directory
        self.install_project(target_dir, extras=extras)

        # get the {"base": ..., "patches": [...]} info for the installed package
        package_patch_info = self._get_patch_info(source_path)

        # install patched dependencies if any
        if install_patched_dependencies:
            libraries_patch_info = self.install_patched_dependencies(
                project_path=target_dir,
                packages_root=repositories_root / "packages",
                patched_packages_root=repositories_root / "patched",
                progress=progress,
            )
            # Check if any patches were applied
        else:
            libraries_patch_info = {}

        return package_patch_info, libraries_patch_info

    def run_in_venv(
        self,
        project_path: Path,
        command: list[str],
        capture_to_file: Path | None = None,
    ) -> None:
        """Run a command inside the virtual environment."""
        if capture_to_file is None:
            subprocess.run(
                command,
                cwd=project_path,
                env=self.build_environment(project_path),
                check=True,
            )
        else:
            import shlex

            # Escape each command argument and join them
            escaped_command = " ".join(shlex.quote(arg) for arg in command)

            # Use bash with tee to capture output to file and print to stdout/stderr
            bash_command = f"set -o pipefail; {escaped_command} 2>&1 | tee {shlex.quote(str(capture_to_file))}"

            subprocess.run(
                ["bash", "-c", bash_command],
                cwd=project_path,
                env=self.build_environment(project_path),
                check=True,
            )
