import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Literal, cast

import marshmallow as ma
from marshmallow_dataclass import class_schema

from .github.types import GitReference
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
        # Ensure that the include, exclude, and freeze lists are lowercase for case-insensitive matching
        self.include = [pkg.lower() for pkg in self.include or []]
        self.exclude = [pkg.lower() for pkg in self.exclude or []]
        self.freeze = [pkg.lower() for pkg in self.freeze or []]
        self.test = [cmd for cmd in self.test]
        self.extras = [extra for extra in self.extras or []]


@dataclass
class TestedPackageInfo:
    """Information about a package that is being tested, derived from the github configuration.

    This one is generated automatically based on the github configuration
    and the dependencies, so it is not extensible.
    """

    reference: GitReference
    test: list[str]
    extras: list[str]
    freeze: list[str]
    patches: list[GitReference] = field(default_factory=list)  # type: ignore[assignment]


@dataclass
class Hooks:
    """
    Hooks configuration. A hook is a python function that is called at a specific point
    during the process. It is written as a string as package.module:function.
    Each hook takes config as the first parameter and can optionally take additional
    parameters depending on the hook type.
    """

    after_config_preprocessing: str | None = None
    after_invenio_repo_clone: str | None = None
    after_dependencies_collected: str | None = None
    before_filtering_packages: str | None = None
    after_filtering_packages: str | None = None
    before_selecting_patches: str | None = None
    after_selecting_patches: str | None = None
    before_cloning_packages: str | None = None
    after_cloning_repository: str | None = None
    after_cloning_e2e_repository: str | None = None
    after_cloning_dependency: str | None = None
    after_cloning_packages: str | None = None


@extensible_dataclass
class Config:
    """Main configuration structure for invenio-testrig.

    Again, we keep this extensible to allow users to add custom fields for their hooks.
    """

    github: list[Github]
    repository: Repository
    patches: list[GitReference] = field(default_factory=list)  # type: ignore[assignment]
    mode: Literal[
        "upstream-overwrite", "upstream-rebase", "pinned-overwrite", "pinned-rebase"
    ] = "upstream-overwrite"
    test_timeout: int = 90  # 90 minutes
    hooks: Hooks = field(default_factory=Hooks)
    packages: dict[str, str] = field(  # type: ignore[assignment]
        default_factory=dict
    )  # package name to version mapping for dependencies
    tested_packages: dict[str, TestedPackageInfo] = field(  # type: ignore[assignment]
        default_factory=dict
    )  # package name to tested package info mapping


ConfigSchema = class_schema(Config)


def load_config(file: str | Path) -> Config:
    """Load configuration data from JSON and optionally validate it."""

    path = Path(file)

    with open(path, "r") as stream:
        raw_data = json.load(stream)
        schema = ConfigSchema()

        if isinstance(raw_data, dict):
            return cast(Config, schema.load(raw_data, unknown=ma.INCLUDE))  # type: ignore[return-value]
        else:
            raise ValueError(
                f"Expected config file to contain a JSON object, got {type(raw_data)}"
            )


def save_config(file: str | Path, config: Config) -> None:
    """Save configuration dictionary to JSON file with consistent formatting."""
    path = Path(file)
    formatted_config = json.dumps(ConfigSchema().dump(config), indent=2, sort_keys=True)
    path.write_text(formatted_config)
