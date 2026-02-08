from .asis import AsIsPatcher
from .base import Patcher
from .pinned import PinnedPatcher
from .upstream import UpstreamPatcher

patchers_by_mode: dict[str, type[Patcher]] = {
    "as-is": AsIsPatcher,
    "pinned": PinnedPatcher,
    "upstream": UpstreamPatcher,
}

__all__ = [
    "Patcher",
    "AsIsPatcher",
    "PinnedPatcher",
    "UpstreamPatcher",
    "patchers_by_mode",
]
