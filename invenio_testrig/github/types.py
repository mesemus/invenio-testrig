"""Type definitions for GitHub-related structures."""

from dataclasses import dataclass, field
from typing import Any

from marshmallow_dataclass import class_schema


@dataclass
class VersionConstraint:
    """Version constraint with operator and version string."""

    operator: str
    version: str


@dataclass
class PullRequestInfo:
    """Pull request information."""

    source_org: str
    source_repo: str
    source_branch: str
    commits: list[str]


@dataclass
class GitReference:
    """Parsed git reference structure.

    Used for both git references with package metadata (with base, versions, pr_info)
    and simple git repository references (where base and pr_info may be None).
    The package field is always populated, defaulting to the repo name if not explicitly specified.
    """

    org: str
    repo: str
    package: str
    branch: str | None = None
    pr: int | None = None
    base: str | None = None
    versions: list[VersionConstraint] = field(default_factory=list)  # type: ignore[assignment]
    pr_info: PullRequestInfo | None = None
    commit: str | None = None

    def __str__(self) -> str:
        ref = f"{self.org}/{self.repo}"
        if self.branch:
            ref += f"@{self.branch}"
        if self.pr is not None:
            ref += f"#{self.pr}"
        if self.base:
            ref += f"[{self.base}]"
        return ref

    def to_dict(self) -> dict[str, Any]:
        """Convert the GitReference to a dictionary."""
        return {
            "org": self.org,
            "repo": self.repo,
            "package": self.package,
            "branch": self.branch,
            "pr": self.pr,
            "base": self.base,
            "versions": [vars(v) for v in self.versions],
            "pr_info": vars(self.pr_info) if self.pr_info else None,
            "commit": self.commit,
        }

    @property
    def github_url(self) -> str:
        """Construct the GitHub URL for this reference."""
        url = f"https://github.com/{self.org}/{self.repo}"
        if self.branch:
            url += f"/tree/{self.branch}"
        elif self.pr is not None:
            url += f"/pull/{self.pr}"
        return url


GitReferenceSchema = class_schema(GitReference)
