from copy import deepcopy

from invenio_testrig.config import GitReference
from invenio_testrig.git_api import git_api

from .base import Patcher


class UpstreamPatcher(Patcher):
    """Patcher for upstream repositories.

    For packages with patches:
    - Uses the upstream branch (normally master)
    - Rebases or cherry-picks patches on top of the pinned version from dependencies
    - Allows multiple patches per package
    """

    def _clone_patched(
        self, reference: GitReference, patches: list[GitReference]
    ) -> None:
        if not patches:
            return

        _, info = self._get_tested_package(reference["package"])

        upstream_reference = deepcopy(reference)
        repo_branch = info.get("repo-branch") or info.get("repo_branch")
        if repo_branch:
            upstream_reference["branch"] = repo_branch
            upstream_reference["commit"] = None

        upstream_reference = git_api.resolve_git(upstream_reference)

        target_dir = self._clone_package(upstream_reference, self.patched_dir)

        for patch in patches:
            git_api.apply_reference(target_dir, patch)

        self._add_patch_info(target_dir, "upstream", upstream_reference, patches)
