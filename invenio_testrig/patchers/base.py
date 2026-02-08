import shutil
import subprocess
from pathlib import Path
from typing import Any
from urllib.parse import parse_qs, urlparse

from invenio_testrig.config import ConfigDict, GitReference
from invenio_testrig.git_api import git_api


class Patcher:
    def __init__(self, config: ConfigDict, unpatched_dir: Path, patched_dir: Path):
        self.config = config
        self.unpatched_dir = unpatched_dir
        self.patched_dir = patched_dir

    def clone(self, package: str) -> None:
        """Clone the package, applying any patches needed."""

        name, info = self._get_tested_package(package)
        reference = git_api.resolve_git(self._build_dependency_reference(name, info))

        self._clone_package(reference, self.unpatched_dir)
        self._add_patch_info(
            self.unpatched_dir / reference["package"], "unpatched", reference, []
        )

        patches = self._filter_patches(name)
        if patches:
            self._clone_patched(reference, patches)

        # remove the .git directory after cloning
        self._remove_git_directory(self.unpatched_dir / reference["package"])
        self._remove_git_directory(self.patched_dir / reference["package"])

    def _remove_git_directory(self, path: Path) -> None:
        """Remove a file or directory from git tracking."""
        git_directory = path / ".git"
        if git_directory.exists():
            shutil.rmtree(git_directory)
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

    def _clone_patched(
        self, reference: GitReference, patches: list[GitReference]
    ) -> None:
        raise NotImplementedError("Subclasses must implement the _clone_patched method")

    def _get_tested_package(self, package: str) -> tuple[str, dict[str, Any]]:
        """Return tested package info matching package name (case-insensitive)."""
        tested_packages = self.config.get("tested_packages", {})

        for name, info in tested_packages.items():
            if name == package:
                return name, info

        raise ValueError(f"Tested package '{package}' not found in configuration")

    def _filter_patches(self, package: str) -> list[GitReference]:
        """Filter patches for the given package (case-insensitive)."""
        patches = self.config.get("patches", [])
        return [p for p in patches if p["package"] == package]

    def _build_dependency_reference(
        self, package_name: str, dep_info: dict[str, Any]
    ) -> GitReference:
        """Build GitReference for a dependency version."""
        version = dep_info.get("version", "")

        branch: str | None = None
        commit: str | None = None

        if isinstance(version, str) and version.startswith("https://github.com/"):
            parsed = urlparse(version)
            query_params = parse_qs(parsed.query)

            if "branch" in query_params:
                branch = query_params["branch"][0]
            elif "rev" in query_params:
                branch = query_params["rev"][0]

            if parsed.fragment:
                commit = parsed.fragment
        elif version:
            version_str = str(version)
            branch = version_str if version_str.startswith("v") else f"v{version_str}"

        return {
            "org": dep_info["org"],
            "repo": dep_info["repo"],
            "package": package_name,
            "branch": branch,
            "pr": None,
            "base": None,
            "versions": [],
            "pr_info": None,
            "commit": commit,
        }

    def _clone_package(self, reference: GitReference, destination: Path) -> Path:
        """Clone the tested package repository and return the target directory."""
        package_dir = destination / reference["package"]
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
            f"reference = {repr(reference)}",
            "applied_patches = [",
        ]

        for patch in applied_patches:
            # Use repr() to get a proper Python representation
            patch_repr = repr(patch)
            # Indent the representation
            indented = "    " + patch_repr.replace("\n", "\n    ")
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
