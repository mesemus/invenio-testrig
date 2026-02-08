import os
import subprocess
from pathlib import Path
from typing import Any, Callable

import httpx
import semver

from .config import GitReference, PullRequestInfo


class GitApi:

    def __init__(self, token: str | None = None):
        self.token = token
        headers = {"Accept": "application/vnd.github+json"}

        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"

        self.client = httpx.Client(
            base_url="https://api.github.com",
            headers=headers,
        )

        # set the global git config to avoid issues with git commands in subprocess
        # only set if not already configured
        result = subprocess.run(
            ["git", "config", "--global", "user.name"],
            capture_output=True,
            text=True,
        )
        if result.returncode != 0 or not result.stdout.strip():
            subprocess.run(
                ["git", "config", "--global", "user.name", "Invenio TestRig"],
                check=True,
                capture_output=True,
                text=True,
            )

        result = subprocess.run(
            ["git", "config", "--global", "user.email"],
            capture_output=True,
            text=True,
        )
        if result.returncode != 0 or not result.stdout.strip():
            subprocess.run(
                ["git", "config", "--global", "user.email", "no-reply@cesnet.cz"],
                check=True,
                capture_output=True,
                text=True,
            )

    def _get(self, url: str) -> Any:
        """Make a GET request and return JSON response.

        Args:
            url: API endpoint URL

        Returns:
            JSON response data

        Raises:
            httpx.HTTPStatusError: If the API request fails
        """
        response = self.client.get(url)
        response.raise_for_status()
        return response.json()

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

        Raises:
            httpx.HTTPStatusError: If the API request fails (e.g., unknown ref)
        """
        url = f"/repos/{org}/{repo}/commits/{branch_or_tag_or_commit}"
        data = self._get(url)
        return data["sha"]

    def resolve_pr(self, org: str, repo: str, pr_number: int) -> PullRequestInfo:
        """
        Resolve pull request information including source details and commits.

        Args:
            org: GitHub organization or user name
            repo: Repository name
            pr_number: Pull request number

        Returns:
            Dictionary containing source_org, source_repo, source_branch, and list of commit SHAs

        Raises:
            httpx.HTTPStatusError: If the API request fails
        """
        # Get PR details
        pr_url = f"/repos/{org}/{repo}/pulls/{pr_number}"
        pr_data = self._get(pr_url)

        # Extract source information
        source_org = pr_data["head"]["repo"]["owner"]["login"]
        source_repo = pr_data["head"]["repo"]["name"]
        source_branch = pr_data["head"]["ref"]

        # Get commits in the PR
        commits_url = f"/repos/{org}/{repo}/pulls/{pr_number}/commits"
        commits_data = self._get(commits_url)

        # Extract commit SHAs
        commit_shas = [commit["sha"] for commit in commits_data]

        return {
            "source_org": source_org,
            "source_repo": source_repo,
            "source_branch": source_branch,
            "commits": commit_shas,
        }

    def get_default_branch(self, org: str, repo: str) -> str:
        """
        Get the default branch name for a repository.

        Args:
            org: GitHub organization or user name
            repo: Repository name

        Returns:
            The default branch name (e.g., "main", "master")

        Raises:
            httpx.HTTPStatusError: If the API request fails
        """
        url = f"/repos/{org}/{repo}"
        data = self._get(url)
        return data["default_branch"]

    def get_branches(self, org: str, repo: str, limit: int | None = None) -> list[str]:
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
        url = f"/repos/{org}/{repo}/branches"
        branches = self._get(url)

        if not branches:
            return []

        # Get commit details for each branch to sort by date
        branch_dates = []

        for branch in branches:
            branch_name = branch["name"]
            commit_sha = branch["commit"]["sha"]

            # Get commit details to find the commit date
            commit_url = f"/repos/{org}/{repo}/commits/{commit_sha}"
            commit_data = self._get(commit_url)
            commit_date = commit_data["commit"]["committer"]["date"]

            branch_dates.append((branch_name, commit_date))

        # Sort by date (most recent first)
        branch_dates.sort(key=lambda x: x[1], reverse=True)

        # Extract branch names
        result = [name for name, _ in branch_dates]

        if limit is not None:
            result = result[:limit]

        return result

    def get_open_prs(self, org: str, repo: str, limit: int | None = None) -> list[int]:
        """
        Get open pull request numbers, sorted by most recently updated.

        Args:
            org: GitHub organization or user name
            repo: Repository name
            limit: Maximum number of PRs to return (None for all available, max 100)

        Returns:
            List of PR numbers sorted by most recent update

        Raises:
            httpx.HTTPStatusError: If the API request fails
        """
        per_page = limit if limit is not None else 100
        url = f"/repos/{org}/{repo}/pulls?state=open&sort=updated&direction=desc&per_page={per_page}"
        prs = self._get(url)

        if not prs:
            return []

        return [pr["number"] for pr in prs]

    def resolve_git(self, git_ref: GitReference) -> GitReference:
        """
        Resolve git reference details using GitHub API.

        Fills in missing commit SHA, PR info, and other details for a GitReference.
        If no branch or PR is specified, uses the default branch.

        Args:
            git_ref: GitReference with at least org and repo populated

        Returns:
            GitReference with commit SHA and other details filled in

        Raises:
            httpx.HTTPStatusError: If GitHub API calls fail
        """
        # Resolve PR info if PR number is specified
        if git_ref["pr"]:
            if not git_ref["pr_info"]:
                pr_number = git_ref["pr"]
                pr_info = self.resolve_pr(git_ref["org"], git_ref["repo"], pr_number)
                git_ref["pr_info"] = pr_info
                git_ref["commit"] = (
                    pr_info["commits"][-1] if pr_info["commits"] else None
                )

        # Fill in commit SHA if not already set
        if not git_ref["commit"]:
            # Use branch if specified, otherwise use default branch
            if git_ref["branch"]:
                reference = git_ref["branch"]
            else:
                reference = self.get_default_branch(git_ref["org"], git_ref["repo"])
                git_ref["branch"] = reference

            commit_sha = self.get_commit(git_ref["org"], git_ref["repo"], reference)
            git_ref["commit"] = commit_sha

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

        Raises:
            subprocess.CalledProcessError: If git commands fail
        """
        import tempfile

        with tempfile.TemporaryDirectory() as tmpdir:
            temp_path = Path(tmpdir) / "repo"

            # Clone the repository
            self.clone_git_reference(reference, temp_path)

            # Get all tags reachable from current commit, sorted by commit date (newest first)
            result = subprocess.run(
                ["git", "tag", "--merged", "HEAD", "--sort=-committerdate"],
                cwd=temp_path,
                capture_output=True,
                text=True,
                check=True,
            )

            # Filter tags by predicate and return first n
            tags = []
            for tag in result.stdout.strip().split("\n"):
                if tag and predicate(tag):
                    tags.append(tag)
                    if len(tags) == n:
                        break

            return tags

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

        Raises:
            subprocess.CalledProcessError: If git commands fail
        """
        # Use PR source org/repo if PR info is available, otherwise use the original
        if reference["pr_info"]:
            org = reference["pr_info"]["source_org"]
            repo = reference["pr_info"]["source_repo"]
            branch = reference["pr_info"]["source_branch"]
        else:
            org = reference["org"]
            repo = reference["repo"]
            branch = reference["branch"]

        # Construct the repository URL
        repo_url = f"https://github.com/{org}/{repo}.git"

        # Clone the repository
        subprocess.run(
            ["git", "clone", repo_url, str(output_directory)],
            check=True,
            capture_output=True,
            text=True,
        )

        # Change to the repository directory for checkout operations
        if reference["commit"]:
            # If commit is specified, checkout that specific commit
            subprocess.run(
                ["git", "checkout", reference["commit"]],
                cwd=output_directory,
                check=True,
                capture_output=True,
                text=True,
            )
        elif branch:
            # If branch is specified (and no commit), checkout that branch
            subprocess.run(
                ["git", "checkout", branch],
                cwd=output_directory,
                check=True,
                capture_output=True,
                text=True,
            )
        # If neither commit nor branch is specified, use the default branch (already checked out)

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
        if not reference["pr"] or not reference["pr_info"]:
            raise ValueError(
                "Reference must be a pull request with pr_info. "
                f"Got pr={reference.get('pr')}, pr_info={reference.get('pr_info')}"
            )

        commits = reference["pr_info"]["commits"]

        if not commits:
            return  # Nothing to apply

        pr_info = reference["pr_info"]
        source_org = pr_info["source_org"]
        source_repo = pr_info["source_repo"]

        # Add the fork as a remote if it's different from the base repo
        # This ensures we can fetch commits even if they're from a fork
        remote_name = f"pr-{reference['pr']}-fork"
        remote_url = f"https://github.com/{source_org}/{source_repo}.git"

        try:
            # Add remote (ignore error if it already exists)
            subprocess.run(
                ["git", "remote", "add", remote_name, remote_url],
                cwd=directory,
                capture_output=True,
                text=True,
            )
        except subprocess.CalledProcessError:
            # Remote might already exist, that's fine
            pass

        # Fetch the commits from the remote
        try:
            subprocess.run(
                ["git", "fetch", remote_name],
                cwd=directory,
                check=True,
                capture_output=True,
                text=True,
            )
        except subprocess.CalledProcessError as e:
            error_msg = f"Failed to fetch from {remote_url}. Git error: {e.stderr}"
            raise subprocess.CalledProcessError(
                e.returncode, e.cmd, e.stdout, error_msg
            ) from e

        # Cherry-pick each commit from the PR
        for commit_sha in commits:
            try:
                subprocess.run(
                    ["git", "cherry-pick", commit_sha],
                    cwd=directory,
                    check=True,
                )
            except subprocess.CalledProcessError as e:
                # Include git error output in the exception message
                error_msg = (
                    f"Failed to cherry-pick commit {commit_sha}. "
                    f"Git error: {e.stderr}"
                )
                raise subprocess.CalledProcessError(
                    e.returncode, e.cmd, e.stdout, error_msg
                ) from e

        # Clean up: remove the temporary remote
        try:
            subprocess.run(
                ["git", "remote", "remove", remote_name],
                cwd=directory,
                capture_output=True,
                text=True,
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


def initialize_git_api() -> GitApi:
    """
    Initialize git api.

    Checks if run within GitHub Actions and initializes the Git API client with the appropriate token.
    If not running in Github Actions, checks if GH_TOKEN or GITHUB_TOKEN environment variable is set and uses it.
    If no token is found, initializes the Git API client without authentication.
    """
    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    return GitApi(token=token)


git_api = initialize_git_api()
