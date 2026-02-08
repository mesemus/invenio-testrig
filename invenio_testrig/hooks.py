import logging
import os
import subprocess
from pathlib import Path

from invenio_testrig.config import ConfigDict, load_config, save_config

logger = logging.getLogger(__name__)


def run_hook(
    config: ConfigDict,
    config_path: str | Path,
    hook_name: str,
    *,
    cwd: Path | None = None,
    env: dict[str, str] | None = None,
) -> ConfigDict:
    """Run a hook by name, passing extra environment variables.

    The hook is a potentially multiline shell script (as a single string)
    that should be invoked with a bash shell. Use /usr/bin/env bash to ensure
    it runs with the user's default bash.
    """
    hooks = config.get("hooks", {})
    hook_func = hooks.get(hook_name)

    if not hook_func:
        return config

    logging.info("Running hook %s", hook_name)

    # Save config before running the hook, so that it can be modified by the hook script if needed
    save_config(config_path, config)

    # Prepare environment with extra variables
    merged_env = os.environ.copy()
    if env is not None:
        merged_env.update(env)

    # Run the hook script with bash
    subprocess.run(
        ["/usr/bin/env", "bash", "-c", hook_func],
        env=merged_env,
        cwd=(cwd or Path(".")).resolve(),
        check=True,
    )
    # Reload config after running the hook, in case it was modified by the hook script
    return load_config(config_path)
