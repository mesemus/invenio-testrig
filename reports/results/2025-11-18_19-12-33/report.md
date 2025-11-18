# Invenio Bugfix Verification Results

> **⏳ Status: Running** - This report is being updated as tests complete.

_Last updated: 2025-11-18 19:13:55 UTC_

## 📊 Overall Status

| Metric | Count |
|--------|-------|
| **Total Packages** | 6 |
| **Patched Packages** | 6 |
| **Unpatched Packages** | 0 |

### Patch Results
| Result | Count |
|--------|-------|
| ✅ Fixed | 0 |
| ❌ Regressions | 0 |
| ⚠️  Still Failing | 0 |
| ℹ️  No Change | 6 |

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
| `invenio-config` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-config/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-config/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-config/test-report-patched.xml)<br>[warnings](packages/invenio-config/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-cache` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-cache/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-cache/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-cache/test-report-patched.xml)<br>[warnings](packages/invenio-cache/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-base` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-base/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-base/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-base/test-report-patched.xml)<br>[warnings](packages/invenio-base/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-assets` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-assets/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-assets/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-assets/test-report-patched.xml) | ✅ Patch applied successfully, tests passed |
| `invenio-search-ui` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-search-ui/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-search-ui/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-search-ui/test-report-patched.xml) | ✅ Patch applied successfully, tests passed |
| `invenio-jsonschemas` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-jsonschemas/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-jsonschemas/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-jsonschemas/test-report-patched.xml)<br>[warnings](packages/invenio-jsonschemas/warnings-patched.md) | ✅ Patch applied successfully, tests passed |

## Collected Warnings

### Patched

#### Warning 1 - 4 occurrences

PytestMockWarning: Mocks returned by pytest-mock do not need to be used as context managers. The mocker fixture automatically undoes mocking at the end of a test. This warning can be ignored if it was triggered by mocking a context manager. https://pytest-mock.readthedocs.io/en/latest/usage.html#usage-as-context-manager

| Package | Count |
|---------|-------|
| `invenio-cache` | 4 |

#### Warning 2 - 1 occurrence

DeprecationWarning: Using the initialization functions in flask_caching.backend is deprecated.  Use the a full path to backend classes directly.

| Package | Count |
|---------|-------|
| `invenio-cache` | 1 |

#### Warning 3 - 1 occurrence

DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).

| Package | Count |
|---------|-------|
| `invenio-cache` | 1 |

#### Warning 4 - 1 occurrence

DeprecationWarning: jsonschema.RefResolver is deprecated as of v4.18.0, in favor of the https://github.com/python-jsonschema/referencing library, which provides more compliant referencing behavior as well as more flexible APIs for customization. A future release will remove RefResolver. Please file a feature request (on referencing) if you are missing an API for the kind of customization you need.

| Package | Count |
|---------|-------|
| `invenio-jsonschemas` | 1 |

#### Warning 5 - 1 occurrence

PendingDeprecationWarning: The WSGI_PROXIES configuration is deprecated and it will be removed, use PROXYFIX_CONFIG instead

| Package | Count |
|---------|-------|
| `invenio-base` | 1 |

#### Warning 6 - 1 occurrence

PytestConfigWarning: Unknown config option: pep8ignore

| Package | Count |
|---------|-------|
| `invenio-jsonschemas` | 1 |

#### Warning 7 - 1 occurrence

UserWarning: Set configuration variable SECRET_KEY with random string

| Package | Count |
|---------|-------|
| `invenio-config` | 1 |

#### Warning 8 - 1 occurrence

UserWarning: Test

| Package | Count |
|---------|-------|
| `invenio-base` | 1 |




---

_For detailed test outputs and diffs, see the [full report](https://mesemus.github.io/invenio-bug-verification/)._