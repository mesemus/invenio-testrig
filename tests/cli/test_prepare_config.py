"""Tests for CLI config commands."""

import json

from click.testing import CliRunner

from invenio_testrig.cli.main import cli
from tests.cli.conftest import requires_github_token


@requires_github_token
def test_config_prepare_minimal(minimal_config_yaml):
    """Test config prepare command with minimal configuration."""
    runner = CliRunner()
    result = runner.invoke(cli, ["config", "prepare", str(minimal_config_yaml)])
    assert result.exit_code == 0

    # Parse the output as JSON
    config = json.loads(result.output)

    # Verify structure
    assert "repository" in config
    assert "git" in config["repository"]

    # Verify git reference was resolved
    git_ref = config["repository"]["git"]
    assert git_ref["org"] == "inveniosoftware"
    assert git_ref["repo"] == "invenio-rdm-records"
    assert git_ref["package"] == "invenio-rdm-records"
    assert "branch" in git_ref
    assert git_ref["branch"] is not None
    assert "commit" in git_ref
    assert git_ref["commit"] is not None
