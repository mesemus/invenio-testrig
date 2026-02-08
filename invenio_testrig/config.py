import json
from collections.abc import Mapping
from pathlib import Path
from typing import Any, Literal, NotRequired, TypedDict, cast, override
from urllib.parse import urlparse

from lark import Lark, Token, Transformer
from lark import exceptions as lark_exceptions
from marshmallow import Schema, ValidationError, fields, post_load, validate
from marshmallow_polyfield import PolyField  # type: ignore[import-untyped]

# TypedDict definitions for loaded config structures


class VersionConstraint(TypedDict):
    """Version constraint with operator and version string."""

    operator: str
    version: str


class PullRequestInfo(TypedDict):
    """Pull request information."""

    source_org: str
    source_repo: str
    source_branch: str
    commits: list[str]


class GitReference(TypedDict):
    """Parsed git reference structure.

    Used for both git references with package metadata (with base, versions, pr_info)
    and simple git repository references (where base and pr_info may be None).
    The package field is always populated, defaulting to the repo name if not explicitly specified.
    """

    org: str
    repo: str
    package: str
    branch: str | None
    pr: int | None
    base: str | None
    versions: list[VersionConstraint]
    pr_info: PullRequestInfo | None
    commit: str | None


class HooksDict(TypedDict, total=False):
    """Hooks configuration with optional bash commands."""

    after_config_preprocessing: str | None
    """Hook called after the yaml config is preprocessed into the json config.
    
    Environment variables:
    - CONFIG_JSON: path to the generated JSON config file (absolute path)
    
    Current working directory: the directory where the command is run
    """

    after_invenio_repo_clone: str | None
    """Hook called after the Invenio repository is cloned.
    
    Environment variables:
    - INVENIO_REPOSITORY_PATH: path to the cloned repository (absolute path)
    - CONFIG_JSON: path to the generated JSON config file (absolute path)
    
    Current working directory: INVENIO_REPOSITORY_PATH
    """

    after_dependencies_collected: str | None
    """Hook called after dependencies are collected and config JSON is updated.
    
    Environment variables:
    - CONFIG_JSON: path to the generated JSON config file (absolute path)
    
    Current working directory: the directory where the command is run
    """

    before_filtering_packages: str | None
    """Hook called before filtering packages that should be tested.
    
    Environment variables:
    - CONFIG_JSON: path to the generated JSON config file (absolute path)
    
    Current working directory: the directory where the command is run
    """

    after_filtering_packages: str | None
    """Hook called after filtering packages that should be tested and config JSON is updated.
    
    Environment variables:
    - CONFIG_JSON: path to the generated JSON config file (absolute path)
    
    Current working directory: the directory where the command is run
    """

    before_repository_checkout: str | None
    after_repository_checkout: str | None
    after_uv_sync: str | None
    after_package_extraction: str | None
    before_cherry_pick: str | None
    after_cherry_pick: str | None
    before_tests: str | None
    after_tests: str | None
    before_e2e_tests: str | None
    after_e2e_tests: str | None


class RepositoryDict(TypedDict):
    """Repository configuration."""

    git: GitReference
    e2e: NotRequired[GitReference | None]


class GithubDict(TypedDict):
    """GitHub organization configuration."""

    org: str
    include: list[str]
    branch: str | None
    exclude: list[str]
    test: list[str]
    extras: list[str]


class ConfigDict(TypedDict):
    """Main configuration structure for invenio-testrig."""

    patches: list[GitReference]
    github: list[GithubDict]
    repository: RepositoryDict
    mode: Literal["as-is", "upstream", "pinned"]
    hooks: dict[str, str]  # see the HooksDict for possible keys
    test_timeout: int
    packages: dict[str, str]
    tested_packages: dict[str, dict[str, Any]]


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
        result: GitReference = {
            "org": "",
            "repo": "",
            "branch": None,
            "pr": None,
            "package": "",
            "base": None,
            "versions": [],
            "pr_info": None,
            "commit": None,
        }

        for item in items:
            if isinstance(item, dict):
                result.update(item)  # type: ignore[typeddict-item]

        # If package was not explicitly provided, use repo name as package name
        if not result["package"]:
            result["package"] = result["repo"].lower()

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
        return {"operator": str(items[0]), "version": str(items[1])}

    def NAME(self, token: Token) -> str:
        return token.value

    def NUMBER(self, token: Token) -> str:
        return token.value

    def OPERATOR(self, token: Token) -> str:
        return token.value

    def VERSION(self, token: Token) -> str:
        return token.value


class PullRequestInfoSchema(Schema):
    """Schema for pull request information."""

    source_org = fields.Str(required=True)
    source_repo = fields.Str(required=True)
    source_branch = fields.Str(required=True)
    commits = fields.List(fields.Str(), required=True)

    class Meta:
        unknown = "INCLUDE"


