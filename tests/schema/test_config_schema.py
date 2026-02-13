"""Tests for config module."""

from collections.abc import Callable
from typing import Any, cast

import pytest
from marshmallow import ValidationError

from invenio_testrig.config import GitReferencePolyField
from invenio_testrig.github.types import GitReference

DeserializeReference = Callable[[str | dict[str, Any]], GitReference]


@pytest.fixture
def git_reference_field() -> GitReferencePolyField:
    """Create GitReferencePolyField instance."""
    return GitReferencePolyField()


@pytest.fixture
def deserialize_reference(
    git_reference_field: GitReferencePolyField,
) -> DeserializeReference:
    """Deserialize a string or dict into a GitReference with proper typing."""

    def _deserialize(value: str | dict[str, Any]) -> GitReference:
        return cast(GitReference, git_reference_field.deserialize(value))  # type: ignore[reportUnknownMemberType]

    return _deserialize


# GitReferencePolyField tests


def test_simple_org_repo(
    deserialize_reference: DeserializeReference,
    empty_git_reference: GitReference,
) -> None:
    """Test parsing simple org/repo format."""
    result = deserialize_reference("inveniosoftware/invenio-base")

    assert result == {
        **empty_git_reference,
        "org": "inveniosoftware",
        "repo": "invenio-base",
        "package": "invenio-base",
    }


def test_org_repo_with_branch(
    deserialize_reference: DeserializeReference,
    empty_git_reference: GitReference,
) -> None:
    """Test parsing org/repo@branch format."""
    result = deserialize_reference("inveniosoftware/invenio-base@master")

    assert result == {
        **empty_git_reference,
        "org": "inveniosoftware",
        "repo": "invenio-base",
        "package": "invenio-base",
        "branch": "master",
    }


def test_org_repo_with_pr(
    deserialize_reference: DeserializeReference,
    empty_git_reference: GitReference,
) -> None:
    """Test parsing org/repo#pr format."""
    result = deserialize_reference("inveniosoftware/invenio-base#123")

    assert result == {
        **empty_git_reference,
        "org": "inveniosoftware",
        "repo": "invenio-base",
        "package": "invenio-base",
        "pr": 123,
    }


def test_with_package_prefix(
    deserialize_reference: DeserializeReference,
    empty_git_reference: GitReference,
) -> None:
    """Test parsing package_name: org/repo format."""
    result = deserialize_reference("invenio-base: inveniosoftware/invenio-base")

    assert result == {
        **empty_git_reference,
        "package": "invenio-base",
        "org": "inveniosoftware",
        "repo": "invenio-base",
    }


def test_with_base_bracket(
    deserialize_reference: DeserializeReference,
    empty_git_reference: GitReference,
) -> None:
    """Test parsing org/repo@branch[base] format."""
    result = deserialize_reference("inveniosoftware/invenio-base@feature[master]")

    assert result == {
        **empty_git_reference,
        "org": "inveniosoftware",
        "repo": "invenio-base",
        "package": "invenio-base",
        "branch": "feature",
        "base": "master",
    }


def test_with_version_constraint_simple(
    deserialize_reference: DeserializeReference,
    empty_git_reference: GitReference,
) -> None:
    """Test parsing org/repo@branch>=2.0.0 format."""
    result = deserialize_reference("inveniosoftware/invenio-base@master>=2.0.0")

    assert result == {
        **empty_git_reference,
        "org": "inveniosoftware",
        "repo": "invenio-base",
        "package": "invenio-base",
        "branch": "master",
        "versions": [{"operator": ">=", "version": "2.0.0"}],
    }


def test_with_version_constraint_range(
    deserialize_reference: DeserializeReference,
    empty_git_reference: GitReference,
) -> None:
    """Test parsing org/repo with version range."""
    result = deserialize_reference("inveniosoftware/invenio-base>=2.0.0,<3.0.0")

    assert result == {
        **empty_git_reference,
        "org": "inveniosoftware",
        "repo": "invenio-base",
        "package": "invenio-base",
        "versions": [
            {"operator": ">=", "version": "2.0.0"},
            {"operator": "<", "version": "3.0.0"},
        ],
    }


