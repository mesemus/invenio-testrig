"""Tests for GitHub URL parsing functionality."""

from invenio_testrig.github.ref_parser import (
    _parse_github_url as parse_github_url,  # type: ignore[reportPrivateUsage]
)
from invenio_testrig.github.types import GitReference


def test_non_https_url_returns_none():
    """Test that non-https URLs return None."""
    assert parse_github_url("http://github.com/org/repo") is None
    assert parse_github_url("git@github.com:org/repo.git") is None
    assert parse_github_url("ftp://github.com/org/repo") is None


def test_non_github_url_returns_none():
    """Test that non-GitHub URLs return None."""
    assert parse_github_url("https://gitlab.com/org/repo") is None
    assert parse_github_url("https://bitbucket.org/org/repo") is None
    assert parse_github_url("https://example.com/org/repo") is None


def test_simple_org_repo_url():
    """Test parsing a simple org/repo URL."""
    result = parse_github_url("https://github.com/inveniosoftware/invenio-rdm-records")

    assert result is not None
    assert result.org == "inveniosoftware"
    assert result.repo == "invenio-rdm-records"
    assert result.package == "invenio-rdm-records"
    assert result.branch is None
    assert result.pr is None
    assert result.base is None
    assert result.versions == []


def test_org_repo_with_git_suffix():
    """Test parsing org/repo URL with .git suffix."""
    result = parse_github_url(
        "https://github.com/inveniosoftware/invenio-rdm-records.git"
    )

    assert result is not None
    assert result.org == "inveniosoftware"
    assert result.repo == "invenio-rdm-records"
    assert result.package == "invenio-rdm-records"


def test_org_repo_tree_branch():
    """Test parsing org/repo/tree/branch-name URL."""
    result = parse_github_url(
        "https://github.com/inveniosoftware/invenio-rdm-records/tree/main"
    )

    assert result is not None
    assert result.org == "inveniosoftware"
    assert result.repo == "invenio-rdm-records"
    assert result.branch == "main"
    assert result.pr is None


def test_org_repo_tree_branch_with_slashes():
    """Test parsing branch names that might contain special characters."""
    result = parse_github_url(
        "https://github.com/inveniosoftware/invenio-rdm-records/tree/fix-form-label"
    )

    assert result is not None
    assert result.org == "inveniosoftware"
    assert result.repo == "invenio-rdm-records"
    assert result.branch == "fix-form-label"


def test_org_repo_heads_branch():
    """Test parsing org/repo/heads/branch-name URL."""
    result = parse_github_url(
        "https://github.com/inveniosoftware/invenio-rdm-records/heads/develop"
    )

    assert result is not None
    assert result.org == "inveniosoftware"
    assert result.repo == "invenio-rdm-records"
    assert result.branch == "develop"
    assert result.pr is None


def test_org_repo_pull_number():
    """Test parsing org/repo/pull/123 URL."""
    result = parse_github_url(
        "https://github.com/inveniosoftware/invenio-rdm-records/pull/2205"
    )

    assert result is not None
    assert result.org == "inveniosoftware"
    assert result.repo == "invenio-rdm-records"
    assert result.pr == 2205
    assert result.branch is None


def test_org_repo_pull_invalid_number():
    """Test parsing org/repo/pull with invalid PR number returns None."""
    result = parse_github_url(
        "https://github.com/inveniosoftware/invenio-rdm-records/pull/abc"
    )

    assert result is None


def test_url_with_trailing_slash():
    """Test that URLs with trailing slashes are handled correctly."""
    result = parse_github_url("https://github.com/inveniosoftware/invenio-rdm-records/")

    assert result is not None
    assert result.org == "inveniosoftware"
    assert result.repo == "invenio-rdm-records"


def test_package_name_lowercased():
    """Test that package names are lowercased."""
    result = parse_github_url("https://github.com/InvenioSoftware/Invenio-RDM-Records")

    assert result is not None
    assert result.org == "InvenioSoftware"
    assert result.repo == "Invenio-RDM-Records"
    assert result.package == "invenio-rdm-records"


def test_org_repo_with_git_suffix_and_tree():
    """Test parsing org/repo.git/tree/branch URL."""
    result = parse_github_url(
        "https://github.com/inveniosoftware/invenio-rdm-records.git/tree/main"
    )

    assert result is not None
    assert result.org == "inveniosoftware"
    assert result.repo == "invenio-rdm-records"
    assert result.branch == "main"


def test_returns_git_reference_type():
    """Test that the function returns a GitReference instance."""
    result = parse_github_url("https://github.com/org/repo")

    assert result is not None
    assert isinstance(result, GitReference)


def test_commit_and_pr_info_are_none():
    """Test that commit and pr_info are initialized as None."""
    result = parse_github_url("https://github.com/org/repo")

    assert result is not None
    assert result.commit is None
    assert result.pr_info is None


def test_pip_installed_github_reference_with_branch():
    result = parse_github_url(
        "https://github.com/inveniosoftware/invenio-records-resources?branch=fix-read-many#c6b973a14802e2a7f73100ab4e32cb0c36bd4672"
    )

    assert result is not None
    assert result.org == "inveniosoftware"
    assert result.repo == "invenio-records-resources"
    assert result.branch == "fix-read-many"
    assert result.commit == "c6b973a14802e2a7f73100ab4e32cb0c36bd4672"
    assert result.pr is None


def test_pip_installed_github_reference_with_rev():
    result = parse_github_url(
        "https://github.com/inveniosoftware/invenio-swh?rev=v0.13.4#828a3a415cf8e725c369939832b61281c44aec40"
    )
    assert result is not None
    assert result.org == "inveniosoftware"
    assert result.repo == "invenio-swh"
    assert result.branch == "v0.13.4"
    assert result.commit == "828a3a415cf8e725c369939832b61281c44aec40"
    assert result.pr is None
