"""GitHub repository setup and workflow management."""

import json
import shutil
import subprocess
import time
import webbrowser
from pathlib import Path

from invenio_testrig.types import Progress


def setup_github_repository(
    target: str | None,
    patches: list[str],
    name: str | None,
    python_version: str,
    disable_codestyle_checks: bool,
    patch_mode: str,
    test_scope: str,
    test_mode: str,
    progress: Progress,
    source_repo: str = "oarepo/invenio-testrig",
) -> None:
    """Setup GitHub repository for testing patches.

    This function:
    1. Forks or updates the inveniosoftware/invenio-testrig repository
    2. Creates a gh-pages branch if it doesn't exist
    3. Optionally dispatches a workflow with the provided patches
    4. Opens a browser window with the workflow run

    Args:
        target: Target repository name in format 'org/repo'. If None, forks to current user as 'invenio-testrig'
        patches: List of patch references to test (e.g., ['org/package#123'])
        name: Test name (used in reports)
        python_version: Python version to use for testing
        disable_codestyle_checks: Disable codestyle checks during tests
        patch_mode: Test upstream or pinned versions
        test_scope: Test scope ('affected' or 'all')
        test_mode: Test selection for patched packages
        progress: Progress reporter for status updates
        source_repo: Source repository name in format 'org/repo'
    """

    username = _get_current_github_username()
    target_repo = _determine_target_repository(target, username, progress)
    repo_exists = _check_repository_exists(target_repo, progress)

    if repo_exists:
        _update_repository(target_repo, source_repo, progress)
    else:
        _fork_repository(source_repo, target_repo, username, progress)

    _ensure_gh_pages_branch(target_repo, progress)

    workflow_url = _dispatch_workflow(
        target_repo,
        patches,
        name,
        python_version,
        disable_codestyle_checks,
        patch_mode,
        test_scope,
        test_mode,
        progress,
    )

    _open_workflow_in_browser(workflow_url, progress)

    progress.success("GitHub repository setup complete!")
    progress.info(f"Repository: https://github.com/{target_repo}")


