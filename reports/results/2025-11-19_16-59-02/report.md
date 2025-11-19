# Invenio Bugfix Verification Results

> **⏳ Status: Running** - This report is being updated as tests complete.

_Last updated: 2025-11-19 17:02:57 UTC_

## 📊 Overall Status

| Metric | Count |
|--------|-------|
| **Total Packages** | 23 |
| **Patched Packages** | 23 |
| **Unpatched Packages** | 0 |

### Patch Results
| Result | Count |
|--------|-------|
| ✅ Fixed | 22 |
| ❌ Regressions | 0 |
| ⚠️  Still Failing | 1 |
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
| `invenio-banners` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-banners/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-banners/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-banners/test-report-patched.xml)<br>[warnings](packages/invenio-banners/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-mail` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-mail/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-mail/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-mail/test-report-patched.xml) | ✅ Patch applied successfully, tests passed |
| `invenio-config` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-config/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-config/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-config/test-report-patched.xml)<br>[warnings](packages/invenio-config/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-cache` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-cache/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-cache/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-cache/test-report-patched.xml)<br>[warnings](packages/invenio-cache/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-base` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-base/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-base/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-base/test-report-patched.xml)<br>[warnings](packages/invenio-base/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-app` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-app/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-app/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-app/test-report-patched.xml)<br>[warnings](packages/invenio-app/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-assets` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-assets/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-assets/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-assets/test-report-patched.xml) | ✅ Patch applied successfully, tests passed |
| `invenio-celery` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-celery/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-celery/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-celery/test-report-patched.xml) | ✅ Patch applied successfully, tests passed |
| `invenio-pidstore` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-pidstore/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-pidstore/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-pidstore/test-report-patched.xml)<br>[warnings](packages/invenio-pidstore/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-db` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-db/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-db/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-db/test-report-patched.xml)<br>[warnings](packages/invenio-db/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-indexer` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-indexer/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-indexer/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-indexer/test-report-patched.xml)<br>[warnings](packages/invenio-indexer/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-drafts-resources` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-drafts-resources/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-drafts-resources/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-drafts-resources/test-report-patched.xml)<br>[warnings](packages/invenio-drafts-resources/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-rest` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-rest/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-rest/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-rest/test-report-patched.xml)<br>[warnings](packages/invenio-rest/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-pages` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-pages/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-pages/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-pages/test-report-patched.xml)<br>[warnings](packages/invenio-pages/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-stats` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-stats/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-stats/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-stats/test-report-patched.xml)<br>[warnings](packages/invenio-stats/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-search-ui` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-search-ui/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-search-ui/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-search-ui/test-report-patched.xml) | ✅ Patch applied successfully, tests passed |
| `invenio-records-files` | pytest-invenio | ❌ Fail<br>[output](packages/invenio-records-files/test-output-original.txt)<br>[output-no-warnings](packages/invenio-records-files/test-output-no-warnings-original.txt) | ❌ Fail<br>[output](packages/invenio-records-files/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-records-files/test-output-no-warnings-patched.txt) | ⚠️ Tests still failing after patch |
| `invenio-logging` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-logging/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-logging/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-logging/test-report-patched.xml)<br>[warnings](packages/invenio-logging/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-formatter` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-formatter/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-formatter/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-formatter/test-report-patched.xml)<br>[warnings](packages/invenio-formatter/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-administration` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-administration/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-administration/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-administration/test-report-patched.xml)<br>[warnings](packages/invenio-administration/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-github` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-github/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-github/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-github/test-report-patched.xml)<br>[warnings](packages/invenio-github/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-i18n` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-i18n/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-i18n/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-i18n/test-report-patched.xml) | ✅ Patch applied successfully, tests passed |
| `invenio-oauth2server` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-oauth2server/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-oauth2server/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-oauth2server/test-report-patched.xml)<br>[warnings](packages/invenio-oauth2server/warnings-patched.md) | ✅ Patch applied successfully, tests passed |

## Collected Warnings

### Patched

