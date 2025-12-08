# Invenio Bugfix Verification Results

> **⏳ Status: Running** - This report is being updated as tests complete.

_Last updated: 2025-12-08 19:05:55 UTC_

## 📊 Overall Status

| Metric | Count |
|--------|-------|
| **Total Packages** | 27 |
| **Patched Packages** | 27 |
| **Unpatched Packages** | 0 |

### Patch Results
| Result | Count |
|--------|-------|
| ✅ Fixed | 24 |
| ❌ Regressions | 2 |
| ⚠️  Still Failing | 1 |
| ℹ️  No Change | 0 |

## 🔧 Configured Patches

| Patched Package | Repository | Branch |
|----------------|------------|--------|
| [pytest-invenio](https://github.com/max-moser/invenio-records-resources/tree/mm/failed-file-upload-cleanup) | https://github.com/max-moser/invenio-records-resources | mm/failed-file-upload-cleanup |

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
| `invenio-config` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-config/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-config/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-config/test-report-patched.xml)<br>[warnings](packages/invenio-config/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-queues` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-queues/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-queues/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-queues/test-report-patched.xml) | ✅ Patch applied successfully, tests passed |
| `invenio-base` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-base/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-base/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-base/test-report-patched.xml)<br>[warnings](packages/invenio-base/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-app` | pytest-invenio | ✅ Pass<br>[output](packages/invenio-app/test-output-original.txt)<br>[output-no-warnings](packages/invenio-app/test-output-no-warnings-original.txt)<br>[xml](packages/invenio-app/test-report-original.xml)<br>[warnings](packages/invenio-app/warnings-original.md) | ❌ Fail<br>[output](packages/invenio-app/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-app/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-app/test-report-patched.xml)<br>[warnings](packages/invenio-app/warnings-patched.md) | ❌ Patch introduced test failures |
| `invenio-assets` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-assets/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-assets/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-assets/test-report-patched.xml) | ✅ Patch applied successfully, tests passed |
| `invenio-indexer` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-indexer/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-indexer/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-indexer/test-report-patched.xml)<br>[warnings](packages/invenio-indexer/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-oaiserver` | pytest-invenio | ✅ Pass<br>[output](packages/invenio-oaiserver/test-output-original.txt)<br>[output-no-warnings](packages/invenio-oaiserver/test-output-no-warnings-original.txt)<br>[xml](packages/invenio-oaiserver/test-report-original.xml)<br>[warnings](packages/invenio-oaiserver/warnings-original.md) | ❌ Fail<br>[output](packages/invenio-oaiserver/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-oaiserver/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-oaiserver/test-report-patched.xml)<br>[warnings](packages/invenio-oaiserver/warnings-patched.md) | ❌ Patch introduced test failures |
| `invenio-drafts-resources` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-drafts-resources/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-drafts-resources/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-drafts-resources/test-report-patched.xml)<br>[warnings](packages/invenio-drafts-resources/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-access` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-access/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-access/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-access/test-report-patched.xml)<br>[warnings](packages/invenio-access/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-rest` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-rest/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-rest/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-rest/test-report-patched.xml)<br>[warnings](packages/invenio-rest/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-requests` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-requests/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-requests/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-requests/test-report-patched.xml)<br>[warnings](packages/invenio-requests/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-records-permissions` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-records-permissions/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-records-permissions/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-records-permissions/test-report-patched.xml)<br>[warnings](packages/invenio-records-permissions/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-collections` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-collections/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-collections/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-collections/test-report-patched.xml)<br>[warnings](packages/invenio-collections/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-userprofiles` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-userprofiles/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-userprofiles/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-userprofiles/test-report-patched.xml)<br>[warnings](packages/invenio-userprofiles/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-search-ui` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-search-ui/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-search-ui/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-search-ui/test-report-patched.xml) | ✅ Patch applied successfully, tests passed |
| `invenio-records-files` | pytest-invenio | ❌ Fail<br>[output](packages/invenio-records-files/test-output-original.txt)<br>[output-no-warnings](packages/invenio-records-files/test-output-no-warnings-original.txt) | ❌ Fail<br>[output](packages/invenio-records-files/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-records-files/test-output-no-warnings-patched.txt) | ⚠️ Tests still failing after patch |
| `invenio-logging` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-logging/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-logging/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-logging/test-report-patched.xml)<br>[warnings](packages/invenio-logging/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-sitemap` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-sitemap/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-sitemap/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-sitemap/test-report-patched.xml)<br>[warnings](packages/invenio-sitemap/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-formatter` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-formatter/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-formatter/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-formatter/test-report-patched.xml)<br>[warnings](packages/invenio-formatter/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-checks` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-checks/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-checks/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-checks/test-report-patched.xml)<br>[warnings](packages/invenio-checks/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-audit-logs` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-audit-logs/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-audit-logs/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-audit-logs/test-report-patched.xml)<br>[warnings](packages/invenio-audit-logs/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-records-resources` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-records-resources/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-records-resources/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-records-resources/test-report-patched.xml)<br>[warnings](packages/invenio-records-resources/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-github` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-github/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-github/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-github/test-report-patched.xml)<br>[warnings](packages/invenio-github/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-i18n` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-i18n/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-i18n/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-i18n/test-report-patched.xml) | ✅ Patch applied successfully, tests passed |
| `invenio-search` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-search/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-search/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-search/test-report-patched.xml) | ✅ Patch applied successfully, tests passed |
| `invenio-accounts` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-accounts/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-accounts/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-accounts/test-report-patched.xml)<br>[warnings](packages/invenio-accounts/warnings-patched.md) | ✅ Patch applied successfully, tests passed |

## Collected Warnings

### Patched

#### Warning 1 - 81 occurrences

DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).

| Package | Count |
|---------|-------|
| `invenio-requests` | 15 |
| `invenio-accounts` | 13 |
| `invenio-drafts-resources` | 7 |
| `invenio-records-resources` | 7 |
| `invenio-audit-logs` | 6 |
| `invenio-banners` | 6 |
| `invenio-collections` | 6 |
| `invenio-github` | 6 |
| `invenio-userprofiles` | 5 |
| `invenio-access` | 3 |
| `invenio-records-permissions` | 3 |
| `invenio-indexer` | 2 |
| `invenio-formatter` | 1 |
| `invenio-rest` | 1 |

#### Warning 2 - 21 occurrences

DeprecationWarning: jsonschema.RefResolver is deprecated as of v4.18.0, in favor of the https://github.com/python-jsonschema/referencing library, which provides more compliant referencing behavior as well as more flexible APIs for customization. A future release will remove RefResolver. Please file a feature request (on referencing) if you are missing an API for the kind of customization you need.

| Package | Count |
|---------|-------|
| `invenio-collections` | 3 |
| `invenio-audit-logs` | 2 |
| `invenio-banners` | 2 |
| `invenio-checks` | 2 |
| `invenio-drafts-resources` | 2 |
| `invenio-indexer` | 2 |
| `invenio-oaiserver` | 2 |
| `invenio-records-permissions` | 2 |
| `invenio-records-resources` | 2 |
| `invenio-requests` | 2 |

#### Warning 3 - 19 occurrences

RemovedInMarshmallow4Warning: The `context` parameter is deprecated and will be removed in marshmallow 4.0. Use `contextvars.ContextVar` to pass context instead.

| Package | Count |
|---------|-------|
| `invenio-audit-logs` | 3 |
| `invenio-collections` | 3 |
| `invenio-drafts-resources` | 3 |
| `invenio-records-resources` | 3 |
| `invenio-requests` | 3 |
| `invenio-banners` | 2 |
| `invenio-checks` | 2 |

#### Warning 4 - 14 occurrences

DeprecationWarning: Deprecated call to `pkg_resources.declare_namespace('fs')`.

| Package | Count |
|---------|-------|
| `invenio-audit-logs` | 2 |
| `invenio-banners` | 2 |
| `invenio-checks` | 2 |
| `invenio-collections` | 2 |
| `invenio-drafts-resources` | 2 |
| `invenio-records-resources` | 2 |
| `invenio-requests` | 2 |

#### Warning 5 - 13 occurrences

DeprecationWarning: 'crypt' is deprecated and slated for removal in Python 3.13

| Package | Count |
|---------|-------|
| `invenio-access` | 1 |
| `invenio-accounts` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-banners` | 1 |
| `invenio-checks` | 1 |
| `invenio-collections` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-github` | 1 |
| `invenio-oaiserver` | 1 |
| `invenio-records-permissions` | 1 |
| `invenio-records-resources` | 1 |
| `invenio-requests` | 1 |
| `invenio-userprofiles` | 1 |

#### Warning 6 - 11 occurrences

FutureWarning: CSRF validation will be enabled by default in the version 1.3.x

| Package | Count |
|---------|-------|
| `invenio-rest` | 2 |
| `invenio-accounts` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-banners` | 1 |
| `invenio-collections` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-github` | 1 |
| `invenio-records-permissions` | 1 |
| `invenio-records-resources` | 1 |
| `invenio-requests` | 1 |

#### Warning 7 - 11 occurrences

UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.

| Package | Count |
|---------|-------|
| `invenio-collections` | 2 |
| `invenio-access` | 1 |
| `invenio-accounts` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-banners` | 1 |
| `invenio-checks` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-oaiserver` | 1 |
| `invenio-records-resources` | 1 |
| `invenio-requests` | 1 |

#### Warning 8 - 10 occurrences

DeprecationWarning: Deprecated call to `pkg_resources.declare_namespace('sphinxcontrib')`.

| Package | Count |
|---------|-------|
| `invenio-access` | 1 |
| `invenio-accounts` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-banners` | 1 |
| `invenio-checks` | 1 |
| `invenio-collections` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-oaiserver` | 1 |
| `invenio-records-resources` | 1 |
| `invenio-requests` | 1 |

#### Warning 9 - 10 occurrences

DeprecationWarning: Using the initialization functions in flask_caching.backend is deprecated.  Use the a full path to backend classes directly.

| Package | Count |
|---------|-------|
| `invenio-app` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-banners` | 1 |
| `invenio-collections` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-github` | 1 |
| `invenio-records-permissions` | 1 |
| `invenio-records-resources` | 1 |
| `invenio-requests` | 1 |
| `invenio-sitemap` | 1 |

#### Warning 10 - 10 occurrences

DeprecationWarning: jsonschema.exceptions.RefResolutionError is deprecated as of version 4.18.0. If you wish to catch potential reference resolution errors, directly catch referencing.exceptions.Unresolvable.

| Package | Count |
|---------|-------|
| `invenio-audit-logs` | 1 |
| `invenio-banners` | 1 |
| `invenio-checks` | 1 |
| `invenio-collections` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-indexer` | 1 |
| `invenio-oaiserver` | 1 |
| `invenio-records-permissions` | 1 |
| `invenio-records-resources` | 1 |
| `invenio-requests` | 1 |

#### Warning 11 - 7 occurrences

DeprecationWarning: Deprecated call to `pkg_resources.declare_namespace('fs.opener')`.

| Package | Count |
|---------|-------|
| `invenio-audit-logs` | 1 |
| `invenio-banners` | 1 |
| `invenio-checks` | 1 |
| `invenio-collections` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-records-resources` | 1 |
| `invenio-requests` | 1 |

#### Warning 12 - 7 occurrences

DeprecationWarning: Link is deprecated and will be removed in v14.0. Use `ExternalLink` for third-party links and `EndpointLink` for InvenioRDM links.

| Package | Count |
|---------|-------|
| `invenio-audit-logs` | 1 |
| `invenio-banners` | 1 |
| `invenio-checks` | 1 |
| `invenio-collections` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-records-resources` | 1 |
| `invenio-requests` | 1 |

#### Warning 13 - 7 occurrences

DeprecationWarning: The '__version_info__' attribute is deprecated and will be removed in in a future version. Use feature detection or 'packaging.Version(importlib.metadata.version("marshmallow")).release' instead.

| Package | Count |
|---------|-------|
| `invenio-audit-logs` | 1 |
| `invenio-banners` | 1 |
| `invenio-checks` | 1 |
| `invenio-collections` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-records-resources` | 1 |
| `invenio-requests` | 1 |

#### Warning 14 - 7 occurrences

RemovedInMarshmallow4Warning: The 'default' argument to fields is deprecated. Use 'dump_default' instead.

| Package | Count |
|---------|-------|
| `invenio-checks` | 2 |
| `invenio-audit-logs` | 1 |
| `invenio-banners` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-records-resources` | 1 |
| `invenio-requests` | 1 |

#### Warning 15 - 6 occurrences

DeprecationWarning: distutils Version classes are deprecated. Use packaging.version instead.

| Package | Count |
|---------|-------|
| `invenio-accounts` | 2 |
| `invenio-collections` | 2 |
| `invenio-oaiserver` | 2 |

#### Warning 16 - 5 occurrences

DeprecationWarning: datetime.datetime.utcfromtimestamp() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.fromtimestamp(timestamp, datetime.UTC).

| Package | Count |
|---------|-------|
| `invenio-accounts` | 1 |
| `invenio-banners` | 1 |
| `invenio-github` | 1 |
| `invenio-requests` | 1 |
| `invenio-userprofiles` | 1 |

#### Warning 17 - 5 occurrences

LegacyAPIWarning: The Query.get() method is considered legacy as of the 1.x series of SQLAlchemy and becomes a legacy construct in 2.0. The method is now available as Session.get() (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)

| Package | Count |
|---------|-------|
| `invenio-collections` | 2 |
| `invenio-accounts` | 1 |
| `invenio-records-resources` | 1 |
| `invenio-requests` | 1 |

#### Warning 18 - 5 occurrences

SAWarning: nested transaction already deassociated from connection

| Package | Count |
|---------|-------|
| `invenio-collections` | 2 |
| `invenio-indexer` | 2 |
| `invenio-requests` | 1 |

#### Warning 19 - 4 occurrences

SADeprecationWarning: The from_engine() method on Inspector is deprecated and will be removed in a future release.  Please use the sqlalchemy.inspect() function on an Engine or Connection in order to acquire an Inspector. (deprecated since: 1.4)

| Package | Count |
|---------|-------|
| `invenio-requests` | 2 |
| `invenio-access` | 1 |
| `invenio-audit-logs` | 1 |

#### Warning 20 - 3 occurrences

DeprecationWarning: Deprecated call to `pkg_resources.declare_namespace('flask_admin')`.

| Package | Count |
|---------|-------|
| `invenio-access` | 1 |
| `invenio-accounts` | 1 |
| `invenio-oaiserver` | 1 |

#### Warning 21 - 3 occurrences

DeprecationWarning: Deprecated call to `pkg_resources.declare_namespace('flask_admin.contrib')`.

| Package | Count |
|---------|-------|
| `invenio-access` | 1 |
| `invenio-accounts` | 1 |
| `invenio-oaiserver` | 1 |

#### Warning 22 - 3 occurrences

DeprecationWarning: No path_separator found in configuration; falling back to legacy splitting on spaces/commas for version_locations.  Consider adding path_separator=os to Alembic config.

| Package | Count |
|---------|-------|
| `invenio-access` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-requests` | 1 |

#### Warning 23 - 3 occurrences

DeprecationWarning: The '__version__' attribute is deprecated and will be removed in in a future version. Use feature detection or 'importlib.metadata.version("marshmallow")' instead.

| Package | Count |
|---------|-------|
| `invenio-accounts` | 1 |
| `invenio-collections` | 1 |
| `invenio-oaiserver` | 1 |

#### Warning 24 - 3 occurrences

DeprecationWarning: The 'warn' method is deprecated, use 'warning' instead

| Package | Count |
|---------|-------|
| `invenio-drafts-resources` | 1 |
| `invenio-logging` | 1 |
| `invenio-records-resources` | 1 |

#### Warning 25 - 3 occurrences

PendingDeprecationWarning: Schema().dump().data and Schema().dump().errors as well as Schema().load().data and Schema().loads().dataattributes are deprecated in marshmallow v3.x.

| Package | Count |
|---------|-------|
| `invenio-rest` | 3 |

#### Warning 26 - 3 occurrences

UserWarning: autoincrement and existing_autoincrement only make sense for MySQL

| Package | Count |
|---------|-------|
| `invenio-access` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-requests` | 1 |

#### Warning 27 - 2 occurrences

ChangedInMarshmallow4Warning: `Field` should not be instantiated. Use `fields.Raw` or  another field subclass instead.

| Package | Count |
|---------|-------|
| `invenio-checks` | 1 |
| `invenio-collections` | 1 |

#### Warning 28 - 2 occurrences

DeprecationWarning: Implicit imports (e.g., 'import idutils; idutils.function;') might be removed in the next major version. Please use explicit imports (e.g., 'from idutils import function;') instead.

| Package | Count |
|---------|-------|
| `invenio-checks` | 1 |
| `invenio-collections` | 1 |

#### Warning 29 - 2 occurrences

DeprecationWarning: Remember me support has been removed.

| Package | Count |
|---------|-------|
| `invenio-audit-logs` | 1 |
| `invenio-requests` | 1 |

#### Warning 30 - 2 occurrences

DeprecationWarning: The 'record_to_index' function is no longer expected to return a tuple (index, doc_type), instead it should only return the index. Support for the tuple will be removed in a future version of 'invenio-indexer'.

| Package | Count |
|---------|-------|
| `invenio-drafts-resources` | 1 |
| `invenio-records-resources` | 1 |

#### Warning 31 - 2 occurrences

DeprecationWarning: get_user method is deprecated, user get_user_by_email/get_user_by_id

| Package | Count |
|---------|-------|
| `invenio-accounts` | 1 |
| `invenio-banners` | 1 |

#### Warning 32 - 2 occurrences

RemovedInMarshmallow4Warning: The 'missing' argument to fields is deprecated. Use 'load_default' instead.

| Package | Count |
|---------|-------|
| `invenio-drafts-resources` | 1 |
| `invenio-records-resources` | 1 |

#### Warning 33 - 2 occurrences

SAWarning: Object of type <ObjectVersion> not in session, add operation along 'Bucket.objects' will not proceed (This warning originated from the Session 'autoflush' process, which was invoked automatically in response to a user-initiated operation. Consider using ``no_autoflush`` context manager if this warning happened while initializing objects.)

| Package | Count |
|---------|-------|
| `invenio-drafts-resources` | 1 |
| `invenio-records-resources` | 1 |

#### Warning 34 - 2 occurrences

UserWarning: Please specify the OAISERVER_ID_PREFIX configuration.default value is: oai:runnervmoqczp:

| Package | Count |
|---------|-------|
| `invenio-collections` | 1 |
| `invenio-oaiserver` | 1 |

#### Warning 35 - 2 occurrences

UserWarning: Set configuration variable SECRET_KEY with random string

| Package | Count |
|---------|-------|
| `invenio-app` | 1 |
| `invenio-config` | 1 |

#### Warning 36 - 1 occurrence

DeprecationWarning: CryptContext.hash(): 'scheme' keyword is deprecated as of Passlib 1.7, and will be removed in Passlib 2.0

| Package | Count |
|---------|-------|
| `invenio-accounts` | 1 |

#### Warning 37 - 1 occurrence

DeprecationWarning: DynamicPermission is scheduled for removal.

| Package | Count |
|---------|-------|
| `invenio-access` | 1 |

#### Warning 38 - 1 occurrence

DeprecationWarning: Flags should be stored in dicts and not in tuples. The next version of WTForms will abandon support for flags in tuples.

| Package | Count |
|---------|-------|
| `invenio-accounts` | 1 |

#### Warning 39 - 1 occurrence

DeprecationWarning: Please use the new command allow-action-for-role instead.

| Package | Count |
|---------|-------|
| `invenio-access` | 1 |

#### Warning 40 - 1 occurrence

DeprecationWarning: Please use the new command allow-action-for-user instead.

| Package | Count |
|---------|-------|
| `invenio-access` | 1 |

#### Warning 41 - 1 occurrence

DeprecationWarning: Please use the new command deny-action-for-role instead.

| Package | Count |
|---------|-------|
| `invenio-access` | 1 |

#### Warning 42 - 1 occurrence

DeprecationWarning: Please use the new command deny-action-for-user instead.

| Package | Count |
|---------|-------|
| `invenio-access` | 1 |

#### Warning 43 - 1 occurrence

DeprecationWarning: Please use the new command remove-action-from-role instead.

| Package | Count |
|---------|-------|
| `invenio-access` | 1 |

#### Warning 44 - 1 occurrence

DeprecationWarning: Please use the new command remove-action-from-user instead.

| Package | Count |
|---------|-------|
| `invenio-access` | 1 |

#### Warning 45 - 1 occurrence

DeprecationWarning: Please use the new command remove-action-global instead.

| Package | Count |
|---------|-------|
| `invenio-access` | 1 |

#### Warning 46 - 1 occurrence

DeprecationWarning: The configuration value 'RDM_FILES_DEFAULT_MAX_FILE_SIZE' is not set. In future, please set it explicitly to define your max file size, or be aware that the default value used i.e. FILES_REST_DEFAULT_MAX_FILE_SIZE will be 10 * (10**9) (10 GB).

| Package | Count |
|---------|-------|
| `invenio-collections` | 1 |

#### Warning 47 - 1 occurrence

DeprecationWarning: The configuration value 'RDM_FILES_DEFAULT_QUOTA_SIZE' is not set. In future, please set it explicitly to define your quota size, or be aware that the default value used i.e. FILES_REST_DEFAULT_QUOTA_SIZE will be 10 * (10**9) (10 GB).

| Package | Count |
|---------|-------|
| `invenio-collections` | 1 |

#### Warning 48 - 1 occurrence

DeprecationWarning: `es_clear` fixture is deprecated, use `search_clear` instead.

| Package | Count |
|---------|-------|
| `invenio-requests` | 1 |

#### Warning 49 - 1 occurrence

DeprecationWarning: current_userprofile is deprecated, use current_user instead

| Package | Count |
|---------|-------|
| `invenio-userprofiles` | 1 |

#### Warning 50 - 1 occurrence

DeprecationWarning: passing settings to invenio_aes_encrypted_email.hash() is deprecated, and won't be supported in Passlib 2.0; use 'invenio_aes_encrypted_email.using(**settings).hash(secret)' instead

| Package | Count |
|---------|-------|
| `invenio-accounts` | 1 |

#### Warning 51 - 1 occurrence

DeprecationWarning: subject_nested is deprecated. Use subject_combined instead.

| Package | Count |
|---------|-------|
| `invenio-collections` | 1 |

#### Warning 52 - 1 occurrence

DeprecationWarning: the method passlib.context.CryptContext.encrypt() is deprecated as of Passlib 1.7, and will be removed in Passlib 2.0, use CryptContext.hash() instead.

| Package | Count |
|---------|-------|
| `invenio-accounts` | 1 |

#### Warning 53 - 1 occurrence

PendingDeprecationWarning: The WSGI_PROXIES configuration is deprecated and it will be removed, use PROXYFIX_CONFIG instead

| Package | Count |
|---------|-------|
| `invenio-base` | 1 |

#### Warning 54 - 1 occurrence

PendingDeprecationWarning: This feature is deprecated.

| Package | Count |
|---------|-------|
| `invenio-logging` | 1 |

#### Warning 55 - 1 occurrence

PytestCollectionWarning: cannot collect test class 'TestAction' because it has a __init__ constructor (from: tests/customizations/test_request_types.py)

| Package | Count |
|---------|-------|
| `invenio-requests` | 1 |

#### Warning 56 - 1 occurrence

PytestCollectionWarning: cannot collect test class 'TestPermissionPolicy' because it has a __init__ constructor (from: tests/test_permissions_base.py)

| Package | Count |
|---------|-------|
| `invenio-records-permissions` | 1 |

#### Warning 57 - 1 occurrence

SADeprecationWarning: Query.values() is deprecated and will be removed in a future release.  Please use Query.with_entities() (deprecated since: 1.4)

| Package | Count |
|---------|-------|
| `invenio-indexer` | 1 |

#### Warning 58 - 1 occurrence

SAWarning: This declarative base already contains a class with the same class name and module name as invenio_records_resources.factories.factory.MyRecordMetadata, and will be replaced in the string-lookup table.

| Package | Count |
|---------|-------|
| `invenio-records-resources` | 1 |

#### Warning 59 - 1 occurrence

UserWarning: Test

| Package | Count |
|---------|-------|
| `invenio-base` | 1 |

#### Warning 60 - 1 occurrence

UserWarning: Using the in-memory storage for tracking rate limits as no storage was explicitly specified. This is not recommended for production use. See: https://flask-limiter.readthedocs.io#configuring-a-storage-backend for documentation about configuring the storage backend.

| Package | Count |
|---------|-------|
| `invenio-app` | 1 |


### Original

#### Warning 1 - 5 occurrences

DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).

