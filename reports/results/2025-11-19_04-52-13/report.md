# Invenio Bugfix Verification Results

> **⏳ Status: Running** - This report is being updated as tests complete.

_Last updated: 2025-11-19 04:57:06 UTC_

## 📊 Overall Status

| Metric | Count |
|--------|-------|
| **Total Packages** | 37 |
| **Patched Packages** | 37 |
| **Unpatched Packages** | 0 |

### Patch Results
| Result | Count |
|--------|-------|
| ✅ Fixed | 0 |
| ❌ Regressions | 0 |
| ⚠️  Still Failing | 1 |
| ℹ️  No Change | 36 |

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
| `invenio-queues` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-queues/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-queues/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-queues/test-report-patched.xml) | ✅ Patch applied successfully, tests passed |
| `invenio-oauthclient` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-oauthclient/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-oauthclient/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-oauthclient/test-report-patched.xml)<br>[warnings](packages/invenio-oauthclient/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-cache` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-cache/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-cache/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-cache/test-report-patched.xml)<br>[warnings](packages/invenio-cache/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-notifications` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-notifications/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-notifications/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-notifications/test-report-patched.xml)<br>[warnings](packages/invenio-notifications/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-base` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-base/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-base/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-base/test-report-patched.xml)<br>[warnings](packages/invenio-base/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-app` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-app/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-app/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-app/test-report-patched.xml)<br>[warnings](packages/invenio-app/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-jobs` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-jobs/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-jobs/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-jobs/test-report-patched.xml)<br>[warnings](packages/invenio-jobs/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-theme` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-theme/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-theme/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-theme/test-report-patched.xml) | ✅ Patch applied successfully, tests passed |
| `invenio-assets` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-assets/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-assets/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-assets/test-report-patched.xml) | ✅ Patch applied successfully, tests passed |
| `invenio-celery` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-celery/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-celery/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-celery/test-report-patched.xml) | ✅ Patch applied successfully, tests passed |
| `invenio-pidstore` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-pidstore/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-pidstore/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-pidstore/test-report-patched.xml)<br>[warnings](packages/invenio-pidstore/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-db` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-db/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-db/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-db/test-report-patched.xml)<br>[warnings](packages/invenio-db/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-indexer` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-indexer/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-indexer/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-indexer/test-report-patched.xml)<br>[warnings](packages/invenio-indexer/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-drafts-resources` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-drafts-resources/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-drafts-resources/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-drafts-resources/test-report-patched.xml)<br>[warnings](packages/invenio-drafts-resources/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-access` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-access/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-access/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-access/test-report-patched.xml)<br>[warnings](packages/invenio-access/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-rest` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-rest/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-rest/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-rest/test-report-patched.xml)<br>[warnings](packages/invenio-rest/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-requests` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-requests/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-requests/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-requests/test-report-patched.xml)<br>[warnings](packages/invenio-requests/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-pages` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-pages/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-pages/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-pages/test-report-patched.xml)<br>[warnings](packages/invenio-pages/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-collections` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-collections/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-collections/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-collections/test-report-patched.xml)<br>[warnings](packages/invenio-collections/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-records-ui` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-records-ui/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-records-ui/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-records-ui/test-report-patched.xml)<br>[warnings](packages/invenio-records-ui/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-search-ui` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-search-ui/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-search-ui/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-search-ui/test-report-patched.xml) | ✅ Patch applied successfully, tests passed |
| `invenio-records-files` | pytest-invenio | ❌ Fail<br>[output](packages/invenio-records-files/test-output-original.txt)<br>[output-no-warnings](packages/invenio-records-files/test-output-no-warnings-original.txt) | ❌ Fail<br>[output](packages/invenio-records-files/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-records-files/test-output-no-warnings-patched.txt) | ⚠️ Tests still failing after patch |
| `invenio-logging` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-logging/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-logging/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-logging/test-report-patched.xml)<br>[warnings](packages/invenio-logging/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-sitemap` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-sitemap/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-sitemap/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-sitemap/test-report-patched.xml)<br>[warnings](packages/invenio-sitemap/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-formatter` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-formatter/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-formatter/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-formatter/test-report-patched.xml)<br>[warnings](packages/invenio-formatter/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-checks` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-checks/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-checks/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-checks/test-report-patched.xml)<br>[warnings](packages/invenio-checks/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-audit-logs` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-audit-logs/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-audit-logs/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-audit-logs/test-report-patched.xml)<br>[warnings](packages/invenio-audit-logs/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-records-rest` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-records-rest/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-records-rest/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-records-rest/test-report-patched.xml)<br>[warnings](packages/invenio-records-rest/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-administration` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-administration/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-administration/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-administration/test-report-patched.xml)<br>[warnings](packages/invenio-administration/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-github` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-github/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-github/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-github/test-report-patched.xml)<br>[warnings](packages/invenio-github/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-i18n` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-i18n/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-i18n/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-i18n/test-report-patched.xml) | ✅ Patch applied successfully, tests passed |
| `invenio-jsonschemas` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-jsonschemas/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-jsonschemas/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-jsonschemas/test-report-patched.xml)<br>[warnings](packages/invenio-jsonschemas/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-accounts` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-accounts/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-accounts/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-accounts/test-report-patched.xml)<br>[warnings](packages/invenio-accounts/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-webhooks` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-webhooks/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-webhooks/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-webhooks/test-report-patched.xml)<br>[warnings](packages/invenio-webhooks/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-records` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-records/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-records/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-records/test-report-patched.xml)<br>[warnings](packages/invenio-records/warnings-patched.md) | ✅ Patch applied successfully, tests passed |

## Collected Warnings

### Patched

#### Warning 1 - 109 occurrences

DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).

| Package | Count |
|---------|-------|
| `invenio-requests` | 15 |
| `invenio-accounts` | 13 |
| `invenio-oauthclient` | 8 |
| `invenio-drafts-resources` | 7 |
| `invenio-jobs` | 7 |
| `invenio-audit-logs` | 6 |
| `invenio-banners` | 6 |
| `invenio-collections` | 6 |
| `invenio-github` | 6 |
| `invenio-pages` | 6 |
| `invenio-records-ui` | 5 |
| `invenio-webhooks` | 5 |
| `invenio-access` | 3 |
| `invenio-administration` | 3 |
| `invenio-records` | 3 |
| `invenio-records-rest` | 3 |
| `invenio-indexer` | 2 |
| `invenio-pidstore` | 2 |
| `invenio-cache` | 1 |
| `invenio-formatter` | 1 |
| `invenio-rest` | 1 |

#### Warning 2 - 36 occurrences

SAWarning: nested transaction already deassociated from connection

| Package | Count |
|---------|-------|
| `invenio-records` | 21 |
| `invenio-pages` | 5 |
| `invenio-records-rest` | 4 |
| `invenio-collections` | 2 |
| `invenio-indexer` | 2 |
| `invenio-records-ui` | 1 |
| `invenio-requests` | 1 |

#### Warning 3 - 31 occurrences

DeprecationWarning: jsonschema.RefResolver is deprecated as of v4.18.0, in favor of the https://github.com/python-jsonschema/referencing library, which provides more compliant referencing behavior as well as more flexible APIs for customization. A future release will remove RefResolver. Please file a feature request (on referencing) if you are missing an API for the kind of customization you need.

| Package | Count |
|---------|-------|
| `invenio-collections` | 3 |
| `invenio-records-rest` | 3 |
| `invenio-administration` | 2 |
| `invenio-audit-logs` | 2 |
| `invenio-banners` | 2 |
| `invenio-checks` | 2 |
| `invenio-drafts-resources` | 2 |
| `invenio-indexer` | 2 |
| `invenio-jobs` | 2 |
| `invenio-notifications` | 2 |
| `invenio-pages` | 2 |
| `invenio-records` | 2 |
| `invenio-records-ui` | 2 |
| `invenio-requests` | 2 |
| `invenio-jsonschemas` | 1 |

#### Warning 4 - 30 occurrences

RemovedInMarshmallow4Warning: The `context` parameter is deprecated and will be removed in marshmallow 4.0. Use `contextvars.ContextVar` to pass context instead.

| Package | Count |
|---------|-------|
| `invenio-records-rest` | 8 |
| `invenio-jobs` | 4 |
| `invenio-audit-logs` | 3 |
| `invenio-collections` | 3 |
| `invenio-drafts-resources` | 3 |
| `invenio-requests` | 3 |
| `invenio-banners` | 2 |
| `invenio-checks` | 2 |
| `invenio-pages` | 2 |

#### Warning 5 - 20 occurrences

DeprecationWarning: Deprecated call to `pkg_resources.declare_namespace('fs')`.

| Package | Count |
|---------|-------|
| `invenio-administration` | 2 |
| `invenio-audit-logs` | 2 |
| `invenio-banners` | 2 |
| `invenio-checks` | 2 |
| `invenio-collections` | 2 |
| `invenio-drafts-resources` | 2 |
| `invenio-jobs` | 2 |
| `invenio-notifications` | 2 |
| `invenio-pages` | 2 |
| `invenio-requests` | 2 |

#### Warning 6 - 18 occurrences

DeprecationWarning: 'crypt' is deprecated and slated for removal in Python 3.13

| Package | Count |
|---------|-------|
| `invenio-access` | 1 |
| `invenio-accounts` | 1 |
| `invenio-administration` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-banners` | 1 |
| `invenio-checks` | 1 |
| `invenio-collections` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-github` | 1 |
| `invenio-jobs` | 1 |
| `invenio-notifications` | 1 |
| `invenio-oauthclient` | 1 |
| `invenio-pages` | 1 |
| `invenio-pidstore` | 1 |
| `invenio-records` | 1 |
| `invenio-records-ui` | 1 |
| `invenio-requests` | 1 |
| `invenio-webhooks` | 1 |

#### Warning 7 - 14 occurrences

DeprecationWarning: jsonschema.exceptions.RefResolutionError is deprecated as of version 4.18.0. If you wish to catch potential reference resolution errors, directly catch referencing.exceptions.Unresolvable.

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-banners` | 1 |
| `invenio-checks` | 1 |
| `invenio-collections` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-indexer` | 1 |
| `invenio-jobs` | 1 |
| `invenio-notifications` | 1 |
| `invenio-pages` | 1 |
| `invenio-records` | 1 |
| `invenio-records-rest` | 1 |
| `invenio-records-ui` | 1 |
| `invenio-requests` | 1 |

#### Warning 8 - 14 occurrences

PendingDeprecationWarning: Schema().dump().data and Schema().dump().errors as well as Schema().load().data and Schema().loads().dataattributes are deprecated in marshmallow v3.x.

| Package | Count |
|---------|-------|
| `invenio-records-rest` | 11 |
| `invenio-rest` | 3 |

#### Warning 9 - 13 occurrences

FutureWarning: CSRF validation will be enabled by default in the version 1.3.x

| Package | Count |
|---------|-------|
| `invenio-rest` | 2 |
| `invenio-accounts` | 1 |
| `invenio-administration` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-banners` | 1 |
| `invenio-collections` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-github` | 1 |
| `invenio-jobs` | 1 |
| `invenio-pages` | 1 |
| `invenio-records-rest` | 1 |
| `invenio-requests` | 1 |

#### Warning 10 - 13 occurrences

UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.

| Package | Count |
|---------|-------|
| `invenio-collections` | 2 |
| `invenio-accounts` | 1 |
| `invenio-administration` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-banners` | 1 |
| `invenio-checks` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-jobs` | 1 |
| `invenio-notifications` | 1 |
| `invenio-oauthclient` | 1 |
| `invenio-pages` | 1 |
| `invenio-requests` | 1 |

#### Warning 11 - 12 occurrences

DeprecationWarning: Deprecated call to `pkg_resources.declare_namespace('sphinxcontrib')`.

| Package | Count |
|---------|-------|
| `invenio-accounts` | 1 |
| `invenio-administration` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-banners` | 1 |
| `invenio-checks` | 1 |
| `invenio-collections` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-jobs` | 1 |
| `invenio-notifications` | 1 |
| `invenio-oauthclient` | 1 |
| `invenio-pages` | 1 |
| `invenio-requests` | 1 |

#### Warning 12 - 12 occurrences

DeprecationWarning: Using the initialization functions in flask_caching.backend is deprecated.  Use the a full path to backend classes directly.

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |
| `invenio-app` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-banners` | 1 |
| `invenio-cache` | 1 |
| `invenio-collections` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-github` | 1 |
| `invenio-jobs` | 1 |
| `invenio-pages` | 1 |
| `invenio-requests` | 1 |
| `invenio-sitemap` | 1 |

#### Warning 13 - 10 occurrences

DeprecationWarning: Deprecated call to `pkg_resources.declare_namespace('fs.opener')`.

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-banners` | 1 |
| `invenio-checks` | 1 |
| `invenio-collections` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-jobs` | 1 |
| `invenio-notifications` | 1 |
| `invenio-pages` | 1 |
| `invenio-requests` | 1 |

#### Warning 14 - 10 occurrences

DeprecationWarning: The '__version_info__' attribute is deprecated and will be removed in in a future version. Use feature detection or 'packaging.Version(importlib.metadata.version("marshmallow")).release' instead.

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-banners` | 1 |
| `invenio-checks` | 1 |
| `invenio-collections` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-jobs` | 1 |
| `invenio-notifications` | 1 |
| `invenio-pages` | 1 |
| `invenio-requests` | 1 |

#### Warning 15 - 10 occurrences

RemovedInMarshmallow4Warning: The 'default' argument to fields is deprecated. Use 'dump_default' instead.

| Package | Count |
|---------|-------|
| `invenio-checks` | 2 |
| `invenio-jobs` | 2 |
| `invenio-administration` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-banners` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-pages` | 1 |
| `invenio-requests` | 1 |

#### Warning 16 - 9 occurrences

DeprecationWarning: Link is deprecated and will be removed in v14.0. Use `ExternalLink` for third-party links and `EndpointLink` for InvenioRDM links.

| Package | Count |
|---------|-------|
| `invenio-audit-logs` | 1 |
| `invenio-banners` | 1 |
| `invenio-checks` | 1 |
| `invenio-collections` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-jobs` | 1 |
| `invenio-notifications` | 1 |
| `invenio-pages` | 1 |
| `invenio-requests` | 1 |

#### Warning 17 - 8 occurrences

DeprecationWarning: datetime.datetime.utcfromtimestamp() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.fromtimestamp(timestamp, datetime.UTC).

| Package | Count |
|---------|-------|
| `invenio-accounts` | 1 |
| `invenio-banners` | 1 |
| `invenio-github` | 1 |
| `invenio-oauthclient` | 1 |
| `invenio-pages` | 1 |
| `invenio-records-ui` | 1 |
| `invenio-requests` | 1 |
| `invenio-webhooks` | 1 |

#### Warning 18 - 6 occurrences

DeprecationWarning: distutils Version classes are deprecated. Use packaging.version instead.

| Package | Count |
|---------|-------|
| `invenio-accounts` | 2 |
| `invenio-collections` | 2 |
| `invenio-records-rest` | 2 |

#### Warning 19 - 6 occurrences

LegacyAPIWarning: The Query.get() method is considered legacy as of the 1.x series of SQLAlchemy and becomes a legacy construct in 2.0. The method is now available as Session.get() (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)

| Package | Count |
|---------|-------|
| `invenio-collections` | 2 |
| `invenio-webhooks` | 2 |
| `invenio-jobs` | 1 |
| `invenio-requests` | 1 |

#### Warning 20 - 5 occurrences

RemovedInMarshmallow4Warning: The 'missing' argument to fields is deprecated. Use 'load_default' instead.

| Package | Count |
|---------|-------|
| `invenio-records-rest` | 4 |
| `invenio-drafts-resources` | 1 |

#### Warning 21 - 4 occurrences

DeprecationWarning: Implicit imports (e.g., 'import idutils; idutils.function;') might be removed in the next major version. Please use explicit imports (e.g., 'from idutils import function;') instead.

| Package | Count |
|---------|-------|
| `invenio-checks` | 1 |
| `invenio-collections` | 1 |
| `invenio-pidstore` | 1 |
| `invenio-records-rest` | 1 |

#### Warning 22 - 4 occurrences

DeprecationWarning: No path_separator found in configuration; falling back to legacy splitting on spaces/commas for version_locations.  Consider adding path_separator=os to Alembic config.

| Package | Count |
|---------|-------|
| `invenio-access` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-db` | 1 |
| `invenio-requests` | 1 |

#### Warning 23 - 4 occurrences

DeprecationWarning: get_user method is deprecated, user get_user_by_email/get_user_by_id

| Package | Count |
|---------|-------|
| `invenio-accounts` | 1 |
| `invenio-banners` | 1 |
| `invenio-pages` | 1 |
| `invenio-webhooks` | 1 |

#### Warning 24 - 4 occurrences

PytestMockWarning: Mocks returned by pytest-mock do not need to be used as context managers. The mocker fixture automatically undoes mocking at the end of a test. This warning can be ignored if it was triggered by mocking a context manager. https://pytest-mock.readthedocs.io/en/latest/usage.html#usage-as-context-manager

| Package | Count |
|---------|-------|
| `invenio-cache` | 4 |

#### Warning 25 - 4 occurrences

SADeprecationWarning: The from_engine() method on Inspector is deprecated and will be removed in a future release.  Please use the sqlalchemy.inspect() function on an Engine or Connection in order to acquire an Inspector. (deprecated since: 1.4)

| Package | Count |
|---------|-------|
| `invenio-requests` | 2 |
| `invenio-access` | 1 |
| `invenio-audit-logs` | 1 |

#### Warning 26 - 3 occurrences

ChangedInMarshmallow4Warning: `Field` should not be instantiated. Use `fields.Raw` or  another field subclass instead.

| Package | Count |
|---------|-------|
| `invenio-checks` | 1 |
| `invenio-collections` | 1 |
| `invenio-jobs` | 1 |

#### Warning 27 - 3 occurrences

DeprecationWarning: The '__version__' attribute is deprecated and will be removed in in a future version. Use feature detection or 'importlib.metadata.version("marshmallow")' instead.

| Package | Count |
|---------|-------|
| `invenio-accounts` | 1 |
| `invenio-collections` | 1 |
| `invenio-records-rest` | 1 |

#### Warning 28 - 3 occurrences

UserWarning: autoincrement and existing_autoincrement only make sense for MySQL

| Package | Count |
|---------|-------|
| `invenio-access` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-requests` | 1 |

#### Warning 29 - 2 occurrences

DeprecationWarning: Remember me support has been removed.

| Package | Count |
|---------|-------|
| `invenio-audit-logs` | 1 |
| `invenio-requests` | 1 |

#### Warning 30 - 2 occurrences

DeprecationWarning: The 'warn' method is deprecated, use 'warning' instead

| Package | Count |
|---------|-------|
| `invenio-drafts-resources` | 1 |
| `invenio-logging` | 1 |

#### Warning 31 - 2 occurrences

DeprecationWarning: The patch() method is deprecated and will be removed.

| Package | Count |
|---------|-------|
| `invenio-records` | 1 |
| `invenio-records-rest` | 1 |

#### Warning 32 - 2 occurrences

PytestConfigWarning: Unknown config option: pep8ignore

| Package | Count |
|---------|-------|
| `invenio-jsonschemas` | 1 |
| `invenio-records-ui` | 1 |

#### Warning 33 - 2 occurrences

PytestDeprecationWarning: @pytest.yield_fixture is deprecated.

| Package | Count |
|---------|-------|
| `invenio-pidstore` | 2 |

#### Warning 34 - 2 occurrences

SAWarning: On mapper Mapper[RecordMetadataVersion(records_metadata_version)], primary key column 'records_metadata_version.transaction_id' is being combined with distinct primary key column 'records_metadata_version.transaction_id' in attribute 'transaction_id'. Use explicit properties to give each column its own mapped attribute name. (This warning originated from the `configure_mappers()` process, which was invoked automatically in response to a user-initiated operation.)

| Package | Count |
|---------|-------|
| `invenio-records` | 2 |

#### Warning 35 - 2 occurrences

UserWarning: Set configuration variable SECRET_KEY with random string

| Package | Count |
|---------|-------|
| `invenio-app` | 1 |
| `invenio-records-rest` | 1 |

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

DeprecationWarning: Please use hash_password instead of encrypt_password.

| Package | Count |
|---------|-------|
| `invenio-records-ui` | 1 |

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

DeprecationWarning: The 'record_to_index' function is no longer expected to return a tuple (index, doc_type), instead it should only return the index. Support for the tuple will be removed in a future version of 'invenio-indexer'.

| Package | Count |
|---------|-------|
| `invenio-drafts-resources` | 1 |

#### Warning 47 - 1 occurrence

DeprecationWarning: The cern contrib is deprecated. Please use the generic keycloak instead.

| Package | Count |
|---------|-------|
| `invenio-oauthclient` | 1 |

#### Warning 48 - 1 occurrence

DeprecationWarning: The configuration value 'RDM_FILES_DEFAULT_MAX_FILE_SIZE' is not set. In future, please set it explicitly to define your max file size, or be aware that the default value used i.e. FILES_REST_DEFAULT_MAX_FILE_SIZE will be 10 * (10**9) (10 GB).

| Package | Count |
|---------|-------|
| `invenio-collections` | 1 |

#### Warning 49 - 1 occurrence

DeprecationWarning: The configuration value 'RDM_FILES_DEFAULT_QUOTA_SIZE' is not set. In future, please set it explicitly to define your quota size, or be aware that the default value used i.e. FILES_REST_DEFAULT_QUOTA_SIZE will be 10 * (10**9) (10 GB).

| Package | Count |
|---------|-------|
| `invenio-collections` | 1 |

#### Warning 50 - 1 occurrence

DeprecationWarning: The post_load hook must take a positional argument data.

| Package | Count |
|---------|-------|
| `invenio-records` | 1 |

#### Warning 51 - 1 occurrence

DeprecationWarning: The pre_dump hook must take a positional argument data.

| Package | Count |
|---------|-------|
| `invenio-records` | 1 |

#### Warning 52 - 1 occurrence

DeprecationWarning: `es_clear` fixture is deprecated, use `search_clear` instead.

| Package | Count |
|---------|-------|
| `invenio-requests` | 1 |

#### Warning 53 - 1 occurrence

DeprecationWarning: passing settings to invenio_aes_encrypted_email.hash() is deprecated, and won't be supported in Passlib 2.0; use 'invenio_aes_encrypted_email.using(**settings).hash(secret)' instead

| Package | Count |
|---------|-------|
| `invenio-accounts` | 1 |

#### Warning 54 - 1 occurrence

DeprecationWarning: subject_nested is deprecated. Use subject_combined instead.

| Package | Count |
|---------|-------|
| `invenio-collections` | 1 |

#### Warning 55 - 1 occurrence

DeprecationWarning: the method passlib.context.CryptContext.encrypt() is deprecated as of Passlib 1.7, and will be removed in Passlib 2.0, use CryptContext.hash() instead.

| Package | Count |
|---------|-------|
| `invenio-accounts` | 1 |

#### Warning 56 - 1 occurrence

PendingDeprecationWarning: The WSGI_PROXIES configuration is deprecated and it will be removed, use PROXYFIX_CONFIG instead

| Package | Count |
|---------|-------|
| `invenio-base` | 1 |

#### Warning 57 - 1 occurrence

PendingDeprecationWarning: This feature is deprecated.

| Package | Count |
|---------|-------|
| `invenio-logging` | 1 |

#### Warning 58 - 1 occurrence

PytestCollectionWarning: cannot collect test class 'TestAction' because it has a __init__ constructor (from: tests/customizations/test_request_types.py)

| Package | Count |
|---------|-------|
| `invenio-requests` | 1 |

#### Warning 59 - 1 occurrence

PytestCollectionWarning: cannot collect test class 'TestCustomView' because it has a __init__ constructor (from: tests/test_base.py)

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |

#### Warning 60 - 1 occurrence

PytestCollectionWarning: cannot collect test class 'TestSchema' because it has a __init__ constructor (from: tests/test_marshmallow_utils.py)

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |

#### Warning 61 - 1 occurrence

RemovedInMarshmallow4Warning: Passing field metadata as keyword arguments is deprecated. Use the explicit `metadata=...` argument instead. Additional metadata: {'load_from': 'from'}

| Package | Count |
|---------|-------|
| `invenio-records-rest` | 1 |

#### Warning 62 - 1 occurrence

RemovedInMarshmallow4Warning: `Field.fail` is deprecated. Use `raise self.make_error("required", ...)` instead.

| Package | Count |
|---------|-------|
| `invenio-records-rest` | 1 |

#### Warning 63 - 1 occurrence

RuntimeWarning: Results are not stored in backend and should not be retrieved when task_always_eager is enabled, unless task_store_eager_result is enabled.

| Package | Count |
|---------|-------|
| `invenio-webhooks` | 1 |

#### Warning 64 - 1 occurrence

RuntimeWarning: You are overriding the default OAuthlib "URL encoded" set of valid characters. Make sure that the characters defined in oauthlib.common.urlencoded are indeed limitting your needs.

| Package | Count |
|---------|-------|
| `invenio-webhooks` | 1 |

#### Warning 65 - 1 occurrence

SADeprecationWarning: Query.values() is deprecated and will be removed in a future release.  Please use Query.with_entities() (deprecated since: 1.4)

| Package | Count |
|---------|-------|
| `invenio-indexer` | 1 |

#### Warning 66 - 1 occurrence

SAWarning: Identity map already had an identity for (<class 'invenio_jobs.models.Run'>, (UUID('2c8808d1-1a54-4ca4-8d9b-37698fa040ca'),), None), replacing it with newly flushed object.   Are there load operations occurring inside of an event handler within the flush?

| Package | Count |
|---------|-------|
| `invenio-jobs` | 1 |

#### Warning 67 - 1 occurrence

SAWarning: Identity map already had an identity for (<class 'invenio_jobs.models.Run'>, (UUID('4e3e679e-886e-4a51-8d79-f0f7b7b9087d'),), None), replacing it with newly flushed object.   Are there load operations occurring inside of an event handler within the flush?

| Package | Count |
|---------|-------|
| `invenio-jobs` | 1 |

#### Warning 68 - 1 occurrence

SAWarning: Identity map already had an identity for (<class 'invenio_jobs.models.Run'>, (UUID('6a04af80-813c-40ce-b332-35d55229a933'),), None), replacing it with newly flushed object.   Are there load operations occurring inside of an event handler within the flush?

| Package | Count |
|---------|-------|
| `invenio-jobs` | 1 |

#### Warning 69 - 1 occurrence

SAWarning: Identity map already had an identity for (<class 'invenio_jobs.models.Run'>, (UUID('6fa776c7-b7f9-45d5-b247-d1f759897b83'),), None), replacing it with newly flushed object.   Are there load operations occurring inside of an event handler within the flush?

| Package | Count |
|---------|-------|
| `invenio-jobs` | 1 |

#### Warning 70 - 1 occurrence

SAWarning: Identity map already had an identity for (<class 'invenio_jobs.models.Run'>, (UUID('7d0f8e37-8c26-4037-9f79-58be9b9ee2a2'),), None), replacing it with newly flushed object.   Are there load operations occurring inside of an event handler within the flush?

| Package | Count |
|---------|-------|
| `invenio-jobs` | 1 |

#### Warning 71 - 1 occurrence

SAWarning: Identity map already had an identity for (<class 'invenio_jobs.models.Run'>, (UUID('d4f1fd6c-860b-441d-a61e-8d05a6894273'),), None), replacing it with newly flushed object.   Are there load operations occurring inside of an event handler within the flush?

| Package | Count |
|---------|-------|
| `invenio-jobs` | 1 |

#### Warning 72 - 1 occurrence

SAWarning: Identity map already had an identity for (<class 'invenio_jobs.models.Run'>, (UUID('ed9a7020-2b65-4f9d-85c8-840038869bb9'),), None), replacing it with newly flushed object.   Are there load operations occurring inside of an event handler within the flush?

| Package | Count |
|---------|-------|
| `invenio-jobs` | 1 |

#### Warning 73 - 1 occurrence

SAWarning: Object of type <ObjectVersion> not in session, add operation along 'Bucket.objects' will not proceed (This warning originated from the Session 'autoflush' process, which was invoked automatically in response to a user-initiated operation. Consider using ``no_autoflush`` context manager if this warning happened while initializing objects.)

| Package | Count |
|---------|-------|
| `invenio-drafts-resources` | 1 |

#### Warning 74 - 1 occurrence

SAWarning: This declarative base already contains a class with the same class name and module name as sqlalchemy_continuum.model_builder.RecordMetadataVersion, and will be replaced in the string-lookup table. (This warning originated from the `configure_mappers()` process, which was invoked automatically in response to a user-initiated operation.)

| Package | Count |
|---------|-------|
| `invenio-records` | 1 |

#### Warning 75 - 1 occurrence

SAWarning: relationship 'RecordMetadataVersion.transaction' will copy column transaction.id to column records_metadata_version.transaction_id, which conflicts with relationship(s): 'RecordMetadataVersion.transaction' (copies transaction.id to records_metadata_version.transaction_id), 'RecordMetadataVersion.transaction' (copies transaction.id to records_metadata_version.transaction_id), 'RecordMetadataVersion.transaction' (copies transaction.id to records_metadata_version.transaction_id), 'RecordMetadataVersion.transaction' (copies transaction.id to records_metadata_version.transaction_id). If this is not the intention, consider if these relationships should be linked with back_populates, or if viewonly=True should be applied to one or more if they are read-only. For the less common case that foreign key constraints are partially overlapping, the orm.foreign() annotation can be used to isolate the columns that should be written towards.   To silence this warning, add the parameter 'overlaps="transaction,transaction,transaction,transaction"' to the 'RecordMetadataVersion.transaction' relationship. (Background on this warning at: https://sqlalche.me/e/20/qzyx) (This warning originated from the `configure_mappers()` process, which was invoked automatically in response to a user-initiated operation.)

| Package | Count |
|---------|-------|
| `invenio-records` | 1 |

#### Warning 76 - 1 occurrence

SAWarning: relationship 'RecordMetadataVersion.transaction' will copy column transaction.id to column records_metadata_version.transaction_id, which conflicts with relationship(s): 'RecordMetadataVersion.transaction' (copies transaction.id to records_metadata_version.transaction_id), 'RecordMetadataVersion.transaction' (copies transaction.id to records_metadata_version.transaction_id), 'RecordMetadataVersion.transaction' (copies transaction.id to records_metadata_version.transaction_id). If this is not the intention, consider if these relationships should be linked with back_populates, or if viewonly=True should be applied to one or more if they are read-only. For the less common case that foreign key constraints are partially overlapping, the orm.foreign() annotation can be used to isolate the columns that should be written towards.   To silence this warning, add the parameter 'overlaps="transaction,transaction,transaction"' to the 'RecordMetadataVersion.transaction' relationship. (Background on this warning at: https://sqlalche.me/e/20/qzyx) (This warning originated from the `configure_mappers()` process, which was invoked automatically in response to a user-initiated operation.)

| Package | Count |
|---------|-------|
| `invenio-records` | 1 |

#### Warning 77 - 1 occurrence

SAWarning: relationship 'RecordMetadataVersion.transaction' will copy column transaction.id to column records_metadata_version.transaction_id, which conflicts with relationship(s): 'RecordMetadataVersion.transaction' (copies transaction.id to records_metadata_version.transaction_id), 'RecordMetadataVersion.transaction' (copies transaction.id to records_metadata_version.transaction_id). If this is not the intention, consider if these relationships should be linked with back_populates, or if viewonly=True should be applied to one or more if they are read-only. For the less common case that foreign key constraints are partially overlapping, the orm.foreign() annotation can be used to isolate the columns that should be written towards.   To silence this warning, add the parameter 'overlaps="transaction,transaction"' to the 'RecordMetadataVersion.transaction' relationship. (Background on this warning at: https://sqlalche.me/e/20/qzyx) (This warning originated from the `configure_mappers()` process, which was invoked automatically in response to a user-initiated operation.)

| Package | Count |
|---------|-------|
| `invenio-records` | 1 |

#### Warning 78 - 1 occurrence

SAWarning: relationship 'RecordMetadataVersion.transaction' will copy column transaction.id to column records_metadata_version.transaction_id, which conflicts with relationship(s): 'RecordMetadataVersion.transaction' (copies transaction.id to records_metadata_version.transaction_id). If this is not the intention, consider if these relationships should be linked with back_populates, or if viewonly=True should be applied to one or more if they are read-only. For the less common case that foreign key constraints are partially overlapping, the orm.foreign() annotation can be used to isolate the columns that should be written towards.   To silence this warning, add the parameter 'overlaps="transaction"' to the 'RecordMetadataVersion.transaction' relationship. (Background on this warning at: https://sqlalche.me/e/20/qzyx) (This warning originated from the `configure_mappers()` process, which was invoked automatically in response to a user-initiated operation.)

| Package | Count |
|---------|-------|
| `invenio-records` | 1 |

#### Warning 79 - 1 occurrence

SyntaxWarning: "is" with 'int' literal. Did you mean "=="?

| Package | Count |
|---------|-------|
| `invenio-records-rest` | 1 |

#### Warning 80 - 1 occurrence

SyntaxWarning: invalid escape sequence '\?'

| Package | Count |
|---------|-------|
| `invenio-records-rest` | 1 |

#### Warning 81 - 1 occurrence

UserWarning: Please specify the OAISERVER_ID_PREFIX configuration.default value is: oai:runnervmg1sw1:

| Package | Count |
|---------|-------|
| `invenio-collections` | 1 |

#### Warning 82 - 1 occurrence

UserWarning: Test

| Package | Count |
|---------|-------|
| `invenio-base` | 1 |

#### Warning 83 - 1 occurrence

UserWarning: Using the in-memory storage for tracking rate limits as no storage was explicitly specified. This is not recommended for production use. See: https://flask-limiter.readthedocs.io#configuring-a-storage-backend for documentation about configuring the storage backend.

| Package | Count |
|---------|-------|
| `invenio-app` | 1 |




---