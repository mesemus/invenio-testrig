## Collected Warnings

### Patched

#### Warning 1 - 35 occurrences

DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).

| Package | Count |
|---------|-------|
| `invenio-oauthclient` | 8 |
| `invenio-audit-logs` | 6 |
| `invenio-github` | 6 |
| `invenio-records-ui` | 5 |
| `invenio-administration` | 3 |
| `invenio-records-permissions` | 3 |
| `invenio-records-rest` | 3 |
| `invenio-cache` | 1 |

#### Warning 2 - 14 occurrences

DeprecationWarning: jsonschema.RefResolver is deprecated as of v4.18.0, in favor of the https://github.com/python-jsonschema/referencing library, which provides more compliant referencing behavior as well as more flexible APIs for customization. A future release will remove RefResolver. Please file a feature request (on referencing) if you are missing an API for the kind of customization you need.

| Package | Count |
|---------|-------|
| `invenio-records-rest` | 3 |
| `invenio-administration` | 2 |
| `invenio-audit-logs` | 2 |
| `invenio-notifications` | 2 |
| `invenio-records-permissions` | 2 |
| `invenio-records-ui` | 2 |
| `invenio-jsonschemas` | 1 |

#### Warning 3 - 11 occurrences

PendingDeprecationWarning: Schema().dump().data and Schema().dump().errors as well as Schema().load().data and Schema().loads().dataattributes are deprecated in marshmallow v3.x.

| Package | Count |
|---------|-------|
| `invenio-records-rest` | 11 |

#### Warning 4 - 11 occurrences

RemovedInMarshmallow4Warning: The `context` parameter is deprecated and will be removed in marshmallow 4.0. Use `contextvars.ContextVar` to pass context instead.

| Package | Count |
|---------|-------|
| `invenio-records-rest` | 8 |
| `invenio-audit-logs` | 3 |

#### Warning 5 - 7 occurrences

DeprecationWarning: 'crypt' is deprecated and slated for removal in Python 3.13

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-github` | 1 |
| `invenio-notifications` | 1 |
| `invenio-oauthclient` | 1 |
| `invenio-records-permissions` | 1 |
| `invenio-records-ui` | 1 |

#### Warning 6 - 6 occurrences

DeprecationWarning: Deprecated call to `pkg_resources.declare_namespace('fs')`.

| Package | Count |
|---------|-------|
| `invenio-administration` | 2 |
| `invenio-audit-logs` | 2 |
| `invenio-notifications` | 2 |

#### Warning 7 - 6 occurrences

DeprecationWarning: jsonschema.exceptions.RefResolutionError is deprecated as of version 4.18.0. If you wish to catch potential reference resolution errors, directly catch referencing.exceptions.Unresolvable.

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-notifications` | 1 |
| `invenio-records-permissions` | 1 |
| `invenio-records-rest` | 1 |
| `invenio-records-ui` | 1 |

#### Warning 8 - 5 occurrences

DeprecationWarning: Using the initialization functions in flask_caching.backend is deprecated.  Use the a full path to backend classes directly.

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-cache` | 1 |
| `invenio-github` | 1 |
| `invenio-records-permissions` | 1 |

#### Warning 9 - 5 occurrences

FutureWarning: CSRF validation will be enabled by default in the version 1.3.x

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-github` | 1 |
| `invenio-records-permissions` | 1 |
| `invenio-records-rest` | 1 |

#### Warning 10 - 5 occurrences

SAWarning: nested transaction already deassociated from connection

| Package | Count |
|---------|-------|
| `invenio-records-rest` | 4 |
| `invenio-records-ui` | 1 |

#### Warning 11 - 4 occurrences

DeprecationWarning: Deprecated call to `pkg_resources.declare_namespace('sphinxcontrib')`.

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-notifications` | 1 |
| `invenio-oauthclient` | 1 |

#### Warning 12 - 4 occurrences

PytestMockWarning: Mocks returned by pytest-mock do not need to be used as context managers. The mocker fixture automatically undoes mocking at the end of a test. This warning can be ignored if it was triggered by mocking a context manager. https://pytest-mock.readthedocs.io/en/latest/usage.html#usage-as-context-manager

| Package | Count |
|---------|-------|
| `invenio-cache` | 4 |

#### Warning 13 - 4 occurrences

RemovedInMarshmallow4Warning: The 'missing' argument to fields is deprecated. Use 'load_default' instead.

| Package | Count |
|---------|-------|
| `invenio-records-rest` | 4 |

#### Warning 14 - 4 occurrences

UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-notifications` | 1 |
| `invenio-oauthclient` | 1 |

#### Warning 15 - 3 occurrences

DeprecationWarning: Deprecated call to `pkg_resources.declare_namespace('fs.opener')`.

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-notifications` | 1 |

#### Warning 16 - 3 occurrences

DeprecationWarning: The '__version_info__' attribute is deprecated and will be removed in in a future version. Use feature detection or 'packaging.Version(importlib.metadata.version("marshmallow")).release' instead.

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-notifications` | 1 |

#### Warning 17 - 3 occurrences

DeprecationWarning: datetime.datetime.utcfromtimestamp() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.fromtimestamp(timestamp, datetime.UTC).

| Package | Count |
|---------|-------|
| `invenio-github` | 1 |
| `invenio-oauthclient` | 1 |
| `invenio-records-ui` | 1 |