| Package | Count |
|---------|-------|
| `invenio-oaiserver` | 5 |

#### Warning 2 - 5 occurrences

SAWarning: nested transaction already deassociated from connection

| Package | Count |
|---------|-------|
| `invenio-oaiserver` | 5 |

#### Warning 3 - 4 occurrences

PendingDeprecationWarning: Schema().dump().data and Schema().dump().errors as well as Schema().load().data and Schema().loads().dataattributes are deprecated in marshmallow v3.x.

| Package | Count |
|---------|-------|
| `invenio-oaiserver` | 4 |

#### Warning 4 - 2 occurrences

DeprecationWarning: distutils Version classes are deprecated. Use packaging.version instead.

| Package | Count |
|---------|-------|
| `invenio-oaiserver` | 2 |

#### Warning 5 - 2 occurrences

DeprecationWarning: jsonschema.RefResolver is deprecated as of v4.18.0, in favor of the https://github.com/python-jsonschema/referencing library, which provides more compliant referencing behavior as well as more flexible APIs for customization. A future release will remove RefResolver. Please file a feature request (on referencing) if you are missing an API for the kind of customization you need.

| Package | Count |
|---------|-------|
| `invenio-oaiserver` | 2 |

#### Warning 6 - 1 occurrence

DeprecationWarning: 'crypt' is deprecated and slated for removal in Python 3.13

