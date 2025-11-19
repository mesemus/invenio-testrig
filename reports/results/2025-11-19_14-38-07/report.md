# Invenio Bugfix Verification Results

> **⏳ Status: Running** - This report is being updated as tests complete.

_Last updated: 2025-11-19 14:41:34 UTC_

## 📊 Overall Status

| Metric | Count |
|--------|-------|
| **Total Packages** | 22 |
| **Patched Packages** | 22 |
| **Unpatched Packages** | 0 |

### Patch Results
| Result | Count |
|--------|-------|
| ✅ Fixed | 22 |
| ❌ Regressions | 0 |
| ⚠️  Still Failing | 0 |
| ℹ️  No Change | 0 |

## 🔧 Configured Patches

| Patched Package | Repository | Branch |
|----------------|------------|--------|
| [pytest-invenio](https://github.com/oarepo/pytest-invenio/tree/nested-db-session-rollback) | https://github.com/oarepo/pytest-invenio | nested-db-session-rollback |

## 🔄 Patched Packages

| Package | Patches Applied | Original | Patched | Result |
|---------|----------------|--------|-------|--------|

## 📦 Packages that do not depend on patched packages

| Package | Build Status |
|---------|--------------|

## 🔄 Packages that depend on patched packages

| Package | Patches Applied | Original | Patched | Result |
|---------|----------------|--------|-------|--------|
| `invenio-mail` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-mail/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-mail/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-mail/test-report-patched.xml) | ✅ Patch applied successfully, tests passed |
| `invenio-queues` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-queues/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-queues/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-queues/test-report-patched.xml) | ✅ Patch applied successfully, tests passed |
| `invenio-cache` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-cache/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-cache/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-cache/test-report-patched.xml)<br>[warnings](packages/invenio-cache/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-app` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-app/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-app/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-app/test-report-patched.xml)<br>[warnings](packages/invenio-app/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-jobs` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-jobs/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-jobs/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-jobs/test-report-patched.xml)<br>[warnings](packages/invenio-jobs/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-theme` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-theme/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-theme/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-theme/test-report-patched.xml) | ✅ Patch applied successfully, tests passed |
| `invenio-assets` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-assets/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-assets/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-assets/test-report-patched.xml) | ✅ Patch applied successfully, tests passed |
| `invenio-celery` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-celery/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-celery/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-celery/test-report-patched.xml) | ✅ Patch applied successfully, tests passed |
| `invenio-pidstore` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-pidstore/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-pidstore/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-pidstore/test-report-patched.xml)<br>[warnings](packages/invenio-pidstore/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-indexer` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-indexer/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-indexer/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-indexer/test-report-patched.xml)<br>[warnings](packages/invenio-indexer/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-oaiserver` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-oaiserver/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-oaiserver/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-oaiserver/test-report-patched.xml)<br>[warnings](packages/invenio-oaiserver/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-drafts-resources` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-drafts-resources/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-drafts-resources/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-drafts-resources/test-report-patched.xml)<br>[warnings](packages/invenio-drafts-resources/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-records-permissions` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-records-permissions/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-records-permissions/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-records-permissions/test-report-patched.xml)<br>[warnings](packages/invenio-records-permissions/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-stats` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-stats/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-stats/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-stats/test-report-patched.xml)<br>[warnings](packages/invenio-stats/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-search-ui` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-search-ui/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-search-ui/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-search-ui/test-report-patched.xml) | ✅ Patch applied successfully, tests passed |
| `invenio-formatter` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-formatter/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-formatter/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-formatter/test-report-patched.xml)<br>[warnings](packages/invenio-formatter/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-checks` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-checks/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-checks/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-checks/test-report-patched.xml)<br>[warnings](packages/invenio-checks/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-audit-logs` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-audit-logs/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-audit-logs/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-audit-logs/test-report-patched.xml)<br>[warnings](packages/invenio-audit-logs/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-records-rest` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-records-rest/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-records-rest/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-records-rest/test-report-patched.xml)<br>[warnings](packages/invenio-records-rest/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-administration` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-administration/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-administration/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-administration/test-report-patched.xml)<br>[warnings](packages/invenio-administration/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-github` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-github/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-github/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-github/test-report-patched.xml)<br>[warnings](packages/invenio-github/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-i18n` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-i18n/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-i18n/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-i18n/test-report-patched.xml) | ✅ Patch applied successfully, tests passed |

## Collected Warnings

### Patched

#### Warning 1 - 57 occurrences

DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).

| Package | Count |
|---------|-------|
| `invenio-stats` | 11 |
| `invenio-drafts-resources` | 7 |
| `invenio-jobs` | 7 |
| `invenio-audit-logs` | 6 |
| `invenio-github` | 6 |
| `invenio-oaiserver` | 5 |
| `invenio-administration` | 3 |
| `invenio-records-permissions` | 3 |
| `invenio-records-rest` | 3 |
| `invenio-indexer` | 2 |
| `invenio-pidstore` | 2 |
| `invenio-cache` | 1 |
| `invenio-formatter` | 1 |

#### Warning 2 - 21 occurrences

DeprecationWarning: jsonschema.RefResolver is deprecated as of v4.18.0, in favor of the https://github.com/python-jsonschema/referencing library, which provides more compliant referencing behavior as well as more flexible APIs for customization. A future release will remove RefResolver. Please file a feature request (on referencing) if you are missing an API for the kind of customization you need.

| Package | Count |
|---------|-------|
| `invenio-records-rest` | 3 |
| `invenio-administration` | 2 |
| `invenio-audit-logs` | 2 |
| `invenio-checks` | 2 |
| `invenio-drafts-resources` | 2 |
| `invenio-indexer` | 2 |
| `invenio-jobs` | 2 |
| `invenio-oaiserver` | 2 |
| `invenio-records-permissions` | 2 |
| `invenio-stats` | 2 |

#### Warning 3 - 20 occurrences

RemovedInMarshmallow4Warning: The `context` parameter is deprecated and will be removed in marshmallow 4.0. Use `contextvars.ContextVar` to pass context instead.

| Package | Count |
|---------|-------|
| `invenio-records-rest` | 8 |
| `invenio-jobs` | 4 |
| `invenio-audit-logs` | 3 |
| `invenio-drafts-resources` | 3 |
| `invenio-checks` | 2 |

#### Warning 4 - 15 occurrences

PendingDeprecationWarning: Schema().dump().data and Schema().dump().errors as well as Schema().load().data and Schema().loads().dataattributes are deprecated in marshmallow v3.x.

| Package | Count |
|---------|-------|
| `invenio-records-rest` | 11 |
| `invenio-oaiserver` | 4 |

#### Warning 5 - 12 occurrences

SAWarning: nested transaction already deassociated from connection

| Package | Count |
|---------|-------|
| `invenio-oaiserver` | 5 |
| `invenio-records-rest` | 4 |
| `invenio-indexer` | 2 |
| `invenio-stats` | 1 |

#### Warning 6 - 10 occurrences

DeprecationWarning: 'crypt' is deprecated and slated for removal in Python 3.13

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-checks` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-github` | 1 |
| `invenio-jobs` | 1 |
| `invenio-oaiserver` | 1 |
| `invenio-pidstore` | 1 |
| `invenio-records-permissions` | 1 |
| `invenio-stats` | 1 |

#### Warning 7 - 10 occurrences

DeprecationWarning: Deprecated call to `pkg_resources.declare_namespace('fs')`.

| Package | Count |
|---------|-------|
| `invenio-administration` | 2 |
| `invenio-audit-logs` | 2 |
| `invenio-checks` | 2 |
| `invenio-drafts-resources` | 2 |
| `invenio-jobs` | 2 |

#### Warning 8 - 10 occurrences

DeprecationWarning: jsonschema.exceptions.RefResolutionError is deprecated as of version 4.18.0. If you wish to catch potential reference resolution errors, directly catch referencing.exceptions.Unresolvable.

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-checks` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-indexer` | 1 |
| `invenio-jobs` | 1 |
| `invenio-oaiserver` | 1 |
| `invenio-records-permissions` | 1 |
| `invenio-records-rest` | 1 |
| `invenio-stats` | 1 |

#### Warning 9 - 9 occurrences

DeprecationWarning: Using the initialization functions in flask_caching.backend is deprecated.  Use the a full path to backend classes directly.

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |
| `invenio-app` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-cache` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-github` | 1 |
| `invenio-jobs` | 1 |
| `invenio-records-permissions` | 1 |
| `invenio-stats` | 1 |

#### Warning 10 - 8 occurrences

FutureWarning: CSRF validation will be enabled by default in the version 1.3.x

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-github` | 1 |
| `invenio-jobs` | 1 |
| `invenio-records-permissions` | 1 |
| `invenio-records-rest` | 1 |
| `invenio-stats` | 1 |

#### Warning 11 - 7 occurrences

DeprecationWarning: Deprecated call to `pkg_resources.declare_namespace('sphinxcontrib')`.

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-checks` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-jobs` | 1 |
| `invenio-oaiserver` | 1 |
| `invenio-pidstore` | 1 |

#### Warning 12 - 7 occurrences

RemovedInMarshmallow4Warning: The 'default' argument to fields is deprecated. Use 'dump_default' instead.

| Package | Count |
|---------|-------|
| `invenio-checks` | 2 |
| `invenio-jobs` | 2 |
| `invenio-administration` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-drafts-resources` | 1 |

#### Warning 13 - 7 occurrences

UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-checks` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-jobs` | 1 |
| `invenio-oaiserver` | 1 |
| `invenio-pidstore` | 1 |

#### Warning 14 - 5 occurrences

DeprecationWarning: Deprecated call to `pkg_resources.declare_namespace('fs.opener')`.

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-checks` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-jobs` | 1 |

#### Warning 15 - 5 occurrences

DeprecationWarning: The '__version_info__' attribute is deprecated and will be removed in in a future version. Use feature detection or 'packaging.Version(importlib.metadata.version("marshmallow")).release' instead.

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-checks` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-jobs` | 1 |

#### Warning 16 - 5 occurrences

RemovedInMarshmallow4Warning: The 'missing' argument to fields is deprecated. Use 'load_default' instead.

| Package | Count |
|---------|-------|
| `invenio-records-rest` | 4 |
| `invenio-drafts-resources` | 1 |

#### Warning 17 - 4 occurrences

DeprecationWarning: Link is deprecated and will be removed in v14.0. Use `ExternalLink` for third-party links and `EndpointLink` for InvenioRDM links.

| Package | Count |
|---------|-------|
| `invenio-audit-logs` | 1 |
| `invenio-checks` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-jobs` | 1 |

#### Warning 18 - 4 occurrences

DeprecationWarning: distutils Version classes are deprecated. Use packaging.version instead.

| Package | Count |
|---------|-------|
| `invenio-oaiserver` | 2 |
| `invenio-records-rest` | 2 |

#### Warning 19 - 4 occurrences

PytestMockWarning: Mocks returned by pytest-mock do not need to be used as context managers. The mocker fixture automatically undoes mocking at the end of a test. This warning can be ignored if it was triggered by mocking a context manager. https://pytest-mock.readthedocs.io/en/latest/usage.html#usage-as-context-manager

| Package | Count |
|---------|-------|
| `invenio-cache` | 4 |

#### Warning 20 - 3 occurrences

DeprecationWarning: Implicit imports (e.g., 'import idutils; idutils.function;') might be removed in the next major version. Please use explicit imports (e.g., 'from idutils import function;') instead.

| Package | Count |
|---------|-------|
| `invenio-checks` | 1 |
| `invenio-pidstore` | 1 |
| `invenio-records-rest` | 1 |

#### Warning 21 - 2 occurrences

ChangedInMarshmallow4Warning: `Field` should not be instantiated. Use `fields.Raw` or  another field subclass instead.

| Package | Count |
|---------|-------|
| `invenio-checks` | 1 |
| `invenio-jobs` | 1 |

#### Warning 22 - 2 occurrences

DeprecationWarning: Deprecated call to `pkg_resources.declare_namespace('flask_admin')`.

| Package | Count |
|---------|-------|
| `invenio-oaiserver` | 1 |
| `invenio-pidstore` | 1 |

#### Warning 23 - 2 occurrences

DeprecationWarning: Deprecated call to `pkg_resources.declare_namespace('flask_admin.contrib')`.

| Package | Count |
|---------|-------|
| `invenio-oaiserver` | 1 |
| `invenio-pidstore` | 1 |

#### Warning 24 - 2 occurrences

DeprecationWarning: The '__version__' attribute is deprecated and will be removed in in a future version. Use feature detection or 'importlib.metadata.version("marshmallow")' instead.

| Package | Count |
|---------|-------|
| `invenio-oaiserver` | 1 |
| `invenio-records-rest` | 1 |

#### Warning 25 - 2 occurrences

DeprecationWarning: datetime.datetime.utcfromtimestamp() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.fromtimestamp(timestamp, datetime.UTC).

| Package | Count |
|---------|-------|
| `invenio-github` | 1 |
| `invenio-stats` | 1 |

#### Warning 26 - 2 occurrences

LegacyAPIWarning: The Query.get() method is considered legacy as of the 1.x series of SQLAlchemy and becomes a legacy construct in 2.0. The method is now available as Session.get() (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)

| Package | Count |
|---------|-------|
| `invenio-jobs` | 1 |
| `invenio-oaiserver` | 1 |

#### Warning 27 - 2 occurrences

PytestDeprecationWarning: @pytest.yield_fixture is deprecated.

| Package | Count |
|---------|-------|
| `invenio-pidstore` | 2 |

#### Warning 28 - 2 occurrences

UserWarning: Set configuration variable SECRET_KEY with random string

| Package | Count |
|---------|-------|
| `invenio-app` | 1 |
| `invenio-records-rest` | 1 |

#### Warning 29 - 1 occurrence

DeprecationWarning: No path_separator found in configuration; falling back to legacy splitting on spaces/commas for version_locations.  Consider adding path_separator=os to Alembic config.

| Package | Count |
|---------|-------|
| `invenio-audit-logs` | 1 |

#### Warning 30 - 1 occurrence

DeprecationWarning: Remember me support has been removed.

| Package | Count |
|---------|-------|
| `invenio-audit-logs` | 1 |

#### Warning 31 - 1 occurrence

DeprecationWarning: The 'record_to_index' function is no longer expected to return a tuple (index, doc_type), instead it should only return the index. Support for the tuple will be removed in a future version of 'invenio-indexer'.

| Package | Count |
|---------|-------|
| `invenio-drafts-resources` | 1 |

#### Warning 32 - 1 occurrence

DeprecationWarning: The 'warn' method is deprecated, use 'warning' instead

| Package | Count |
|---------|-------|
| `invenio-drafts-resources` | 1 |

#### Warning 33 - 1 occurrence

DeprecationWarning: The patch() method is deprecated and will be removed.

| Package | Count |
|---------|-------|
| `invenio-records-rest` | 1 |

#### Warning 34 - 1 occurrence

DeprecationWarning: get_user method is deprecated, user get_user_by_email/get_user_by_id

| Package | Count |
|---------|-------|
| `invenio-stats` | 1 |

#### Warning 35 - 1 occurrence

PytestCollectionWarning: cannot collect test class 'TestCustomView' because it has a __init__ constructor (from: tests/test_base.py)

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |

#### Warning 36 - 1 occurrence

PytestCollectionWarning: cannot collect test class 'TestPermissionPolicy' because it has a __init__ constructor (from: tests/test_permissions_base.py)

| Package | Count |
|---------|-------|
| `invenio-records-permissions` | 1 |

#### Warning 37 - 1 occurrence

PytestCollectionWarning: cannot collect test class 'TestSchema' because it has a __init__ constructor (from: tests/test_marshmallow_utils.py)

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |

#### Warning 38 - 1 occurrence

RemovedInMarshmallow4Warning: Passing field metadata as keyword arguments is deprecated. Use the explicit `metadata=...` argument instead. Additional metadata: {'load_from': 'from'}

| Package | Count |
|---------|-------|
| `invenio-records-rest` | 1 |

#### Warning 39 - 1 occurrence

RemovedInMarshmallow4Warning: `Field.fail` is deprecated. Use `raise self.make_error("required", ...)` instead.

| Package | Count |
|---------|-------|
| `invenio-records-rest` | 1 |

#### Warning 40 - 1 occurrence

SADeprecationWarning: Query.values() is deprecated and will be removed in a future release.  Please use Query.with_entities() (deprecated since: 1.4)

| Package | Count |
|---------|-------|
| `invenio-indexer` | 1 |

#### Warning 41 - 1 occurrence

SADeprecationWarning: The from_engine() method on Inspector is deprecated and will be removed in a future release.  Please use the sqlalchemy.inspect() function on an Engine or Connection in order to acquire an Inspector. (deprecated since: 1.4)

| Package | Count |
|---------|-------|
| `invenio-audit-logs` | 1 |

#### Warning 42 - 1 occurrence

SAWarning: Identity map already had an identity for (<class 'invenio_jobs.models.Run'>, (UUID('14b0fdc4-c62b-413d-8287-1d50ec89f3a8'),), None), replacing it with newly flushed object.   Are there load operations occurring inside of an event handler within the flush?

| Package | Count |
|---------|-------|
| `invenio-jobs` | 1 |

#### Warning 43 - 1 occurrence

SAWarning: Identity map already had an identity for (<class 'invenio_jobs.models.Run'>, (UUID('15ae4b08-c977-45bb-9071-ff86689cb41f'),), None), replacing it with newly flushed object.   Are there load operations occurring inside of an event handler within the flush?

| Package | Count |
|---------|-------|
| `invenio-jobs` | 1 |

#### Warning 44 - 1 occurrence

SAWarning: Identity map already had an identity for (<class 'invenio_jobs.models.Run'>, (UUID('19ce8144-9614-4a67-ac5a-51669dee6d0d'),), None), replacing it with newly flushed object.   Are there load operations occurring inside of an event handler within the flush?

| Package | Count |
|---------|-------|
| `invenio-jobs` | 1 |

#### Warning 45 - 1 occurrence

SAWarning: Identity map already had an identity for (<class 'invenio_jobs.models.Run'>, (UUID('aa9d88f8-1860-4ed8-9c11-d4821fb51ab0'),), None), replacing it with newly flushed object.   Are there load operations occurring inside of an event handler within the flush?

| Package | Count |
|---------|-------|
| `invenio-jobs` | 1 |

#### Warning 46 - 1 occurrence

SAWarning: Identity map already had an identity for (<class 'invenio_jobs.models.Run'>, (UUID('d6c3561f-fd21-42d0-8f19-c97ed92d7acb'),), None), replacing it with newly flushed object.   Are there load operations occurring inside of an event handler within the flush?

| Package | Count |
|---------|-------|
| `invenio-jobs` | 1 |

#### Warning 47 - 1 occurrence

SAWarning: Identity map already had an identity for (<class 'invenio_jobs.models.Run'>, (UUID('dbbc86fe-25ed-404a-bacf-d87f55505f93'),), None), replacing it with newly flushed object.   Are there load operations occurring inside of an event handler within the flush?

| Package | Count |
|---------|-------|
| `invenio-jobs` | 1 |

#### Warning 48 - 1 occurrence

SAWarning: Identity map already had an identity for (<class 'invenio_jobs.models.Run'>, (UUID('f6060d3d-29d5-4be4-82db-ccc359d4933c'),), None), replacing it with newly flushed object.   Are there load operations occurring inside of an event handler within the flush?

| Package | Count |
|---------|-------|
| `invenio-jobs` | 1 |

#### Warning 49 - 1 occurrence

SAWarning: Object of type <ObjectVersion> not in session, add operation along 'Bucket.objects' will not proceed (This warning originated from the Session 'autoflush' process, which was invoked automatically in response to a user-initiated operation. Consider using ``no_autoflush`` context manager if this warning happened while initializing objects.)

| Package | Count |
|---------|-------|
| `invenio-drafts-resources` | 1 |

#### Warning 50 - 1 occurrence

SyntaxWarning: "is" with 'int' literal. Did you mean "=="?

| Package | Count |
|---------|-------|
| `invenio-records-rest` | 1 |

#### Warning 51 - 1 occurrence

SyntaxWarning: invalid escape sequence '\?'

| Package | Count |
|---------|-------|
| `invenio-records-rest` | 1 |

#### Warning 52 - 1 occurrence

UserWarning: Please specify the OAISERVER_ID_PREFIX configuration.default value is: oai:runnervmg1sw1:

| Package | Count |
|---------|-------|
| `invenio-oaiserver` | 1 |

#### Warning 53 - 1 occurrence

UserWarning: Using the in-memory storage for tracking rate limits as no storage was explicitly specified. This is not recommended for production use. See: https://flask-limiter.readthedocs.io#configuring-a-storage-backend for documentation about configuring the storage backend.

| Package | Count |
|---------|-------|
| `invenio-app` | 1 |

#### Warning 54 - 1 occurrence

UserWarning: autoincrement and existing_autoincrement only make sense for MySQL

| Package | Count |
|---------|-------|
| `invenio-audit-logs` | 1 |




---