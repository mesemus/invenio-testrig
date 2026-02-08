"""Tests for git_api module."""

import os
import tempfile
from pathlib import Path
from unittest.mock import patch

import httpx
import pytest
import respx

from invenio_testrig import JSON
from invenio_testrig.git_api import GitApi, git_api, initialize_git_api

# Skip marker for tests requiring GitHub API access
requires_github_token = pytest.mark.skipif(
    not os.environ.get("GITHUB_TOKEN"),
    reason="Requires GITHUB_TOKEN environment variable",
)

# Test GitApi initialization


def test_init_without_token(git_api_no_token: GitApi) -> None:
    """Test initialization without authentication token."""
    assert git_api_no_token.token is None
    assert git_api_no_token.client.base_url == "https://api.github.com"
    assert git_api_no_token.client.headers["Accept"] == "application/vnd.github+json"
    assert "Authorization" not in git_api_no_token.client.headers


def test_init_with_token(git_api_with_token: GitApi) -> None:
    """Test initialization with authentication token."""
    assert git_api_with_token.token == "test_token_123"
    assert git_api_with_token.client.base_url == "https://api.github.com"
    assert git_api_with_token.client.headers["Accept"] == "application/vnd.github+json"
    assert git_api_with_token.client.headers["Authorization"] == "Bearer test_token_123"


# Test get_commit method


@respx.mock
def test_get_commit_success(git_api_no_token: GitApi) -> None:
    """Test successful get_commit request."""
    mock_response: JSON = {"sha": "abc123def456"}

    respx.get(
        "https://api.github.com/repos/inveniosoftware/invenio-app/commits/main"
    ).mock(return_value=httpx.Response(200, json=mock_response))

    result = git_api_no_token.get_commit("inveniosoftware", "invenio-app", "main")

    assert result == "abc123def456"


@respx.mock
def test_get_commit_not_found(git_api_no_token: GitApi) -> None:
    """Test get_commit with non-existent branch."""
    respx.get(
        "https://api.github.com/repos/inveniosoftware/invenio-app/commits/nonexistent"
    ).mock(return_value=httpx.Response(404, json={"message": "Branch not found"}))

    with pytest.raises(httpx.HTTPStatusError):
        git_api_no_token.get_commit("inveniosoftware", "invenio-app", "nonexistent")


@respx.mock
def test_get_commit_with_auth(git_api_with_token: GitApi) -> None:
    """Test get_commit with authentication token."""
    mock_response: JSON = {"sha": "xyz789abc123"}

    route = respx.get(
        "https://api.github.com/repos/private-org/private-repo/commits/develop"
    ).mock(return_value=httpx.Response(200, json=mock_response))

    result = git_api_with_token.get_commit("private-org", "private-repo", "develop")

    assert result == "xyz789abc123"
    # Verify authorization header was sent
    assert route.calls.last.request.headers["Authorization"] == "Bearer test_token_123"


# Test resolve_pr method


@respx.mock
def test_resolve_pr_success(git_api_no_token: GitApi) -> None:
    """Test successful PR resolution."""
    pr_response: JSON = {
        "head": {
            "ref": "feature-branch",
            "repo": {"name": "invenio-app", "owner": {"login": "contributor"}},
        }
    }

    commits_response: list[JSON] = [
        {"sha": "commit1abc"},
        {"sha": "commit2def"},
        {"sha": "commit3ghi"},
    ]

    respx.get(
        "https://api.github.com/repos/inveniosoftware/invenio-app/pulls/123"
    ).mock(return_value=httpx.Response(200, json=pr_response))
    respx.get(
        "https://api.github.com/repos/inveniosoftware/invenio-app/pulls/123/commits"
    ).mock(return_value=httpx.Response(200, json=commits_response))

    result = git_api_no_token.resolve_pr("inveniosoftware", "invenio-app", 123)

    assert result["source_org"] == "contributor"
    assert result["source_repo"] == "invenio-app"
    assert result["source_branch"] == "feature-branch"
    assert result["commits"] == ["commit1abc", "commit2def", "commit3ghi"]


@respx.mock
def test_resolve_pr_single_commit(git_api_no_token: GitApi) -> None:
    """Test PR resolution with single commit."""
    pr_response: JSON = {
        "head": {
            "ref": "hotfix",
            "repo": {"name": "invenio-rdm", "owner": {"login": "maintainer"}},
        }
    }

    commits_response: list[JSON] = [{"sha": "single123"}]

    respx.get("https://api.github.com/repos/inveniosoftware/invenio-rdm/pulls/42").mock(
        return_value=httpx.Response(200, json=pr_response)
    )
    respx.get(
        "https://api.github.com/repos/inveniosoftware/invenio-rdm/pulls/42/commits"
    ).mock(return_value=httpx.Response(200, json=commits_response))

    result = git_api_no_token.resolve_pr("inveniosoftware", "invenio-rdm", 42)

    assert result["commits"] == ["single123"]


