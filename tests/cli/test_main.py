"""Tests for CLI main module commands."""

import json
import tempfile
from pathlib import Path

from click.testing import CliRunner

from invenio_testrig.cli.main import cli
from tests.cli.conftest import requires_github_token, slow_integration_test


def test_cli_group():
    """Test main CLI group is accessible."""
    runner = CliRunner()
    result = runner.invoke(cli, ["--help"])
    assert result.exit_code == 0
    assert "Invenio TestRig" in result.output
    assert "repo" in result.output
    assert "package" in result.output
    assert "config" in result.output


def test_repo_group():
    """Test repo subcommand group is accessible."""
    runner = CliRunner()
    result = runner.invoke(cli, ["repo", "--help"])
    assert result.exit_code == 0
    assert "Repository" in result.output


def test_package_group():
    """Test package subcommand group is accessible."""
    runner = CliRunner()
    result = runner.invoke(cli, ["package", "--help"])
    assert result.exit_code == 0
    assert "Package" in result.output


def test_config_group():
    """Test config subcommand group is accessible."""
    runner = CliRunner()
    result = runner.invoke(cli, ["config", "--help"])
    assert result.exit_code == 0
    assert "Configuration" in result.output


# Repository Command Tests


@requires_github_token
def test_repo_commit():
    """Test repo commit command."""
    runner = CliRunner()
    result = runner.invoke(
        cli, ["repo", "commit", "inveniosoftware", "invenio-app", "master"]
    )
    assert result.exit_code == 0
    # Should return a commit SHA (40 characters hex)
    output = result.output.strip()
    assert len(output) == 40
    assert all(c in "0123456789abcdef" for c in output)


@requires_github_token
def test_repo_commit_invalid_branch():
    """Test repo commit command with invalid branch."""
    runner = CliRunner()
    result = runner.invoke(
        cli,
        [
            "repo",
            "commit",
            "inveniosoftware",
            "invenio-app",
            "nonexistent-branch-xyz",
        ],
    )
    assert result.exit_code == 1
    assert "Error" in result.output


@requires_github_token
def test_repo_pr():
    """Test repo pr command."""
    runner = CliRunner()
    # Using a known closed PR from invenio-app
    result = runner.invoke(cli, ["repo", "pr", "inveniosoftware", "invenio-app", "1"])
    assert result.exit_code == 0
    # Should return JSON with PR info
    output = json.loads(result.output)
    assert "org" in output
    assert "repo" in output
    assert "pr" in output
    assert output["org"] == "inveniosoftware"
    assert output["repo"] == "invenio-app"
    assert output["pr"] == 1


@requires_github_token
def test_repo_pr_invalid():
    """Test repo pr command with invalid PR number."""
    runner = CliRunner()
    result = runner.invoke(
        cli, ["repo", "pr", "inveniosoftware", "invenio-app", "999999"]
    )
    assert result.exit_code == 1
    assert "Error" in result.output


@requires_github_token
def test_repo_branch():
    """Test repo branch command."""
    runner = CliRunner()
    result = runner.invoke(cli, ["repo", "branch", "inveniosoftware", "invenio-app"])
    assert result.exit_code == 0
    output = result.output.strip()
    # Should return a branch name (typically 'main' or 'master')
    assert output in ["main", "master"]


@requires_github_token
def test_repo_branch_invalid_repo():
    """Test repo branch command with invalid repository."""
    runner = CliRunner()
    result = runner.invoke(
        cli, ["repo", "branch", "inveniosoftware", "nonexistent-repo-xyz"]
    )
    assert result.exit_code == 1
    assert "Error" in result.output


@requires_github_token
def test_repo_info_with_branch(existing_branch_git_reference):
    """Test repo info command with branch reference."""
    runner = CliRunner()
    result = runner.invoke(cli, ["repo", "info", existing_branch_git_reference])
    assert result.exit_code == 0
    # Should return JSON with resolved git reference
    output = json.loads(result.output)
    assert output["org"] == "inveniosoftware"
    assert output["repo"] == "invenio-rdm-records"
    assert "branch" in output
    assert output["branch"] is not None
    assert "commit" in output
    assert output["commit"] is not None


@requires_github_token
def test_repo_info_with_pr(existing_pr_git_reference):
    """Test repo info command with PR reference."""
    runner = CliRunner()
    result = runner.invoke(cli, ["repo", "info", existing_pr_git_reference])
    assert result.exit_code == 0
    # Should return JSON with resolved PR reference
    output = json.loads(result.output)
    assert output["org"] == "inveniosoftware"
    assert output["repo"] == "invenio-rdm-records"
    assert "pr" in output
    assert output["pr"] is not None
    assert "pr_info" in output


@requires_github_token
def test_repo_info_repo_only():
    """Test repo info command with repository only."""
    runner = CliRunner()
    result = runner.invoke(cli, ["repo", "info", "inveniosoftware/invenio-app"])
    assert result.exit_code == 0
    # Should return JSON with resolved reference (defaults to default branch)
    output = json.loads(result.output)
    assert output["org"] == "inveniosoftware"
    assert output["repo"] == "invenio-app"
    assert output["branch"] in ["main", "master"]
    assert "commit" in output


@requires_github_token
def test_repo_tags():
    """Test repo tags command."""
    runner = CliRunner()
    result = runner.invoke(cli, ["repo", "tags", "inveniosoftware/invenio-app", "5"])
    assert result.exit_code == 0
    # Should return up to 5 tags, one per line
    tags = result.output.strip().split("\n")
    assert len(tags) <= 5
    assert all(tag for tag in tags)  # No empty tags