#### Warning 1 - 56 occurrences

DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).

| Package | Count |
|---------|-------|
| `invenio-stats` | 11 |
| `invenio-oauth2server` | 10 |
| `invenio-drafts-resources` | 7 |
| `invenio-banners` | 6 |
| `invenio-github` | 6 |
| `invenio-pages` | 6 |
| `invenio-administration` | 3 |
| `invenio-indexer` | 2 |
| `invenio-pidstore` | 2 |
| `invenio-cache` | 1 |
| `invenio-formatter` | 1 |
| `invenio-rest` | 1 |

#### Warning 2 - 12 occurrences

DeprecationWarning: jsonschema.RefResolver is deprecated as of v4.18.0, in favor of the https://github.com/python-jsonschema/referencing library, which provides more compliant referencing behavior as well as more flexible APIs for customization. A future release will remove RefResolver. Please file a feature request (on referencing) if you are missing an API for the kind of customization you need.

| Package | Count |
|---------|-------|
| `invenio-administration` | 2 |
| `invenio-banners` | 2 |
| `invenio-drafts-resources` | 2 |
| `invenio-indexer` | 2 |
| `invenio-pages` | 2 |
| `invenio-stats` | 2 |

#### Warning 3 - 8 occurrences

DeprecationWarning: 'crypt' is deprecated and slated for removal in Python 3.13

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |
| `invenio-banners` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-github` | 1 |
| `invenio-oauth2server` | 1 |
| `invenio-pages` | 1 |
| `invenio-pidstore` | 1 |
| `invenio-stats` | 1 |

#### Warning 4 - 8 occurrences

DeprecationWarning: Deprecated call to `pkg_resources.declare_namespace('fs')`.

| Package | Count |
|---------|-------|
| `invenio-administration` | 2 |
| `invenio-banners` | 2 |
| `invenio-drafts-resources` | 2 |
| `invenio-pages` | 2 |

#### Warning 5 - 8 occurrences

DeprecationWarning: Using the initialization functions in flask_caching.backend is deprecated.  Use the a full path to backend classes directly.

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |
| `invenio-app` | 1 |
| `invenio-banners` | 1 |
| `invenio-cache` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-github` | 1 |
| `invenio-pages` | 1 |
| `invenio-stats` | 1 |

#### Warning 6 - 8 occurrences

FutureWarning: CSRF validation will be enabled by default in the version 1.3.x

| Package | Count |
|---------|-------|
| `invenio-rest` | 2 |
| `invenio-administration` | 1 |
| `invenio-banners` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-github` | 1 |
| `invenio-pages` | 1 |
| `invenio-stats` | 1 |

#### Warning 7 - 8 occurrences

SAWarning: nested transaction already deassociated from connection

| Package | Count |
|---------|-------|
| `invenio-pages` | 5 |
| `invenio-indexer` | 2 |
| `invenio-stats` | 1 |

#### Warning 8 - 7 occurrences

RemovedInMarshmallow4Warning: The `context` parameter is deprecated and will be removed in marshmallow 4.0. Use `contextvars.ContextVar` to pass context instead.

| Package | Count |
|---------|-------|
| `invenio-drafts-resources` | 3 |
| `invenio-banners` | 2 |
| `invenio-pages` | 2 |

#### Warning 9 - 6 occurrences

DeprecationWarning: jsonschema.exceptions.RefResolutionError is deprecated as of version 4.18.0. If you wish to catch potential reference resolution errors, directly catch referencing.exceptions.Unresolvable.

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |
| `invenio-banners` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-indexer` | 1 |
| `invenio-pages` | 1 |
| `invenio-stats` | 1 |

#### Warning 10 - 5 occurrences

