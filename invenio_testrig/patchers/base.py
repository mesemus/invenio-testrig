import shutil
import subprocess
from pathlib import Path

from invenio_testrig.github.api import git_api
from invenio_testrig.github.types import GitReference

from ..config import Config, TestedPackageInfo


class Patcher:
    def __init__(self, config: Config, unpatched_dir: Path, patched_dir: Path):
        self.config = config
        self.unpatched_dir = unpatched_dir
        self.patched_dir = patched_dir

    def clone(self, package: str) -> None:
        """Clone the package, applying any patches needed."""

        name, info = self._get_tested_package(package)

        unpatched_reference = self._build_unpatched_reference(name, info)
        unpatched_reference = git_api.resolve_reference(unpatched_reference)
        unpatched_reference_path = self._clone_package(
            unpatched_reference, self.unpatched_dir
        )

        patched_reference = self._build_patched_reference(name, info)
        patched_reference_path = None
        if patched_reference:
            patched_reference = git_api.resolve_reference(patched_reference)
            patched_reference_path = self._clone_package(
                patched_reference, self.patched_dir
            )
            self._apply_patches(patched_reference_path, name, info, patched_reference)
            self._add_patch_info(
                patched_reference_path,
                patch_mode=self.config.mode,
                reference=patched_reference,
                applied_patches=info.patches or [],
            )

        # remove the .git directory after cloning
        if unpatched_reference_path:
            self._remove_git_directory(unpatched_reference_path)
            self._fix_check_manifest(unpatched_reference_path)
        if patched_reference_path:
            self._remove_git_directory(patched_reference_path)
            self._fix_check_manifest(patched_reference_path)

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

    def _remove_git_directory(self, path: Path) -> None:
        """Remove a file or directory from git tracking."""
        git_directory = path / ".git"
        if git_directory.exists():
            shutil.rmtree(git_directory)

    def _fix_check_manifest(self, path: Path) -> None:
        # invenio: if there is a run-tests.sh script, it might contain a check-manifest
        # command. This command will fail if there are untracked files in the repository,
        # so we need to remove the command.
        run_tests_script = path / "run-tests.sh"
        if run_tests_script.exists():
            content = run_tests_script.read_text()
            if "check_manifest" in content:
                new_content = "\n".join(
                    line
                    for line in content.splitlines()
                    if "check_manifest" not in line
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
        git_api.clone_git_reference(reference, package_dir)
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

            # Call black to format the file. We suppose that black is always installed.
            subprocess.check_call(
                ["black", patch_info_file],
            )

        top_level_info = target_dir / "patch_info.py"
        top_level_info.write_text(content)
        subprocess.check_call(
            ["black", top_level_info],
        )
