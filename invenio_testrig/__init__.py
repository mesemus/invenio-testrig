"""Invenio Test Rig - Common test automation utilities."""

from typing import Any, cast

from .config import GitReference, GitReferenceField
from .git_api import git_api

# Common type alias for JSON data structures
JSON = dict[str, Any]


def parse_github_reference(reference: str) -> GitReference:
    """
    Parse a GitHub reference string and fill in details using the GitHub API.

    Args:
        reference: GitHub reference string in format like:
            - "org/repo"
            - "org/repo@branch"
            - "org/repo#pr_number"

    Returns:
        GitReference dictionary with all fields populated, including:
        - commit SHA if branch is specified
        - PR info if PR number is specified

    Raises:
        ValidationError: If the reference string format is invalid
        httpx.HTTPStatusError: If GitHub API calls fail

    Examples:
        >>> ref = parse_github_reference("zenodo/zenodo-rdm")
        >>> ref = parse_github_reference("inveniosoftware/invenio-rdm-records@maint-22.x")
        >>> ref = parse_github_reference("inveniosoftware/invenio-app#123")
    """
    # Parse the reference string using the schema field
    field = GitReferenceField()
    parsed_ref = cast(GitReference, field.deserialize(reference, None, None))

    # Resolve git reference details (commit SHA, PR info, etc.)
    parsed_ref = git_api.resolve_git(parsed_ref)

    return parsed_ref


__all__ = ["JSON", "parse_github_reference"]
