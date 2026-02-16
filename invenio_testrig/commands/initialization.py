"""Initialization command implementation."""

from datetime import UTC, datetime
from pathlib import Path
from typing import cast

import marshmallow as ma
import yaml

from invenio_testrig.config import Config, ConfigSchema
from invenio_testrig.github import GitApi, GitCache, GitReferenceSchema
from invenio_testrig.hooks import run_hook
from invenio_testrig.types import Progress


def initialize_config(
    config_yaml_path_or_url: str,
    workdir: Path,
    progress: Progress,
) -> Config:
    """Initialize workflow by preparing configuration.

    Resolves all git references in the YAML configuration and outputs JSON.

    Args:
        config_yaml_path: Path to the input YAML configuration file
        workdir: Path to the working directory
        progress: Progress reporter for status updates
        python_version: Python version to use for testing
        uv_executable: Path to uv executable
        disable_codestyle_checks: Whether to disable codestyle checks
    """
    # Read the yaml config file
    schema = GitReferenceSchema()
    git_api = GitApi(GitCache(workdir / "git_cache"))
    if config_yaml_path_or_url.startswith(
        "http://"
    ) or config_yaml_path_or_url.startswith("https://"):
        # If it's a URL, fetch the content
        import httpx

        response = httpx.get(config_yaml_path_or_url)
        response.raise_for_status()
        config_data = yaml.safe_load(response.text)
    else:
        with open(config_yaml_path_or_url, "r") as f:
            config_data = yaml.safe_load(f)

    # resolve all references before loading
    config_data["patches"] = [
        schema.dump(git_api.parse_reference(x))
        for x in (config_data.get("patches") or [])
    ]
    repository = config_data.get("repository", {})
    if "git" in repository and repository["git"]:
        repository["git"] = schema.dump(git_api.parse_reference(repository["git"]))
    if "e2e" in repository and repository["e2e"]:
        repository["e2e"] = schema.dump(git_api.parse_reference(repository["e2e"]))
    config_data["hooks"] = config_data.get("hooks", {}) or {}

    config = cast(Config, ConfigSchema().load(config_data, unknown=ma.INCLUDE))

    config.started_at = datetime.now(UTC).isoformat()

    # Run after-config-preprocessing hook if it exists
    run_hook(
        config,
        "after_config_preprocessing",
    )
    progress.success("Configuration prepared")

    return config