#### Warning 18 - 2 occurrences

DeprecationWarning: Link is deprecated and will be removed in v14.0. Use `ExternalLink` for third-party links and `EndpointLink` for InvenioRDM links.

| Package | Count |
|---------|-------|
| `invenio-audit-logs` | 1 |
| `invenio-notifications` | 1 |

#### Warning 19 - 2 occurrences

DeprecationWarning: No path_separator found in configuration; falling back to legacy splitting on spaces/commas for version_locations.  Consider adding path_separator=os to Alembic config.

| Package | Count |
|---------|-------|
| `invenio-audit-logs` | 1 |
| `invenio-db` | 1 |

#### Warning 20 - 2 occurrences

DeprecationWarning: distutils Version classes are deprecated. Use packaging.version instead.

| Package | Count |
|---------|-------|
| `invenio-records-rest` | 2 |

#### Warning 21 - 2 occurrences

PytestConfigWarning: Unknown config option: pep8ignore

| Package | Count |
|---------|-------|
| `invenio-jsonschemas` | 1 |
| `invenio-records-ui` | 1 |

#### Warning 22 - 2 occurrences

RemovedInMarshmallow4Warning: The 'default' argument to fields is deprecated. Use 'dump_default' instead.

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |
| `invenio-audit-logs` | 1 |

#### Warning 23 - 1 occurrence

DeprecationWarning: Implicit imports (e.g., 'import idutils; idutils.function;') might be removed in the next major version. Please use explicit imports (e.g., 'from idutils import function;') instead.

| Package | Count |
|---------|-------|
| `invenio-records-rest` | 1 |

#### Warning 24 - 1 occurrence

DeprecationWarning: Please use hash_password instead of encrypt_password.

| Package | Count |
|---------|-------|
| `invenio-records-ui` | 1 |

#### Warning 25 - 1 occurrence

DeprecationWarning: Remember me support has been removed.

| Package | Count |
|---------|-------|
| `invenio-audit-logs` | 1 |

#### Warning 26 - 1 occurrence

DeprecationWarning: The '__version__' attribute is deprecated and will be removed in in a future version. Use feature detection or 'importlib.metadata.version("marshmallow")' instead.

| Package | Count |
|---------|-------|
| `invenio-records-rest` | 1 |

#### Warning 27 - 1 occurrence

DeprecationWarning: The cern contrib is deprecated. Please use the generic keycloak instead.

| Package | Count |
|---------|-------|
| `invenio-oauthclient` | 1 |

#### Warning 28 - 1 occurrence

DeprecationWarning: The patch() method is deprecated and will be removed.

| Package | Count |
|---------|-------|
| `invenio-records-rest` | 1 |

#### Warning 29 - 1 occurrence

PendingDeprecationWarning: The WSGI_PROXIES configuration is deprecated and it will be removed, use PROXYFIX_CONFIG instead

| Package | Count |
|---------|-------|
| `invenio-base` | 1 |

#### Warning 30 - 1 occurrence

PytestCollectionWarning: cannot collect test class 'TestCustomView' because it has a __init__ constructor (from: tests/test_base.py)

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |

#### Warning 31 - 1 occurrence

PytestCollectionWarning: cannot collect test class 'TestPermissionPolicy' because it has a __init__ constructor (from: tests/test_permissions_base.py)

| Package | Count |
|---------|-------|
| `invenio-records-permissions` | 1 |

#### Warning 32 - 1 occurrence

PytestCollectionWarning: cannot collect test class 'TestSchema' because it has a __init__ constructor (from: tests/test_marshmallow_utils.py)

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |

#### Warning 33 - 1 occurrence

RemovedInMarshmallow4Warning: Passing field metadata as keyword arguments is deprecated. Use the explicit `metadata=...` argument instead. Additional metadata: {'load_from': 'from'}

| Package | Count |
|---------|-------|
| `invenio-records-rest` | 1 |

#### Warning 34 - 1 occurrence

RemovedInMarshmallow4Warning: `Field.fail` is deprecated. Use `raise self.make_error("required", ...)` instead.

| Package | Count |
|---------|-------|
| `invenio-records-rest` | 1 |

#### Warning 35 - 1 occurrence

SADeprecationWarning: The from_engine() method on Inspector is deprecated and will be removed in a future release.  Please use the sqlalchemy.inspect() function on an Engine or Connection in order to acquire an Inspector. (deprecated since: 1.4)

| Package | Count |
|---------|-------|
| `invenio-audit-logs` | 1 |

#### Warning 36 - 1 occurrence

SyntaxWarning: "is" with 'int' literal. Did you mean "=="?

| Package | Count |
|---------|-------|
| `invenio-records-rest` | 1 |

#### Warning 37 - 1 occurrence

SyntaxWarning: invalid escape sequence '\?'

| Package | Count |
|---------|-------|
| `invenio-records-rest` | 1 |

#### Warning 38 - 1 occurrence

UserWarning: Set configuration variable SECRET_KEY with random string

| Package | Count |
|---------|-------|
| `invenio-records-rest` | 1 |

#### Warning 39 - 1 occurrence

UserWarning: Test

| Package | Count |
|---------|-------|
| `invenio-base` | 1 |

#### Warning 40 - 1 occurrence

UserWarning: autoincrement and existing_autoincrement only make sense for MySQL

| Package | Count |
|---------|-------|
| `invenio-audit-logs` | 1 |