| Package | Count |
|---------|-------|
| `invenio-oaiserver` | 1 |

#### Warning 7 - 1 occurrence

DeprecationWarning: Deprecated call to `pkg_resources.declare_namespace('flask_admin')`.

| Package | Count |
|---------|-------|
| `invenio-oaiserver` | 1 |

#### Warning 8 - 1 occurrence

DeprecationWarning: Deprecated call to `pkg_resources.declare_namespace('flask_admin.contrib')`.

| Package | Count |
|---------|-------|
| `invenio-oaiserver` | 1 |

#### Warning 9 - 1 occurrence

DeprecationWarning: Deprecated call to `pkg_resources.declare_namespace('sphinxcontrib')`.

| Package | Count |
|---------|-------|
| `invenio-oaiserver` | 1 |

#### Warning 10 - 1 occurrence

DeprecationWarning: The '__version__' attribute is deprecated and will be removed in in a future version. Use feature detection or 'importlib.metadata.version("marshmallow")' instead.

| Package | Count |
|---------|-------|
| `invenio-oaiserver` | 1 |

#### Warning 11 - 1 occurrence

DeprecationWarning: Using the initialization functions in flask_caching.backend is deprecated.  Use the a full path to backend classes directly.

| Package | Count |
|---------|-------|
| `invenio-app` | 1 |