class VersionConstraintSchema(Schema):
    """Schema for version constraint."""

    operator = fields.Str(required=True)
    version = fields.Str(required=True)

    class Meta:
        unknown = "INCLUDE"


class GitReferenceSchema(Schema):
    """Schema for git reference dictionary (cached/deserialized form)."""

    org = fields.Str(required=True)
    repo = fields.Str(required=True)
    package = fields.Str(required=True)
    branch = fields.Str(allow_none=True)
    pr = fields.Int(allow_none=True)
    base = fields.Str(allow_none=True)
    versions: fields.List[VersionConstraintSchema] = fields.List(
        fields.Nested(VersionConstraintSchema), load_default=list
    )
    pr_info = fields.Nested(PullRequestInfoSchema, allow_none=True)
    commit = fields.Str(allow_none=True)

    @post_load
    def convert_package_to_lower(
        self, data: dict[str, Any], **kwargs: Any
    ) -> dict[str, Any]:
        """Ensure package name is always lowercase after loading."""
        if "package" in data and isinstance(data["package"], str):
            data["package"] = data["package"].lower()
        return data

    class Meta:
        unknown = "INCLUDE"


class GitReferenceField(fields.Field):  # type: ignore[type-arg]
    """
    Custom field that parses git reference strings into structured dictionaries using Lark.

    Supported formats:
    - org/package@branch
    - org/package#pr_number
    - org/package@branch[base]
    - org/package[@branch|#pr]version-range
    - package_name: org/package...
    - https://github.com/org/repo
    - https://github.com/org/repo/tree/branch-name
    - https://github.com/org/repo/pull/123
    """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.parser: Lark = Lark(
            GIT_REFERENCE_GRAMMAR, start="git_reference", parser="lalr"
        )
        self.transformer: GitReferenceTransformer = GitReferenceTransformer()

    def _parse_github_url(self, url: str) -> GitReference | None:
        """Parse a GitHub URL into a GitReference structure.

        Supports:
        - https://github.com/org/repo
        - https://github.com/org/repo/tree/branch-name
        - https://github.com/org/repo/pull/123

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

        if not parts:
            # Simple URL with no branch or PR specified
            pass
        if parts[0] in ("tree", "heads"):
            branch = parts[1]
        elif parts[0] == "pull":
            try:
                pr = int(parts[1])
            except ValueError:
                return None

        # Create GitReference structure
        result: GitReference = {
            "org": org,
            "repo": repo,
            "package": repo.lower(),
            "branch": branch,
            "pr": pr,
            "base": None,
            "versions": [],
            "pr_info": None,
            "commit": None,
        }

        return result

    @override
    def _deserialize(
        self,
        value: Any,
        attr: str | None,
        data: Mapping[str, Any] | None,
        **kwargs: Any,
    ) -> GitReference:
        if not isinstance(value, str):
            raise ValidationError("Git reference must be a string")

        # Try to parse as GitHub URL first
        github_ref = self._parse_github_url(value)
        if github_ref is not None:
            return github_ref

        # Fall back to Lark parser for custom format
        try:
            tree = self.parser.parse(value)  # pyright: ignore[reportUnknownMemberType]
            result = cast(GitReference, self.transformer.transform(tree))  # type: ignore[misc]
            return result
        except lark_exceptions.LarkError as e:
            raise ValidationError(
                f"Invalid git reference format: '{value}'. Expected formats: "
                "org/package@branch, org/package#pr_number, "
                "org/package@branch[base], org/package[@branch|#pr]version-range, "
                "package_name: org/package..., or a GitHub URL "
                "(https://github.com/org/repo, https://github.com/org/repo/tree/branch, "
                "https://github.com/org/repo/pull/123)"
            ) from e


def git_reference_deserialization_schema_selector(
    base_object: Any, parent_object: Any
) -> fields.Field[Any] | Schema:
    """Select appropriate schema based on input type."""
    if isinstance(base_object, str):
        return GitReferenceField()
    elif isinstance(base_object, dict):
        # Create schema instance with context initialized
        schema = GitReferenceSchema()
        # TODO: this is a workaround to make PolyField work with marshmallow 4.
        if not hasattr(schema, "context"):
            schema.context = {}  # type: ignore[attr-defined]
        return schema
    else:
        raise ValidationError("Git reference must be a string or dictionary")


class GitReferencePolyField(PolyField):  # type: ignore[misc]
    """Polymorphic field for git reference that accepts string or dict."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(  # type: ignore[misc]
            deserialization_schema_selector=git_reference_deserialization_schema_selector,
            *args,
            **kwargs,
        )


