"""Shared type definitions and protocols for invenio-testrig."""

from dataclasses import dataclass, field

from invenio_testrig.github.types import GitReference


@dataclass
class TestedPackageInfo:
    """Information about a package that is being tested, derived from the github configuration.

    This one is generated automatically based on the github configuration
    and the dependencies, so it is not extensible.
    """

    reference: GitReference
    test: list[str]
    extras: list[str]
    freeze: list[str]
    patches: list[GitReference] = field(default_factory=list)  # type: ignore[assignment]
    unpatched_reference: GitReference | None = None
    patched_reference: GitReference | None = None


@dataclass
class ExecutionStatus:
    """Execution status for a tested package."""

    status: str  # e.g. "passed", "failed", "skipped" or "pending"
    package: TestedPackageInfo
    dependencies: list[TestedPackageInfo] = field(default_factory=list)  # type: ignore[assignment]

    @property
    def package_name(self) -> str:
        """Return the package name of the base reference."""
        return self.package.reference.package


@dataclass
class ReportPackageData:
    """Data structure for package test results in reports."""

    info: TestedPackageInfo
    artefact_dir: str  # directory name relative to the report where the artefacts for this package are stored (e.g. logs, status files, etc.)
    patched: ExecutionStatus
    original: ExecutionStatus


class Progress:
    """Protocol for reporting progress of the testing process."""

    def start(self, message: str, icon: str | None = None) -> None:
        """Report the start of a new step in the testing process."""
        ...

    def info(self, message: str, icon: str | None = None) -> None:
        """Report informational messages about the testing process."""
        ...

    def success(self, message: str, icon: str | None = None) -> None:
        """Report successful completion of a step in the testing process."""
        ...

    def warning(self, message: str, icon: str | None = None) -> None:
        """Report a warning during the testing process."""
        ...

    def error(self, message: str, icon: str | None = None) -> None:
        """Report an error during the testing process."""
        ...
