"""Base patcher class with common functionality for cloning and patching.

This module defines the abstract Patcher base class that provides shared
logic for cloning repositories and applying patches. Subclasses implement
specific strategies for handling unpatched and patched versions.
"""

import shutil
import subprocess
from pathlib import Path

import black

from invenio_testrig.github.api import GitApi, GitCache
from invenio_testrig.github.types import GitReference

from ..config import Config
from ..types import Progress, TestedPackageInfo


class Patcher:
    """Base class for applying patches to repository clones.

    Provides common functionality for cloning repositories with and without
    patches, and applying patches according to different strategies.
    Subclasses must implement specific patching strategies.
    """

    def __init__(
        self, config: Config, unpatched_dir: Path, patched_dir: Path, progress: Progress
    ):
        """Initialize the Patcher with configuration and directory paths.

        Args:
            config: Configuration object containing patch and package information
            unpatched_dir: Directory where unpatched repositories will be cloned
            patched_dir: Directory where patched repositories will be cloned
            progress: Progress reporter for outputting status messages
        """
        self.config = config
        self.git_api = GitApi(GitCache(config.workdir_path("git_cache")))
        self.unpatched_dir = unpatched_dir
        self.patched_dir = patched_dir
        self.progress = progress

    def clone(self, package: str) -> tuple[GitReference, GitReference | None]:
        """Clone the package, applying any patches needed."""

        name, info = self._get_tested_package(package)

        unpatched_reference = self._build_unpatched_reference(name, info)
        unpatched_reference = self.git_api.resolve_reference(unpatched_reference)
        self.progress.info(f"Cloning unpatched: {str(unpatched_reference)}")
        unpatched_reference_path = self._clone_package(
            unpatched_reference, self.unpatched_dir
        )
        self._show_commit_log(unpatched_reference_path, 20)

        patched_reference = self._build_patched_reference(name, info)
        patched_reference_path = None
        if patched_reference:
            patched_reference = self.git_api.resolve_reference(patched_reference)
            self.progress.info(f"Cloning patched: {str(patched_reference)}")
            patched_reference_path = self._clone_package(
                patched_reference, self.patched_dir
            )
            self._show_commit_log(patched_reference_path, 20)
            self._apply_patches(patched_reference_path, name, info, patched_reference)
            self._add_patch_info(
                patched_reference_path,
                patch_mode=self.config.patch_mode,
                reference=patched_reference,
                applied_patches=info.patches or [],
            )

        # remove the .git directory after cloning
        if unpatched_reference_path:
            self._remove_git_directory(unpatched_reference_path)
            self._fix_check_manifest(unpatched_reference_path)
            self._fix_run_sphinx(unpatched_reference_path)
        if patched_reference_path:
            self._remove_git_directory(patched_reference_path)
            self._fix_check_manifest(patched_reference_path)
            self._fix_run_sphinx(patched_reference_path)

        return (unpatched_reference, patched_reference)

    def _build_unpatched_reference(
        self, package_name: str, package_info: TestedPackageInfo
    ) -> GitReference:
        """Build GitReference for the unpatched version of the dependency."""
        raise NotImplementedError(
            "Subclasses must implement the _build_unpatched_reference method"
        )

    def _build_patched_reference(
        self, package_name: str, package_info: TestedPackageInfo
    ) -> GitReference | None:
        """Build GitReference for the patched version of the dependency."""
        raise NotImplementedError(
            "Subclasses must implement the _build_patched_reference method"
        )

    def _apply_patches(
        self,
        patched_reference_path: Path,
        package_name: str,
        package_info: TestedPackageInfo,
        reference: GitReference,
    ) -> None:
        """Apply patches to the target directory. The patches are applied in order."""
        raise NotImplementedError("Subclasses must implement the _apply_patches method")

    def _show_commit_log(self, path: Path, number_of_commits: int) -> None:
        """Get and display the last N commits from a repository.

        Args:
            path: Path to the repository directory
            number_of_commits: Number of recent commits to display
        """
        try:
            result = subprocess.run(
                [
                    "git",
                    "log",
                    f"-{number_of_commits}",
                    "--pretty=format:%h - %s (%an, %ar)",
                ],
                cwd=path,
                capture_output=True,
                text=True,
                check=True,
            )
            if result.stdout:
                self.progress.info(f"\nLast {number_of_commits} commits:")
                for line in result.stdout.splitlines():
                    self.progress.info(f"  {line}")
                self.progress.info("")  # Empty line for readability
        except subprocess.CalledProcessError as e:
            self.progress.warning(f"Failed to get commit log: {e}")

    def _remove_git_directory(self, path: Path) -> None:
        """Remove a file or directory from git tracking."""
        git_directory = path / ".git"
        if git_directory.exists():
            shutil.rmtree(git_directory)

    def _fix_check_manifest(self, path: Path) -> None:
        """Remove check-manifest commands from run-tests.sh script.

        The check_manifest command fails when there are untracked files (like
        removed .git directories), so we remove it from test scripts.

        Args:
            path: Path to the repository directory
        """
        self._remove_from_runtest_sh(path, "check_manifest")

    def _fix_run_sphinx(self, path: Path) -> None:
        """Remove run-sphinx commands from run-tests.sh script.

        The run-sphinx command currently fails here inside tests, so we
        remove it from test scripts.

        We remove sphinx.cmd.build lines from run-tests.sh

        Args:
            path: Path to the repository directory
        """
        self._remove_from_runtest_sh(path, "sphinx.cmd.build")

    def _remove_from_runtest_sh(self, path: Path, search_string: str) -> None:
        """Remove lines containing search_string from run-tests.sh script.

        Args:
            path: Path to the repository directory
            search_string: String to search for in the script, lines containing this string will be removed
        """
        run_tests_script = path / "run-tests.sh"
        if run_tests_script.exists():
            content = run_tests_script.read_text()
            if search_string in content:
                new_content = "\n".join(
                    line for line in content.splitlines() if search_string not in line
                )
                run_tests_script.write_text(new_content)

    def _get_tested_package(self, package: str) -> tuple[str, TestedPackageInfo]:
        """Return tested package info matching package name (case-insensitive)."""
        tested_packages = self.config.tested_packages or {}

        for name, info in tested_packages.items():
            if name == package:
                return name, info

        raise ValueError(f"Tested package '{package}' not found in configuration")

    def _clone_package(self, reference: GitReference, destination: Path) -> Path:
        """Clone the tested package repository and return the target directory."""
        package_dir = destination / reference.package
        if package_dir.exists():
            shutil.rmtree(package_dir)
        self.git_api.clone_git_reference(reference, package_dir)
        return package_dir

    def _add_patch_info(
        self,
        target_dir: Path,
        patch_mode: str,
        reference: GitReference,
        applied_patches: list[GitReference],
    ) -> None:
        """Add clone info file to the target directory.

        It finds all directories in the target directory that contain a __init__.py file,
        inside creates a patch_info.py containing:

        patch_mode = "..."
        applied_patches = [
            {...},
            {...},
        ]
        """

        # Generate the content for patch_info.py
        lines = [
            '"""Clone information for this package."""',
            "",
            f'patch_mode = "{patch_mode}"',
            "",
            f"reference = {reference.to_dict()}",
            "applied_patches = [",
        ]

        for patch in applied_patches:
            # Indent the representation
            indented = "    " + repr(patch.to_dict()).replace("\n", "\n    ")
            lines.append(f"{indented},")

        lines.append("]")
        lines.append("if __name__ == '__main__':")
        lines.append("    import json")
        lines.append("    print(json.dumps({")
        lines.append("        'patch_mode': patch_mode,")
        lines.append("        'reference': reference,")
        lines.append("        'applied_patches': applied_patches,")
        lines.append("    }, indent=2))")
        content = "\n".join(lines) + "\n"

        # Find top-level directories containing __init__.py (Python packages)
        # Ignore test directories
        for init_file in target_dir.glob("*/__init__.py"):
            package_dir = init_file.parent

            # Skip test directories
            if package_dir.name in ("test", "tests"):
                continue

            patch_info_file = package_dir / "patch_info.py"

            # Write the file
            patch_info_file.write_text(content)

            # Call black to format the file.
            black.format_file_in_place(
                patch_info_file,
                fast=False,
                mode=black.Mode(),
                write_back=black.WriteBack.YES,
            )

        top_level_info = target_dir / "patch_info.py"
        top_level_info.write_text(content)
        black.format_file_in_place(
            top_level_info,
            fast=False,
            mode=black.Mode(),
            write_back=black.WriteBack.YES,
        )
