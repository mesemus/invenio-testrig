"""Type definitions for GitHub-related structures."""

import logging
from dataclasses import dataclass, field
from typing import Any

import semver
from marshmallow_dataclass import class_schema

log = logging.getLogger(__name__)


@dataclass
class VersionConstraint:
    """Version constraint with operator and version string."""

    operator: str
    version: str

    def applies_to(self, version_str: str) -> bool:
        self_version = semver.Version.parse(self.version)
        tested_version = semver.Version.parse(version_str)

        if self.operator == "==":
            return tested_version == self_version
        elif self.operator == ">=":
            return tested_version >= self_version
        elif self.operator == "<=":
            return tested_version <= self_version
        elif self.operator == ">":
            return tested_version > self_version
        elif self.operator == "<":
            return tested_version < self_version
        elif self.operator == "!=":
            return tested_version != self_version
        raise ValueError(f"Unsupported operator {self.operator} in version constraint")


@dataclass
class PullRequestInfo:
    """Pull request information."""

    source_org: str
    source_repo: str
    source_branch: str
    commits: list[str]
    """Commits included in the PR, as a list of commit SHAs. 
    
       The order is oldest to newest.
    """


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
    actual_version: str | None = None
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
            "versions": [vars(v) for v in getattr(self, "versions", [])],
            "pr_info": vars(self.pr_info) if self.pr_info else None,
            "commit": self.commit,
            "actual_version": self.actual_version,
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


@dataclass
class Patch(GitReference):
    """Patch information, extending GitReference with patch-specific behaviour."""

    versions: list[VersionConstraint] = field(default_factory=list)  # type: ignore[assignment]

    def applies_to(self, another: GitReference) -> bool:
        """Check if this patch applies to another reference."""
        if self.package != another.package:
            return False

        # If no version constraints, it applies to any reference with the same package
        if not self.versions:
            return True

        # If the other reference doesn't have an actual version, we can't determine applicability
        if not another.actual_version:
            log.error(
                f"Cannot determine if patch {self} applies to {another} because the other reference does not have an actual version resolved."
            )
            return False
        # Check if any of the version constraints match the other reference's actual version
        for constraint in self.versions:
            if not constraint.applies_to(another.actual_version):
                return False
        return True


GitReferenceSchema = class_schema(GitReference)
PatchSchema = class_schema(Patch)