@pytest.mark.parametrize(
    "git_ref_str,expected_version",
    [
        ("inveniosoftware/invenio-base>=2.0.0a1", "2.0.0a1"),
        ("inveniosoftware/invenio-base>=2.0.0alpha1", "2.0.0alpha1"),
        ("inveniosoftware/invenio-base>=2.0.0b2", "2.0.0b2"),
        ("inveniosoftware/invenio-base>=2.0.0beta2", "2.0.0beta2"),
        ("inveniosoftware/invenio-base>=2.0.0rc1", "2.0.0rc1"),
        ("inveniosoftware/invenio-base>=2.0.0c1", "2.0.0c1"),
    ],
)
def test_with_pre_release_version(
    deserialize_reference: DeserializeReference,
    empty_git_reference: GitReference,
    git_ref_str: str,
    expected_version: str,
) -> None:
    """Test parsing with pre-release version (alpha, beta, rc)."""
    result = deserialize_reference(git_ref_str)
    assert result == {
        **empty_git_reference,
        "org": "inveniosoftware",
        "repo": "invenio-base",
        "package": "invenio-base",
        "versions": [{"operator": ">=", "version": expected_version}],
    }


def test_with_post_release_version(
    deserialize_reference: DeserializeReference,
    empty_git_reference: GitReference,
) -> None:
    """Test parsing with post-release version."""
    result = deserialize_reference("inveniosoftware/invenio-base>=2.0.0.post1")

    assert result == {
        **empty_git_reference,
        "org": "inveniosoftware",
        "repo": "invenio-base",
        "package": "invenio-base",
        "versions": [{"operator": ">=", "version": "2.0.0.post1"}],
    }


def test_with_dev_version(
    deserialize_reference: DeserializeReference,
    empty_git_reference: GitReference,
) -> None:
    """Test parsing with dev version."""
    result = deserialize_reference("inveniosoftware/invenio-base>=2.0.0.dev1")

    assert result == {
        **empty_git_reference,
        "org": "inveniosoftware",
        "repo": "invenio-base",
        "package": "invenio-base",
        "versions": [{"operator": ">=", "version": "2.0.0.dev1"}],
    }


def test_with_local_version(
    deserialize_reference: DeserializeReference,
    empty_git_reference: GitReference,
) -> None:
    """Test parsing with local version identifier."""
    result = deserialize_reference("inveniosoftware/invenio-base>=2.0.0+local.1")

    assert result == {
        **empty_git_reference,
        "org": "inveniosoftware",
        "repo": "invenio-base",
        "package": "invenio-base",
        "versions": [{"operator": ">=", "version": "2.0.0+local.1"}],
    }


def test_complex_version_combination(
    deserialize_reference: DeserializeReference,
    empty_git_reference: GitReference,
) -> None:
    """Test parsing with complex version combination."""
    result = deserialize_reference(
        "inveniosoftware/invenio-base>=2.0.0rc1.post1.dev2+local"
    )

    assert result == {
        **empty_git_reference,
        "org": "inveniosoftware",
        "repo": "invenio-base",
        "package": "invenio-base",
        "versions": [{"operator": ">=", "version": "2.0.0rc1.post1.dev2+local"}],
    }


def test_all_features_combined(
    deserialize_reference: DeserializeReference,
    empty_git_reference: GitReference,
) -> None:
    """Test parsing with all features combined."""
    result = deserialize_reference(
        "invenio-base: inveniosoftware/invenio-base@feature[master]>=2.0.0,<3.0.0"
    )

    assert result == {
        **empty_git_reference,
        "package": "invenio-base",
        "org": "inveniosoftware",
        "repo": "invenio-base",
        "branch": "feature",
        "base": "master",
        "versions": [
            {"operator": ">=", "version": "2.0.0"},
            {"operator": "<", "version": "3.0.0"},
        ],
    }


def test_with_pr_and_base(
    deserialize_reference: DeserializeReference,
    empty_git_reference: GitReference,
) -> None:
    """Test parsing with PR and base."""
    result = deserialize_reference("inveniosoftware/invenio-base#123[master]")

    assert result == {
        **empty_git_reference,
        "org": "inveniosoftware",
        "repo": "invenio-base",
        "package": "invenio-base",
        "pr": 123,
        "base": "master",
    }


