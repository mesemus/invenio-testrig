"""Common utility functions and decorators.

This module provides shared utilities including the extensible_dataclass
decorator for creating dataclasses that accept unknown keyword arguments,
and subprocess execution helpers.
"""

import logging
import subprocess
from dataclasses import dataclass, field, fields
from typing import Any, TypeVar, cast, dataclass_transform

log = logging.getLogger(__name__)

T = TypeVar("T")


@dataclass
class ExtensibleMixin:
    """A mixin that adds an _extra field to store unknown kwargs."""

    _extra: dict[str, Any] = field(default_factory=dict)  # type: ignore


@dataclass_transform()
def extensible_dataclass(cls: type[T]) -> type[T]:
    """
    Decorator that turns a dataclass into one that collects unknown __init__ kwargs
    into an _extra dict.
    """
    cls = dataclass(cls)  # make it a normal dataclass first

    known_fields = {f.name for f in fields(cls) if f.init}

    class Initialization:
        def __init__(self, **kwargs: Any):
            super().__init__()  # call dataclass __init__ to initialize fields with defaults

            _extra = kwargs.pop("_extra", {})
            for k, v in kwargs.items():
                if k in known_fields:
                    setattr(self, k, v)
                else:
                    _extra[k] = v
            self._extra = _extra

    return cast(
        type[T],
        dataclass(kw_only=True, init=False)(
            type(
                cls.__name__,
                (Initialization, ExtensibleMixin, cls),
                {},
            )
        ),
    )


def extra_data(instance: Any) -> dict[str, Any]:
    """Get the extra data stored in an instance created by extensible_dataclass."""
    return getattr(instance, "_extra", {})


def call_executable_quietly(cmd: list[str], **kwargs: Any) -> tuple[str, str]:
    """Call an executable command quietly, capturing stdout and stderr.

    If the command fails (non-zero exit code), print the captured output and raise an exception.

    Args:
        cmd: The command to execute as a list of strings
        **kwargs: Additional keyword arguments to pass to subprocess.run

    Returns:
        A tuple of (stdout, stderr) captured from the command execution

    Raises:
        subprocess.CalledProcessError: If the command exits with a non-zero status
    """

    log.info("%s", " ".join(cmd))
    result = subprocess.run(cmd, capture_output=True, text=True, **kwargs)

    if result.returncode != 0:
        log.error("Command failed: %s", " ".join(cmd))
        log.error("CWD: %s", kwargs.get("cwd", "."))
        log.error("%s", result.stdout)
        log.error("%s", result.stderr)

        raise subprocess.CalledProcessError(
            result.returncode, cmd, output=result.stdout, stderr=result.stderr
        )

    return result.stdout, result.stderr
