"""Git reference parsing utilities."""

from typing import Any, cast
from urllib.parse import parse_qs, urlparse

from lark import Lark, Token, Transformer
from lark import exceptions as lark_exceptions
from marshmallow import ValidationError

from .api import GitApi
from .api import git_api as default_git_api
from .types import GitReference, GitReferenceSchema, VersionConstraint


def parse_reference(
    reference: str | GitReference | dict[str, Any], git_api: GitApi | None = None
) -> GitReference:
    """Parse a git reference string into a GitReference structure.

    Supported formats:
    - org/package@branch
    - org/package#pr_number
    - org/package@branch[base]
    - org/package[@branch|#pr]version-range
    - package_name: org/package...
    - https://github.com/org/repo
    - https://github.com/org/repo/tree/branch-name
    - https://github.com/org/repo/pull/123

    Also pip-installed github references:
    - https://github.com/inveniosoftware/invenio-records-resources?branch=fix-read-many#c6b973a14802e2a7f73100ab4e32cb0c36bd4672
    - https://github.com/inveniosoftware/invenio-swh?rev=v0.13.4#828a3a415cf8e725c369939832b61281c44aec40

    Args:
        reference: Git reference string to parse

    Returns:
        Parsed GitReference structure

    Raises:
        ValidationError: If the reference string is invalid
    """

    if isinstance(reference, str):
        parsed_reference = _parse_string_reference(reference)
    elif isinstance(reference, dict):
        parsed_reference = cast(GitReference, GitReferenceSchema().load(reference))
    else:
        parsed_reference = reference

    return (git_api or default_git_api).resolve_reference(parsed_reference)


def _parse_string_reference(reference: str) -> GitReference:
    # Try to parse as GitHub URL first
    github_ref = _parse_github_url(reference)
    if github_ref is not None:
        return github_ref

    # Fall back to Lark parser for custom format
    try:
        tree = _parser.parse(reference)  # pyright: ignore[reportUnknownMemberType]
        result = cast(GitReference, _transformer.transform(tree))  # type: ignore[misc]
        return result
    except lark_exceptions.LarkError as e:
        raise ValidationError(
            f"Invalid git reference format: '{reference}'. Expected formats: "
            "org/package@branch, org/package#pr_number, "
            "org/package@branch[base], org/package[@branch|#pr]version-range, "
            "package_name: org/package..., or a GitHub URL "
            "(https://github.com/org/repo, https://github.com/org/repo/tree/branch, "
            "https://github.com/org/repo/pull/123)"
        ) from e


GIT_REFERENCE_GRAMMAR = r"""
    git_reference: [package_prefix] repo_ref [base_bracket] [version_constraints]
    
    package_prefix: NAME ":" WS*
    
    repo_ref: NAME "/" NAME (branch_ref | pr_ref)?
    
    branch_ref: "@" NAME
    pr_ref: "#" NUMBER
    
    base_bracket: "[" NAME "]"
    
    version_constraints: version_constraint (WS* "," WS* version_constraint)*
    
    version_constraint: OPERATOR VERSION
    
    OPERATOR: ">=" | "<=" | ">" | "<" | "==" | "!="
    VERSION: /\d+(\.\d+)*((a|alpha|b|beta|rc|c)(\.?\d+))?(\.post\d+)?(\.dev\d+)?(\+[\w\.]+)?/
    NAME: /[\w\-\.]+/
    NUMBER: /\d+/
    
    WS: /\s+/
    
    %ignore WS
"""


class GitReferenceTransformer(Transformer):  # type: ignore[type-arg]
    """Transform parsed git reference tree into a dictionary."""

    def git_reference(self, items: list[Any]) -> GitReference:
        result = GitReference(
            org="",
            repo="",
            branch=None,
            pr=None,
            package="",
            base=None,
            versions=[],
            pr_info=None,
            commit=None,
        )

        for item in items:
            if isinstance(item, dict):
                for k, v in item.items():  # type: ignore[union-attr]
                    setattr(result, k, v)  # type: ignore[union-attr]

        if not result.package:
            result.package = result.repo.lower()

        return result

    def package_prefix(self, items: list[str]) -> dict[str, str]:
        return {"package": str(items[0]).lower()}

    def repo_ref(self, items: list[Any]) -> dict[str, str | None]:
        result: dict[str, str | None] = {"org": str(items[0]), "repo": str(items[1])}
        if len(items) > 2 and isinstance(items[2], dict):
            result.update(items[2])  # type: ignore[arg-type]
        return result

    def branch_ref(self, items: list[str]) -> dict[str, str]:
        return {"branch": str(items[0])}

    def pr_ref(self, items: list[str]) -> dict[str, int]:
        return {"pr": int(items[0])}

    def base_bracket(self, items: list[str]) -> dict[str, str]:
        return {"base": str(items[0])}

    def version_constraints(
        self, items: list[VersionConstraint]
    ) -> dict[str, list[VersionConstraint]]:
        return {"versions": items}

    def version_constraint(self, items: list[str]) -> VersionConstraint:
        return VersionConstraint(operator=str(items[0]), version=str(items[1]))

    def NAME(self, token: Token) -> str:
        return token.value

    def NUMBER(self, token: Token) -> str:
        return token.value

    def OPERATOR(self, token: Token) -> str:
        return token.value

    def VERSION(self, token: Token) -> str:
        return token.value


def _parse_github_url(url: str) -> GitReference | None:
    """Parse a GitHub URL into a GitReference structure.

    Supports:
    - https://github.com/org/repo
    - https://github.com/org/repo/tree/branch-name
    - https://github.com/org/repo/pull/123

    Also pip-installed github references:
    - https://github.com/inveniosoftware/invenio-records-resources?branch=fix-read-many#c6b973a14802e2a7f73100ab4e32cb0c36bd4672
    - https://github.com/inveniosoftware/invenio-swh?rev=v0.13.4#828a3a415cf8e725c369939832b61281c44aec40

    Returns None if the URL is not a valid GitHub URL.
    """
    if not url.startswith("https://"):
        return None

    parsed = urlparse(url)

    # Check if it's a GitHub URL
    if parsed.netloc != "github.com":
        return None

    # Parse the path: /org/repo[/tree/branch | /pull/number]

    org, repo, *parts = parsed.path.strip("/").split("/")
    if repo.endswith(".git"):
        repo = repo[:-4]

    branch: str | None = None
    pr: int | None = None
    commit: str | None = None

    if parts:
        if parts[0] in ("tree", "heads"):
            branch = parts[1]
        elif parts[0] == "pull":
            try:
                pr = int(parts[1])
            except ValueError:
                return None

    # Handle pip-installed github references with query parameters
    # e.g., ?branch=fix-read-many or ?rev=v0.13.4
    if parsed.query and branch is None:
        query_dict = parse_qs(parsed.query)
        # Check for 'branch' or 'rev' parameters
        if "branch" in query_dict:
            branch = query_dict["branch"][0]
        elif "rev" in query_dict:
            branch = query_dict["rev"][0]
        # there might be a commit after the # in the URL

    if parsed.fragment:
        commit = parsed.fragment

    # Create GitReference structure
    result = GitReference(
        org=org,
        repo=repo,
        package=repo.lower(),
        branch=branch,
        pr=pr,
        base=None,
        versions=[],
        pr_info=None,
        commit=commit,
    )

    return result


# Initialize parser and transformer once at module level for efficiency
_parser: Lark = Lark(GIT_REFERENCE_GRAMMAR, start="git_reference", parser="lalr")
_transformer: GitReferenceTransformer = GitReferenceTransformer()
