"""Upstream branch patching strategies.

This module provides patchers that use the upstream default branch for
unpatched versions and apply patches on top, with either overwrite or rebase modes.
"""

from pathlib import Path

from invenio_testrig.github.types import GitReference

from ..types import TestedPackageInfo
from .base import Patcher


class UpstreamOverwritePatcher(Patcher):
    """Patcher for upstream repositories.

    For packages with patches:
    - Uses the upstream branch (normally master) for the unpatched version
    - Expects a single patch per package and use it instead of master branch for the patched version
    - Fail if there are multiple patches for the same package
    """

    def _build_unpatched_reference(
        self, package_name: str, package_info: TestedPackageInfo
    ) -> GitReference:
        """Build GitReference for the unpatched version of the dependency."""
        return GitReference(
            org=package_info.reference.org,
            repo=package_info.reference.repo,
            package=package_name,
        )

    def _build_patched_reference(
        self, package_name: str, package_info: TestedPackageInfo
    ) -> GitReference | None:
        if not package_info.patches:
            return None
        if len(package_info.patches) > 1:
            raise ValueError(
                f"Multiple patches found for package {package_name}, but only one is supported in 'upstream-overwrite' mode"
            )
        return package_info.patches[0]

    def _apply_patches(
        self,
        patched_reference_path: Path,
        package_name: str,
        package_info: TestedPackageInfo,
        reference: GitReference,
    ) -> None:
        """Apply the patch to the cloned repository."""
        # does nothing, as we already cloned the patched version
        pass


class UpstreamRebasePatcher(Patcher):
    """Patcher for upstream repositories with rebase.

    For packages with patches:
    - Uses the upstream branch (normally master) for the unpatched version
    - Expects one or more patches per package, and applies them on top of the upstream branch for the patched version
    """

    def _build_unpatched_reference(
        self, package_name: str, package_info: TestedPackageInfo
    ) -> GitReference:
        """Build GitReference for the unpatched version of the dependency."""
        return GitReference(
            org=package_info.reference.org,
            repo=package_info.reference.repo,
            package=package_name,
        )

    def _build_patched_reference(
        self, package_name: str, package_info: TestedPackageInfo
    ) -> GitReference | None:
        if not package_info.patches:
            return None

        return self._build_unpatched_reference(package_name, package_info)

    def _apply_patches(
        self,
        patched_reference_path: Path,
        package_name: str,
        package_info: TestedPackageInfo,
        reference: GitReference,
    ) -> None:
        """Apply the patch to the cloned repository."""
        # does nothing, as we already cloned the patched version

        for patch in package_info.patches:
            self.git_api.apply_reference(patched_reference_path, patch)