@respx.mock
def test_resolve_pr_not_found(git_api_no_token: GitApi) -> None:
    """Test PR resolution with non-existent PR."""
    respx.get(
        "https://api.github.com/repos/inveniosoftware/invenio-app/pulls/999"
    ).mock(return_value=httpx.Response(404, json={"message": "Not Found"}))

    with pytest.raises(httpx.HTTPStatusError):
        git_api_no_token.resolve_pr("inveniosoftware", "invenio-app", 999)


@respx.mock
def test_resolve_pr_empty_commits(git_api_no_token: GitApi) -> None:
    """Test PR resolution with no commits (edge case)."""
    pr_response: JSON = {
        "head": {
            "ref": "empty-branch",
            "repo": {"name": "test-repo", "owner": {"login": "test-user"}},
        }
    }

    commits_response: list[JSON] = []

    respx.get("https://api.github.com/repos/test-org/test-repo/pulls/1").mock(
        return_value=httpx.Response(200, json=pr_response)
    )
    respx.get("https://api.github.com/repos/test-org/test-repo/pulls/1/commits").mock(
        return_value=httpx.Response(200, json=commits_response)
    )

    result = git_api_no_token.resolve_pr("test-org", "test-repo", 1)

    assert result["commits"] == []


@respx.mock
def test_resolve_pr_with_auth(git_api_with_token: GitApi) -> None:
    """Test PR resolution with authentication."""
    pr_response: JSON = {
        "head": {
            "ref": "private-feature",
            "repo": {"name": "private-repo", "owner": {"login": "private-org"}},
        }
    }

    commits_response: list[JSON] = [{"sha": "private1"}, {"sha": "private2"}]

    pr_route = respx.get(
        "https://api.github.com/repos/private-org/private-repo/pulls/10"
    ).mock(return_value=httpx.Response(200, json=pr_response))
    commits_route = respx.get(
        "https://api.github.com/repos/private-org/private-repo/pulls/10/commits"
    ).mock(return_value=httpx.Response(200, json=commits_response))

    result = git_api_with_token.resolve_pr("private-org", "private-repo", 10)

    assert result["source_org"] == "private-org"
    # Verify authorization header was sent for both requests
    assert (
        pr_route.calls.last.request.headers["Authorization"] == "Bearer test_token_123"
    )
    assert (
        commits_route.calls.last.request.headers["Authorization"]
        == "Bearer test_token_123"
    )


# Test initialize_git_api function


def test_initialize_without_env_token() -> None:
    """Test initialization without GITHUB_TOKEN environment variable."""
    with patch.dict(os.environ, {}, clear=True):
        api = initialize_git_api()
        assert api.token is None


def test_initialize_with_env_token() -> None:
    """Test initialization with GITHUB_TOKEN environment variable."""
    with patch.dict(os.environ, {"GITHUB_TOKEN": "env_token_456"}):
        api = initialize_git_api()
        assert api.token == "env_token_456"
        assert api.client.headers["Authorization"] == "Bearer env_token_456"


def test_initialize_preserves_other_env_vars() -> None:
    """Test that initialization doesn't affect other environment variables."""
    with patch.dict(os.environ, {"GITHUB_TOKEN": "test_token", "OTHER_VAR": "value"}):
        api = initialize_git_api()
        assert api.token == "test_token"
        assert os.environ.get("OTHER_VAR") == "value"


# Test _get private method


@respx.mock
def test_get_raises_on_error(git_api_no_token: GitApi) -> None:
    """Test that _get raises HTTPStatusError on failed requests."""
    respx.get("https://api.github.com/test/endpoint").mock(
        return_value=httpx.Response(500, json={"message": "Internal Server Error"})
    )

    with pytest.raises(httpx.HTTPStatusError):
        git_api_no_token._get("/test/endpoint")  # type: ignore[reportPrivateUsage]


@respx.mock
def test_get_returns_json(git_api_no_token: GitApi) -> None:
    """Test that _get returns JSON response data."""
    mock_data: JSON = {"key": "value", "number": 42}
    respx.get("https://api.github.com/test/data").mock(
        return_value=httpx.Response(200, json=mock_data)
    )

    result = git_api_no_token._get("/test/data")  # type: ignore[reportPrivateUsage]

    assert result == mock_data


@respx.mock
def test_get_handles_different_status_codes(git_api_no_token: GitApi) -> None:
    """Test that _get handles various HTTP error status codes."""
    test_codes = [400, 401, 403, 404, 500, 502, 503]

    for code in test_codes:
        respx.get(f"https://api.github.com/test/{code}").mock(
            return_value=httpx.Response(code, json={"error": f"Error {code}"})
        )

        with pytest.raises(httpx.HTTPStatusError):
            git_api_no_token._get(f"/test/{code}")  # type: ignore[reportPrivateUsage]