def test_invalid_format_no_slash(deserialize_reference: DeserializeReference) -> None:
    """Test that invalid format without slash raises error."""
    with pytest.raises(ValidationError) as exc_info:
        deserialize_reference("invenio-base")

    assert "Invalid git reference format" in str(exc_info.value)


def test_invalid_format_empty_string(
    deserialize_reference: DeserializeReference,
) -> None:
    """Test that empty string raises error."""
    with pytest.raises(ValidationError):
        deserialize_reference("")


def test_invalid_format_missing_repo(
    deserialize_reference: DeserializeReference,
) -> None:
    """Test that missing repo name raises error."""
    with pytest.raises(ValidationError):
        deserialize_reference("inveniosoftware/")


def test_non_string_input(deserialize_reference: DeserializeReference) -> None:
    """Test that non-string input raises error."""
    with pytest.raises(ValidationError) as exc_info:
        deserialize_reference(123)  # type: ignore[arg-type]

    assert "Git reference must be a string or dictionary" in str(exc_info.value)


def test_with_hyphens_in_names(
    deserialize_reference: DeserializeReference,
    empty_git_reference: GitReference,
) -> None:
    """Test parsing with hyphens in org, repo, and branch names."""
    result = deserialize_reference("my-org/my-repo@my-branch")

    assert result == {
        **empty_git_reference,
        "org": "my-org",
        "repo": "my-repo",
        "package": "my-repo",
        "branch": "my-branch",
    }


def test_with_underscores_in_names(
    deserialize_reference: DeserializeReference,
    empty_git_reference: GitReference,
) -> None:
    """Test parsing with underscores in names."""
    result = deserialize_reference("my_org/my_repo@my_branch")

    assert result == {
        **empty_git_reference,
        "org": "my_org",
        "repo": "my_repo",
        "package": "my_repo",
        "branch": "my_branch",
    }


@pytest.mark.parametrize("operator", [">=", "<=", ">", "<", "==", "!="])
def test_version_operators(
    deserialize_reference: DeserializeReference,
    empty_git_reference: GitReference,
    operator: str,
) -> None:
    """Test all version operators."""
    result = deserialize_reference(f"org/repo{operator}1.0.0")
    assert result == {
        **empty_git_reference,
        "org": "org",
        "repo": "repo",
        "package": "repo",
        "versions": [{"operator": operator, "version": "1.0.0"}],
    }


# GitReferencePolyField dictionary input tests


def test_git_reference_dict_simple_input(
    deserialize_reference: DeserializeReference,
    empty_git_reference: GitReference,
) -> None:
    """Test parsing dict input without pr_info."""
    input_dict: dict[str, Any] = {
        "org": "inveniosoftware",
        "repo": "invenio-base",
        "package": "invenio-base",
        "branch": "master",
        "pr": None,
        "base": None,
        "versions": [],
        "pr_info": None,
        "commit": None,
    }
    result = deserialize_reference(input_dict)

    assert result == {
        **empty_git_reference,
        "org": "inveniosoftware",
        "repo": "invenio-base",
        "package": "invenio-base",
        "branch": "master",
        "pr_info": None,
    }


def test_git_reference_dict_with_pr_info(
    deserialize_reference: DeserializeReference,
    empty_git_reference: GitReference,
) -> None:
    """Test parsing dict input with pr_info."""
    input_dict: dict[str, Any] = {
        "org": "inveniosoftware",
        "repo": "invenio-rdm-records",
        "package": "invenio-rdm-records",
        "pr": 123,
        "branch": None,
        "base": None,
        "versions": [],
        "pr_info": {
            "source_org": "contributor",
            "source_repo": "invenio-rdm-records",
            "source_branch": "fix-bug",
            "commits": ["abc123def456", "789ghi012jkl"],
        },
    }
    result = deserialize_reference(input_dict)

    assert result["org"] == "inveniosoftware"
    assert result["repo"] == "invenio-rdm-records"
    assert result["pr"] == 123
    assert result["pr_info"] is not None
    assert result["pr_info"]["source_org"] == "contributor"
    assert result["pr_info"]["source_repo"] == "invenio-rdm-records"
    assert result["pr_info"]["source_branch"] == "fix-bug"
    assert len(result["pr_info"]["commits"]) == 2
    assert result["pr_info"]["commits"][0] == "abc123def456"