def _get_current_github_username() -> str:
    """Get the current GitHub username using the gh CLI."""
    result = subprocess.run(
        ["gh", "api", "user", "--jq", ".login"],
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout.strip()


def _determine_target_repository(target: str | None, username: str, progress: Progress):
    """Determine the target repository for forking.

    Args:
        target: Target repository name in format 'org/repo' or None
        username: GitHub username of the current user
        progress: Progress reporter for status updates

    Returns:
        Target repository name in format 'org/repo'

    Raises:
        SystemExit: If target is None and GitHub username cannot be determined
    """
    if target:
        if "/" not in target:
            target = f"{target}/invenio-testrig"
        progress.info(f"Using target repository: {target}")
        return target

    # Put the testrig into the user's namespace by default
    try:
        target_repo = f"{username}/invenio-testrig"
        progress.info(f"Will use default target: {target_repo}")
        return target_repo
    except subprocess.CalledProcessError:
        progress.error(
            "Failed to get GitHub username. Are you logged in to gh? "
            "Run 'gh auth login' first."
        )
        raise SystemExit(1)


def _check_repository_exists(target_repo: str, progress: Progress) -> bool:
    """Check if the target repository exists.

    Args:
        target_repo: Repository name in format 'org/repo'
        progress: Progress reporter for status updates

    Returns:
        True if repository exists, False otherwise
    """
    progress.start("Checking if target repository exists", icon="🔍")
    try:
        subprocess.run(
            ["gh", "repo", "view", target_repo],
            capture_output=True,
            check=True,
            text=True,
        )
        progress.info(f"Repository {target_repo} already exists")
        return True
    except subprocess.CalledProcessError:
        progress.info(f"Repository {target_repo} does not exist")
        return False


def _update_repository(target_repo: str, source_repo: str, progress: Progress) -> None:
    """Update existing repository to match upstream.

    Args:
        target_repo: Repository name in format 'org/repo'
        source_repo: Source repository name in format 'org/repo'
        progress: Progress reporter for status updates

    Raises:
        SystemExit: If update fails
    """
    progress.start(f"Updating {target_repo} to match {source_repo}", icon="🔄")
    try:
        temp_dir = Path.cwd() / ".tmp_invenio_testrig"
        if temp_dir.exists():
            shutil.rmtree(temp_dir)

        # Clone the repository
        subprocess.run(
            ["gh", "repo", "clone", target_repo, str(temp_dir)],
            check=True,
            capture_output=True,
        )

        # Add upstream remote and sync
        subprocess.run(
            [
                "git",
                "remote",
                "add",
                "upstream",
                f"https://github.com/{source_repo}.git",
            ],
            cwd=temp_dir,
            capture_output=True,
        )

        subprocess.run(
            ["git", "fetch", "upstream"],
            cwd=temp_dir,
            check=True,
            capture_output=True,
        )

        default_branch = "master"

        # Reset to upstream
        subprocess.run(
            ["git", "checkout", default_branch],
            cwd=temp_dir,
            check=True,
            capture_output=True,
        )

        subprocess.run(
            ["git", "rebase", f"upstream/{default_branch}"],
            cwd=temp_dir,
            check=True,
            capture_output=True,
        )

        subprocess.run(
            ["git", "push", "origin", default_branch, "--force"],
            cwd=temp_dir,
            check=True,
            capture_output=True,
        )

        # Cleanup
        shutil.rmtree(temp_dir)
        progress.success(f"Updated {target_repo} to match {source_repo}")

    except subprocess.CalledProcessError as e:
        progress.error(f"Failed to update repository: {e}")
        raise SystemExit(1)


def _fork_repository(
    source_repo: str, target_repo: str, username: str, progress: Progress
) -> None:
    """Fork the source repository to target.

    Args:
        source_repo: Source repository name in format 'org/repo'
        target_repo: Target repository name in format 'org/repo'
        username: GitHub username of the current user
        progress: Progress reporter for status updates

    Raises:
        SystemExit: If fork fails
    """
    progress.start(f"Forking {source_repo} to {target_repo}", icon="🍴")
    try:
        # Extract repo name from target
        repo_org = target_repo.split("/")[0]
        repo_name = target_repo.split("/")[1]
        fork_params = [
            "gh",
            "repo",
            "fork",
            source_repo,
            "--fork-name",
            repo_name,
            "--clone=false",
            "--default-branch-only",
        ]
        if repo_org != username:
            fork_params.extend(["--org", repo_org])
        subprocess.run(
            fork_params,
            check=True,
            capture_output=True,
        )
        progress.success(f"Forked {source_repo} to {target_repo}")

    except subprocess.CalledProcessError as e:
        progress.error(f"Failed to fork repository: {e}")
        raise SystemExit(1)


def _ensure_gh_pages_branch(target_repo: str, progress: Progress) -> None:
    """Ensure gh-pages branch exists in the target repository.

    Args:
        target_repo: Repository name in format 'org/repo'
        progress: Progress reporter for status updates

    Raises:
        SystemExit: If gh-pages branch creation fails
    """
    progress.start("Checking gh-pages branch", icon="📄")
    try:
        result = subprocess.run(
            ["gh", "api", f"repos/{target_repo}/branches/gh-pages"],
            capture_output=True,
            text=True,
        )
        if result.returncode == 0:
            progress.info("gh-pages branch already exists")
            return
        raise subprocess.CalledProcessError(result.returncode, result.args)
    except subprocess.CalledProcessError:
        pass

    # Create gh-pages branch
    progress.info("Creating gh-pages branch")
    try:
        temp_dir = Path.cwd() / ".tmp_invenio_testrig"
        if temp_dir.exists():
            shutil.rmtree(temp_dir)

        subprocess.run(
            ["gh", "repo", "clone", target_repo, str(temp_dir)],
            check=True,
            capture_output=True,
        )

        # Create orphan gh-pages branch
        subprocess.run(
            ["git", "checkout", "--orphan", "gh-pages"],
            cwd=temp_dir,
            check=True,
            capture_output=True,
        )

        subprocess.run(
            ["git", "rm", "-rf", "."],
            cwd=temp_dir,
            capture_output=True,
        )

        subprocess.run(
            ["git", "commit", "--allow-empty", "-m", "Initialize gh-pages branch"],
            cwd=temp_dir,
            check=True,
            capture_output=True,
        )

        subprocess.run(
            ["git", "push", "origin", "gh-pages"],
            cwd=temp_dir,
            check=True,
            capture_output=True,
        )

        # Cleanup
        shutil.rmtree(temp_dir)
        progress.success("Created gh-pages branch")

    except subprocess.CalledProcessError as e:
        progress.error(f"Failed to create gh-pages branch: {e}")
        raise SystemExit(1)


def _dispatch_workflow(
    target_repo: str,
    patches: list[str],
    name: str | None,
    python_version: str,
    disable_codestyle_checks: bool,
    patch_mode: str,
    test_scope: str,
    test_mode: str,
    progress: Progress,
) -> str | None:
    """Dispatch workflow or return workflow page URL.

    Args:
        target_repo: Repository name in format 'org/repo'
        patches: List of patch references to test
        name: Test name (used in reports)
        python_version: Python version to use for testing
        disable_codestyle_checks: Disable codestyle checks during tests
        patch_mode: Test upstream or pinned versions
        test_scope: Test scope ('affected' or 'all')
        test_mode: Test selection for patched packages
        progress: Progress reporter for status updates

    Returns:
        Workflow URL if available, None otherwise
    """
    workflow_url = None

    if not patches:
        progress.info(
            "No patches provided. You can start the workflow manually from the Actions tab."
        )
        return f"https://github.com/{target_repo}/actions/workflows/verify-patches.yml"

    progress.start("Dispatching workflow with patches", icon="🚀")
    try:
        # Build workflow dispatch command
        patches_str = " ".join(patches)
        workflow_cmd = [
            "gh",
            "workflow",
            "run",
            "verify-patches.yml",
            "--repo",
            target_repo,
            "-f",
            f"patches={patches_str}",
            "-f",
            f"python-version={python_version}",
            "-f",
            f"disable-codestyle-checks={str(disable_codestyle_checks).lower()}",
            "-f",
            f"patch-mode={patch_mode}",
            "-f",
            f"test-scope={test_scope}",
            "-f",
            f"test-mode={test_mode}",
        ]

        # Add name if provided
        if name:
            workflow_cmd.extend(["-f", f"name={name}"])

        # Dispatch the workflow
        subprocess.run(
            workflow_cmd,
            check=True,
            capture_output=True,
        )

        # Wait a moment for the workflow to be created
        time.sleep(2)

        # Get the latest workflow run
        result = subprocess.run(
            [
                "gh",
                "run",
                "list",
                "--repo",
                target_repo,
                "--workflow=verify-patches.yml",
                "--limit",
                "1",
                "--json",
                "databaseId,url",
            ],
            capture_output=True,
            text=True,
            check=True,
        )

        runs = json.loads(result.stdout)
        if runs:
            workflow_url = runs[0]["url"]
            progress.success("Workflow dispatched successfully")
            progress.info(f"Workflow URL: {workflow_url}")

    except subprocess.CalledProcessError:
        progress.warning(
            "Failed to dispatch workflow. You can start it manually from the Actions tab."
        )
        workflow_url = (
            f"https://github.com/{target_repo}/actions/workflows/verify-patches.yml"
        )

    return workflow_url


def _open_workflow_in_browser(workflow_url: str | None, progress: Progress) -> None:
    """Open workflow URL in browser.

    Args:
        workflow_url: Workflow URL to open
        progress: Progress reporter for status updates
    """
    if not workflow_url:
        return

    progress.info("Opening browser with workflow page...")
    try:
        webbrowser.open(workflow_url)
    except Exception as e:
        progress.warning(f"Failed to open browser: {e}")
        progress.info(f"Please visit: {workflow_url}")
