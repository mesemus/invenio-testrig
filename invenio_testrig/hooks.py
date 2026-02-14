"""Hook execution system for running custom Python functions at workflow stages.

Hooks allow users to inject custom Python code at specific points during the
testrig workflow, enabling configuration modifications and custom processing.
"""

import importlib.metadata as importlib_metadata
import logging
from typing import Any

from .config import Config

logger = logging.getLogger(__name__)


def get_hooks(hook_name):
    """Load hooks from the entrypoints. Hooks are named as
    invenio_testrig.hooks.<hook_name>
    """
    for ep in importlib_metadata.entry_points(group="invenio_testrig.hooks"):
        if ep.name == hook_name:
            yield ep.load()


def run_hook(
    config: Config,
    hook_name: str,
    **extra_parameters: Any,
) -> None:
    """Run a hook by name. A hook is a python function defined as a string in the config
    which is called at a specific point during the process. The hook function can optionally take
    additional environment variables and a working directory.
    """
    for hook_ep_name, hook_func in get_hooks(hook_name):
        logging.info("Running hook %s", hook_ep_name)

        # Call the hook function with config, config_path, and other parameters
        hook_func(
            config=config,
            **extra_parameters,
        )
