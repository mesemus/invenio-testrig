from invenio_testrig.config import GitReference
from invenio_testrig.git_api import git_api

from .base import Patcher


class PinnedPatcher(Patcher):
    """Patcher for pinned repositories.

    For packages with patches:
    - Uses the pinned version from dependencies
    - Applies patches on top of the pinned version
    - Allows multiple patches per package
    """

    def _clone_patched(
        self, reference: GitReference, patches: list[GitReference]
    ) -> None:
        if not patches:
            return

        target_dir = self._clone_package(reference, self.patched_dir)

        for patch in patches:
            git_api.apply_reference(target_dir, patch)

        self._add_patch_info(target_dir, "pinned", reference, patches)
