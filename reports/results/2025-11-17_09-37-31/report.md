# Invenio Bugfix Verification Results

_Last updated: 2025-11-17 09:37:32 UTC_

## 📊 Overall Status

| Metric | Count |
|--------|-------|
| **Total Packages** | 52 |
| **Patched Packages** | 49 |
| **Unpatched Packages** | 3 |

### Patch Results
| Result | Count |
|--------|-------|
| ✅ Fixed | 0 |
| ❌ Regressions | 1 |
| ⚠️  Still Failing | 8 |
| ℹ️  No Change | 40 |

## 🔧 Configured Patches

| Patched Package | Repository | Branch |
|----------------|------------|--------|
| [pytest-invenio](https://github.com/oarepo/pytest-invenio/tree/nested-db-session-rollback) | https://github.com/oarepo/pytest-invenio | nested-db-session-rollback |
| [invenio-files-rest](https://github.com/fenekku/invenio-files-res/tree/support_3.14) | https://github.com/fenekku/invenio-files-res | support_3.14 |

## 🔄 Patched Packages

| Package | Patches Applied | Original | Patched | Result |
|---------|----------------|--------|-------|--------|
| `invenio-files-rest` <br/> [original](packages/invenio-files-rest/test-output-original.txt) [patched](packages/invenio-files-rest/test-output-patched.txt) [xml-original](packages/invenio-files-rest/test-report-original.xml) [xml-patched](packages/invenio-files-rest/test-report-patched.xml) [warnings-original](packages/invenio-files-rest/warnings-original.md) [warnings-patched](packages/invenio-files-rest/warnings-patched.md) | pytest-invenio | ❌ Fail | ❌ Fail | ⚠️ Tests still failing after patch |

## 📦 Packages that do not depend on patched packages

| Package | Build Status |
|---------|--------------|
| `invenio-rdm-records` | ⏭️  Skipped |
| `invenio-pages` | ⏭️  Skipped |
| `invenio-vocabularies` | ⏭️  Skipped |

## 🔄 Packages that depend on patched packages

| Package | Patches Applied | Original | Patched | Result |
|---------|----------------|--------|-------|--------|
| `invenio-banners` <br/> [patched](packages/invenio-banners/test-output-patched.txt) [warnings-patched](packages/invenio-banners/warnings-patched.md) | pytest-invenio invenio-files-rest | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-mail` <br/> [patched](packages/invenio-mail/test-output-patched.txt) [warnings-patched](packages/invenio-mail/warnings-patched.md) | pytest-invenio | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-config` <br/> [patched](packages/invenio-config/test-output-patched.txt) [warnings-patched](packages/invenio-config/warnings-patched.md) | pytest-invenio | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-queues` <br/> [patched](packages/invenio-queues/test-output-patched.txt) | pytest-invenio | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-oauthclient` <br/> [patched](packages/invenio-oauthclient/test-output-patched.txt) [xml-patched](packages/invenio-oauthclient/test-report-patched.xml) [warnings-patched](packages/invenio-oauthclient/warnings-patched.md) | pytest-invenio | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-cache` <br/> [patched](packages/invenio-cache/test-output-patched.txt) [warnings-patched](packages/invenio-cache/warnings-patched.md) | pytest-invenio | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-notifications` <br/> [patched](packages/invenio-notifications/test-output-patched.txt) [warnings-patched](packages/invenio-notifications/warnings-patched.md) | pytest-invenio invenio-files-rest | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-base` <br/> [patched](packages/invenio-base/test-output-patched.txt) [warnings-patched](packages/invenio-base/warnings-patched.md) | pytest-invenio | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-app` <br/> [patched](packages/invenio-app/test-output-patched.txt) [warnings-patched](packages/invenio-app/warnings-patched.md) | pytest-invenio | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-jobs` <br/> [patched](packages/invenio-jobs/test-output-patched.txt) [warnings-patched](packages/invenio-jobs/warnings-patched.md) | pytest-invenio invenio-files-rest | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-theme` <br/> [patched](packages/invenio-theme/test-output-patched.txt) | pytest-invenio | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-assets` <br/> [patched](packages/invenio-assets/test-output-patched.txt) | pytest-invenio | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-celery` <br/> [patched](packages/invenio-celery/test-output-patched.txt) | pytest-invenio | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-pidstore` <br/> [patched](packages/invenio-pidstore/test-output-patched.txt) [warnings-patched](packages/invenio-pidstore/warnings-patched.md) | pytest-invenio | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-db` <br/> [patched](packages/invenio-db/test-output-patched.txt) | pytest-invenio | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-indexer` <br/> [patched](packages/invenio-indexer/test-output-patched.txt) [warnings-patched](packages/invenio-indexer/warnings-patched.md) | pytest-invenio | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-oaiserver` <br/> [patched](packages/invenio-oaiserver/test-output-patched.txt) [warnings-patched](packages/invenio-oaiserver/warnings-patched.md) | pytest-invenio | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-drafts-resources` <br/> [original](packages/invenio-drafts-resources/test-output-original.txt) [patched](packages/invenio-drafts-resources/test-output-patched.txt) [xml-original](packages/invenio-drafts-resources/test-report-original.xml) [xml-patched](packages/invenio-drafts-resources/test-report-patched.xml) [warnings-original](packages/invenio-drafts-resources/warnings-original.md) [warnings-patched](packages/invenio-drafts-resources/warnings-patched.md) | pytest-invenio invenio-files-rest | ✅ Pass | ❌ Fail | ❌ Patch introduced test failures |
| `invenio-access` <br/> [original](packages/invenio-access/test-output-original.txt) [patched](packages/invenio-access/test-output-patched.txt) [xml-original](packages/invenio-access/test-report-original.xml) [xml-patched](packages/invenio-access/test-report-patched.xml) [warnings-original](packages/invenio-access/warnings-original.md) [warnings-patched](packages/invenio-access/warnings-patched.md) | pytest-invenio | ❌ Fail | ❌ Fail | ⚠️ Tests still failing after patch |
| `invenio-rest` <br/> [patched](packages/invenio-rest/test-output-patched.txt) [warnings-patched](packages/invenio-rest/warnings-patched.md) | pytest-invenio | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-requests` <br/> [original](packages/invenio-requests/test-output-original.txt) [patched](packages/invenio-requests/test-output-patched.txt) [xml-original](packages/invenio-requests/test-report-original.xml) [xml-patched](packages/invenio-requests/test-report-patched.xml) [warnings-original](packages/invenio-requests/warnings-original.md) [warnings-patched](packages/invenio-requests/warnings-patched.md) | pytest-invenio invenio-files-rest | ❌ Fail | ❌ Fail | ⚠️ Tests still failing after patch |
| `invenio-records-permissions` <br/> [patched](packages/invenio-records-permissions/test-output-patched.txt) [warnings-patched](packages/invenio-records-permissions/warnings-patched.md) | pytest-invenio | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-app-rdm` <br/> [patched](packages/invenio-app-rdm/test-output-patched.txt) [xml-patched](packages/invenio-app-rdm/test-report-patched.xml) [warnings-patched](packages/invenio-app-rdm/warnings-patched.md) | pytest-invenio invenio-files-rest | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-collections` <br/> [patched](packages/invenio-collections/test-output-patched.txt) [xml-patched](packages/invenio-collections/test-report-patched.xml) [warnings-patched](packages/invenio-collections/warnings-patched.md) | pytest-invenio invenio-files-rest | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-records-ui` <br/> [patched](packages/invenio-records-ui/test-output-patched.txt) [warnings-patched](packages/invenio-records-ui/warnings-patched.md) | pytest-invenio | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-stats` <br/> [original](packages/invenio-stats/test-output-original.txt) [patched](packages/invenio-stats/test-output-patched.txt) [warnings-original](packages/invenio-stats/warnings-original.md) [warnings-patched](packages/invenio-stats/warnings-patched.md) | pytest-invenio invenio-files-rest | ❌ Fail | ❌ Fail | ⚠️ Tests still failing after patch |
| `invenio-userprofiles` <br/> [patched](packages/invenio-userprofiles/test-output-patched.txt) [xml-patched](packages/invenio-userprofiles/test-report-patched.xml) [warnings-patched](packages/invenio-userprofiles/warnings-patched.md) | pytest-invenio | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-previewer` <br/> [patched](packages/invenio-previewer/test-output-patched.txt) [warnings-patched](packages/invenio-previewer/warnings-patched.md) | pytest-invenio invenio-files-rest | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-communities` <br/> [patched](packages/invenio-communities/test-output-patched.txt) [xml-patched](packages/invenio-communities/test-report-patched.xml) [warnings-patched](packages/invenio-communities/warnings-patched.md) | pytest-invenio invenio-files-rest | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-search-ui` <br/> [patched](packages/invenio-search-ui/test-output-patched.txt) | pytest-invenio | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-records-files` <br/> [original](packages/invenio-records-files/test-output-original.txt) [patched](packages/invenio-records-files/test-output-patched.txt) | pytest-invenio invenio-files-rest | ❌ Fail | ❌ Fail | ⚠️ Tests still failing after patch |
| `invenio-logging` <br/> [patched](packages/invenio-logging/test-output-patched.txt) [warnings-patched](packages/invenio-logging/warnings-patched.md) | pytest-invenio | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-sitemap` <br/> [patched](packages/invenio-sitemap/test-output-patched.txt) [xml-patched](packages/invenio-sitemap/test-report-patched.xml) [warnings-patched](packages/invenio-sitemap/warnings-patched.md) | pytest-invenio | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-formatter` <br/> [patched](packages/invenio-formatter/test-output-patched.txt) [warnings-patched](packages/invenio-formatter/warnings-patched.md) | pytest-invenio | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-checks` <br/> [patched](packages/invenio-checks/test-output-patched.txt) [warnings-patched](packages/invenio-checks/warnings-patched.md) | pytest-invenio invenio-files-rest | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-audit-logs` <br/> [original](packages/invenio-audit-logs/test-output-original.txt) [patched](packages/invenio-audit-logs/test-output-patched.txt) [warnings-original](packages/invenio-audit-logs/warnings-original.md) [warnings-patched](packages/invenio-audit-logs/warnings-patched.md) | pytest-invenio invenio-files-rest | ❌ Fail | ❌ Fail | ⚠️ Tests still failing after patch |
| `invenio-records-rest` <br/> [patched](packages/invenio-records-rest/test-output-patched.txt) [xml-patched](packages/invenio-records-rest/test-report-patched.xml) [warnings-patched](packages/invenio-records-rest/warnings-patched.md) | pytest-invenio | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-administration` <br/> [patched](packages/invenio-administration/test-output-patched.txt) [warnings-patched](packages/invenio-administration/warnings-patched.md) | pytest-invenio invenio-files-rest | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-records-resources` <br/> [patched](packages/invenio-records-resources/test-output-patched.txt) [xml-patched](packages/invenio-records-resources/test-report-patched.xml) [warnings-patched](packages/invenio-records-resources/warnings-patched.md) | pytest-invenio invenio-files-rest | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-github` <br/> [original](packages/invenio-github/test-output-original.txt) [patched](packages/invenio-github/test-output-patched.txt) [xml-original](packages/invenio-github/test-report-original.xml) [xml-patched](packages/invenio-github/test-report-patched.xml) [warnings-original](packages/invenio-github/warnings-original.md) [warnings-patched](packages/invenio-github/warnings-patched.md) | pytest-invenio invenio-files-rest | ❌ Fail | ❌ Fail | ⚠️ Tests still failing after patch |
| `invenio-i18n` <br/> [patched](packages/invenio-i18n/test-output-patched.txt) | pytest-invenio | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-oauth2server` <br/> [patched](packages/invenio-oauth2server/test-output-patched.txt) [warnings-patched](packages/invenio-oauth2server/warnings-patched.md) | pytest-invenio | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-jsonschemas` <br/> [patched](packages/invenio-jsonschemas/test-output-patched.txt) [warnings-patched](packages/invenio-jsonschemas/warnings-patched.md) | pytest-invenio | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-search` <br/> [original](packages/invenio-search/test-output-original.txt) [patched](packages/invenio-search/test-output-patched.txt) | pytest-invenio | ❌ Fail | ❌ Fail | ⚠️ Tests still failing after patch |
| `invenio-accounts` <br/> [patched](packages/invenio-accounts/test-output-patched.txt) [xml-patched](packages/invenio-accounts/test-report-patched.xml) [warnings-patched](packages/invenio-accounts/warnings-patched.md) | pytest-invenio | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-users-resources` <br/> [patched](packages/invenio-users-resources/test-output-patched.txt) [xml-patched](packages/invenio-users-resources/test-report-patched.xml) [warnings-patched](packages/invenio-users-resources/warnings-patched.md) | pytest-invenio invenio-files-rest | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-webhooks` <br/> [patched](packages/invenio-webhooks/test-output-patched.txt) [warnings-patched](packages/invenio-webhooks/warnings-patched.md) | pytest-invenio | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-records` <br/> [patched](packages/invenio-records/test-output-patched.txt) [xml-patched](packages/invenio-records/test-report-patched.xml) [warnings-patched](packages/invenio-records/warnings-patched.md) | pytest-invenio | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |

## Collected Warnings

### Patched

#### Warning 1 - 207 occurrences

DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).

| Package | Count |
|---------|-------|
| `invenio-communities` | 34 |
| `invenio-app-rdm` | 14 |
| `invenio-requests` | 14 |
| `invenio-accounts` | 13 |
| `invenio-users-resources` | 11 |
| `invenio-oauth2server` | 10 |
| `invenio-oauthclient` | 8 |
| `invenio-drafts-resources` | 7 |
| `invenio-files-rest` | 7 |
| `invenio-jobs` | 7 |
| `invenio-records-resources` | 7 |
| `invenio-audit-logs` | 6 |
| `invenio-banners` | 6 |
| `invenio-collections` | 6 |
| `invenio-github` | 6 |
| `unknown` | 6 |
| `invenio-oaiserver` | 5 |
| `invenio-records-ui` | 5 |
| `invenio-userprofiles` | 5 |
| `invenio-webhooks` | 5 |
| `invenio-access` | 3 |
| `invenio-administration` | 3 |
| `invenio-previewer` | 3 |
| `invenio-records` | 3 |
| `invenio-records-permissions` | 3 |
| `invenio-records-rest` | 3 |
| `invenio-indexer` | 2 |
| `invenio-pidstore` | 2 |
| `invenio-cache` | 1 |
| `invenio-formatter` | 1 |
| `invenio-rest` | 1 |

#### Warning 2 - 52 occurrences

RemovedInMarshmallow4Warning: The `context` parameter is deprecated and will be removed in marshmallow 4.0. Use `contextvars.ContextVar` to pass context instead.

| Package | Count |
|---------|-------|
| `invenio-records-rest` | 8 |
| `invenio-app-rdm` | 6 |
| `invenio-communities` | 5 |
| `unknown` | 5 |
| `invenio-jobs` | 4 |
| `invenio-audit-logs` | 3 |
| `invenio-collections` | 3 |
| `invenio-drafts-resources` | 3 |
| `invenio-records-resources` | 3 |
| `invenio-requests` | 3 |
| `invenio-users-resources` | 3 |
| `invenio-banners` | 2 |
| `invenio-checks` | 2 |
| `invenio-files-rest` | 2 |

#### Warning 3 - 48 occurrences

DeprecationWarning: jsonschema.RefResolver is deprecated as of v4.18.0, in favor of the https://github.com/python-jsonschema/referencing library, which provides more compliant referencing behavior as well as more flexible APIs for customization. A future release will remove RefResolver. Please file a feature request (on referencing) if you are missing an API for the kind of customization you need.

| Package | Count |
|---------|-------|
| `invenio-app-rdm` | 3 |
| `invenio-collections` | 3 |
| `invenio-records-rest` | 3 |
| `invenio-administration` | 2 |
| `invenio-audit-logs` | 2 |
| `invenio-banners` | 2 |
| `invenio-checks` | 2 |
| `invenio-communities` | 2 |
| `invenio-drafts-resources` | 2 |
| `invenio-github` | 2 |
| `invenio-indexer` | 2 |
| `invenio-jobs` | 2 |
| `invenio-notifications` | 2 |
| `invenio-oaiserver` | 2 |
| `invenio-previewer` | 2 |
| `invenio-records` | 2 |
| `invenio-records-permissions` | 2 |
| `invenio-records-resources` | 2 |
| `invenio-records-ui` | 2 |
| `invenio-requests` | 2 |
| `invenio-users-resources` | 2 |
| `unknown` | 2 |
| `invenio-jsonschemas` | 1 |

#### Warning 4 - 43 occurrences

SAWarning: nested transaction already deassociated from connection

| Package | Count |
|---------|-------|
| `invenio-records` | 21 |
| `invenio-app-rdm` | 6 |
| `invenio-oaiserver` | 5 |
| `invenio-records-rest` | 4 |
| `invenio-collections` | 2 |
| `invenio-indexer` | 2 |
| `invenio-previewer` | 1 |
| `invenio-records-ui` | 1 |
| `invenio-requests` | 1 |

#### Warning 5 - 32 occurrences

DeprecationWarning: Deprecated call to `pkg_resources.declare_namespace('fs')`.

| Package | Count |
|---------|-------|
| `invenio-administration` | 2 |
| `invenio-app-rdm` | 2 |
| `invenio-audit-logs` | 2 |
| `invenio-banners` | 2 |
| `invenio-checks` | 2 |
| `invenio-collections` | 2 |
| `invenio-communities` | 2 |
| `invenio-drafts-resources` | 2 |
| `invenio-files-rest` | 2 |
| `invenio-jobs` | 2 |
| `invenio-notifications` | 2 |
| `invenio-previewer` | 2 |
| `invenio-records-resources` | 2 |
| `invenio-requests` | 2 |
| `invenio-users-resources` | 2 |
| `unknown` | 2 |

#### Warning 6 - 32 occurrences

UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.

| Package | Count |
|---------|-------|
| `invenio-accounts` | 3 |
| `invenio-banners` | 3 |
| `invenio-jobs` | 3 |
| `invenio-app-rdm` | 2 |
| `invenio-audit-logs` | 2 |
| `invenio-collections` | 2 |
| `invenio-communities` | 2 |
| `invenio-files-rest` | 2 |
| `invenio-requests` | 2 |
| `invenio-users-resources` | 2 |
| `unknown` | 2 |
| `invenio-administration` | 1 |
| `invenio-checks` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-notifications` | 1 |
| `invenio-oauthclient` | 1 |
| `invenio-previewer` | 1 |
| `invenio-records-resources` | 1 |

#### Warning 7 - 28 occurrences

DeprecationWarning: 'crypt' is deprecated and slated for removal in Python 3.13

| Package | Count |
|---------|-------|
| `invenio-access` | 1 |
| `invenio-accounts` | 1 |
| `invenio-administration` | 1 |
| `invenio-app-rdm` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-banners` | 1 |
| `invenio-checks` | 1 |
| `invenio-collections` | 1 |
| `invenio-communities` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-files-rest` | 1 |
| `invenio-github` | 1 |
| `invenio-jobs` | 1 |
| `invenio-notifications` | 1 |
| `invenio-oaiserver` | 1 |
| `invenio-oauth2server` | 1 |
| `invenio-oauthclient` | 1 |
| `invenio-pidstore` | 1 |
| `invenio-previewer` | 1 |
| `invenio-records` | 1 |
| `invenio-records-permissions` | 1 |
| `invenio-records-resources` | 1 |
| `invenio-records-ui` | 1 |
| `invenio-requests` | 1 |
| `invenio-userprofiles` | 1 |
| `invenio-users-resources` | 1 |
| `invenio-webhooks` | 1 |
| `unknown` | 1 |

#### Warning 8 - 22 occurrences

DeprecationWarning: jsonschema.exceptions.RefResolutionError is deprecated as of version 4.18.0. If you wish to catch potential reference resolution errors, directly catch referencing.exceptions.Unresolvable.

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |
| `invenio-app-rdm` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-banners` | 1 |
| `invenio-checks` | 1 |
| `invenio-collections` | 1 |
| `invenio-communities` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-github` | 1 |
| `invenio-indexer` | 1 |
| `invenio-jobs` | 1 |
| `invenio-notifications` | 1 |
| `invenio-oaiserver` | 1 |
| `invenio-previewer` | 1 |
| `invenio-records` | 1 |
| `invenio-records-permissions` | 1 |
| `invenio-records-resources` | 1 |
| `invenio-records-rest` | 1 |
| `invenio-records-ui` | 1 |
| `invenio-requests` | 1 |
| `invenio-users-resources` | 1 |
| `unknown` | 1 |

#### Warning 9 - 21 occurrences

FutureWarning: CSRF validation will be enabled by default in the version 1.3.x

| Package | Count |
|---------|-------|
| `invenio-github` | 2 |
| `invenio-rest` | 2 |
| `invenio-accounts` | 1 |
| `invenio-administration` | 1 |
| `invenio-app-rdm` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-banners` | 1 |
| `invenio-collections` | 1 |
| `invenio-communities` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-files-rest` | 1 |
| `invenio-jobs` | 1 |
| `invenio-records-permissions` | 1 |
| `invenio-records-resources` | 1 |
| `invenio-records-rest` | 1 |
| `invenio-requests` | 1 |
| `invenio-stats` | 1 |
| `invenio-users-resources` | 1 |
| `unknown` | 1 |

#### Warning 10 - 21 occurrences

PendingDeprecationWarning: Schema().dump().data and Schema().dump().errors as well as Schema().load().data and Schema().loads().dataattributes are deprecated in marshmallow v3.x.

| Package | Count |
|---------|-------|
| `invenio-records-rest` | 11 |
| `invenio-oaiserver` | 4 |
| `invenio-files-rest` | 3 |
| `invenio-rest` | 3 |

#### Warning 11 - 18 occurrences

DeprecationWarning: Deprecated call to `pkg_resources.declare_namespace('sphinxcontrib')`.

| Package | Count |
|---------|-------|
| `invenio-accounts` | 1 |
| `invenio-administration` | 1 |
| `invenio-app-rdm` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-banners` | 1 |
| `invenio-checks` | 1 |
| `invenio-collections` | 1 |
| `invenio-communities` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-files-rest` | 1 |
| `invenio-jobs` | 1 |
| `invenio-notifications` | 1 |
| `invenio-oauthclient` | 1 |
| `invenio-previewer` | 1 |
| `invenio-records-resources` | 1 |
| `invenio-requests` | 1 |
| `invenio-users-resources` | 1 |
| `unknown` | 1 |

#### Warning 12 - 17 occurrences

DeprecationWarning: Using the initialization functions in flask_caching.backend is deprecated.  Use the a full path to backend classes directly.

| Package | Count |
|---------|-------|
| `invenio-github` | 2 |
| `invenio-administration` | 1 |
| `invenio-app` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-banners` | 1 |
| `invenio-cache` | 1 |
| `invenio-collections` | 1 |
| `invenio-communities` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-jobs` | 1 |
| `invenio-records-permissions` | 1 |
| `invenio-records-resources` | 1 |
| `invenio-requests` | 1 |
| `invenio-sitemap` | 1 |
| `invenio-users-resources` | 1 |
| `unknown` | 1 |

#### Warning 13 - 16 occurrences

DeprecationWarning: Deprecated call to `pkg_resources.declare_namespace('fs.opener')`.

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |
| `invenio-app-rdm` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-banners` | 1 |
| `invenio-checks` | 1 |
| `invenio-collections` | 1 |
| `invenio-communities` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-files-rest` | 1 |
| `invenio-jobs` | 1 |
| `invenio-notifications` | 1 |
| `invenio-previewer` | 1 |
| `invenio-records-resources` | 1 |
| `invenio-requests` | 1 |
| `invenio-users-resources` | 1 |
| `unknown` | 1 |

#### Warning 14 - 16 occurrences

DeprecationWarning: distutils Version classes are deprecated. Use packaging.version instead.

| Package | Count |
|---------|-------|
| `invenio-accounts` | 2 |
| `invenio-app-rdm` | 2 |
| `invenio-collections` | 2 |
| `invenio-files-rest` | 2 |
| `invenio-github` | 2 |
| `invenio-oaiserver` | 2 |
| `invenio-previewer` | 2 |
| `invenio-records-rest` | 2 |

#### Warning 15 - 15 occurrences

LegacyAPIWarning: The Query.get() method is considered legacy as of the 1.x series of SQLAlchemy and becomes a legacy construct in 2.0. The method is now available as Session.get() (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)

| Package | Count |
|---------|-------|
| `invenio-files-rest` | 4 |
| `invenio-app-rdm` | 2 |
| `invenio-collections` | 2 |
| `invenio-webhooks` | 2 |
| `invenio-communities` | 1 |
| `invenio-jobs` | 1 |
| `invenio-records-resources` | 1 |
| `invenio-requests` | 1 |
| `invenio-users-resources` | 1 |

#### Warning 16 - 14 occurrences

DeprecationWarning: The '__version_info__' attribute is deprecated and will be removed in in a future version. Use feature detection or 'packaging.Version(importlib.metadata.version("marshmallow")).release' instead.

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |
| `invenio-app-rdm` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-banners` | 1 |
| `invenio-checks` | 1 |
| `invenio-collections` | 1 |
| `invenio-communities` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-jobs` | 1 |
| `invenio-notifications` | 1 |
| `invenio-records-resources` | 1 |
| `invenio-requests` | 1 |
| `invenio-users-resources` | 1 |
| `unknown` | 1 |

#### Warning 17 - 14 occurrences

DeprecationWarning: datetime.datetime.utcfromtimestamp() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.fromtimestamp(timestamp, datetime.UTC).

| Package | Count |
|---------|-------|
| `invenio-accounts` | 1 |
| `invenio-app-rdm` | 1 |
| `invenio-banners` | 1 |
| `invenio-communities` | 1 |
| `invenio-files-rest` | 1 |
| `invenio-github` | 1 |
| `invenio-oauth2server` | 1 |
| `invenio-oauthclient` | 1 |
| `invenio-records-ui` | 1 |
| `invenio-requests` | 1 |
| `invenio-userprofiles` | 1 |
| `invenio-users-resources` | 1 |
| `invenio-webhooks` | 1 |
| `unknown` | 1 |

#### Warning 18 - 13 occurrences

DeprecationWarning: Link is deprecated and will be removed in v14.0. Use `ExternalLink` for third-party links and `EndpointLink` for InvenioRDM links.

| Package | Count |
|---------|-------|
| `invenio-app-rdm` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-banners` | 1 |
| `invenio-checks` | 1 |
| `invenio-collections` | 1 |
| `invenio-communities` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-jobs` | 1 |
| `invenio-notifications` | 1 |
| `invenio-records-resources` | 1 |
| `invenio-requests` | 1 |
| `invenio-users-resources` | 1 |
| `unknown` | 1 |

#### Warning 19 - 13 occurrences

RemovedInMarshmallow4Warning: The 'default' argument to fields is deprecated. Use 'dump_default' instead.

| Package | Count |
|---------|-------|
| `invenio-checks` | 2 |
| `invenio-jobs` | 2 |
| `unknown` | 2 |
| `invenio-administration` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-banners` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-records-resources` | 1 |
| `invenio-requests` | 1 |
| `invenio-users-resources` | 1 |

#### Warning 20 - 8 occurrences

DeprecationWarning: The '__version__' attribute is deprecated and will be removed in in a future version. Use feature detection or 'importlib.metadata.version("marshmallow")' instead.

| Package | Count |
|---------|-------|
| `invenio-accounts` | 1 |
| `invenio-app-rdm` | 1 |
| `invenio-collections` | 1 |
| `invenio-files-rest` | 1 |
| `invenio-github` | 1 |
| `invenio-oaiserver` | 1 |
| `invenio-previewer` | 1 |
| `invenio-records-rest` | 1 |

#### Warning 21 - 8 occurrences

DeprecationWarning: The 'warn' method is deprecated, use 'warning' instead

| Package | Count |
|---------|-------|
| `invenio-users-resources` | 2 |
| `invenio-communities` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-logging` | 1 |
| `invenio-oauth2server` | 1 |
| `invenio-records-resources` | 1 |
| `unknown` | 1 |

#### Warning 22 - 8 occurrences

DeprecationWarning: ast.Str is deprecated and will be removed in Python 3.14; use ast.Constant instead

| Package | Count |
|---------|-------|
| `invenio-mail` | 8 |

#### Warning 23 - 7 occurrences

DeprecationWarning: Implicit imports (e.g., 'import idutils; idutils.function;') might be removed in the next major version. Please use explicit imports (e.g., 'from idutils import function;') instead.

| Package | Count |
|---------|-------|
| `invenio-app-rdm` | 1 |
| `invenio-checks` | 1 |
| `invenio-collections` | 1 |
| `invenio-communities` | 1 |
| `invenio-pidstore` | 1 |
| `invenio-records-rest` | 1 |
| `unknown` | 1 |

#### Warning 24 - 6 occurrences

ChangedInMarshmallow4Warning: `Field` should not be instantiated. Use `fields.Raw` or  another field subclass instead.

| Package | Count |
|---------|-------|
| `invenio-app-rdm` | 1 |
| `invenio-checks` | 1 |
| `invenio-collections` | 1 |
| `invenio-communities` | 1 |
| `invenio-jobs` | 1 |
| `unknown` | 1 |

#### Warning 25 - 6 occurrences

DeprecationWarning: get_user method is deprecated, user get_user_by_email/get_user_by_id

| Package | Count |
|---------|-------|
| `invenio-accounts` | 1 |
| `invenio-banners` | 1 |
| `invenio-communities` | 1 |
| `invenio-oauth2server` | 1 |
| `invenio-users-resources` | 1 |
| `invenio-webhooks` | 1 |

#### Warning 26 - 6 occurrences

RemovedInMarshmallow4Warning: The 'missing' argument to fields is deprecated. Use 'load_default' instead.

| Package | Count |
|---------|-------|
| `invenio-records-rest` | 4 |
| `invenio-drafts-resources` | 1 |
| `invenio-records-resources` | 1 |

#### Warning 27 - 4 occurrences

DeprecationWarning: Remember me support has been removed.

| Package | Count |
|---------|-------|
| `invenio-app-rdm` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-requests` | 1 |
| `unknown` | 1 |

#### Warning 28 - 4 occurrences

PytestMockWarning: Mocks returned by pytest-mock do not need to be used as context managers. The mocker fixture automatically undoes mocking at the end of a test. This warning can be ignored if it was triggered by mocking a context manager. https://pytest-mock.readthedocs.io/en/latest/usage.html#usage-as-context-manager

| Package | Count |
|---------|-------|
| `invenio-cache` | 4 |

#### Warning 29 - 4 occurrences

SyntaxWarning: invalid escape sequence '\_'

| Package | Count |
|---------|-------|
| `invenio-mail` | 4 |

#### Warning 30 - 3 occurrences

DeprecationWarning: The 'record_to_index' function is no longer expected to return a tuple (index, doc_type), instead it should only return the index. Support for the tuple will be removed in a future version of 'invenio-indexer'.

| Package | Count |
|---------|-------|
| `invenio-drafts-resources` | 1 |
| `invenio-records-resources` | 1 |
| `unknown` | 1 |

#### Warning 31 - 3 occurrences

RuntimeWarning: You are overriding the default OAuthlib "URL encoded" set of valid characters. Make sure that the characters defined in oauthlib.common.urlencoded are indeed limitting your needs.

| Package | Count |
|---------|-------|
| `invenio-github` | 1 |
| `invenio-oauth2server` | 1 |
| `invenio-webhooks` | 1 |

#### Warning 32 - 3 occurrences

SAWarning: Object of type <ObjectVersion> not in session, add operation along 'Bucket.objects' will not proceed (This warning originated from the Session 'autoflush' process, which was invoked automatically in response to a user-initiated operation. Consider using ``no_autoflush`` context manager if this warning happened while initializing objects.)

| Package | Count |
|---------|-------|
| `invenio-drafts-resources` | 1 |
| `invenio-files-rest` | 1 |
| `invenio-records-resources` | 1 |

#### Warning 33 - 3 occurrences

SyntaxWarning: invalid escape sequence '\*'

| Package | Count |
|---------|-------|
| `invenio-mail` | 3 |

#### Warning 34 - 3 occurrences

UserWarning: Please specify the OAISERVER_ID_PREFIX configuration.default value is: oai:runnervmg1sw1:

| Package | Count |
|---------|-------|
| `invenio-collections` | 1 |
| `invenio-communities` | 1 |
| `invenio-oaiserver` | 1 |

#### Warning 35 - 3 occurrences

UserWarning: Set configuration variable SECRET_KEY with random string

| Package | Count |
|---------|-------|
| `invenio-app` | 1 |
| `invenio-config` | 1 |
| `invenio-records-rest` | 1 |

#### Warning 36 - 2 occurrences

DeprecationWarning: 'pkgutil.get_loader' is deprecated and slated for removal in Python 3.14; use importlib.util.find_spec() instead

| Package | Count |
|---------|-------|
| `invenio-mail` | 2 |

#### Warning 37 - 2 occurrences

DeprecationWarning: The configuration value 'RDM_FILES_DEFAULT_MAX_FILE_SIZE' is not set. In future, please set it explicitly to define your max file size, or be aware that the default value used i.e. FILES_REST_DEFAULT_MAX_FILE_SIZE will be 10 * (10**9) (10 GB).

| Package | Count |
|---------|-------|
| `invenio-app-rdm` | 1 |
| `invenio-collections` | 1 |

#### Warning 38 - 2 occurrences

DeprecationWarning: The configuration value 'RDM_FILES_DEFAULT_QUOTA_SIZE' is not set. In future, please set it explicitly to define your quota size, or be aware that the default value used i.e. FILES_REST_DEFAULT_QUOTA_SIZE will be 10 * (10**9) (10 GB).

| Package | Count |
|---------|-------|
| `invenio-app-rdm` | 1 |
| `invenio-collections` | 1 |

#### Warning 39 - 2 occurrences

DeprecationWarning: The patch() method is deprecated and will be removed.

| Package | Count |
|---------|-------|
| `invenio-records` | 1 |
| `invenio-records-rest` | 1 |

#### Warning 40 - 2 occurrences

DeprecationWarning: `es_clear` fixture is deprecated, use `search_clear` instead.

| Package | Count |
|---------|-------|
| `invenio-app-rdm` | 1 |
| `invenio-requests` | 1 |

#### Warning 41 - 2 occurrences

DeprecationWarning: subject_nested is deprecated. Use subject_combined instead.

| Package | Count |
|---------|-------|
| `invenio-app-rdm` | 1 |
| `invenio-collections` | 1 |

#### Warning 42 - 2 occurrences

PytestConfigWarning: Unknown config option: pep8ignore

| Package | Count |
|---------|-------|
| `invenio-jsonschemas` | 1 |
| `invenio-records-ui` | 1 |

#### Warning 43 - 2 occurrences

PytestDeprecationWarning: @pytest.yield_fixture is deprecated.

| Package | Count |
|---------|-------|
| `invenio-pidstore` | 2 |

#### Warning 44 - 2 occurrences

SAWarning: Object of type <Client> not in session, add operation along 'User.oauth2clients' will not proceed (This warning originated from the Session 'autoflush' process, which was invoked automatically in response to a user-initiated operation. Consider using ``no_autoflush`` context manager if this warning happened while initializing objects.)

| Package | Count |
|---------|-------|
| `invenio-oauth2server` | 2 |

#### Warning 45 - 2 occurrences

SAWarning: On mapper Mapper[RecordMetadataVersion(records_metadata_version)], primary key column 'records_metadata_version.transaction_id' is being combined with distinct primary key column 'records_metadata_version.transaction_id' in attribute 'transaction_id'. Use explicit properties to give each column its own mapped attribute name. (This warning originated from the `configure_mappers()` process, which was invoked automatically in response to a user-initiated operation.)

| Package | Count |
|---------|-------|
| `invenio-records` | 2 |

#### Warning 46 - 1 occurrence

DeprecationWarning: 'pkgutil.find_loader' is deprecated and slated for removal in Python 3.14; use importlib.util.find_spec() instead

| Package | Count |
|---------|-------|
| `invenio-mail` | 1 |

#### Warning 47 - 1 occurrence

DeprecationWarning: Attribute s is deprecated and will be removed in Python 3.14; use value instead

| Package | Count |
|---------|-------|
| `invenio-mail` | 1 |

#### Warning 48 - 1 occurrence

DeprecationWarning: CryptContext.hash(): 'scheme' keyword is deprecated as of Passlib 1.7, and will be removed in Passlib 2.0

| Package | Count |
|---------|-------|
| `invenio-accounts` | 1 |

#### Warning 49 - 1 occurrence

DeprecationWarning: Deprecated call to `pkg_resources.declare_namespace('flask_admin')`.

| Package | Count |
|---------|-------|
| `invenio-files-rest` | 1 |

#### Warning 50 - 1 occurrence

DeprecationWarning: Deprecated call to `pkg_resources.declare_namespace('flask_admin.contrib')`.

| Package | Count |
|---------|-------|
| `invenio-files-rest` | 1 |

#### Warning 51 - 1 occurrence

DeprecationWarning: DynamicPermission is scheduled for removal.

| Package | Count |
|---------|-------|
| `invenio-access` | 1 |

#### Warning 52 - 1 occurrence

DeprecationWarning: Please use hash_password instead of encrypt_password.

| Package | Count |
|---------|-------|
| `invenio-records-ui` | 1 |

#### Warning 53 - 1 occurrence

DeprecationWarning: Please use the new command allow-action-for-role instead.

| Package | Count |
|---------|-------|
| `invenio-access` | 1 |

#### Warning 54 - 1 occurrence

DeprecationWarning: Please use the new command allow-action-for-user instead.

| Package | Count |
|---------|-------|
| `invenio-access` | 1 |

#### Warning 55 - 1 occurrence

DeprecationWarning: Please use the new command deny-action-for-role instead.

| Package | Count |
|---------|-------|
| `invenio-access` | 1 |

#### Warning 56 - 1 occurrence

DeprecationWarning: Please use the new command deny-action-for-user instead.

| Package | Count |
|---------|-------|
| `invenio-access` | 1 |

#### Warning 57 - 1 occurrence

DeprecationWarning: Please use the new command remove-action-from-role instead.

| Package | Count |
|---------|-------|
| `invenio-access` | 1 |

#### Warning 58 - 1 occurrence

DeprecationWarning: Please use the new command remove-action-from-user instead.

| Package | Count |
|---------|-------|
| `invenio-access` | 1 |

#### Warning 59 - 1 occurrence

DeprecationWarning: Please use the new command remove-action-global instead.

| Package | Count |
|---------|-------|
| `invenio-access` | 1 |

#### Warning 60 - 1 occurrence

DeprecationWarning: The cern contrib is deprecated. Please use the generic keycloak instead.

| Package | Count |
|---------|-------|
| `invenio-oauthclient` | 1 |

#### Warning 61 - 1 occurrence

DeprecationWarning: The post_load hook must take a positional argument data.

| Package | Count |
|---------|-------|
| `invenio-records` | 1 |

#### Warning 62 - 1 occurrence

DeprecationWarning: The pre_dump hook must take a positional argument data.

| Package | Count |
|---------|-------|
| `invenio-records` | 1 |

#### Warning 63 - 1 occurrence

DeprecationWarning: ast.NameConstant is deprecated and will be removed in Python 3.14; use ast.Constant instead

| Package | Count |
|---------|-------|
| `invenio-mail` | 1 |

#### Warning 64 - 1 occurrence

DeprecationWarning: current_userprofile is deprecated, use current_user instead

| Package | Count |
|---------|-------|
| `invenio-userprofiles` | 1 |

#### Warning 65 - 1 occurrence

DeprecationWarning: passing settings to invenio_aes_encrypted_email.hash() is deprecated, and won't be supported in Passlib 2.0; use 'invenio_aes_encrypted_email.using(**settings).hash(secret)' instead

| Package | Count |
|---------|-------|
| `invenio-accounts` | 1 |

#### Warning 66 - 1 occurrence

DeprecationWarning: the method passlib.context.CryptContext.encrypt() is deprecated as of Passlib 1.7, and will be removed in Passlib 2.0, use CryptContext.hash() instead.

| Package | Count |
|---------|-------|
| `invenio-accounts` | 1 |

#### Warning 67 - 1 occurrence

PendingDeprecationWarning: The WSGI_PROXIES configuration is deprecated and it will be removed, use PROXYFIX_CONFIG instead

| Package | Count |
|---------|-------|
| `invenio-base` | 1 |

#### Warning 68 - 1 occurrence

PendingDeprecationWarning: This feature is deprecated.

| Package | Count |
|---------|-------|
| `invenio-logging` | 1 |

#### Warning 69 - 1 occurrence

PendingDeprecationWarning: Usage of model and modelview kwargs are deprecated in favor of view_class, args and kwargs.

| Package | Count |
|---------|-------|
| `invenio-files-rest` | 1 |

#### Warning 70 - 1 occurrence

PytestCollectionWarning: cannot collect test class 'TestAction' because it has a __init__ constructor (from: tests/customizations/test_request_types.py)

| Package | Count |
|---------|-------|
| `invenio-requests` | 1 |

#### Warning 71 - 1 occurrence

PytestCollectionWarning: cannot collect test class 'TestCustomView' because it has a __init__ constructor (from: tests/test_base.py)

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |

#### Warning 72 - 1 occurrence

PytestCollectionWarning: cannot collect test class 'TestPermissionPolicy' because it has a __init__ constructor (from: tests/test_permissions_base.py)

| Package | Count |
|---------|-------|
| `invenio-records-permissions` | 1 |

#### Warning 73 - 1 occurrence

PytestCollectionWarning: cannot collect test class 'TestReader' because it has a __init__ constructor (from: tests/resources/test_tasks_resources.py)

| Package | Count |
|---------|-------|
| `unknown` | 1 |

#### Warning 74 - 1 occurrence

PytestCollectionWarning: cannot collect test class 'TestSchema' because it has a __init__ constructor (from: tests/test_marshmallow_utils.py)

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |

#### Warning 75 - 1 occurrence

PytestCollectionWarning: cannot collect test class 'TestWriter' because it has a __init__ constructor (from: tests/resources/test_tasks_resources.py)

| Package | Count |
|---------|-------|
| `unknown` | 1 |

#### Warning 76 - 1 occurrence

RemovedInMarshmallow4Warning: Passing field metadata as keyword arguments is deprecated. Use the explicit `metadata=...` argument instead. Additional metadata: {'load_from': 'from'}

| Package | Count |
|---------|-------|
| `invenio-records-rest` | 1 |

#### Warning 77 - 1 occurrence

RemovedInMarshmallow4Warning: `Field.fail` is deprecated. Use `raise self.make_error("required", ...)` instead.

| Package | Count |
|---------|-------|
| `invenio-records-rest` | 1 |

#### Warning 78 - 1 occurrence

RuntimeWarning: Results are not stored in backend and should not be retrieved when task_always_eager is enabled, unless task_store_eager_result is enabled.

| Package | Count |
|---------|-------|
| `invenio-webhooks` | 1 |

#### Warning 79 - 1 occurrence

SADeprecationWarning: Query.values() is deprecated and will be removed in a future release.  Please use Query.with_entities() (deprecated since: 1.4)

| Package | Count |
|---------|-------|
| `invenio-indexer` | 1 |

#### Warning 80 - 1 occurrence

SAWarning: Identity map already had an identity for (<class 'invenio_jobs.models.Run'>, (UUID('597504a7-65f5-4883-b1bf-3150c9a92831'),), None), replacing it with newly flushed object.   Are there load operations occurring inside of an event handler within the flush?

| Package | Count |
|---------|-------|
| `invenio-jobs` | 1 |

#### Warning 81 - 1 occurrence

SAWarning: Identity map already had an identity for (<class 'invenio_jobs.models.Run'>, (UUID('7b87f5d6-8b5d-42a6-9e0c-09748e676e31'),), None), replacing it with newly flushed object.   Are there load operations occurring inside of an event handler within the flush?

| Package | Count |
|---------|-------|
| `invenio-jobs` | 1 |

#### Warning 82 - 1 occurrence

SAWarning: Identity map already had an identity for (<class 'invenio_jobs.models.Run'>, (UUID('8b749167-8dfe-4c2c-81c7-c3b081cd1c00'),), None), replacing it with newly flushed object.   Are there load operations occurring inside of an event handler within the flush?

| Package | Count |
|---------|-------|
| `invenio-jobs` | 1 |

#### Warning 83 - 1 occurrence

SAWarning: Identity map already had an identity for (<class 'invenio_jobs.models.Run'>, (UUID('8c784525-e7e0-41eb-b334-e1daf2fb8cf2'),), None), replacing it with newly flushed object.   Are there load operations occurring inside of an event handler within the flush?

| Package | Count |
|---------|-------|
| `invenio-jobs` | 1 |

#### Warning 84 - 1 occurrence

SAWarning: Identity map already had an identity for (<class 'invenio_jobs.models.Run'>, (UUID('b170b199-4670-4fcb-ba4b-d1560b253bcb'),), None), replacing it with newly flushed object.   Are there load operations occurring inside of an event handler within the flush?

| Package | Count |
|---------|-------|
| `invenio-jobs` | 1 |

#### Warning 85 - 1 occurrence

SAWarning: Identity map already had an identity for (<class 'invenio_jobs.models.Run'>, (UUID('c70ccef0-7e3e-44f2-b80c-fb3727d5ce4f'),), None), replacing it with newly flushed object.   Are there load operations occurring inside of an event handler within the flush?

| Package | Count |
|---------|-------|
| `invenio-jobs` | 1 |

#### Warning 86 - 1 occurrence

SAWarning: Identity map already had an identity for (<class 'invenio_jobs.models.Run'>, (UUID('f1be18f9-35d7-4274-ad23-c6f15ec67ab4'),), None), replacing it with newly flushed object.   Are there load operations occurring inside of an event handler within the flush?

| Package | Count |
|---------|-------|
| `invenio-jobs` | 1 |

#### Warning 87 - 1 occurrence

SAWarning: Object of type <Client> not in session, add operation along 'User.oauth2clients' will not proceed

| Package | Count |
|---------|-------|
| `invenio-oauth2server` | 1 |

#### Warning 88 - 1 occurrence

SAWarning: Object of type <Token> not in session, add operation along 'User.oauth2tokens' will not proceed

| Package | Count |
|---------|-------|
| `invenio-oauth2server` | 1 |

#### Warning 89 - 1 occurrence

SAWarning: This declarative base already contains a class with the same class name and module name as invenio_records_resources.factories.factory.MyRecordMetadata, and will be replaced in the string-lookup table.

| Package | Count |
|---------|-------|
| `invenio-records-resources` | 1 |

#### Warning 90 - 1 occurrence

SAWarning: This declarative base already contains a class with the same class name and module name as sqlalchemy_continuum.model_builder.RecordMetadataVersion, and will be replaced in the string-lookup table. (This warning originated from the `configure_mappers()` process, which was invoked automatically in response to a user-initiated operation.)

| Package | Count |
|---------|-------|
| `invenio-records` | 1 |

#### Warning 91 - 1 occurrence

SAWarning: relationship 'RecordMetadataVersion.transaction' will copy column transaction.id to column records_metadata_version.transaction_id, which conflicts with relationship(s): 'RecordMetadataVersion.transaction' (copies transaction.id to records_metadata_version.transaction_id), 'RecordMetadataVersion.transaction' (copies transaction.id to records_metadata_version.transaction_id), 'RecordMetadataVersion.transaction' (copies transaction.id to records_metadata_version.transaction_id), 'RecordMetadataVersion.transaction' (copies transaction.id to records_metadata_version.transaction_id). If this is not the intention, consider if these relationships should be linked with back_populates, or if viewonly=True should be applied to one or more if they are read-only. For the less common case that foreign key constraints are partially overlapping, the orm.foreign() annotation can be used to isolate the columns that should be written towards.   To silence this warning, add the parameter 'overlaps="transaction,transaction,transaction,transaction"' to the 'RecordMetadataVersion.transaction' relationship. (Background on this warning at: https://sqlalche.me/e/20/qzyx) (This warning originated from the `configure_mappers()` process, which was invoked automatically in response to a user-initiated operation.)

| Package | Count |
|---------|-------|
| `invenio-records` | 1 |

#### Warning 92 - 1 occurrence

SAWarning: relationship 'RecordMetadataVersion.transaction' will copy column transaction.id to column records_metadata_version.transaction_id, which conflicts with relationship(s): 'RecordMetadataVersion.transaction' (copies transaction.id to records_metadata_version.transaction_id), 'RecordMetadataVersion.transaction' (copies transaction.id to records_metadata_version.transaction_id), 'RecordMetadataVersion.transaction' (copies transaction.id to records_metadata_version.transaction_id). If this is not the intention, consider if these relationships should be linked with back_populates, or if viewonly=True should be applied to one or more if they are read-only. For the less common case that foreign key constraints are partially overlapping, the orm.foreign() annotation can be used to isolate the columns that should be written towards.   To silence this warning, add the parameter 'overlaps="transaction,transaction,transaction"' to the 'RecordMetadataVersion.transaction' relationship. (Background on this warning at: https://sqlalche.me/e/20/qzyx) (This warning originated from the `configure_mappers()` process, which was invoked automatically in response to a user-initiated operation.)

| Package | Count |
|---------|-------|
| `invenio-records` | 1 |

#### Warning 93 - 1 occurrence

SAWarning: relationship 'RecordMetadataVersion.transaction' will copy column transaction.id to column records_metadata_version.transaction_id, which conflicts with relationship(s): 'RecordMetadataVersion.transaction' (copies transaction.id to records_metadata_version.transaction_id), 'RecordMetadataVersion.transaction' (copies transaction.id to records_metadata_version.transaction_id). If this is not the intention, consider if these relationships should be linked with back_populates, or if viewonly=True should be applied to one or more if they are read-only. For the less common case that foreign key constraints are partially overlapping, the orm.foreign() annotation can be used to isolate the columns that should be written towards.   To silence this warning, add the parameter 'overlaps="transaction,transaction"' to the 'RecordMetadataVersion.transaction' relationship. (Background on this warning at: https://sqlalche.me/e/20/qzyx) (This warning originated from the `configure_mappers()` process, which was invoked automatically in response to a user-initiated operation.)

| Package | Count |
|---------|-------|
| `invenio-records` | 1 |

#### Warning 94 - 1 occurrence

SAWarning: relationship 'RecordMetadataVersion.transaction' will copy column transaction.id to column records_metadata_version.transaction_id, which conflicts with relationship(s): 'RecordMetadataVersion.transaction' (copies transaction.id to records_metadata_version.transaction_id). If this is not the intention, consider if these relationships should be linked with back_populates, or if viewonly=True should be applied to one or more if they are read-only. For the less common case that foreign key constraints are partially overlapping, the orm.foreign() annotation can be used to isolate the columns that should be written towards.   To silence this warning, add the parameter 'overlaps="transaction"' to the 'RecordMetadataVersion.transaction' relationship. (Background on this warning at: https://sqlalche.me/e/20/qzyx) (This warning originated from the `configure_mappers()` process, which was invoked automatically in response to a user-initiated operation.)

| Package | Count |
|---------|-------|
| `invenio-records` | 1 |

#### Warning 95 - 1 occurrence

SyntaxWarning: "is" with 'int' literal. Did you mean "=="?

| Package | Count |
|---------|-------|
| `invenio-records-rest` | 1 |

#### Warning 96 - 1 occurrence

SyntaxWarning: "is" with 'str' literal. Did you mean "=="?

| Package | Count |
|---------|-------|
| `invenio-mail` | 1 |

#### Warning 97 - 1 occurrence

SyntaxWarning: invalid escape sequence '\ '

| Package | Count |
|---------|-------|
| `invenio-mail` | 1 |

#### Warning 98 - 1 occurrence

SyntaxWarning: invalid escape sequence '\?'

| Package | Count |
|---------|-------|
| `invenio-records-rest` | 1 |

#### Warning 99 - 1 occurrence

UserWarning: OpenSearch v2 mappings files not found, falling back to Elasticsearch v7 mappings for module mock_module.mappings. Please add the missing OpenSearch os-v2 mappings.

| Package | Count |
|---------|-------|
| `unknown` | 1 |

#### Warning 100 - 1 occurrence

UserWarning: OpenSearch v2 mappings files not found, falling back to Elasticsearch v7 mappings for module tests.records.mock_module.mappings. Please add the missing OpenSearch os-v2 mappings.

| Package | Count |
|---------|-------|
| `invenio-communities` | 1 |

#### Warning 101 - 1 occurrence

UserWarning: Test

| Package | Count |
|---------|-------|
| `invenio-base` | 1 |

#### Warning 102 - 1 occurrence

UserWarning: This streaming does not support multiple storage backends.

| Package | Count |
|---------|-------|
| `invenio-files-rest` | 1 |

#### Warning 103 - 1 occurrence

UserWarning: Using the in-memory storage for tracking rate limits as no storage was explicitly specified. This is not recommended for production use. See: https://flask-limiter.readthedocs.io#configuring-a-storage-backend for documentation about configuring the storage backend.

| Package | Count |
|---------|-------|
| `invenio-app` | 1 |


### Original

#### Warning 1 - 43 occurrences

DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).

| Package | Count |
|---------|-------|
| `invenio-requests` | 14 |
| `invenio-drafts-resources` | 7 |
| `invenio-files-rest` | 7 |
| `invenio-audit-logs` | 6 |
| `invenio-github` | 6 |
| `invenio-access` | 3 |

#### Warning 2 - 11 occurrences

RemovedInMarshmallow4Warning: The `context` parameter is deprecated and will be removed in marshmallow 4.0. Use `contextvars.ContextVar` to pass context instead.

| Package | Count |
|---------|-------|
| `invenio-audit-logs` | 3 |
| `invenio-drafts-resources` | 3 |
| `invenio-requests` | 3 |
| `invenio-files-rest` | 2 |

#### Warning 3 - 8 occurrences

DeprecationWarning: Deprecated call to `pkg_resources.declare_namespace('fs')`.

| Package | Count |
|---------|-------|
| `invenio-audit-logs` | 2 |
| `invenio-drafts-resources` | 2 |
| `invenio-files-rest` | 2 |
| `invenio-requests` | 2 |

#### Warning 4 - 8 occurrences

DeprecationWarning: jsonschema.RefResolver is deprecated as of v4.18.0, in favor of the https://github.com/python-jsonschema/referencing library, which provides more compliant referencing behavior as well as more flexible APIs for customization. A future release will remove RefResolver. Please file a feature request (on referencing) if you are missing an API for the kind of customization you need.

| Package | Count |
|---------|-------|
| `invenio-audit-logs` | 2 |
| `invenio-drafts-resources` | 2 |
| `invenio-github` | 2 |
| `invenio-requests` | 2 |

#### Warning 5 - 8 occurrences

UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.

| Package | Count |
|---------|-------|
| `invenio-audit-logs` | 2 |
| `invenio-files-rest` | 2 |
| `invenio-requests` | 2 |
| `invenio-drafts-resources` | 1 |
| `unknown` | 1 |

#### Warning 6 - 7 occurrences

FutureWarning: CSRF validation will be enabled by default in the version 1.3.x

| Package | Count |
|---------|-------|
| `invenio-github` | 2 |
| `invenio-audit-logs` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-files-rest` | 1 |
| `invenio-requests` | 1 |
| `invenio-stats` | 1 |

#### Warning 7 - 6 occurrences

DeprecationWarning: 'crypt' is deprecated and slated for removal in Python 3.13

| Package | Count |
|---------|-------|
| `invenio-access` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-files-rest` | 1 |
| `invenio-github` | 1 |
| `invenio-requests` | 1 |

#### Warning 8 - 5 occurrences

DeprecationWarning: Using the initialization functions in flask_caching.backend is deprecated.  Use the a full path to backend classes directly.

| Package | Count |
|---------|-------|
| `invenio-github` | 2 |
| `invenio-audit-logs` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-requests` | 1 |

#### Warning 9 - 5 occurrences

LegacyAPIWarning: The Query.get() method is considered legacy as of the 1.x series of SQLAlchemy and becomes a legacy construct in 2.0. The method is now available as Session.get() (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)

| Package | Count |
|---------|-------|
| `invenio-files-rest` | 4 |
| `invenio-requests` | 1 |

#### Warning 10 - 4 occurrences

DeprecationWarning: Deprecated call to `pkg_resources.declare_namespace('fs.opener')`.

| Package | Count |
|---------|-------|
| `invenio-audit-logs` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-files-rest` | 1 |
| `invenio-requests` | 1 |

#### Warning 11 - 4 occurrences

DeprecationWarning: Deprecated call to `pkg_resources.declare_namespace('sphinxcontrib')`.

| Package | Count |
|---------|-------|
| `invenio-audit-logs` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-files-rest` | 1 |
| `invenio-requests` | 1 |

#### Warning 12 - 4 occurrences

DeprecationWarning: distutils Version classes are deprecated. Use packaging.version instead.

| Package | Count |
|---------|-------|
| `invenio-files-rest` | 2 |
| `invenio-github` | 2 |

#### Warning 13 - 4 occurrences

DeprecationWarning: jsonschema.exceptions.RefResolutionError is deprecated as of version 4.18.0. If you wish to catch potential reference resolution errors, directly catch referencing.exceptions.Unresolvable.

| Package | Count |
|---------|-------|
| `invenio-audit-logs` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-github` | 1 |
| `invenio-requests` | 1 |

#### Warning 14 - 3 occurrences

DeprecationWarning: Link is deprecated and will be removed in v14.0. Use `ExternalLink` for third-party links and `EndpointLink` for InvenioRDM links.

| Package | Count |
|---------|-------|
| `invenio-audit-logs` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-requests` | 1 |

#### Warning 15 - 3 occurrences

DeprecationWarning: The '__version_info__' attribute is deprecated and will be removed in in a future version. Use feature detection or 'packaging.Version(importlib.metadata.version("marshmallow")).release' instead.

| Package | Count |
|---------|-------|
| `invenio-audit-logs` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-requests` | 1 |

#### Warning 16 - 3 occurrences

DeprecationWarning: datetime.datetime.utcfromtimestamp() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.fromtimestamp(timestamp, datetime.UTC).

| Package | Count |
|---------|-------|
| `invenio-files-rest` | 1 |
| `invenio-github` | 1 |
| `invenio-requests` | 1 |

#### Warning 17 - 3 occurrences

PendingDeprecationWarning: Schema().dump().data and Schema().dump().errors as well as Schema().load().data and Schema().loads().dataattributes are deprecated in marshmallow v3.x.

| Package | Count |
|---------|-------|
| `invenio-files-rest` | 3 |

#### Warning 18 - 3 occurrences

RemovedInMarshmallow4Warning: The 'default' argument to fields is deprecated. Use 'dump_default' instead.

| Package | Count |
|---------|-------|
| `invenio-audit-logs` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-requests` | 1 |

#### Warning 19 - 2 occurrences

DeprecationWarning: Remember me support has been removed.

| Package | Count |
|---------|-------|
| `invenio-audit-logs` | 1 |
| `invenio-requests` | 1 |

#### Warning 20 - 2 occurrences

DeprecationWarning: The '__version__' attribute is deprecated and will be removed in in a future version. Use feature detection or 'importlib.metadata.version("marshmallow")' instead.

| Package | Count |
|---------|-------|
| `invenio-files-rest` | 1 |
| `invenio-github` | 1 |

#### Warning 21 - 2 occurrences

SAWarning: Object of type <ObjectVersion> not in session, add operation along 'Bucket.objects' will not proceed (This warning originated from the Session 'autoflush' process, which was invoked automatically in response to a user-initiated operation. Consider using ``no_autoflush`` context manager if this warning happened while initializing objects.)

| Package | Count |
|---------|-------|
| `invenio-drafts-resources` | 1 |
| `invenio-files-rest` | 1 |

#### Warning 22 - 1 occurrence

DeprecationWarning: DynamicPermission is scheduled for removal.

| Package | Count |
|---------|-------|
| `invenio-access` | 1 |

#### Warning 23 - 1 occurrence

DeprecationWarning: Please use the new command allow-action-for-role instead.

| Package | Count |
|---------|-------|
| `invenio-access` | 1 |

#### Warning 24 - 1 occurrence

DeprecationWarning: Please use the new command allow-action-for-user instead.

| Package | Count |
|---------|-------|
| `invenio-access` | 1 |

#### Warning 25 - 1 occurrence

DeprecationWarning: Please use the new command deny-action-for-role instead.

| Package | Count |
|---------|-------|
| `invenio-access` | 1 |

#### Warning 26 - 1 occurrence

DeprecationWarning: Please use the new command deny-action-for-user instead.

| Package | Count |
|---------|-------|
| `invenio-access` | 1 |

#### Warning 27 - 1 occurrence

DeprecationWarning: Please use the new command remove-action-from-role instead.

| Package | Count |
|---------|-------|
| `invenio-access` | 1 |

#### Warning 28 - 1 occurrence

DeprecationWarning: Please use the new command remove-action-from-user instead.

| Package | Count |
|---------|-------|
| `invenio-access` | 1 |

#### Warning 29 - 1 occurrence

DeprecationWarning: Please use the new command remove-action-global instead.

| Package | Count |
|---------|-------|
| `invenio-access` | 1 |

#### Warning 30 - 1 occurrence

DeprecationWarning: The 'record_to_index' function is no longer expected to return a tuple (index, doc_type), instead it should only return the index. Support for the tuple will be removed in a future version of 'invenio-indexer'.

| Package | Count |
|---------|-------|
| `invenio-drafts-resources` | 1 |

#### Warning 31 - 1 occurrence

DeprecationWarning: The 'warn' method is deprecated, use 'warning' instead

| Package | Count |
|---------|-------|
| `invenio-drafts-resources` | 1 |

#### Warning 32 - 1 occurrence

DeprecationWarning: `es_clear` fixture is deprecated, use `search_clear` instead.

| Package | Count |
|---------|-------|
| `invenio-requests` | 1 |

#### Warning 33 - 1 occurrence

PytestCollectionWarning: cannot collect test class 'TestAction' because it has a __init__ constructor (from: tests/customizations/test_request_types.py)

| Package | Count |
|---------|-------|
| `invenio-requests` | 1 |

#### Warning 34 - 1 occurrence

RemovedInMarshmallow4Warning: The 'missing' argument to fields is deprecated. Use 'load_default' instead.

| Package | Count |
|---------|-------|
| `invenio-drafts-resources` | 1 |

#### Warning 35 - 1 occurrence

RuntimeWarning: You are overriding the default OAuthlib "URL encoded" set of valid characters. Make sure that the characters defined in oauthlib.common.urlencoded are indeed limitting your needs.

| Package | Count |
|---------|-------|
| `invenio-github` | 1 |

#### Warning 36 - 1 occurrence

SAWarning: nested transaction already deassociated from connection

| Package | Count |
|---------|-------|
| `invenio-requests` | 1 |

#### Warning 37 - 1 occurrence

UserWarning: This streaming does not support multiple storage backends.

| Package | Count |
|---------|-------|
| `invenio-files-rest` | 1 |




---

_For detailed test outputs and diffs, see the [full report](https://mesemus.github.io/invenio-bug-verification/)._