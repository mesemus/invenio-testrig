# Invenio Bugfix Verification Results

_Last updated: 2025-11-15 20:20:31 UTC_

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
| ❌ Regressions | 14 |
| ⚠️  Still Failing | 14 |
| ℹ️  No Change | 24 |

## 🔧 Configured Patches

## 🔄 Patched Packages

| Package | Patches Applied | Original | Patched | Result |
|---------|----------------|--------|-------|--------|
| `invenio-db` <br/>  [patched](invenio-db/test-output-patched.txt) | pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |

## 📦 Packages that do not depend on patched packages

| Package | Build Status |
|---------|--------------|

## 🔄 Packages that depend on patched packages

| Package | Patches Applied | Original | Patched | Result |
|---------|----------------|--------|-------|--------|
| `invenio-access` <br/>  [original](invenio-access/test-output-original.txt)  [patched](invenio-access/test-output-patched.txt) | invenio-db pytest-invenio  | ✅ Pass | ❌ Fail | ❌ Patch introduced test failures |
| `invenio-accounts` <br/>  [original](invenio-accounts/test-output-original.txt)  [patched](invenio-accounts/test-output-patched.txt) | invenio-db pytest-invenio  | ✅ Pass | ❌ Fail | ❌ Patch introduced test failures |
| `invenio-administration` <br/>  [original](invenio-administration/test-output-original.txt)  [patched](invenio-administration/test-output-patched.txt) | invenio-db pytest-invenio  | ✅ Pass | ❌ Fail | ❌ Patch introduced test failures |
| `invenio-app-rdm` <br/>  [original](invenio-app-rdm/test-output-original.txt)  [patched](invenio-app-rdm/test-output-patched.txt) | invenio-db pytest-invenio  | ❌ Fail | ❌ Fail | ⚠️ Tests still failing after patch |
| `invenio-app` <br/>  [patched](invenio-app/test-output-patched.txt) | pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-assets` <br/>  [patched](invenio-assets/test-output-patched.txt) | pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-audit-logs` <br/>  [patched](invenio-audit-logs/test-output-patched.txt) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-banners` <br/>  [original](invenio-banners/test-output-original.txt)  [patched](invenio-banners/test-output-patched.txt) | invenio-db pytest-invenio  | ✅ Pass | ❌ Fail | ❌ Patch introduced test failures |
| `invenio-base` <br/>  [patched](invenio-base/test-output-patched.txt) | pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-cache` <br/>  [original](invenio-cache/test-output-original.txt)  [patched](invenio-cache/test-output-patched.txt) | pytest-invenio  | ❌ Fail | ❌ Fail | ⚠️ Tests still failing after patch |
| `invenio-celery` <br/>  [patched](invenio-celery/test-output-patched.txt) | pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-checks` <br/>  [patched](invenio-checks/test-output-patched.txt) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-collections` <br/>  [patched](invenio-collections/test-output-patched.txt) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-communities` <br/>  [patched](invenio-communities/test-output-patched.txt) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-config` <br/>  [original](invenio-config/test-output-original.txt)  [patched](invenio-config/test-output-patched.txt) | pytest-invenio  | ✅ Pass | ❌ Fail | ❌ Patch introduced test failures |
| `invenio-db` <br/>  [patched](invenio-db/test-output-patched.txt) | pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-drafts-resources` <br/>  [patched](invenio-drafts-resources/test-output-patched.txt) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-files-rest` <br/>  [original](invenio-files-rest/test-output-original.txt)  [patched](invenio-files-rest/test-output-patched.txt) | invenio-db pytest-invenio  | ❌ Fail | ❌ Fail | ⚠️ Tests still failing after patch |
| `invenio-formatter` <br/>  [patched](invenio-formatter/test-output-patched.txt) | pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-github` <br/>  [original](invenio-github/test-output-original.txt)  [patched](invenio-github/test-output-patched.txt) | invenio-db pytest-invenio  | ✅ Pass | ❌ Fail | ❌ Patch introduced test failures |
| `invenio-i18n` <br/>  [patched](invenio-i18n/test-output-patched.txt) | pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-indexer` <br/>  [patched](invenio-indexer/test-output-patched.txt) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-jobs` <br/>  [patched](invenio-jobs/test-output-patched.txt) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-jsonschemas` <br/>  [original](invenio-jsonschemas/test-output-original.txt)  [patched](invenio-jsonschemas/test-output-patched.txt) | pytest-invenio  | ❌ Fail | ❌ Fail | ⚠️ Tests still failing after patch |
| `invenio-logging` <br/>  [patched](invenio-logging/test-output-patched.txt) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-mail` <br/>  [patched](invenio-mail/test-output-patched.txt) | pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-notifications` <br/>  [patched](invenio-notifications/test-output-patched.txt) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-oaiserver` <br/>  [original](invenio-oaiserver/test-output-original.txt)  [patched](invenio-oaiserver/test-output-patched.txt) | invenio-db pytest-invenio  | ❌ Fail | ❌ Fail | ⚠️ Tests still failing after patch |
| `invenio-oauth2server` <br/>  [original](invenio-oauth2server/test-output-original.txt)  [patched](invenio-oauth2server/test-output-patched.txt) | invenio-db pytest-invenio  | ✅ Pass | ❌ Fail | ❌ Patch introduced test failures |
| `invenio-oauthclient` <br/>  [original](invenio-oauthclient/test-output-original.txt)  [patched](invenio-oauthclient/test-output-patched.txt) | invenio-db pytest-invenio  | ❌ Fail | ❌ Fail | ⚠️ Tests still failing after patch |
| `invenio-pages` <br/>  [original](invenio-pages/test-output-original.txt)  [patched](invenio-pages/test-output-patched.txt) | invenio-db pytest-invenio  | ❌ Fail | ❌ Fail | ⚠️ Tests still failing after patch |
| `invenio-pidstore` <br/>  [original](invenio-pidstore/test-output-original.txt)  [patched](invenio-pidstore/test-output-patched.txt) | invenio-db pytest-invenio  | ❌ Fail | ❌ Fail | ⚠️ Tests still failing after patch |
| `invenio-previewer` <br/>  [original](invenio-previewer/test-output-original.txt)  [patched](invenio-previewer/test-output-patched.txt) | invenio-db pytest-invenio  | ✅ Pass | ❌ Fail | ❌ Patch introduced test failures |
| `invenio-queues` <br/>  [original](invenio-queues/test-output-original.txt)  [patched](invenio-queues/test-output-patched.txt) | pytest-invenio  | ✅ Pass | ❌ Fail | ❌ Patch introduced test failures |
| `invenio-rdm-records` <br/>  [original](invenio-rdm-records/test-output-original.txt)  [patched](invenio-rdm-records/test-output-patched.txt) | invenio-db pytest-invenio  | ✅ Pass | ❌ Fail | ❌ Patch introduced test failures |
| `invenio-records-files` <br/>  [patched](invenio-records-files/test-output-patched.txt) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-records-permissions` <br/>  [original](invenio-records-permissions/test-output-original.txt)  [patched](invenio-records-permissions/test-output-patched.txt) | invenio-db pytest-invenio  | ❌ Fail | ❌ Fail | ⚠️ Tests still failing after patch |
| `invenio-records-resources` <br/>  [original](invenio-records-resources/test-output-original.txt)  [patched](invenio-records-resources/test-output-patched.txt) | invenio-db pytest-invenio  | ❌ Fail | ❌ Fail | ⚠️ Tests still failing after patch |
| `invenio-records-rest` <br/>  [original](invenio-records-rest/test-output-original.txt)  [patched](invenio-records-rest/test-output-patched.txt) | invenio-db pytest-invenio  | ✅ Pass | ❌ Fail | ❌ Patch introduced test failures |
| `invenio-records-ui` <br/>  [patched](invenio-records-ui/test-output-patched.txt) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-records` <br/>  [patched](invenio-records/test-output-patched.txt) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-requests` <br/>  [patched](invenio-requests/test-output-patched.txt) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-rest` <br/>  [original](invenio-rest/test-output-original.txt)  [patched](invenio-rest/test-output-patched.txt) | invenio-db pytest-invenio  | ❌ Fail | ❌ Fail | ⚠️ Tests still failing after patch |
| `invenio-search-ui` <br/>  [original](invenio-search-ui/test-output-original.txt)  [patched](invenio-search-ui/test-output-patched.txt) | invenio-db pytest-invenio  | ✅ Pass | ❌ Fail | ❌ Patch introduced test failures |
| `invenio-search` <br/>  [patched](invenio-search/test-output-patched.txt) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-sitemap` <br/>  [original](invenio-sitemap/test-output-original.txt)  [patched](invenio-sitemap/test-output-patched.txt) | invenio-db pytest-invenio  | ❌ Fail | ❌ Fail | ⚠️ Tests still failing after patch |
| `invenio-stats` <br/>  [original](invenio-stats/test-output-original.txt)  [patched](invenio-stats/test-output-patched.txt) | invenio-db pytest-invenio  | ✅ Pass | ❌ Fail | ❌ Patch introduced test failures |
| `invenio-theme` <br/>  [original](invenio-theme/test-output-original.txt)  [patched](invenio-theme/test-output-patched.txt) | pytest-invenio  | ✅ Pass | ❌ Fail | ❌ Patch introduced test failures |
| `invenio-userprofiles` <br/>  [original](invenio-userprofiles/test-output-original.txt)  [patched](invenio-userprofiles/test-output-patched.txt) | invenio-db pytest-invenio  | ❌ Fail | ❌ Fail | ⚠️ Tests still failing after patch |
| `invenio-users-resources` <br/>  [patched](invenio-users-resources/test-output-patched.txt) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-vocabularies` <br/>  [patched](invenio-vocabularies/test-output-patched.txt) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-webhooks` <br/>  [original](invenio-webhooks/test-output-original.txt)  [patched](invenio-webhooks/test-output-patched.txt) | invenio-db pytest-invenio  | ❌ Fail | ❌ Fail | ⚠️ Tests still failing after patch |

---

_For detailed test outputs and diffs, see the [full report](https://mesemus.github.io/invenio-bug-verification/)._
