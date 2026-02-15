"""Configuration schema definitions and management.

This module defines the complete configuration schema for invenio-testrig,
including repository settings, GitHub organization patterns, patch configurations,
and execution status tracking. It also provides functions for loading and saving
configuration files.
"""

import json
from dataclasses import field
from pathlib import Path
from typing import Literal, Self, cast

import marshmallow as ma
from marshmallow_dataclass import class_schema

from .github.types import GitReference
from .types import ExecutionStatus, TestedPackageInfo
from .utils import extensible_dataclass


@extensible_dataclass
class Repository:
    """Repository configuration.

    People might add information here for their hooks, so we keep
    it extensible via extensible_dataclass.
    """

    git: GitReference
    e2e: GitReference | None


@extensible_dataclass
class Github:
    """GitHub organization configuration.

    People might add information here for their hooks, so we keep
    it extensible via extensible_dataclass."""

    org: str
    """Organization name on GitHub to match against when resolving repositories."""

    test: list[str]
    """The test command to run to tested packages that match include directive."""

    include: list[str] | None = field(default_factory=list)  # type: ignore[assignment]
    """List of package names to include in the testing process. If empty, all packages are included."""

    exclude: list[str] | None = field(default_factory=list)  # type: ignore[assignment]
    """List of package names to exclude from the testing process. If empty, no packages are excluded."""

    extras: list[str] | None = field(default_factory=list)  # type: ignore[assignment]
    """List of extras to install for tested packages that match include directive."""

    freeze: list[str] | None = field(default_factory=list)  # type: ignore[assignment]
    """List of version constraints to apply when resolving dependencies for tested packages that match include directive.
    
    If specified, these packages will be reinstalled with the specified version constraints before running the tests. 
    """

    def __post_init__(self):
        """Normalize package lists to lowercase for case-insensitive matching."""
        # Ensure that the include, exclude, and freeze lists are lowercase for case-insensitive matching
        self.include = [pkg.lower() for pkg in self.include or []]
        self.exclude = [pkg.lower() for pkg in self.exclude or []]
        self.freeze = [pkg.lower() for pkg in self.freeze or []]
        self.test = [cmd for cmd in self.test]
        self.extras = [extra for extra in self.extras or []]


@extensible_dataclass
class Config:
    """Main configuration structure for invenio-testrig.

    Again, we keep this extensible to allow users to add custom fields for their hooks.
    """

    github: list[Github]
    repository: Repository
    name: str | None = None
    """Optional name for this test configuration run."""
    started_at: str | None = None
    """ISO datetime when the configuration was initialized."""
    patches: list[GitReference] = field(default_factory=list)  # type: ignore[assignment]
    mode: Literal[
        "upstream-overwrite", "upstream-rebase", "pinned-overwrite", "pinned-rebase"
    ] = "upstream-overwrite"
    test_timeout: int = 90  # 90 minutes

    # runtime information
    packages: dict[str, str] = field(  # type: ignore[assignment]
        default_factory=dict
    )  # package name to version mapping for dependencies
    tested_packages: dict[str, TestedPackageInfo] = field(  # type: ignore[assignment]
        default_factory=dict
    )  # package name to tested package info mapping

    # Execution options
    python_version: str = "python3"
    """Python version to use for testing."""

    uv_executable: str = "uv"
    """Path to uv executable."""

    disable_codestyle_checks: bool = False
    """Whether to disable codestyle checks (--black, --isort, --pydocstyle) in test configuration."""

    debug: bool = False
    """Whether to enable debug mode with full traceback on errors."""

    verbose: bool = False
    """Whether to enable verbose output with additional logging information."""

    @property
    def workdir(self) -> Path:
        """Get the working directory path."""
        # workdir is always the parent directory of the config file
        config_path = self.config_path
        if config_path is None:
            raise ValueError("Config path is not set. Cannot determine workdir.")
        return config_path.parent.resolve()

    def workdir_path(self, subdir: str | None = None) -> Path:
        """Get the Path object for the working directory or a subdirectory within it."""
        if subdir:
            return self.workdir / subdir
        return self.workdir

    @property
    def config_path(self) -> Path | None:
        """Path to the config JSON file, if loaded from a file."""
        return getattr(self, "_config_path", None)

    @config_path.setter
    def config_path(self, value: Path) -> None:
        """Set the path to the config JSON file."""
        self._config_path = value

    @classmethod
    def load(cls: type[Self], file: str | Path) -> Self:
        """Load configuration from a JSON file."""
        path = Path(file)

        with open(path, "r") as stream:
            raw_data = json.load(stream)
            schema = ConfigSchema()

            if isinstance(raw_data, dict):
                ret = cast(Self, schema.load(raw_data, unknown=ma.INCLUDE))  # type: ignore[return-value]
                ret.config_path = path
                return ret
            else:
                raise ValueError(
                    f"Expected config file to contain a JSON object, got {type(raw_data)}"
                )

    def save(self, file: str | Path | None = None) -> None:
        """Save configuration to a JSON file."""
        if file:
            self.config_path = Path(file)
        elif not self.config_path:
            raise ValueError("No file path specified for saving configuration.")
        formatted_config = json.dumps(
            ConfigSchema().dump(self), indent=2, sort_keys=True
        )
        self.config_path.write_text(formatted_config)


ConfigSchema = class_schema(Config)


def load_config(file: str | Path) -> Config:
    """Load configuration data from JSON and optionally validate it."""
    return Config.load(file)


def save_config(file: str | Path, config: Config) -> None:
    """Save configuration dictionary to JSON file with consistent formatting."""
    config.save(file)


ExecutionStatusSchema = class_schema(ExecutionStatus)


def load_execution_status(file: str | Path) -> ExecutionStatus:
    """Load execution status from JSON file."""
    path = Path(file)
    with open(path, "r") as stream:
        raw_data = json.load(stream)
        schema = ExecutionStatusSchema()
        if isinstance(raw_data, dict):
            return cast(ExecutionStatus, schema.load(raw_data))  # type: ignore[return-value]
        else:
            raise ValueError(
                f"Expected execution status file to contain a JSON object, got {type(raw_data)}"
            )


def save_execution_status(file: str | Path, status: ExecutionStatus) -> None:
    """Save execution status to JSON file."""
    path = Path(file)
    formatted_status = json.dumps(
        ExecutionStatusSchema().dump(status), indent=2, sort_keys=True
    )
    path.write_text(formatted_status)