DeprecationWarning: Deprecated call to `pkg_resources.declare_namespace('sphinxcontrib')`.

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |
| `invenio-banners` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-pages` | 1 |
| `invenio-pidstore` | 1 |

#### Warning 11 - 5 occurrences

DeprecationWarning: datetime.datetime.utcfromtimestamp() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.fromtimestamp(timestamp, datetime.UTC).

| Package | Count |
|---------|-------|
| `invenio-banners` | 1 |
| `invenio-github` | 1 |
| `invenio-oauth2server` | 1 |
| `invenio-pages` | 1 |
| `invenio-stats` | 1 |

#### Warning 12 - 5 occurrences

UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |
| `invenio-banners` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-pages` | 1 |
| `invenio-pidstore` | 1 |

#### Warning 13 - 4 occurrences

DeprecationWarning: Deprecated call to `pkg_resources.declare_namespace('fs.opener')`.

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |
| `invenio-banners` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-pages` | 1 |

#### Warning 14 - 4 occurrences

DeprecationWarning: The '__version_info__' attribute is deprecated and will be removed in in a future version. Use feature detection or 'packaging.Version(importlib.metadata.version("marshmallow")).release' instead.

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |
| `invenio-banners` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-pages` | 1 |

#### Warning 15 - 4 occurrences

DeprecationWarning: get_user method is deprecated, user get_user_by_email/get_user_by_id

| Package | Count |
|---------|-------|
| `invenio-banners` | 1 |
| `invenio-oauth2server` | 1 |
| `invenio-pages` | 1 |
| `invenio-stats` | 1 |

#### Warning 16 - 4 occurrences

PytestMockWarning: Mocks returned by pytest-mock do not need to be used as context managers. The mocker fixture automatically undoes mocking at the end of a test. This warning can be ignored if it was triggered by mocking a context manager. https://pytest-mock.readthedocs.io/en/latest/usage.html#usage-as-context-manager

| Package | Count |
|---------|-------|
| `invenio-cache` | 4 |

#### Warning 17 - 4 occurrences

RemovedInMarshmallow4Warning: The 'default' argument to fields is deprecated. Use 'dump_default' instead.

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |
| `invenio-banners` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-pages` | 1 |

#### Warning 18 - 3 occurrences

DeprecationWarning: Link is deprecated and will be removed in v14.0. Use `ExternalLink` for third-party links and `EndpointLink` for InvenioRDM links.

| Package | Count |
|---------|-------|
| `invenio-banners` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-pages` | 1 |

#### Warning 19 - 3 occurrences

DeprecationWarning: The 'warn' method is deprecated, use 'warning' instead

| Package | Count |
|---------|-------|
| `invenio-drafts-resources` | 1 |
| `invenio-logging` | 1 |
| `invenio-oauth2server` | 1 |

#### Warning 20 - 3 occurrences

PendingDeprecationWarning: Schema().dump().data and Schema().dump().errors as well as Schema().load().data and Schema().loads().dataattributes are deprecated in marshmallow v3.x.

| Package | Count |
|---------|-------|
| `invenio-rest` | 3 |

#### Warning 21 - 2 occurrences

PytestDeprecationWarning: @pytest.yield_fixture is deprecated.

| Package | Count |
|---------|-------|
| `invenio-pidstore` | 2 |

#### Warning 22 - 2 occurrences

SAWarning: Object of type <Client> not in session, add operation along 'User.oauth2clients' will not proceed (This warning originated from the Session 'autoflush' process, which was invoked automatically in response to a user-initiated operation. Consider using ``no_autoflush`` context manager if this warning happened while initializing objects.)

| Package | Count |
|---------|-------|
| `invenio-oauth2server` | 2 |

#### Warning 23 - 2 occurrences

UserWarning: Set configuration variable SECRET_KEY with random string

| Package | Count |
|---------|-------|
| `invenio-app` | 1 |
| `invenio-config` | 1 |

#### Warning 24 - 1 occurrence

DeprecationWarning: Deprecated call to `pkg_resources.declare_namespace('flask_admin')`.

| Package | Count |
|---------|-------|
| `invenio-pidstore` | 1 |

#### Warning 25 - 1 occurrence

DeprecationWarning: Deprecated call to `pkg_resources.declare_namespace('flask_admin.contrib')`.