def test_git_reference_dict_with_versions(
    deserialize_reference: DeserializeReference,
    empty_git_reference: GitReference,
) -> None:
    """Test parsing dict input with version constraints."""
    input_dict: dict[str, Any] = {
        "org": "inveniosoftware",
        "repo": "invenio-base",
        "package": "invenio-base",
        "branch": "master",
        "pr": None,
        "base": None,
        "versions": [
            {"operator": ">=", "version": "2.0.0"},
            {"operator": "<", "version": "3.0.0"},
        ],
        "pr_info": None,
        "commit": None,
    }
    result = deserialize_reference(input_dict)

    assert result == {
        **empty_git_reference,
        "org": "inveniosoftware",
        "repo": "invenio-base",
        "package": "invenio-base",
        "branch": "master",
        "versions": [
            {"operator": ">=", "version": "2.0.0"},
            {"operator": "<", "version": "3.0.0"},
        ],
        "pr_info": None,
    }


def test_git_reference_dict_with_all_fields(
    deserialize_reference: DeserializeReference,
    empty_git_reference: GitReference,
) -> None:
    """Test parsing dict input with all fields populated."""
    input_dict: dict[str, Any] = {
        "org": "inveniosoftware",
        "repo": "invenio-base",
        "branch": "feature",
        "pr": 456,
        "package": "invenio-base",
        "base": "master",
        "versions": [{"operator": ">=", "version": "2.0.0"}],
        "pr_info": {
            "source_org": "contributor",
            "source_repo": "invenio-base",
            "source_branch": "feature-branch",
            "commits": ["commit1", "commit2", "commit3"],
        },
    }
    result = deserialize_reference(input_dict)

    assert result["org"] == "inveniosoftware"
    assert result["repo"] == "invenio-base"
    assert result["branch"] == "feature"
    assert result["pr"] == 456
    assert result["package"] == "invenio-base"
    assert result["base"] == "master"
    assert len(result["versions"]) == 1
    assert result["versions"][0]["operator"] == ">="
    assert result["pr_info"] is not None
    assert len(result["pr_info"]["commits"]) == 3


def test_git_reference_dict_missing_required_field(
    deserialize_reference: DeserializeReference,
) -> None:
    """Test that dict input missing required fields raises error."""
    input_dict: dict[str, Any] = {
        "org": "inveniosoftware",
        # Missing 'repo' and 'package' fields
        "branch": "master",
    }
    with pytest.raises(ValidationError) as exc_info:
        deserialize_reference(input_dict)

    error_str = str(exc_info.value)
    assert "repo" in error_str or "package" in error_str


def test_git_reference_dict_invalid_pr_info(
    deserialize_reference: DeserializeReference,
) -> None:
    """Test that dict input with invalid pr_info raises error."""
    input_dict: dict[str, Any] = {
        "org": "inveniosoftware",
        "repo": "invenio-base",
        "package": "invenio-base",
        "pr": 123,
        "pr_info": {
            "source_org": "contributor",
            # Missing required fields: source_repo, source_branch, commits
        },
    }
    with pytest.raises(ValidationError) as exc_info:
        deserialize_reference(input_dict)

    error_str = str(exc_info.value)
    assert (
        "source_repo" in error_str
        or "source_branch" in error_str
        or "commits" in error_str
    )


def test_git_reference_dict_pr_info_none(
    deserialize_reference: DeserializeReference,
    empty_git_reference: GitReference,
) -> None:
    """Test parsing dict input with pr_info explicitly set to None."""
    input_dict: dict[str, Any] = {
        "org": "inveniosoftware",
        "repo": "invenio-base",
        "package": "invenio-base",
        "pr": 123,
        "branch": None,
        "base": None,
        "versions": [],
        "pr_info": None,
        "commit": None,
    }
    result = deserialize_reference(input_dict)

    assert result == {
        **empty_git_reference,
        "org": "inveniosoftware",
        "repo": "invenio-base",
        "package": "invenio-base",
        "pr": 123,
        "pr_info": None,
    }
