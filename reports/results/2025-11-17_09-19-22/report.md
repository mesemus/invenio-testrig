# Invenio Bugfix Verification Results

_Last updated: 2025-11-17 09:19:23 UTC_

## 📊 Overall Status

| Metric | Count |
|--------|-------|
| **Total Packages** | 52 |
| **Patched Packages** | 52 |
| **Unpatched Packages** | 0 |

### Patch Results
| Result | Count |
|--------|-------|
| ✅ Fixed | 0 |
| ❌ Regressions | 0 |
| ⚠️  Still Failing | 0 |
| ℹ️  No Change | 52 |

## 🔧 Configured Patches

| Patched Package | Repository | Branch |
|----------------|------------|--------|
| [pytest-invenio](https://github.com/oarepo/pytest-invenio/tree/nested-db-session-rollback) | https://github.com/oarepo/pytest-invenio | nested-db-session-rollback |
| [invenio-files-rest](https://github.com/fenekku/invenio-files-res/tree/support_3.14) | https://github.com/fenekku/invenio-files-res | support_3.14 |

## 🔄 Patched Packages

| Package | Patches Applied | Original | Patched | Result |
|---------|----------------|--------|-------|--------|
| `invenio-files-rest` | pytest-invenio | ⏭️  Skip | ⏭️  Skip | ❓ Unknown |

## 📦 Packages that do not depend on patched packages

| Package | Build Status |
|---------|--------------|

## 🔄 Packages that depend on patched packages

| Package | Patches Applied | Original | Patched | Result |
|---------|----------------|--------|-------|--------|
| `invenio-banners` | pytest-invenio invenio-files-rest | ⏭️  Skip | ⏭️  Skip | ❓ Unknown |
| `invenio-mail` | pytest-invenio | ⏭️  Skip | ⏭️  Skip | ❓ Unknown |
| `invenio-config` | pytest-invenio | ⏭️  Skip | ⏭️  Skip | ❓ Unknown |
| `invenio-queues` | pytest-invenio | ⏭️  Skip | ⏭️  Skip | ❓ Unknown |
| `invenio-oauthclient` | pytest-invenio | ⏭️  Skip | ⏭️  Skip | ❓ Unknown |
| `invenio-cache` | pytest-invenio | ⏭️  Skip | ⏭️  Skip | ❓ Unknown |
| `invenio-notifications` | pytest-invenio invenio-files-rest | ⏭️  Skip | ⏭️  Skip | ❓ Unknown |
| `invenio-base` | pytest-invenio | ⏭️  Skip | ⏭️  Skip | ❓ Unknown |
| `invenio-rdm-records` | pytest-invenio invenio-files-rest | ⏭️  Skip | ⏭️  Skip | ❓ Unknown |
| `invenio-app` | pytest-invenio | ⏭️  Skip | ⏭️  Skip | ❓ Unknown |
| `invenio-jobs` | pytest-invenio invenio-files-rest | ⏭️  Skip | ⏭️  Skip | ❓ Unknown |
| `invenio-theme` | pytest-invenio | ⏭️  Skip | ⏭️  Skip | ❓ Unknown |
| `invenio-assets` | pytest-invenio | ⏭️  Skip | ⏭️  Skip | ❓ Unknown |
| `invenio-celery` | pytest-invenio | ⏭️  Skip | ⏭️  Skip | ❓ Unknown |
| `invenio-pidstore` | pytest-invenio | ⏭️  Skip | ⏭️  Skip | ❓ Unknown |
| `invenio-db` | pytest-invenio | ⏭️  Skip | ⏭️  Skip | ❓ Unknown |
| `invenio-indexer` | pytest-invenio | ⏭️  Skip | ⏭️  Skip | ❓ Unknown |
| `invenio-oaiserver` | pytest-invenio | ⏭️  Skip | ⏭️  Skip | ❓ Unknown |
| `invenio-drafts-resources` | pytest-invenio invenio-files-rest | ⏭️  Skip | ⏭️  Skip | ❓ Unknown |
| `invenio-access` | pytest-invenio | ⏭️  Skip | ⏭️  Skip | ❓ Unknown |
| `invenio-rest` | pytest-invenio | ⏭️  Skip | ⏭️  Skip | ❓ Unknown |
| `invenio-requests` | pytest-invenio invenio-files-rest | ⏭️  Skip | ⏭️  Skip | ❓ Unknown |
| `invenio-pages` | pytest-invenio invenio-files-rest | ⏭️  Skip | ⏭️  Skip | ❓ Unknown |
| `invenio-records-permissions` | pytest-invenio | ⏭️  Skip | ⏭️  Skip | ❓ Unknown |
| `invenio-app-rdm` | pytest-invenio invenio-files-rest | ⏭️  Skip | ⏭️  Skip | ❓ Unknown |
| `invenio-collections` | pytest-invenio invenio-files-rest | ⏭️  Skip | ⏭️  Skip | ❓ Unknown |
| `invenio-records-ui` | pytest-invenio | ⏭️  Skip | ⏭️  Skip | ❓ Unknown |
| `invenio-stats` | pytest-invenio invenio-files-rest | ⏭️  Skip | ⏭️  Skip | ❓ Unknown |
| `invenio-userprofiles` | pytest-invenio | ⏭️  Skip | ⏭️  Skip | ❓ Unknown |
| `invenio-previewer` | pytest-invenio invenio-files-rest | ⏭️  Skip | ⏭️  Skip | ❓ Unknown |
| `invenio-communities` | pytest-invenio invenio-files-rest | ⏭️  Skip | ⏭️  Skip | ❓ Unknown |
| `invenio-search-ui` | pytest-invenio | ⏭️  Skip | ⏭️  Skip | ❓ Unknown |
| `invenio-records-files` | pytest-invenio invenio-files-rest | ⏭️  Skip | ⏭️  Skip | ❓ Unknown |
| `invenio-logging` | pytest-invenio | ⏭️  Skip | ⏭️  Skip | ❓ Unknown |
| `invenio-sitemap` | pytest-invenio | ⏭️  Skip | ⏭️  Skip | ❓ Unknown |
| `invenio-formatter` | pytest-invenio | ⏭️  Skip | ⏭️  Skip | ❓ Unknown |
| `invenio-checks` | pytest-invenio invenio-files-rest | ⏭️  Skip | ⏭️  Skip | ❓ Unknown |
| `invenio-audit-logs` | pytest-invenio invenio-files-rest | ⏭️  Skip | ⏭️  Skip | ❓ Unknown |
| `invenio-records-rest` | pytest-invenio | ⏭️  Skip | ⏭️  Skip | ❓ Unknown |
| `invenio-administration` | pytest-invenio invenio-files-rest | ⏭️  Skip | ⏭️  Skip | ❓ Unknown |
| `invenio-records-resources` | pytest-invenio invenio-files-rest | ⏭️  Skip | ⏭️  Skip | ❓ Unknown |
| `invenio-github` | pytest-invenio invenio-files-rest | ⏭️  Skip | ⏭️  Skip | ❓ Unknown |
| `invenio-i18n` | pytest-invenio | ⏭️  Skip | ⏭️  Skip | ❓ Unknown |
| `invenio-oauth2server` | pytest-invenio | ⏭️  Skip | ⏭️  Skip | ❓ Unknown |
| `invenio-jsonschemas` | pytest-invenio | ⏭️  Skip | ⏭️  Skip | ❓ Unknown |
| `invenio-vocabularies` | pytest-invenio invenio-files-rest | ⏭️  Skip | ⏭️  Skip | ❓ Unknown |
| `invenio-search` | pytest-invenio | ⏭️  Skip | ⏭️  Skip | ❓ Unknown |
| `invenio-accounts` | pytest-invenio | ⏭️  Skip | ⏭️  Skip | ❓ Unknown |
| `invenio-users-resources` | pytest-invenio invenio-files-rest | ⏭️  Skip | ⏭️  Skip | ❓ Unknown |
| `invenio-webhooks` | pytest-invenio | ⏭️  Skip | ⏭️  Skip | ❓ Unknown |
| `invenio-records` | pytest-invenio | ⏭️  Skip | ⏭️  Skip | ❓ Unknown |

## Collected Warnings

No warnings found in any package.


---

_For detailed test outputs and diffs, see the [full report](https://mesemus.github.io/invenio-bug-verification/)._