"""GitHub API client wrapper for git operations.

This module provides a high-level interface for interacting with GitHub
repositories, including resolving references, fetching commits, managing
branches and tags, and handling pull requests.
"""

import logging
import re
import shutil
import subprocess
from collections.abc import Callable
from pathlib import Path
from typing import Any, cast

from ..errors import PatchApplicationError
from ..utils import call_executable_quietly
from .cache import GitCache
from .types import GitReference, GitReferenceSchema, Patch, PullRequestInfo

log = logging.getLogger(__name__)


class GitApi:
    """High-level GitHub API client for git operations.

    Provides methods for resolving git references, cloning repositories,
    applying patches, and managing branches, tags, and pull requests.
    """

    def __init__(self, cache: GitCache):
        """Initialize GitApi with a cache instance.

        Args:
            cache: GitCache instance for caching repository data
        """
        self._cache = cache

    def parse_reference(
        self, reference: str | GitReference | dict[str, Any]
    ) -> GitReference:
        """Parse a git reference string into a GitReference structure.

        Supported formats:
        - org/package@branch
        - org/package#pr_number
        - org/package@branch[base]
        - org/package[@branch|#pr]
        - package_name: org/package...
        - https://github.com/org/repo
        - https://github.com/org/repo/tree/branch-name
        - https://github.com/org/repo/pull/123

        Also pip-installed github references:
        - https://github.com/inveniosoftware/invenio-records-resources?branch=fix-read-many#c6b973a14802e2a7f73100ab4e32cb0c36bd4672
        - https://github.com/inveniosoftware/invenio-swh?rev=v0.13.4#828a3a415cf8e725c369939832b61281c44aec40
        In these two cases, fragments (sha commit) are not parsed because pip can use their obsolete version.


        Args:
            reference: Git reference string to parse

        Returns:
            Parsed GitReference structure

        Raises:
            ValidationError: If the reference string is invalid
        """
        # Import here to avoid circular imports
        from .ref_parser import parse_string_reference

        if isinstance(reference, str):
            parsed_reference = parse_string_reference(reference)
        elif isinstance(reference, dict):
            parsed_reference = cast(GitReference, GitReferenceSchema().load(reference))
        else:
            parsed_reference = reference

        return self.resolve_reference(parsed_reference)

    def parse_patch(self, patch: str | GitReference | dict[str, Any]) -> Patch:
        """Parse a patch reference string into a Patch structure.

        Patch reference is the same as GitReference, but might have an extra versions
        (version-range) after the reference. The versions always start with '>', '<' or '='
        and are separated by commas if there are multiple.
        """
        from .ref_parser import parse_version_constraints

        versions_part = None
        if isinstance(patch, str):
            # Split the reference and the version constraints
            matches = re.match(r"(.*?)([><=!].*)$", patch)
            if matches:
                patch, versions_part = matches.groups()

        reference = self.parse_reference(patch)

        # Parse version constraints if present
        versions = []
        if versions_part:
            versions = parse_version_constraints(versions_part)

        return Patch(
            org=reference.org,
            repo=reference.repo,
            package=reference.package,
            branch=reference.branch,
            pr=reference.pr,
            base=reference.base,
            actual_version=reference.actual_version,
            pr_info=reference.pr_info,
            commit=reference.commit,
            versions=versions,
        )

    def get_commit(self, org: str, repo: str, branch_or_tag_or_commit: str) -> str:
        """Resolve any git reference to a commit SHA.

        The GitHub commits API accepts branch names, tag names, or direct commit
        SHAs. Using it ensures we can resolve all reference types uniformly.

        Args:
            org: GitHub organization or user name
            repo: Repository name
            branch_or_tag_or_commit: Branch name, tag name, or commit SHA

        Returns:
            The commit SHA referenced by the input
        """
        return self._cache.get_branch_commit(org, repo, branch_or_tag_or_commit)

    def resolve_pr(self, org: str, repo: str, pr_number: int) -> PullRequestInfo:
        """
        Resolve pull request information including source details and commits.

        Args:
            org: GitHub organization or user name
            repo: Repository name
            pr_number: Pull request number

        Returns:
            Dictionary containing source_org, source_repo, source_branch, and list of commit SHAs
        """
        return self._cache.get_pr_info(org, repo, pr_number)

    def get_default_branch(self, org: str, repo: str) -> str:
        """
        Get the default branch name for a repository.

        Args:
            org: GitHub organization or user name
            repo: Repository name

        Returns:
            The default branch name (e.g., "main", "master")
        """
        return self._cache.get_default_branch(org, repo)

    def get_branches(self, org: str, repo: str) -> list[str]:
        """
        Get branch names from the repository, sorted by most recently updated.

        Args:
            org: GitHub organization or user name
            repo: Repository name
            limit: Maximum number of branches to return (None for all)

        Returns:
            List of branch names sorted by most recent update

        Raises:
            httpx.HTTPStatusError: If the API request fails
        """
        return self._cache.get_branches(org, repo)

    def resolve_reference(self, git_ref: GitReference) -> GitReference:
        """
        Resolve git reference details using GitHub API.

        Fills in missing commit SHA, PR info, and other details for a GitReference.
        If no branch or PR is specified, uses the default branch.

        Args:
            git_ref: GitReference with at least org and repo populated

        Returns:
            GitReference with commit SHA and other details filled in
        """

        if git_ref.pr is not None and git_ref.pr_info is None:
            # we have a PR number but no PR info, let's resolve it
            pr_info = self.resolve_pr(git_ref.org, git_ref.repo, git_ref.pr)
            git_ref.pr_info = pr_info

        if (
            git_ref.pr_info is None
            and git_ref.base is not None
            and git_ref.branch is not None
        ):
            # This is a non-PR reference with a base, we can generate virtual PR info
            # by taking commits between the branch and the base
            git_ref.pr_info = self._cache.virtual_pr_info(
                git_ref.org,
                git_ref.repo,
                git_ref.branch,
                git_ref.base,
            )

        if git_ref.pr_info is not None and not git_ref.commit:
            # if we have PR info but no commit,
            # we can set the commit to the latest commit in the PR
            git_ref.commit = (
                git_ref.pr_info.commits[-1] if git_ref.pr_info.commits else None
            )

        if not git_ref.commit:
            # finally, if we still don't have a commit,
            # we resolve the branch or default branch to get the commit
            git_ref.commit = self.get_commit(
                git_ref.org,
                git_ref.repo,
                git_ref.branch or self.get_default_branch(git_ref.org, git_ref.repo),
            )

        git_ref.actual_version = self.get_last_version_before_commit(git_ref)
        git_ref.commits_from_version = self.get_commits_from_version(git_ref)

        return git_ref

    def last_n_tags_from_git_reference(
        self,
        reference: GitReference,
        n: int,
        predicate: Callable[[str], bool] = lambda tag: True,
    ) -> list[str]:
        """
        Return the last n tag names reachable from the git reference (newest -> oldest),
        where predicate(tag_name) == True.

        Args:
            reference: GitReference to clone and search tags from
            n: Number of tags to return
            predicate: Function to filter tag names

        Returns:
            List of tag names (up to n) that match the predicate
        """
        if reference.pr_info:
            tags = self._cache.get_tags(
                reference.pr_info.source_org, reference.pr_info.source_repo
            )
        else:
            tags = self._cache.get_tags(reference.org, reference.repo)
        return [tag for idx, tag in enumerate(tags) if idx < n and predicate(tag)]

    def clone_git_reference(
        self, reference: GitReference, output_directory: Path
    ) -> None:
        """
        Clone a git repository and checkout the specified commit or branch.

        If pr_info is present, clones from the PR's source repository (fork),
        otherwise clones from the original repository.

        Args:
            reference: GitReference containing org, repo, branch, and commit information
            output_directory: Path where the repository should be cloned
        """
        if reference.pr_info:
            org = reference.pr_info.source_org
            repo = reference.pr_info.source_repo
        else:
            org = reference.org
            repo = reference.repo

        cache_path = self._cache.get_path(org, repo)

        # use git to clone the repository from cache to the output directory
        shutil.copytree(cache_path, output_directory)

        # checkout the specified commit or branch
        checkout_target = reference.commit or reference.branch
        if checkout_target:
            call_executable_quietly(
                ["git", "checkout", checkout_target],
                cwd=output_directory,
                check=True,
            )

    def apply_reference(self, directory: Path, reference: GitReference) -> None:
        """
        Apply commits from a pull request reference to an existing repository.

        Cherry-picks all commits from the PR into the current branch of the
        repository at the specified directory. If the PR is from a fork,
        fetches the commits from the fork first.

        Args:
            directory: Path to the git repository where commits should be applied
            reference: GitReference that must contain PR information

        Raises:
            ValueError: If the reference is not a PR (no pr_info)
            subprocess.CalledProcessError: If git operations fail
        """
        if not reference.pr_info:
            raise ValueError(
                f"Reference must be a pull request with pr_info, got {reference}"
            )

        commits = reference.pr_info.commits

        if not commits:
            return  # Nothing to apply

        pr_info = reference.pr_info
        source_org = pr_info.source_org
        source_repo = pr_info.source_repo

        # Add the fork as a remote if it's different from the base repo
        # This ensures we can fetch commits even if they're from a fork
        if reference.pr:
            remote_name = str(reference.pr)
        elif pr_info.commits:
            remote_name = pr_info.commits[-1][:7]  # use short SHA as remote name
        else:
            raise ValueError(
                f"Cannot determine remote name for PR {reference}, {reference.pr_info}"
            )
        remote_name = f"pr-{remote_name}-fork"
        remote_url = f"https://github.com/{source_org}/{source_repo}.git"

        try:
            # Add remote (ignore error if it already exists)
            call_executable_quietly(
                ["git", "remote", "add", remote_name, remote_url],
                cwd=directory,
            )
        except subprocess.CalledProcessError:
            # Remote might already exist, that's fine
            pass

        # Fetch the commits from the remote
        try:
            call_executable_quietly(
                ["git", "fetch", remote_name],
                cwd=directory,
            )
        except subprocess.CalledProcessError as e:
            error_msg = f"Failed to fetch from {remote_url}"
            raise PatchApplicationError(
                error_msg,
                patch_reference=reference,
                repository_path=directory,
            ) from e

        # Cherry-pick each commit from the PR
        log.info(
            f"Applying {len(commits)} commits from PR #{reference} to {directory}..."
        )
        log.info("Commits to apply:")
        log.info(f"    {'\n    '.join(commits)}")
        for commit_sha in commits:
            try:
                call_executable_quietly(
                    [
                        "git",
                        "cherry-pick",
                        "--allow-empty",
                        "--allow-empty-message",
                        "--empty=drop",
                        commit_sha,
                    ],
                    cwd=directory,
                )
            except subprocess.CalledProcessError as e:
                # Include git error output in the exception message
                error_msg = f"Failed to cherry-pick commit {commit_sha}"
                raise PatchApplicationError(
                    error_msg,
                    patch_reference=reference,
                    repository_path=directory,
                ) from e

        # Clean up: remove the temporary remote
        try:
            call_executable_quietly(
                ["git", "remote", "remove", remote_name],
                cwd=directory,
            )
        except subprocess.CalledProcessError:
            # If cleanup fails, it's not critical
            pass

    def get_last_version_before_commit(self, ref: GitReference) -> str | None:
        """
        Get the last version tag that is an ancestor of the specified commit.

        This method returns the most recent version tag that is on the commit or
        before the specified commit in the commit history. If the latest release version
        is the same as the current commit, it will return the version on the commit.

        Args:
            ref: GitReference containing repository and commit information
        Returns:
            The last version tag before the specified commit, or None if no such
            version exists.
        """
        if ref.commit is None:
            raise ValueError(
                "GitReference must have a commit to find the last version before it."
            )
        return self._cache.get_last_version_on_or_before_commit(
            ref.org, ref.repo, ref.commit
        )

    def get_commits_from_version(self, ref: GitReference) -> list[str]:
        """
        Get a list of commit SHAs from the latest release version to the current commit.

        If a latest release version is found, returns the list of commits that are
        reachable from the current commit but not from the latest release tag.
        If no release version is present, returns an empty list.

        Args:
            ref: GitReference containing repository and commit information
        Returns:
            List of commit SHAs from the latest release version to the current commit,
            excluding the actual_version commit. If the actual version is the same
            as the current commit, returns an empty list. If no release version is found,
            returns all the commits reachable from the current commit.
        """
        if ref.commit is None:
            raise ValueError(
                "GitReference must have a commit to find commits from version."
            )
        return self._cache.get_commits_from_version(
            ref.org,
            ref.repo,
            ref.commit,
            f"v{ref.actual_version}" if ref.actual_version else None,
        )

    def get_last_commits(
        self, repository_path: Path, number_of_commits: int
    ) -> list[tuple[str, str]]:
        """Get the last N commits from a repository.

        Args:
            repository_path: Path to the repository directory
            number_of_commits: Number of recent commits to retrieve

        Returns:
            List of tuples containing (commit_hash, commit_message)
        """
        try:
            result = subprocess.run(
                [
                    "git",
                    "log",
                    f"-{number_of_commits}",
                    "--pretty=format:%h|%s",
                ],
                cwd=repository_path,
                capture_output=True,
                text=True,
                check=True,
            )
            if not result.stdout:
                return []

            commits = []
            for line in result.stdout.splitlines():
                if "|" in line:
                    hash_part, message = line.split("|", 1)
                    commits.append((hash_part.strip(), message.strip()))
            return commits
        except subprocess.CalledProcessError:
            return []
