"""Tests for prepare_config module."""

import httpx
import respx

from invenio_testrig import JSON
from invenio_testrig.config import GitReference
from invenio_testrig.git_api import git_api


@respx.mock
def test_resolve_git_with_pr() -> None:
    """Test resolving a git reference with PR number."""
    git_ref: GitReference = {
        "org": "inveniosoftware",
        "repo": "invenio-rdm-records",
        "branch": None,
        "pr": 2249,
        "package": "invenio-rdm-records",
        "base": None,
        "versions": [],
        "pr_info": None,
        "commit": None,
    }

    # Mock PR details response
    pr_response: JSON = {
        "head": {
            "ref": "feature-branch",
            "repo": {
                "name": "invenio-rdm-records",
                "owner": {"login": "contributor"},
            },
        }
    }

    # Mock commits response
    commits_response: list[JSON] = [
        {"sha": "commit1abc"},
        {"sha": "commit2def"},
    ]

    respx.get(
        "https://api.github.com/repos/inveniosoftware/invenio-rdm-records/pulls/2249"
    ).mock(return_value=httpx.Response(200, json=pr_response))
    respx.get(
        "https://api.github.com/repos/inveniosoftware/invenio-rdm-records/pulls/2249/commits"
    ).mock(return_value=httpx.Response(200, json=commits_response))

    result = git_api.resolve_git(git_ref)

    assert result["pr_info"] is not None
    assert result["pr_info"]["source_org"] == "contributor"
    assert result["pr_info"]["source_repo"] == "invenio-rdm-records"
    assert result["pr_info"]["source_branch"] == "feature-branch"
    assert result["pr_info"]["commits"] == ["commit1abc", "commit2def"]
    # Verify commit is set to the last commit from PR
    assert result["commit"] == "commit2def"


@respx.mock
def test_resolve_git_with_branch() -> None:
    """Test resolving a git reference with branch."""
    git_ref: GitReference = {
        "org": "inveniosoftware",
        "repo": "invenio-app",
        "branch": "main",
        "pr": None,
        "package": "invenio-app",
        "base": None,
        "versions": [],
        "pr_info": None,
        "commit": None,
    }

    # Mock branch commit response
    branch_response: JSON = {"commit": {"sha": "abc123def456"}}

    respx.get(
        "https://api.github.com/repos/inveniosoftware/invenio-app/branches/main"
    ).mock(return_value=httpx.Response(200, json=branch_response))

    result = git_api.resolve_git(git_ref)

    # Should have commit populated from branch HEAD
    assert result["pr_info"] is None
    assert result["org"] == "inveniosoftware"
    assert result["repo"] == "invenio-app"
    assert result["branch"] == "main"
    assert result["commit"] == "abc123def456"


@respx.mock
def test_resolve_git_without_pr_or_branch() -> None:
    """Test resolving a git reference without PR number or branch."""
    git_ref: GitReference = {
        "org": "inveniosoftware",
        "repo": "invenio-app",
        "branch": None,
        "pr": None,
        "package": "invenio-app",
        "base": None,
        "versions": [],
        "pr_info": None,
        "commit": None,
    }

    # Mock default branch response
    repo_response: JSON = {"default_branch": "master"}
    respx.get("https://api.github.com/repos/inveniosoftware/invenio-app").mock(
        return_value=httpx.Response(200, json=repo_response)
    )

    # Mock branch commit response
    branch_response: JSON = {"commit": {"sha": "default123"}}
    respx.get(
        "https://api.github.com/repos/inveniosoftware/invenio-app/branches/master"
    ).mock(return_value=httpx.Response(200, json=branch_response))

    result = git_api.resolve_git(git_ref)

    # Should fetch default branch and its commit
    assert result["pr_info"] is None
    assert result["branch"] == "master"
    assert result["commit"] == "default123"
    assert result["org"] == "inveniosoftware"
    assert result["repo"] == "invenio-app"


@respx.mock
def test_resolve_git_with_package_name() -> None:
    """Test resolving a git reference with package name."""
    git_ref: GitReference = {
        "org": "custom-org",
        "repo": "custom-repo",
        "branch": None,
        "pr": 42,
        "package": "custom-package",
        "base": None,
        "versions": [],
        "pr_info": None,
        "commit": None,
    }

    # Mock PR details response
    pr_response: JSON = {
        "head": {
            "ref": "bugfix",
            "repo": {
                "name": "custom-repo",
                "owner": {"login": "custom-org"},
            },
        }
    }

    # Mock commits response
    commits_response: list[JSON] = [{"sha": "fix123"}]

    respx.get("https://api.github.com/repos/custom-org/custom-repo/pulls/42").mock(
        return_value=httpx.Response(200, json=pr_response)
    )
    respx.get(
        "https://api.github.com/repos/custom-org/custom-repo/pulls/42/commits"
    ).mock(return_value=httpx.Response(200, json=commits_response))

    result = git_api.resolve_git(git_ref)

    assert result["package"] == "custom-package"
    assert result["pr_info"] is not None
    assert result["pr_info"]["source_org"] == "custom-org"
    assert result["pr_info"]["commits"] == ["fix123"]
    # Verify commit is set to the last (only) commit from PR
    assert result["commit"] == "fix123"
