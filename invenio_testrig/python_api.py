"""Python package management and installation using uv.

This module provides a wrapper around the uv package manager for creating
virtual environments, installing packages, and managing Python dependencies.
It handles various project configurations including modern pyproject.toml
and legacy setup.py based projects.
"""

import json
import logging
import os
import shutil
import subprocess
from pathlib import Path

from invenio_testrig.types import Progress
from invenio_testrig.utils import call_executable_quietly

log = logging.getLogger(__name__)


class PythonAPI:
    """Python package management API using uv.

    Provides methods for creating virtual environments, installing packages,
    managing dependencies, and running commands within virtual environments.
    """

    def __init__(
        self, uv_executable: str = "uv", python_version: str = "python3"
    ) -> None:
        """Initialize the PythonAPI with uv executable and Python version.

        Args:
            uv_executable: Path to the uv executable (default: "uv")
            python_version: Python version to use (default: "python3")
        """
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
            call_executable_quietly(
                [
                    self.uv_executable,
                    "sync",
                    "--locked",
                    "--python",
                    self.python_version,
                ],
                cwd=project_path,
                env=self.build_environment(project_path),
            )
            return

        # Strategy 2: If pyproject.toml has [project] table, use uv sync
        if pyproject_path.exists():
            try:
                with open(pyproject_path, "rb") as f:
                    pyproject_data = tomllib.load(f)

                sync_extras = []
                for extra in extras or []:
                    sync_extras.append("--extra")
                    sync_extras.append(extra)

                if "project" in pyproject_data:
                    call_executable_quietly(
                        [
                            self.uv_executable,
                            "sync",
                            "--python",
                            self.python_version,
                            *sync_extras,
                        ],
                        cwd=project_path,
                        env=self.build_environment(project_path),
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

        call_executable_quietly(
            [
                self.uv_executable,
                "venv",
                "--python",
                self.python_version,
            ],
            cwd=project_path,
            env=clean_env,
        )

        # Then install using the new venv's environment
        extras_str = f"[{','.join(extras)}]" if extras else ""
        project_spec = f".{extras_str}"
        call_executable_quietly(
            [self.uv_executable, "pip", "install", "-e", project_spec],
            cwd=project_path,
            env=self.build_environment(project_path),
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
        stdout, _ = call_executable_quietly(
            [self.uv_executable, "pip", "list", "--format", "json"],
            cwd=project_path,
            env=self.build_environment(project_path),
        )

        # Parse JSON output
        packages_list = json.loads(stdout)

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
        progress: Progress,
    ) -> list[str]:
        """Reinstall dependencies with local patches when available.

        Returns:
            A list of installed dependencies (package names).
        """
        all_dependencies = self.get_installed_dependencies(project_path)
        dependencies: list[str] = []

        paths_to_install: list[Path] = []
        for library_package in all_dependencies.keys():
            library_path = None

            if (patched_packages_root / library_package).exists():
                progress.info(f"Installing patched dependency '{library_package}'")
                library_path = patched_packages_root / library_package
            elif (packages_root / library_package).exists():
                progress.info(
                    f"Installing dependency '{library_package}' from local clone"
                )
                library_path = packages_root / library_package

            # If we installed from a local library, get patch info
            if library_path:
                paths_to_install.append(library_path)
                dependencies.append(library_package)

        self.install_external_libraries(project_path, *paths_to_install)

        return dependencies

    def install_external_libraries(
        self, project_path: Path, *library_paths: Path
    ) -> None:
        """Install a project directory using uv pip install."""

        args = [self.uv_executable, "pip", "install"]
        args.extend(["--no-deps", "--force-reinstall"])
        args.extend([str(library_path) for library_path in library_paths])

        call_executable_quietly(
            args,
            cwd=project_path,
            env=self.build_environment(project_path),
        )

    def install_with_patches(
        self,
        repositories_root: Path,
        package_name: str,
        target_dir: Path,
        install_patched_dependencies: bool,
        progress: Progress,
        *,
        extras: list[str] | None = None,
        freeze: list[str] | None = None,
    ) -> list[str]:
        """Install a package with patches applied.

        Args:
            repositories_root: Root directory containing both patched and regular packages
            package_name: Name of the package to install
            target_dir: Directory where the package should be installed
            install_patched_dependencies: Whether to install patched dependencies.
            extras: Optional list of extras to install with the package
            freeze: Optional list of dependencies to freeze after installation (e.g. ["package==1.2.3"])
            progress: Callback function to report progress messages


        Returns:
            A list of installed dependencies

        Strategy:
        1. Check if patched version of the package exists in patched_packages_root
        2. If not, check if the package exists in packages_root
        3. Copy the source code to the target directory
        4. Install the package in the target directory
        5. Install patched dependencies if any
        6. Apply the freeze list if provided
        """

        if target_dir.exists():
            raise FileExistsError(f"Target directory '{target_dir}' already exists")

        # get the source path for the package, prioritizing patched version
        # if should test patched dependencies, and raise an error if the package is
        # not found in either location
        candidates = [repositories_root / "packages" / package_name]
        if install_patched_dependencies:
            candidates.insert(0, repositories_root / "patched" / package_name)
        try:
            source_path = next(path for path in candidates if path.exists())
        except StopIteration:
            raise FileNotFoundError(
                f"Package '{package_name}' not found in patched or regular packages directories"
            )

        progress.info(
            f"Copying package '{package_name}' from {source_path} to {target_dir}"
        )

        shutil.copytree(source_path, target_dir)

        progress.info(f"Installing package '{package_name}' in {target_dir}")
        # install the package in the target directory
        self.install_project(target_dir, extras=extras)

        # install patched dependencies if any
        dependencies: list[str]
        if install_patched_dependencies:
            dependencies = self.install_patched_dependencies(
                project_path=target_dir,
                packages_root=repositories_root / "packages",
                patched_packages_root=repositories_root / "patched",
                progress=progress,
            )
            # Check if any patches were applied
        else:
            dependencies = []

        if freeze:
            progress.info(
                f"Applying freeze list for package '{package_name}': {freeze}"
            )
            stdout, stderr = call_executable_quietly(
                [
                    self.uv_executable,
                    "pip",
                    "install",
                    "--force-reinstall",
                    "-U",
                    *freeze,
                ],
                cwd=target_dir,
                env=self.build_environment(target_dir),
            )
            print(stdout, stderr)
            progress.success(f"Freeze list applied for package '{package_name}'")

        return dependencies

    def run_in_venv(
        self,
        project_path: Path,
        command: list[str],
        capture_to_file: Path | None = None,
        tee_output: bool = True,
    ) -> None:
        """Run a command inside the virtual environment."""
        if capture_to_file is None:
            subprocess.run(
                command,
                cwd=project_path,
                env=self.build_environment(project_path),
                check=True,
            )
        elif tee_output:
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
        else:
            with open(capture_to_file, "w") as f:
                subprocess.run(
                    command,
                    cwd=project_path,
                    env=self.build_environment(project_path),
                    stdout=f,
                    stderr=subprocess.STDOUT,
                    check=True,
                )
