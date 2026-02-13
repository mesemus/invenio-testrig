import shutil
import subprocess
from collections.abc import Callable
from pathlib import Path

import semver

from ..utils import call_executable_quietly
from .cache import GitCache, git_cache
from .types import GitReference, PullRequestInfo


class GitApi:
    def __init__(self, cache: GitCache):
        self._cache = cache

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
        if not reference.pr or not reference.pr_info:
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
        remote_name = f"pr-{reference.pr}-fork"
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
            error_msg = f"Failed to fetch from {remote_url}. Git error: {e.stderr}"
            raise subprocess.CalledProcessError(
                e.returncode, e.cmd, e.stdout, error_msg
            ) from e

        # Cherry-pick each commit from the PR
        for commit_sha in commits:
            try:
                call_executable_quietly(
                    ["git", "cherry-pick", commit_sha],
                    cwd=directory,
                )
            except subprocess.CalledProcessError as e:
                # Include git error output in the exception message
                error_msg = (
                    f"Failed to cherry-pick commit {commit_sha}. Git error: {e.stderr}"
                )
                raise subprocess.CalledProcessError(
                    e.returncode, e.cmd, e.stdout, error_msg
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

    def get_latest_release_version(self, ref: GitReference) -> str | None:
        """
        Find the latest release tag in the commit history.

        Searches through repository tags to find the most recent semantic version
        tag (vX.Y.Z with optional pre-release/build metadata) that is an ancestor
        of the specified commit.

        Args:
            ref: GitReference containing repository and commit information

        Returns:
            The latest version tag (e.g., "v1.2.3") found in the history, or None
            if no version tags are found.

        Raises:
            subprocess.CalledProcessError: If git commands fail
        """

        def predicate(tag_name: str) -> bool:
            # Valid semantic version tags start with 'v' followed by a version number
            if not tag_name.startswith("v"):
                return False
            version_str = tag_name[1:]
            try:
                semver.Version.parse(version_str)
                return True
            except ValueError:
                return False

        matching = self.last_n_tags_from_git_reference(
            reference=ref,
            n=1,
            predicate=predicate,
        )
        return matching[0] if matching else None


git_api = GitApi(cache=git_cache)