# Test clone_git_reference function


def test_clone_git_reference_with_commit() -> None:
    """Test cloning a repository and checking out a specific commit."""
    from invenio_testrig import parse_github_reference

    # Create a temporary directory for cloning
    with tempfile.TemporaryDirectory() as tmpdir:
        output_dir = Path(tmpdir) / "zenodo-rdm"

        # Parse zenodo/zenodo-rdm repository reference
        reference = parse_github_reference("zenodo/zenodo-rdm")
        # Override commit to use a relative reference
        reference["commit"] = "HEAD~5"  # Use a commit 5 commits before HEAD

        git_api.clone_git_reference(reference, output_dir)

        # Verify the repository was cloned
        assert output_dir.exists()
        assert (output_dir / ".git").exists()
        assert (output_dir / "pyproject.toml").exists()


def test_clone_git_reference_with_branch() -> None:
    """Test cloning a repository and checking out a specific branch."""
    from invenio_testrig import parse_github_reference

    # Create a temporary directory for cloning
    with tempfile.TemporaryDirectory() as tmpdir:
        output_dir = Path(tmpdir) / "invenio-rdm-records"

        # Parse inveniosoftware/invenio-rdm-records with maint-22.x branch
        reference = parse_github_reference(
            "inveniosoftware/invenio-rdm-records@maint-22.x"
        )

        git_api.clone_git_reference(reference, output_dir)

        # Verify the repository was cloned
        assert output_dir.exists()
        assert (output_dir / ".git").exists()
        assert (output_dir / "setup.py").exists() or (
            output_dir / "pyproject.toml"
        ).exists()
        # Verify commit was filled in by parse_github_reference
        assert reference["commit"] is not None


def test_clone_git_reference_default_branch() -> None:
    """Test cloning a repository without specifying branch or commit."""
    from invenio_testrig import parse_github_reference

    # Create a temporary directory for cloning
    with tempfile.TemporaryDirectory() as tmpdir:
        output_dir = Path(tmpdir) / "zenodo-rdm-default"

        # Parse zenodo/zenodo-rdm without branch (uses default branch)
        reference = parse_github_reference("zenodo/zenodo-rdm")

        git_api.clone_git_reference(reference, output_dir)

        # Verify the repository was cloned
        assert output_dir.exists()
        assert (output_dir / ".git").exists()
        assert (output_dir / "pyproject.toml").exists()


# Test last_n_tags_from_commit function


@requires_github_token
def test_last_n_tags_from_commit_zenodo_rdm() -> None:
    """Test getting last n tags from zenodo/zenodo-rdm repository."""
    from invenio_testrig import parse_github_reference

    # Parse zenodo/zenodo-rdm to get the latest commit
    reference = parse_github_reference("zenodo/zenodo-rdm")

    # Get the commit SHA (should be populated by parse_github_reference)
    commit_sha = reference["commit"]
    assert commit_sha is not None, "Commit SHA should be populated"

    # Get the last 5 tags from the commit history
    tags = git_api.last_n_tags_from_git_reference(reference, n=5)

    # Verify we got some tags back
    assert isinstance(tags, list)
    assert len(tags) <= 5  # Should not exceed requested count

    # All tags should be strings
    for tag in tags:
        assert isinstance(tag, str)
        assert len(tag) > 0


@requires_github_token
def test_last_n_tags_from_commit_with_predicate() -> None:
    """Test getting last n tags with a version predicate from zenodo/zenodo-rdm."""
    from invenio_testrig import parse_github_reference

    # Parse zenodo/zenodo-rdm to get the latest commit
    reference = parse_github_reference("zenodo/zenodo-rdm")

    commit_sha = reference["commit"]
    assert commit_sha is not None

    # Get the last 3 tags that start with 'v' (version tags)
    tags = git_api.last_n_tags_from_git_reference(
        reference,
        n=3,
        predicate=lambda tag: tag.startswith("v"),
    )

    # Verify we got some tags back
    assert isinstance(tags, list)
    assert len(tags) <= 3

    # All tags should start with 'v'
    for tag in tags:
        assert isinstance(tag, str)
        assert tag.startswith("v"), f"Tag {tag} should start with 'v'"


@requires_github_token
def test_last_n_tags_from_commit_single_tag() -> None:
    """Test getting just the last tag from zenodo/zenodo-rdm."""
    from invenio_testrig import parse_github_reference

    # Parse zenodo/zenodo-rdm to get the latest commit
    reference = parse_github_reference("zenodo/zenodo-rdm")

    commit_sha = reference["commit"]
    assert commit_sha is not None

    # Get just the last tag
    tags = git_api.last_n_tags_from_git_reference(reference, n=1)

    # Verify we got at most one tag
    assert isinstance(tags, list)
    assert len(tags) <= 1

    if len(tags) == 1:
        assert isinstance(tags[0], str)
        assert len(tags[0]) > 0
