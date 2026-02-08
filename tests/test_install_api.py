"""Tests for python_api module."""

import os
import tempfile
from pathlib import Path

import pytest

from invenio_testrig import parse_github_reference
from invenio_testrig.git_api import git_api
from invenio_testrig.python_api import PythonAPI

# Skip marker for slow integration tests that install real packages
slow_integration_test = pytest.mark.skipif(
    not os.environ.get("RUN_INTEGRATION_TESTS"),
    reason="Requires RUN_INTEGRATION_TESTS environment variable (slow test)",
)


@pytest.fixture
def python_api() -> PythonAPI:
    """Create PythonAPI instance."""
    return PythonAPI()


def test_install_directory_invenio_rdm_records(python_api: PythonAPI) -> None:
    """Test installing invenio-rdm-records package from maint-22.x branch."""
    # Create a temporary directory for cloning and installation
    with tempfile.TemporaryDirectory() as tmpdir:
        output_dir = Path(tmpdir) / "invenio-rdm-records"

        # Parse and clone inveniosoftware/invenio-rdm-records with maint-22.x branch
        reference = parse_github_reference(
            "inveniosoftware/invenio-rdm-records@maint-22.x"
        )
        git_api.clone_git_reference(reference, output_dir)

        # Install the package
        python_api.install_project(output_dir)

        # Verify .venv was created
        venv_path = output_dir / ".venv"
        assert venv_path.exists()
        assert venv_path.is_dir()

        # Verify basic venv structure
        assert (venv_path / "pyvenv.cfg").exists()


@slow_integration_test
def test_get_dependencies_zenodo_rdm(python_api: PythonAPI) -> None:
    """Test getting dependencies from installed zenodo-rdm package."""
    # Create a temporary directory for cloning and installation
    with tempfile.TemporaryDirectory() as tmpdir:
        output_dir = Path(tmpdir) / "zenodo-rdm"

        # Parse and clone zenodo/zenodo-rdm repository
        reference = parse_github_reference("zenodo/zenodo-rdm")
        git_api.clone_git_reference(reference, output_dir)

        # Get dependencies
        dependencies = python_api.get_dependencies(output_dir)

        # Verify dependencies is a dictionary
        assert isinstance(dependencies, dict)

        # Verify it contains some packages (at least setuptools, pip, wheel)
        assert len(dependencies) > 0

        # Verify each entry has a package name and version string
        for package_name, version in dependencies.items():
            assert isinstance(package_name, str)
            assert isinstance(version, str)
            assert len(package_name) > 0
            assert len(version) > 0

        # Zenodo-rdm should be in the dependencies (installed in editable mode)
        assert "zenodo-rdm" in dependencies


def test_get_dependencies_invenio_rdm_records(python_api: PythonAPI) -> None:
    """Test getting dependencies from installed invenio-rdm-records package."""
    # Create a temporary directory for cloning and installation
    with tempfile.TemporaryDirectory() as tmpdir:
        output_dir = Path(tmpdir) / "invenio-rdm-records"

        # Parse and clone inveniosoftware/invenio-rdm-records with maint-22.x branch
        reference = parse_github_reference(
            "inveniosoftware/invenio-rdm-records@maint-22.x"
        )
        git_api.clone_git_reference(reference, output_dir)

        # Get dependencies
        dependencies = python_api.get_dependencies(output_dir)

        # Verify dependencies is a dictionary
        assert isinstance(dependencies, dict)

        # Verify it contains some packages
        assert len(dependencies) > 0

        # Verify each entry has a package name and version string
        for package_name, version in dependencies.items():
            assert isinstance(package_name, str)
            assert isinstance(version, str)
            assert len(package_name) > 0
            assert len(version) > 0

        # invenio-rdm-records should be in the dependencies
        assert "invenio-rdm-records" in dependencies

        # Check for some expected dependencies (these are common Invenio dependencies)
        # Note: specific dependencies may vary by version, so we don't assert on specific ones
        # but we can check that the structure is correct