| Package | Count |
|---------|-------|
| `invenio-pidstore` | 1 |

#### Warning 26 - 1 occurrence

DeprecationWarning: Implicit imports (e.g., 'import idutils; idutils.function;') might be removed in the next major version. Please use explicit imports (e.g., 'from idutils import function;') instead.

| Package | Count |
|---------|-------|
| `invenio-pidstore` | 1 |

#### Warning 27 - 1 occurrence

DeprecationWarning: No path_separator found in configuration; falling back to legacy splitting on spaces/commas for version_locations.  Consider adding path_separator=os to Alembic config.

| Package | Count |
|---------|-------|
| `invenio-db` | 1 |

#### Warning 28 - 1 occurrence

DeprecationWarning: The 'record_to_index' function is no longer expected to return a tuple (index, doc_type), instead it should only return the index. Support for the tuple will be removed in a future version of 'invenio-indexer'.

| Package | Count |
|---------|-------|
| `invenio-drafts-resources` | 1 |

#### Warning 29 - 1 occurrence

PendingDeprecationWarning: The WSGI_PROXIES configuration is deprecated and it will be removed, use PROXYFIX_CONFIG instead

| Package | Count |
|---------|-------|
| `invenio-base` | 1 |

#### Warning 30 - 1 occurrence

PendingDeprecationWarning: This feature is deprecated.

| Package | Count |
|---------|-------|
| `invenio-logging` | 1 |

#### Warning 31 - 1 occurrence

PytestCollectionWarning: cannot collect test class 'TestCustomView' because it has a __init__ constructor (from: tests/test_base.py)

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |

#### Warning 32 - 1 occurrence

PytestCollectionWarning: cannot collect test class 'TestSchema' because it has a __init__ constructor (from: tests/test_marshmallow_utils.py)

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |

#### Warning 33 - 1 occurrence

RemovedInMarshmallow4Warning: The 'missing' argument to fields is deprecated. Use 'load_default' instead.

| Package | Count |
|---------|-------|
| `invenio-drafts-resources` | 1 |

#### Warning 34 - 1 occurrence

RuntimeWarning: You are overriding the default OAuthlib "URL encoded" set of valid characters. Make sure that the characters defined in oauthlib.common.urlencoded are indeed limitting your needs.

| Package | Count |
|---------|-------|
| `invenio-oauth2server` | 1 |

#### Warning 35 - 1 occurrence

SADeprecationWarning: Query.values() is deprecated and will be removed in a future release.  Please use Query.with_entities() (deprecated since: 1.4)

| Package | Count |
|---------|-------|
| `invenio-indexer` | 1 |

#### Warning 36 - 1 occurrence

SAWarning: Object of type <Client> not in session, add operation along 'User.oauth2clients' will not proceed

| Package | Count |
|---------|-------|
| `invenio-oauth2server` | 1 |

#### Warning 37 - 1 occurrence

SAWarning: Object of type <ObjectVersion> not in session, add operation along 'Bucket.objects' will not proceed (This warning originated from the Session 'autoflush' process, which was invoked automatically in response to a user-initiated operation. Consider using ``no_autoflush`` context manager if this warning happened while initializing objects.)

| Package | Count |
|---------|-------|
| `invenio-drafts-resources` | 1 |

#### Warning 38 - 1 occurrence

SAWarning: Object of type <Token> not in session, add operation along 'User.oauth2tokens' will not proceed

| Package | Count |
|---------|-------|
| `invenio-oauth2server` | 1 |

#### Warning 39 - 1 occurrence

UserWarning: Test

| Package | Count |
|---------|-------|
| `invenio-base` | 1 |

#### Warning 40 - 1 occurrence

UserWarning: Using the in-memory storage for tracking rate limits as no storage was explicitly specified. This is not recommended for production use. See: https://flask-limiter.readthedocs.io#configuring-a-storage-backend for documentation about configuring the storage backend.

| Package | Count |
|---------|-------|
| `invenio-app` | 1 |




---