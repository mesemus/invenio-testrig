# Invenio Bugfix Verification Results

_Last updated: 2025-11-18 09:21:35 UTC_

## 📊 Overall Status

| Metric | Count |
|--------|-------|
| **Total Packages** | 19 |
| **Patched Packages** | 1 |
| **Unpatched Packages** | 18 |

### Patch Results
| Result | Count |
|--------|-------|
| ✅ Fixed | 0 |
| ❌ Regressions | 0 |
| ⚠️  Still Failing | 0 |
| ℹ️  No Change | 1 |

## 🔧 Configured Patches

| Patched Package | Repository | Branch |
|----------------|------------|--------|
| [pytest-invenio](https://github.com/oarepo/pytest-invenio/tree/nested-db-session-rollback) | https://github.com/oarepo/pytest-invenio | nested-db-session-rollback |
| [invenio-files-rest](https://github.com/fenekku/invenio-files-res/tree/support_3.14) | https://github.com/fenekku/invenio-files-res | support_3.14 |

## 🔄 Patched Packages

| Package | Patches Applied | Original | Patched | Result |
|---------|----------------|--------|-------|--------|

## 📦 Packages that do not depend on patched packages

| Package | Build Status |
|---------|--------------|
| `invenio-mail` | ⏭️  Skipped |
| `invenio-queues` | ⏭️  Skipped |
| `invenio-oauthclient` | ⏭️  Skipped |
| `invenio-notifications` | ⏭️  Skipped |
| `invenio-app` | ⏭️  Skipped |
| `invenio-jobs` | ⏭️  Skipped |
| `invenio-assets` | ⏭️  Skipped |
| `invenio-celery` | ⏭️  Skipped |
| `invenio-db` | ⏭️  Skipped |
| `invenio-access` | ⏭️  Skipped |
| `invenio-collections` | ⏭️  Skipped |
| `invenio-records-ui` | ⏭️  Skipped |
| `invenio-previewer` | ⏭️  Skipped |
| `invenio-communities` | ⏭️  Skipped |
| `invenio-files-rest` | ⏭️  Skipped |
| `invenio-checks` | ⏭️  Skipped |
| `invenio-audit-logs` | ⏭️  Skipped |
| `invenio-oauth2server` | ⏭️  Skipped |

## 🔄 Packages that depend on patched packages

| Package | Patches Applied | Original | Patched | Result |
|---------|----------------|--------|-------|--------|
| `invenio-config` <br/> [patched](packages/invenio-config/test-output-patched.txt) [xml-patched](packages/invenio-config/test-report-patched.xml) [warnings-patched](packages/invenio-config/warnings-patched.md) | pytest-invenio | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |

## Collected Warnings

### Patched

#### Warning 1 - 8 occurrences

DeprecationWarning: ast.Str is deprecated and will be removed in Python 3.14; use ast.Constant instead

| Package | Count |
|---------|-------|
| `unknown` | 8 |

#### Warning 2 - 4 occurrences

SyntaxWarning: invalid escape sequence '\_'

| Package | Count |
|---------|-------|
| `unknown` | 4 |

#### Warning 3 - 3 occurrences

SyntaxWarning: invalid escape sequence '\*'

| Package | Count |
|---------|-------|
| `unknown` | 3 |

#### Warning 4 - 2 occurrences

DeprecationWarning: 'pkgutil.get_loader' is deprecated and slated for removal in Python 3.14; use importlib.util.find_spec() instead

| Package | Count |
|---------|-------|
| `unknown` | 2 |

#### Warning 5 - 2 occurrences

UserWarning: Set configuration variable SECRET_KEY with random string

| Package | Count |
|---------|-------|
| `invenio-config` | 1 |
| `unknown` | 1 |

#### Warning 6 - 1 occurrence

DeprecationWarning: 'pkgutil.find_loader' is deprecated and slated for removal in Python 3.14; use importlib.util.find_spec() instead

| Package | Count |
|---------|-------|
| `unknown` | 1 |

#### Warning 7 - 1 occurrence

DeprecationWarning: Attribute s is deprecated and will be removed in Python 3.14; use value instead

| Package | Count |
|---------|-------|
| `unknown` | 1 |

#### Warning 8 - 1 occurrence

DeprecationWarning: Using the initialization functions in flask_caching.backend is deprecated.  Use the a full path to backend classes directly.

| Package | Count |
|---------|-------|
| `unknown` | 1 |

#### Warning 9 - 1 occurrence

DeprecationWarning: ast.NameConstant is deprecated and will be removed in Python 3.14; use ast.Constant instead

| Package | Count |
|---------|-------|
| `unknown` | 1 |

#### Warning 10 - 1 occurrence

SyntaxWarning: "is" with 'str' literal. Did you mean "=="?

| Package | Count |
|---------|-------|
| `unknown` | 1 |

#### Warning 11 - 1 occurrence

SyntaxWarning: invalid escape sequence '\ '

| Package | Count |
|---------|-------|
| `unknown` | 1 |

#### Warning 12 - 1 occurrence

UserWarning: Using the in-memory storage for tracking rate limits as no storage was explicitly specified. This is not recommended for production use. See: https://flask-limiter.readthedocs.io#configuring-a-storage-backend for documentation about configuring the storage backend.

| Package | Count |
|---------|-------|
| `unknown` | 1 |

#### Warning 13 - 1 occurrence

UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.

| Package | Count |
|---------|-------|
| `unknown` | 1 |




---

_For detailed test outputs and diffs, see the [full report](https://mesemus.github.io/invenio-bug-verification/)._