@requires_github_token
def test_repo_tags_with_filter():
    """Test repo tags command with filter."""
    runner = CliRunner()
    result = runner.invoke(
        cli, ["repo", "tags", "inveniosoftware/invenio-app", "5", "--filter", "v"]
    )
    assert result.exit_code == 0
    # Should return up to 5 tags starting with 'v'
    tags = result.output.strip().split("\n")
    assert len(tags) <= 5
    # Check that all tags start with 'v'
    if tags and tags[0]:  # Only check if there are tags
        assert all(tag.startswith("v") for tag in tags if tag)


@requires_github_token
def test_repo_tags_with_branch(existing_branch_git_reference):
    """Test repo tags command with branch specified."""
    runner = CliRunner()
    result = runner.invoke(cli, ["repo", "tags", existing_branch_git_reference, "3"])
    assert result.exit_code == 0
    # Should work with branch specified
    output = result.output.strip()
    # May or may not have tags, so just check it doesn't error
    assert result.exit_code == 0


@slow_integration_test
def test_package_clone(existing_branch_git_reference):
    """Test package clone command (slow integration test)."""
    runner = CliRunner()
    with tempfile.TemporaryDirectory() as tmpdir:
        output_dir = Path(tmpdir) / "cloned-repo"
        result = runner.invoke(
            cli, ["package", "clone", existing_branch_git_reference, str(output_dir)]
        )
        assert result.exit_code == 0
        assert "Successfully cloned" in result.output
        # Verify the directory was created and contains a git repo
        assert output_dir.exists()
        assert (output_dir / ".git").exists()


@requires_github_token
def test_repo_release():
    """Test repo release command."""
    runner = CliRunner()
    result = runner.invoke(cli, ["repo", "release", "inveniosoftware/invenio-app"])
    assert result.exit_code == 0
    # Should return a version string
    version = result.output.strip()
    assert version
    # Version should have a format like v1.2.3 or 1.2.3
    assert any(c.isdigit() for c in version)


# Package Command Tests


@slow_integration_test
def test_package_install():
    """Test package install command (slow integration test)."""
    runner = CliRunner()
    with tempfile.TemporaryDirectory() as tmpdir:
        # First clone a repository
        package_dir = Path(tmpdir) / "invenio-app"
        clone_result = runner.invoke(
            cli,
            [
                "package",
                "clone",
                "inveniosoftware/invenio-app@master",
                str(package_dir),
            ],
        )
        assert clone_result.exit_code == 0

        # Now install it
        result = runner.invoke(cli, ["package", "install", str(package_dir)])
        assert result.exit_code == 0
        assert "Successfully installed" in result.output
        # Verify .venv was created
        assert (package_dir / ".venv").exists()


@slow_integration_test
def test_package_install_custom_uv():
    """Test package install command with custom uv path."""
    runner = CliRunner()
    with tempfile.TemporaryDirectory() as tmpdir:
        # First clone a repository
        package_dir = Path(tmpdir) / "invenio-app"
        clone_result = runner.invoke(
            cli,
            [
                "package",
                "clone",
                "inveniosoftware/invenio-app@master",
                str(package_dir),
            ],
        )
        assert clone_result.exit_code == 0

        # Now install it with custom uv path
        result = runner.invoke(
            cli, ["package", "install", str(package_dir), "--uv", "uv"]
        )
        assert result.exit_code == 0
        assert "Successfully installed" in result.output


def test_package_install_nonexistent():
    """Test package install command with nonexistent directory."""
    runner = CliRunner()
    result = runner.invoke(cli, ["package", "install", "/nonexistent/path"])
    assert result.exit_code == 2  # Click exits with 2 for usage errors
    assert "does not exist" in result.output.lower()


@slow_integration_test
def test_package_deps_json():
    """Test package deps command with JSON output."""
    runner = CliRunner()
    with tempfile.TemporaryDirectory() as tmpdir:
        # First clone and install a repository
        package_dir = Path(tmpdir) / "invenio-app"
        clone_result = runner.invoke(
            cli,
            [
                "package",
                "clone",
                "inveniosoftware/invenio-app@master",
                str(package_dir),
            ],
        )
        assert clone_result.exit_code == 0

        install_result = runner.invoke(cli, ["package", "install", str(package_dir)])
        assert install_result.exit_code == 0

        # Get dependencies
        result = runner.invoke(
            cli, ["package", "deps", str(package_dir), "--format", "json"]
        )
        assert result.exit_code == 0
        # Should return valid JSON
        dependencies = json.loads(result.output)
        assert isinstance(dependencies, dict)
        # Should have some dependencies
        assert len(dependencies) > 0


@slow_integration_test
def test_package_deps_text():
    """Test package deps command with text output."""
    runner = CliRunner()
    with tempfile.TemporaryDirectory() as tmpdir:
        # First clone and install a repository
        package_dir = Path(tmpdir) / "invenio-app"
        clone_result = runner.invoke(
            cli,
            [
                "package",
                "clone",
                "inveniosoftware/invenio-app@master",
                str(package_dir),
            ],
        )
        assert clone_result.exit_code == 0

        install_result = runner.invoke(cli, ["package", "install", str(package_dir)])
        assert install_result.exit_code == 0

        # Get dependencies in text format
        result = runner.invoke(
            cli, ["package", "deps", str(package_dir), "--format", "text"]
        )
        assert result.exit_code == 0
        # Should have lines in format "package==version"
        lines = result.output.strip().split("\n")
        assert len(lines) > 0
        # Check format of at least one line
        assert any("==" in line for line in lines)


def test_package_deps_nonexistent():
    """Test package deps command with nonexistent directory."""
    runner = CliRunner()
    result = runner.invoke(cli, ["package", "deps", "/nonexistent/path"])
    assert result.exit_code == 2  # Click exits with 2 for usage errors
    assert "does not exist" in result.output.lower()
