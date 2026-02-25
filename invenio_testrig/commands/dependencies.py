"""Dependency collection and filtering command implementations."""

import re
import tempfile
from pathlib import Path

from invenio_testrig.config import (
    Config,
    Github,
)
from invenio_testrig.github import (
    GitApi,
    GitCache,
    GitReference,
)
from invenio_testrig.hooks import run_hook
from invenio_testrig.python_api import PythonAPI
from invenio_testrig.types import Progress, TestedPackageInfo


def collect_dependencies(
    config: Config,
    uv_executable: str,
    python_version: str,
    ignore_uv_lock: bool,
    progress: Progress,
) -> None:
    """Collect dependencies/libraries for the repository.

    Clones the repository, installs it (if uv.lock is not found),
    and collects dependencies. Updates the config JSON with a "packages" key
    containing all detected dependencies and their versions.

    Args:
        config: Config object
        uv_executable: Path to uv executable
        python_version: Python version to use
        progress: Progress reporter for status updates
    """
    # Read the config JSON

    git_ref = config.repository.git
    git_api = GitApi(GitCache(config.workdir_path("git_cache")))

    # Clone the repository to a temporary directory
    with tempfile.TemporaryDirectory() as tmpdir:
        repo_path = Path(tmpdir) / "repo"
        progress.start("Cloning invenio repository...", icon="🔄")
        git_api.clone_git_reference(git_ref, repo_path)

        run_hook(
            config,
            "after_invenio_repo_clone",
            repository_path=repo_path,
        )
        # Install and get dependencies
        progress.start(
            "Collecting dependencies (might take a while as the repository might be installed)...",
            icon="📦",
        )
        python_api = PythonAPI(uv_executable, python_version)
        dependencies = python_api.get_dependencies(
            repo_path, ignore_uv_lock=ignore_uv_lock
        )

    # Add dependencies to the config
    config.packages = dependencies

    run_hook(
        config,
        "after_dependencies_collected",
    )

    progress.success(
        f"Collected {len(dependencies)} dependencies and updated {config.config_path}"
    )


def filter_packages(
    config: Config,
    progress: Progress,
) -> None:
    """Filter dependencies based on GitHub include/exclude patterns.

    Reads packages and filters entries based on github.include and
    github.exclude patterns inside the config file. Creates a new
    "tested_packages" key with matching entries. For each matched package,
    get the branch name and potential commit.

    The version might be:
    - semver version (e.g. 1.2.3). The branch name is v<version> (e.g. v1.2.3)
    - full github url (e.g.https://github.com/inveniosoftware/invenio-swh?rev=v0.13.4#<hash>
      or https://github.com/inveniosoftware/invenio-records-resources?branch=fix-read-many#<hash>)

    Args:
        config: Config object
        progress: Progress reporter for status updates

    Raises:
        ValueError: If no packages exist in config
    """
    # Read the config JSON
    git_cache = GitCache(config.workdir_path("git_cache"))
    git_api = GitApi(git_cache)

    run_hook(
        config,
        "before_filtering_packages",
    )

    # Check if packages exists
    if not config.packages:
        raise ValueError("No packages in config")

    packages_map = config.packages

    # Filter dependencies based on github patterns
    tested_packages: dict[str, TestedPackageInfo] = {}

    github_entries: dict[str, Github] = {}

    for package_name, version in packages_map.items():
        # Check each github config entry
        github_entry = find_git_repository_config(config, package_name)
        if github_entry:
            github_entries[package_name] = github_entry

    git_cache.cache_repositories(
        [
            (
                github_entry.org,
                package_name,
            )
            for package_name, github_entry in github_entries.items()
        ],
        progress,
    )

    for package_name, version in packages_map.items():
        # Check each github config entry
        if package_name not in github_entries:
            continue
        github_entry = github_entries[package_name]
        progress.info(
            f"Adding package {package_name} to a set of tested packages ...", icon="🔍"
        )

        if version.startswith("https://"):
            # If the version is a full github url, parse it to get the branch and potential commit
            reference = git_api.parse_reference(version)
        else:
            reference = GitReference(
                org=github_entry.org or "",
                repo=package_name,
                package=package_name,
                branch=f"v{version}",
            )
        reference = git_api.resolve_reference(reference)
        progress.info(
            f" ... resolved reference: {str(reference)}, commit {reference.commit}"
        )

        # Package matches this github config
        tested_packages[package_name] = TestedPackageInfo(
            reference=reference,
            test=github_entry.test,
            extras=github_entry.extras or [],
            freeze=github_entry.freeze or [],
        )

    # Add tested packages to the config
    config.tested_packages = tested_packages

    run_hook(
        config,
        "after_filtering_packages",
    )

    progress.success(
        f"Filtered {len(tested_packages)} packages from {len(packages_map)} "
        f"total dependencies and updated {config.config_path}"
    )


def find_git_repository_config(config: Config, package_name: str) -> Github | None:
    """Find the matching GitHub configuration entry for a package.

    Args:
        config: Configuration object
        package_name: Name of the package to find configuration for

    Returns:
        Matching Github configuration entry or None if no match found
    """
    for github_entry in config.github or []:
        exclude_patterns = github_entry.exclude or []

        # Check if package matches any include pattern
        for pattern in github_entry.include or []:
            if re.match(pattern, package_name, re.IGNORECASE):
                break
        else:
            return None

        # Check if package matches any exclude pattern
        if any(
            re.match(pattern, package_name, re.IGNORECASE)
            for pattern in exclude_patterns
        ):
            continue
        return github_entry
    return None