#### Warning 12 - 1 occurrence

DeprecationWarning: jsonschema.exceptions.RefResolutionError is deprecated as of version 4.18.0. If you wish to catch potential reference resolution errors, directly catch referencing.exceptions.Unresolvable.

| Package | Count |
|---------|-------|
| `invenio-oaiserver` | 1 |

#### Warning 13 - 1 occurrence

LegacyAPIWarning: The Query.get() method is considered legacy as of the 1.x series of SQLAlchemy and becomes a legacy construct in 2.0. The method is now available as Session.get() (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)

| Package | Count |
|---------|-------|
| `invenio-oaiserver` | 1 |

#### Warning 14 - 1 occurrence

UserWarning: Please specify the OAISERVER_ID_PREFIX configuration.default value is: oai:runnervmoqczp:

| Package | Count |
|---------|-------|
| `invenio-oaiserver` | 1 |

#### Warning 15 - 1 occurrence

UserWarning: Set configuration variable SECRET_KEY with random string

| Package | Count |
|---------|-------|
| `invenio-app` | 1 |

#### Warning 16 - 1 occurrence

UserWarning: Using the in-memory storage for tracking rate limits as no storage was explicitly specified. This is not recommended for production use. See: https://flask-limiter.readthedocs.io#configuring-a-storage-backend for documentation about configuring the storage backend.

| Package | Count |
|---------|-------|
| `invenio-app` | 1 |

#### Warning 17 - 1 occurrence

UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.

| Package | Count |
|---------|-------|
| `invenio-oaiserver` | 1 |




---