class HooksSchema(Schema):
    """Schema for hooks configuration."""

    after_config_preprocessing = fields.Str(
        data_key="after-config-preprocessing",
        allow_none=True,
    )
    before_repository_checkout = fields.Str(
        data_key="before-repository-checkout",
        allow_none=True,
    )
    after_repository_checkout = fields.Str(
        data_key="after-repository-checkout",
        allow_none=True,
    )
    after_uv_sync = fields.Str(
        data_key="after-uv-sync",
        allow_none=True,
    )
    after_package_extraction = fields.Str(
        data_key="after-package-extraction",
        allow_none=True,
    )
    before_cherry_pick = fields.Str(
        data_key="before-cherry-pick",
        allow_none=True,
    )
    after_cherry_pick = fields.Str(
        data_key="after-cherry-pick",
        allow_none=True,
    )
    before_tests = fields.Str(
        data_key="before-tests",
        allow_none=True,
    )
    after_tests = fields.Str(
        data_key="after-tests",
        allow_none=True,
    )
    before_e2e_tests = fields.Str(
        data_key="before-e2e-tests",
        allow_none=True,
    )
    after_e2e_tests = fields.Str(
        data_key="after-e2e-tests",
        allow_none=True,
    )

    class Meta:
        unknown = "INCLUDE"


class RepositorySchema(Schema):
    """Schema for repository configuration."""

    git = GitReferencePolyField(required=True)
    e2e = GitReferencePolyField(allow_none=True)

    class Meta:
        unknown = "INCLUDE"


class GithubSchema(Schema):
    """Schema for GitHub organization configuration."""

    org = fields.Str(required=True)
    include = fields.List(fields.Str(), required=True)
    branch = fields.Str(allow_none=True)
    exclude_ = fields.List(
        fields.Str(), load_default=list, attribute="exclude", data_key="exclude"
    )
    test = fields.List(fields.Str(), required=True)
    extras = fields.List(fields.Str(), load_default=list)

    @post_load
    def convert_include_to_lower(
        self, data: dict[str, Any], **kwargs: Any
    ) -> dict[str, Any]:
        """Ensure included repository patterns are lowercase after loading."""
        if "include" in data and isinstance(data["include"], list):
            data["include"] = [str(item).lower() for item in data["include"]]
        return data

    @post_load
    def convert_exclude_to_lower(
        self, data: dict[str, Any], **kwargs: Any
    ) -> dict[str, Any]:
        """Ensure excluded repository patterns are lowercase after loading."""
        if "exclude" in data and isinstance(data["exclude"], list):
            data["exclude"] = [str(item).lower() for item in data["exclude"]]
        return data

    class Meta:
        unknown = "INCLUDE"


class ConfigSchema(Schema):
    """Main configuration schema for invenio-testrig."""

    patches: fields.List[GitReference] = fields.List(
        GitReferencePolyField(), load_default=list, allow_none=True
    )
    github: fields.List[GithubDict] = fields.List(
        fields.Nested(GithubSchema), required=True
    )
    repository: fields.Nested = fields.Nested(RepositorySchema, required=True)
    mode: fields.Str = fields.Str(
        load_default="as-is", validate=validate.OneOf(["as-is", "upstream", "pinned"])
    )
    hooks: fields.Nested = fields.Nested(HooksSchema, load_default=dict)
    test_timeout: fields.Int = fields.Int(load_default=90)
    packages: fields.Dict = fields.Dict(
        keys=fields.Str(), values=fields.Str(), load_default=dict
    )
    tested_packages: fields.Dict = fields.Dict(
        keys=fields.Str(),
        values=fields.Dict(keys=fields.Str(), values=fields.Raw()),
        load_default=dict,
    )

    @post_load
    def convert_nulls_to_defaults(
        self, data: dict[str, Any], **kwargs: Any
    ) -> dict[str, Any]:
        """Convert null patches to empty list after loading."""
        if data.get("patches") is None:
            data["patches"] = []
        if data.get("packages") is None:
            data["packages"] = {}
        if data.get("tested_packages") is None:
            data["tested_packages"] = {}
        return data

    class Meta:
        unknown = "INCLUDE"


def load_config(file: str | Path) -> ConfigDict:
    """Load configuration data from JSON and optionally validate it."""

    path = Path(file)

    with open(path, "r") as stream:
        raw_data = json.load(stream)

    if not isinstance(raw_data, dict):
        raise ValueError("Configuration file must contain a JSON object")

    schema = ConfigSchema()
    return cast(ConfigDict, schema.load(raw_data))


def save_config(file: str | Path, config_dict: ConfigDict) -> None:
    """Save configuration dictionary to JSON file with consistent formatting."""
    path = Path(file)
    formatted_config = json.dumps(config_dict, indent=2, sort_keys=True)
    path.write_text(formatted_config)
