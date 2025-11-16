# Invenio Bugfix Verification Results

_Last updated: 2025-11-16 11:38:59 UTC_

## 📊 Overall Status

| Metric | Count |
|--------|-------|
| **Total Packages** | 52 |
| **Patched Packages** | 37 |
| **Unpatched Packages** | 15 |

### Patch Results
| Result | Count |
|--------|-------|
| ✅ Fixed | 0 |
| ❌ Regressions | 0 |
| ⚠️  Still Failing | 4 |
| ℹ️  No Change | 33 |

## 🔧 Configured Patches

## 🔄 Patched Packages

| Package | Patches Applied | Original | Patched | Result |
|---------|----------------|--------|-------|--------|
| `invenio-db` <br/>  [patched](packages/invenio-db/test-output-patched.txt) | pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |

## 📦 Packages that do not depend on patched packages

| Package | Build Status |
|---------|--------------|
| `null` | ❓ Unknown |
| `null` | ❓ Unknown |
| `null` | ❓ Unknown |
| `null` | ❓ Unknown |
| `null` | ❓ Unknown |
| `null` | ❓ Unknown |
| `null` | ❓ Unknown |
| `null` | ❓ Unknown |
| `null` | ❓ Unknown |
| `null` | ❓ Unknown |
| `null` | ❓ Unknown |
| `null` | ❓ Unknown |
| `null` | ❓ Unknown |
| `null` | ❓ Unknown |
| `null` | ❓ Unknown |

## 🔄 Packages that depend on patched packages

| Package | Patches Applied | Original | Patched | Result |
|---------|----------------|--------|-------|--------|
| `invenio-access` <br/>  [patched](packages/invenio-access/test-output-patched.txt) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-accounts` <br/>  [patched](packages/invenio-accounts/test-output-patched.txt) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-app` <br/>  [patched](packages/invenio-app/test-output-patched.txt) | pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-assets` <br/>  [patched](packages/invenio-assets/test-output-patched.txt) | pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-base` <br/>  [patched](packages/invenio-base/test-output-patched.txt) | pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-cache` <br/>  [patched](packages/invenio-cache/test-output-patched.txt) | pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-celery` <br/>  [patched](packages/invenio-celery/test-output-patched.txt) | pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-checks` <br/>  [patched](packages/invenio-checks/test-output-patched.txt) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-collections` <br/>  [patched](packages/invenio-collections/test-output-patched.txt) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-config` <br/>  [patched](packages/invenio-config/test-output-patched.txt) | pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-db` <br/>  [patched](packages/invenio-db/test-output-patched.txt) | pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-files-rest` <br/>  [original](packages/invenio-files-rest/test-output-original.txt)  [patched](packages/invenio-files-rest/test-output-patched.txt) | invenio-db pytest-invenio  | ❌ Fail | ❌ Fail | ⚠️ Tests still failing after patch |
| `invenio-formatter` <br/>  [patched](packages/invenio-formatter/test-output-patched.txt) | pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-i18n` <br/>  [patched](packages/invenio-i18n/test-output-patched.txt) | pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-indexer` <br/>  [patched](packages/invenio-indexer/test-output-patched.txt) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-jsonschemas` <br/>  [patched](packages/invenio-jsonschemas/test-output-patched.txt) | pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-logging` <br/>  [patched](packages/invenio-logging/test-output-patched.txt) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-mail` <br/>  [patched](packages/invenio-mail/test-output-patched.txt) | pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-notifications` <br/>  [patched](packages/invenio-notifications/test-output-patched.txt) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-oaiserver` <br/>  [patched](packages/invenio-oaiserver/test-output-patched.txt) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-oauth2server` <br/>  [patched](packages/invenio-oauth2server/test-output-patched.txt) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-oauthclient` <br/>  [patched](packages/invenio-oauthclient/test-output-patched.txt) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-pidstore` <br/>  [patched](packages/invenio-pidstore/test-output-patched.txt) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-previewer` <br/>  [patched](packages/invenio-previewer/test-output-patched.txt) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-queues` <br/>  [patched](packages/invenio-queues/test-output-patched.txt) | pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-records-files` <br/>  [original](packages/invenio-records-files/test-output-original.txt)  [patched](packages/invenio-records-files/test-output-patched.txt) | invenio-db pytest-invenio  | ❌ Fail | ❌ Fail | ⚠️ Tests still failing after patch |
| `invenio-records-rest` <br/>  [patched](packages/invenio-records-rest/test-output-patched.txt) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-records-ui` <br/>  [patched](packages/invenio-records-ui/test-output-patched.txt) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-records` <br/>  [patched](packages/invenio-records/test-output-patched.txt) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-rest` <br/>  [patched](packages/invenio-rest/test-output-patched.txt) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-search-ui` <br/>  [patched](packages/invenio-search-ui/test-output-patched.txt) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-search` <br/>  [original](packages/invenio-search/test-output-original.txt)  [patched](packages/invenio-search/test-output-patched.txt) | invenio-db pytest-invenio  | ❌ Fail | ❌ Fail | ⚠️ Tests still failing after patch |
| `invenio-sitemap` <br/>  [patched](packages/invenio-sitemap/test-output-patched.txt) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-stats` <br/>  [original](packages/invenio-stats/test-output-original.txt)  [patched](packages/invenio-stats/test-output-patched.txt) | invenio-db pytest-invenio  | ❌ Fail | ❌ Fail | ⚠️ Tests still failing after patch |
| `invenio-theme` <br/>  [patched](packages/invenio-theme/test-output-patched.txt) | pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-userprofiles` <br/>  [patched](packages/invenio-userprofiles/test-output-patched.txt) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-webhooks` <br/>  [patched](packages/invenio-webhooks/test-output-patched.txt) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |

## Collected Warnings

No warnings found in any package.
---

_For detailed test outputs and diffs, see the [full report](https://mesemus.github.io/invenio-bug-verification/)._
