"""Patcher implementations for applying patches to repositories.

This module provides different patching strategies for managing repository
versions with and without patches, including pinned and upstream modes.
"""

from .base import Patcher
from .pinned import PinnedRebasePatcher
from .upstream import UpstreamRebasePatcher

patchers_by_mode: dict[str, type[Patcher]] = {
    "pinned": PinnedRebasePatcher,
    "upstream": UpstreamRebasePatcher,
}

__all__ = [
    "Patcher",
    "UpstreamRebasePatcher",
    "PinnedRebasePatcher",
    "patchers_by_mode",
]
