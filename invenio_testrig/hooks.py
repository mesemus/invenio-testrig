import logging
from pathlib import Path
from typing import Any

from .config import Config

logger = logging.getLogger(__name__)


def run_hook(
    config: Config,
    config_path: str | Path,
    hook_name: str,
    **extra_parameters: Any,
) -> Config:
    """Run a hook by name. A hook is a python function defined as a string in the config
    which is called at a specific point during the process. The hook function can optionally take
    additional environment variables and a working directory.
    """
    hook_func = getattr(config.hooks, hook_name, None)

    if not hook_func:
        return config

    logging.info("Running hook %s", hook_name)

    # Import the Python function from package.module:function string
    if ":" not in hook_func:
        raise ValueError(
            f"Invalid hook format: {hook_func}. Expected 'package.module:function'"
        )

    module_path, func_name = hook_func.rsplit(":", 1)

    # Import the module
    import importlib

    module = importlib.import_module(module_path)

    # Get the function from the module
    func = getattr(module, func_name)

    # Call the hook function with config, config_path, and other parameters
    func(
        config=config,
        config_path=config_path,
        **extra_parameters,
    )

    return config
