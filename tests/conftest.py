"""Shared pytest fixtures for all tests."""

from pathlib import Path

import pytest
from dotenv import load_dotenv

from invenio_testrig.github.api import GitApi, git_api
from invenio_testrig.github.types import GitReference

# Load environment variables from .env file at the project root
env_path = Path(__file__).parent.parent / ".env"
if env_path.exists():
    load_dotenv(env_path)


@pytest.fixture
def git_api_no_token() -> GitApi:
    """Create GitApi instance without token."""
    return GitApi(token=None)


@pytest.fixture
def git_api_with_token() -> GitApi:
    """Create GitApi instance with token."""
    return GitApi(token="test_token_123")


@pytest.fixture
def empty_git_reference() -> GitReference:
    """Empty git reference structure with all fields set to None/empty."""
    return {
        "org": "",
        "repo": "",
        "package": "",
        "branch": None,
        "pr": None,
        "base": None,
        "versions": [],
        "pr_info": None,
        "commit": None,
    }


@pytest.fixture
def existing_branch_git_reference() -> str:
    """Get the latest branch from inveniosoftware/invenio-rdm-records."""
    branches = git_api.get_branches("inveniosoftware", "invenio-rdm-records", limit=1)
    return f"inveniosoftware/invenio-rdm-records@{branches[0]}"


@pytest.fixture
def existing_pr_git_reference() -> str:
    """Get the latest open PR from inveniosoftware/invenio-rdm-records."""
    prs = git_api.get_open_prs("inveniosoftware", "invenio-rdm-records", limit=1)
    return f"inveniosoftware/invenio-rdm-records#{prs[0]}"
