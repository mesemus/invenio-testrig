from .base import Patcher
from .pinned import PinnedOverwritePatcher, PinnedRebasePatcher
from .upstream import UpstreamOverwritePatcher, UpstreamRebasePatcher

patchers_by_mode: dict[str, type[Patcher]] = {
    "pinned-overwrite": PinnedOverwritePatcher,
    "pinned-rebase": PinnedRebasePatcher,
    "upstream-overwrite": UpstreamOverwritePatcher,
    "upstream-rebase": UpstreamRebasePatcher,
}

__all__ = [
    "Patcher",
    "UpstreamOverwritePatcher",
    "UpstreamRebasePatcher",
    "PinnedOverwritePatcher",
    "PinnedRebasePatcher",
    "patchers_by_mode",
]
