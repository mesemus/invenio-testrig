"""Git repository caching layer to minimize GitHub API calls.

This module provides a caching mechanism for git repository data using
local clones instead of API calls to avoid rate limiting. It caches
repository metadata, branch information, and pull request details.
"""

import json
import multiprocessing
import shutil
import subprocess
from pathlib import Path
from typing import Any

from ..types import Progress
from ..utils import call_executable_quietly
from .types import PullRequestInfo


class GitCache:
    """
    As github API calls are rate limited (at most 5000 per hour for authenticated requests),
    we use a normal git operations (such as clone) to have the local state of the repository.
    These are not capped by the API rate limits.

    We will use the API calls (via the gh client) just to resolve PRs as they are not
    available via notmal git operations.

    The cache will be stored in a temporary directory and will be cleared on initialization.
    It takes care of common operations:
    - Cloning repositories
    - Fetching branch commits
    - Getting default branch name
    - Fetching PR information
    - Getting names of branches and tags sorted by most recently updated
    """

    def __init__(self, cache_dir: Path):
        self._cache_dir = cache_dir.resolve()
        self._pr_cache: dict[tuple[str, str, int], PullRequestInfo] = {}

    @property
    def cache_dir(self) -> Path:
        """Get the path to the cache directory."""
        return self._cache_dir

    def clear_cache(self):
        """Clear the cache by removing all cached repositories."""
        print("Clearing git cache at", self._cache_dir)
        if self._cache_dir.exists():
            shutil.rmtree(self._cache_dir)
        self._pr_cache.clear()

    def get_path(self, org: str, repo: str) -> Path:
        """Get the local cache path for the specified repository."""
        return self._clone_repo(org, repo)

    def get_pr_info(self, org: str, repo: str, pr: int) -> PullRequestInfo:
        """Get cached PR information for the given reference."""
        if (org, repo, pr) not in self._pr_cache:
            self._prepare_pr(org, repo, pr)

        return self._pr_cache[(org, repo, pr)]

    def virtual_pr_info(
        self, org: str, repo: str, branch: str, base: str
    ) -> PullRequestInfo:
        """Generate a virtual PR info for a non-PR reference by comparing the branch with the base."""
        cache_path = self._clone_repo(org, repo)

        # Resolve base and branch to commit SHAs (handles branches, tags, and commits)
        base_commit = self.get_branch_commit(org, repo, branch=base)
        branch_commit = self.get_branch_commit(org, repo, branch=branch)

        # Get the list of commits between base and branch
        output, _ = call_executable_quietly(
            ["git", "rev-list", f"{base_commit}..{branch_commit}"],
            cwd=cache_path,
        )
        commits = output.strip().split("\n") if output.strip() else []
        return PullRequestInfo(
            source_org=org,
            source_repo=repo,
            source_branch=branch,
            commits=commits,
        )

    def get_branch_commit(self, org: str, repo: str, branch: str | None = None) -> str:
        """Get the latest commit SHA for the specified branch."""
        cache_path = self._clone_repo(org, repo)

        if branch is None:
            ref = "HEAD"
        else:
            ref = branch

        # Get all remotes to try remote branches
        try:
            remotes_output, _ = call_executable_quietly(
                ["git", "remote"],
                cwd=cache_path,
            )
            remotes = (
                remotes_output.strip().split("\n") if remotes_output.strip() else []
            )
        except subprocess.CalledProcessError:
            remotes = []

        # Try multiple strategies to resolve to a real commit ID
        # The ^{commit} suffix ensures we get a commit object, not an annotated tag object
        ref_patterns = [
            f"{ref}^{{commit}}",  # Direct ref (local branch, commit ID)
            f"refs/tags/{ref}^{{commit}}",  # Tag (annotated or lightweight)
            f"refs/heads/{ref}^{{commit}}",  # Explicit local branch ref
        ]

        # Add remote branch patterns for all remotes
        for remote in remotes:
            ref_patterns.append(f"{remote}/{ref}^{{commit}}")

        for pattern in ref_patterns:
            try:
                output, _ = call_executable_quietly(
                    ["git", "rev-parse", pattern],
                    cwd=cache_path,
                )
                return output.strip()
            except subprocess.CalledProcessError:
                continue

        # If all strategies failed and this was for HEAD, that's an error
        if branch is None:
            raise ValueError(f"Could not resolve default branch for {org}/{repo}")

        # Last resort: try to find it in for-each-ref output
        try:
            output, _ = call_executable_quietly(
                [
                    "git",
                    "for-each-ref",
                    "--format=%(refname:short) %(objectname) %(*objectname)",
                    "refs/heads/",
                    "refs/tags/",
                    "refs/remotes/",
                ],
                cwd=cache_path,
            )
            for line in output.strip().split("\n"):
                parts = line.split()
                if len(parts) < 2:
                    continue
                name = parts[0]
                # For annotated tags, %(*objectname) gives the dereferenced commit
                # For everything else, it's empty and we use %(objectname)
                commit = parts[2] if len(parts) > 2 and parts[2] else parts[1]

                # Match against the short name directly
                if name == ref:
                    return commit

                # Also try matching with any remote prefix stripped (e.g., "origin/main" matches "main")
                for remote in remotes:
                    if name == f"{remote}/{ref}":
                        return commit
        except subprocess.CalledProcessError:
            pass

        raise ValueError(f"Could not resolve ref '{ref}' for {org}/{repo}")

    def get_default_branch(self, org: str, repo: str) -> str:
        """Get the default branch name for the specified repository."""
        self.get_branch_commit(org, repo)  # Ensure cache is populated
        cache_path = self._clone_repo(org, repo)
        output, _ = call_executable_quietly(
            ["git", "symbolic-ref", "refs/remotes/origin/HEAD"],
            cwd=cache_path,
        )
        return output.strip().split("/")[-1]

    def get_branches(self, org: str, repo: str) -> list[str]:
        """Get branch names from the repository, sorted by most recently updated."""
        self.get_branch_commit(org, repo)  # Ensure cache is populated
        cache_path = self._clone_repo(org, repo)
        output, _ = call_executable_quietly(
            [
                "git",
                "for-each-ref",
                "--sort=-committerdate",
                "--format=%(refname:short)",
                "refs/remotes/origin/",
            ],
            cwd=cache_path,
        )
        branches = output.strip().split("\n")
        return [
            branch.replace("origin/", "")
            for branch in branches
            if branch.startswith("origin/")
        ]

    def get_tags(self, org: str, repo: str) -> list[str]:
        """Get all tags from the repository, sorted by most recently updated."""
        self.get_branch_commit(org, repo)  # Ensure cache is populated
        cache_path = self._clone_repo(org, repo)
        output, _ = call_executable_quietly(
            [
                "git",
                "for-each-ref",
                "--sort=-taggerdate",
                "--format=%(refname:short)",
                "refs/tags/",
            ],
            cwd=cache_path,
        )
        return output.strip().split("\n")

    def cache_repositories(
        self, repositories: list[tuple[str, str]], progress: Progress
    ) -> None:
        """Cache multiple repositories in parallel using multiprocessing.

        Args:
            repositories: List of (org, repo) tuples to cache
            progress: Progress callback for status updates
        """
        if not repositories:
            return

        progress.info(
            f"Caching {len(repositories)} repositories in parallel...", icon="📦"
        )

        # Prepare arguments for the worker pool
        clone_args = [(self, org, repo, progress) for org, repo in repositories]

        # Use multiprocessing to clone repositories in parallel
        # Use cpu_count for number of workers, but cap at reasonable limit
        num_workers = min(multiprocessing.cpu_count(), len(repositories), 8)

        with multiprocessing.Pool(processes=num_workers) as pool:
            pool.starmap(_clone_repo_worker, clone_args)

        progress.info(f"Finished caching {len(repositories)} repositories", icon="✅")

    def _prepare_pr(self, org: str, repo: str, pr: int) -> None:
        """Prepare the local cache for the given PR reference.

        Note: this call uses the api on the background to resolve PR details,
        we will cache the results to avoid hitting the API rate limits.
        """
        # use the gh client to fetch information about the PR
        output, _ = call_executable_quietly(
            [
                "gh",
                "pr",
                "view",
                str(pr),
                "--repo",
                f"{org}/{repo}",
                "--json",
                "commits,headRepository,headRefName,headRepositoryOwner",
            ]
        )
        pr_info: Any = json.loads(output)
        head_org = pr_info["headRepositoryOwner"]["login"]
        head_repo = pr_info["headRepository"]["name"]
        head_branch = pr_info["headRefName"]
        commits = [commit["oid"] for commit in pr_info["commits"]]

        self._pr_cache[(org, repo, pr)] = PullRequestInfo(
            source_org=head_org,
            source_repo=head_repo,
            source_branch=head_branch,
            commits=commits,
        )

    def _clone_repo(self, org: str, repo: str) -> Path:
        """Clone the specified branch of the repository into the cache."""
        repo_cache_path = self._cache_dir / org / repo
        if repo_cache_path.exists():
            return repo_cache_path

        repo_cache_path.parent.mkdir(parents=True, exist_ok=True)

        call_executable_quietly(
            [
                "gh",
                "repo",
                "clone",
                f"{org}/{repo}",
                str(repo_cache_path),
            ]
        )
        call_executable_quietly(
            [
                "git",
                "fetch",
                "--all",
            ],
            cwd=repo_cache_path,
        )

        return repo_cache_path


def _clone_repo_worker(
    cache: GitCache, org: str, repo: str, progress: Progress
) -> None:
    """Worker function for parallel repository cloning.

    Args:
        cache: GitCache instance
        org: GitHub organization
        repo: GitHub repository
        progress: Progress reporter

    Returns:
        Path to the cached repository
    """

    progress.info(f"Caching repository {org}/{repo}...", icon="📦")
    cache._clone_repo(org, repo)  # type: ignore[reportPrivateUsage]
