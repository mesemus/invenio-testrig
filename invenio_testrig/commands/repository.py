"""Repository cloning and patch selection command implementations."""

from pathlib import Path

from invenio_testrig.config import Config
from invenio_testrig.github import GitApi, GitCache
from invenio_testrig.hooks import run_hook
from invenio_testrig.patchers import patchers_by_mode
from invenio_testrig.types import Progress


def select_patches(
    config: Config,
    progress: Progress,
) -> None:
    """Select patches for the filtered out packages.

    Reads tested_packages and for each package, checks if there are any patches
    that match the package name. If there are, adds them to the config under a new
    "patches" key for each package. This will be used in the cloning step to determine
    which packages need to be cloned with patches applied.

    Args:
        config: Config object
        progress: Progress reporter for status updates
    """
    # Read the config JSON
    run_hook(
        config,
        "before_selecting_patches",
    )

    # Check if patches exists
    if not config.patches:
        progress.warning("No patches in config, will skip patch selection")
        return

    applied_patches_count = 0
    applied_packages_count = 0
    for tested_package_name, tested_package_info in (
        config.tested_packages or {}
    ).items():
        matching_patches = [
            patch for patch in config.patches if patch.package == tested_package_name
        ]

        run_hook(
            config,
            "selecting_package_patch",
            package_name=tested_package_name,
            package_info=tested_package_info,
            matching_patches=matching_patches,
        )
        tested_package_info.patches = matching_patches
        if matching_patches:
            applied_packages_count += 1
            applied_patches_count += len(matching_patches)
            progress.info(
                f"Selected {', '.join(str(patch) for patch in matching_patches)} for package {tested_package_name}",
                icon="📌",
            )

    run_hook(
        config,
        "after_selecting_patches",
    )

    # Write back to the JSON file
    config.save()

    progress.success(
        f"Selected {applied_patches_count} patches to apply to {applied_packages_count} packages"
    )


def clone_repositories(
    config: Config,
    clone_path: Path,
    progress: Progress,
) -> None:
    """Clone packages from configuration.

    Clone repository.git and repository.e2e (if configured) to the output directory.
    Then clone all packages specified in "tested_packages" into the packages/ subdirectory.
    If a package has patches, also clone it into the patched/ subdirectory and apply patches.
    The patching behavior depends on the patch_mode specified in the config (as-is, upstream, or custom).

    Layout of the output directory:
        clone_path/
        ├── repo/                # Cloned repository.git
        ├── invenio-e2e/         # Cloned repository.e2e (if configured)
        ├── packages/            # Cloned dependencies without patches
        |     └── package_name/     # Cloned dependency repository with pinned version
        └── patched/             # Cloned dependencies with patches applied
              └── package_name/     # Cloned dependency repository with patches applied

    Args:
        config: Config object
        clone_path: Path where repositories will be cloned
        progress: Progress reporter for status updates

    Raises:
        ValueError: If the clone_path already exists or if the patch_mode is unsupported
    """
    # Check if output directory exists
    if clone_path.exists():
        raise ValueError(f"Output directory {clone_path} already exists")

    git_api = GitApi(GitCache(config.workdir_path("git_cache")))

    # Read the config JSON
    run_hook(
        config,
        "before_cloning_packages",
        clone_path=clone_path,
    )

    # Create output directory
    clone_path.mkdir(parents=True, exist_ok=False)

    # Clone repository.git
    repo_git = config.repository.git
    repo_dir = clone_path / "repo"
    progress.start(f"Cloning {repo_git.org}/{repo_git.repo} to {repo_dir}", icon="🔄")
    git_api.clone_git_reference(repo_git, repo_dir)

    run_hook(
        config,
        "after_cloning_repository",
        repository_path=repo_dir,
        clone_path=clone_path,
    )

    # Clone repository.e2e if it exists
    if config.repository.e2e:
        e2e_ref = config.repository.e2e
        e2e_dir = clone_path / "invenio-e2e"
        progress.start(f"Cloning {e2e_ref.org}/{e2e_ref.repo} to {e2e_dir}", icon="🔄")
        git_api.clone_git_reference(e2e_ref, e2e_dir)

        run_hook(
            config,
            "after_cloning_e2e_repository",
            e2e_repository_path=e2e_dir,
            clone_path=clone_path,
        )

    # Clone dependencies using appropriate patcher mode
    tested_packages = config.tested_packages or {}
    mode = config.patch_mode
    patcher_cls = patchers_by_mode.get(mode)

    if patcher_cls is None:
        raise ValueError(f"Unsupported patch_mode '{mode}'")

    if tested_packages:
        packages_dir = clone_path / "packages"
        packages_dir.mkdir(parents=True, exist_ok=True)
        patched_packages_dir = clone_path / "patched"
        patched_packages_dir.mkdir(parents=True, exist_ok=True)

        patcher = patcher_cls(config, packages_dir, patched_packages_dir, progress)

        for tested_package_name in tested_packages.keys():
            progress.info(
                f"Cloning dependency {tested_package_name} using '{mode}' mode",
                icon="📦",
            )
            patcher.clone(tested_package_name)
            run_hook(
                config,
                "after_cloning_dependency",
                clone_path=clone_path,
                package_name=tested_package_name,
                package_clone_path=packages_dir / tested_package_name,
                patched_package_clone_path=patched_packages_dir / tested_package_name,
            )

    run_hook(
        config,
        "after_cloning_packages",
        clone_path=clone_path,
    )

    progress.success(f"Successfully cloned repositories to {clone_path}")
