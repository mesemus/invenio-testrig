from copy import deepcopy

from invenio_testrig.config import GitReference
from invenio_testrig.git_api import git_api

from .base import Patcher


class AsIsPatcher(Patcher):
    """Patcher for as-is mode.

    For packages with patches:
    - Uses the exact branch/PR specified in patches
    - No rebasing or cherry-picking
    - Only allows one patch per package

    For packages without patches:
    - Uses the pinned version from dependencies (like PinnedPatcher)
    """

    def _clone_patched(
        self, reference: GitReference, patches: list[GitReference]
    ) -> None:
        if not patches:
            return

        if len(patches) > 1:
            raise ValueError(
                "AsIs mode only allows one patch per package, "
                f"but found {len(patches)} patches for {reference['package']}"
            )

        patch_reference = git_api.resolve_git(deepcopy(patches[0]))
        target_dir = self._clone_package(patch_reference, self.patched_dir)
        self._add_patch_info(target_dir, "as-is", patch_reference, patches)
