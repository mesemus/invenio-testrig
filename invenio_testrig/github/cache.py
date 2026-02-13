import json
import shutil
from pathlib import Path
from typing import Any

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
            output, _ = call_executable_quietly(
                ["git", "rev-parse", "HEAD"],
                cwd=cache_path,
            )
        else:
            output, _ = call_executable_quietly(
                [
                    "git",
                    "for-each-ref",
                    f"refs/tags/{branch}",
                    f"refs/remotes/origin/{branch}",
                    "--format=%(objectname)",
                ],
                cwd=cache_path,
            )
        return output.strip()

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

        return repo_cache_path


# default global cache instance used by the rest of the codebase
git_cache = GitCache(cache_dir=Path("/tmp").resolve() / ".invenio_testrig_git_cache")

if __name__ == "__main__":
    # Example usage
    git_cache.clear_cache()  # Clear cache before starting
    pr_info = git_cache.get_pr_info("inveniosoftware", "invenio-rdm-records", 2205)
    print("PR Info for inveniosoftware/invenio-rdm-records#1234", pr_info)

    branch_commit = git_cache.get_branch_commit(
        "inveniosoftware", "invenio-rdm-records"
    )
    print(
        "Latest commit on default branch for inveniosoftware/invenio-rdm-records",
        branch_commit,
    )

    branch_commit = git_cache.get_branch_commit(
        "inveniosoftware", "invenio-rdm-records", branch="v10.0.0"
    )
    print(
        "Latest commit on branch v10.0.0 for inveniosoftware/invenio-rdm-records",
        branch_commit,
    )
    print("Cache path:", git_cache.cache_dir)
