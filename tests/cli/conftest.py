"""Shared pytest fixtures for CLI tests."""

import os
import tempfile
from pathlib import Path

import pytest


@pytest.fixture
def temp_dir():
    """Create a temporary directory for tests."""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield Path(tmpdir)


@pytest.fixture
def sample_config_yaml(
    temp_dir, existing_branch_git_reference, existing_pr_git_reference
):
    """Create a sample YAML config file for testing."""
    config_content = f"""
repository:
  git: {existing_branch_git_reference}
  e2e: zenodo/zenodo-rdm@master

patches:
  - {existing_pr_git_reference}
  - inveniosoftware/invenio-records@v1.0.0

github:
  - org: inveniosoftware
    include:
      - invenio-.*
"""
    config_file = temp_dir / "config.yaml"
    config_file.write_text(config_content)
    return config_file


@pytest.fixture
def minimal_config_yaml(temp_dir, existing_branch_git_reference):
    """Create a minimal YAML config file for testing."""
    config_content = f"""
repository:
  git: {existing_branch_git_reference}

github:
  - org: inveniosoftware
    include:
      - invenio-.*
"""
    config_file = temp_dir / "config.yaml"
    config_file.write_text(config_content)
    return config_file


# Skip marker for tests requiring GitHub API access
requires_github_token = pytest.mark.skipif(
    not os.environ.get("GITHUB_TOKEN"),
    reason="Requires GITHUB_TOKEN environment variable",
)

# Skip marker for slow integration tests
slow_integration_test = pytest.mark.skipif(
    not os.environ.get("RUN_INTEGRATION_TESTS"),
    reason="Requires RUN_INTEGRATION_TESTS environment variable (slow test)",
)
