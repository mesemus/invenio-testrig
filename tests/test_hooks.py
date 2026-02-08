"""Tests for hooks module."""

import tempfile
from pathlib import Path
from typing import cast

from invenio_testrig.config import ConfigDict
from invenio_testrig.hooks import run_hook


def test_run_hook_multiline():
    """Test that multiline hook scripts work correctly."""
    # Create a temporary file to capture output
    with tempfile.NamedTemporaryFile(mode="w+", delete=True, suffix=".txt") as f:
        output_file = Path(f.name)

        # Define a multiline hook script that redirects to the file
        multiline_script = f"""
echo "First line $blah" >> {output_file}
echo "Second line" >> {output_file}
"""

        config = {"hooks": {"test_hook": multiline_script}}

        # Run the hook
        run_hook(
            cast(ConfigDict, config), "test_hook", cwd=Path("."), env={"blah": "aaa"}
        )

        # Read and verify the file contents
        output_content = output_file.read_text()
        assert "First line aaa" in output_content
        assert "Second line" in output_content


def test_run_hook_nonexistent():
    """Test that running a non-existent hook does nothing."""

    # Should not raise an error
    run_hook(cast(ConfigDict, {"hooks": {}}), "nonexistent_hook", cwd=Path("."), env={})
