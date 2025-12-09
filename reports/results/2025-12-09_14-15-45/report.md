# Invenio Bugfix Verification Results

> **⏳ Status: Running** - This report is being updated as tests complete.

_Last updated: 2025-12-09 14:18:56 UTC_

## 📊 Overall Status

| Metric | Count |
|--------|-------|
| **Total Packages** | 39 |
| **Patched Packages** | 6 |
| **Unpatched Packages** | 33 |

### Patch Results
| Result | Count |
|--------|-------|
| ✅ Fixed | 6 |
| ❌ Regressions | 0 |
| ⚠️  Still Failing | 0 |
| ℹ️  No Change | 0 |

## 🔧 Configured Patches

| Patched Package | Repository | Branch |
|----------------|------------|--------|
| [invenio-records-resources](https://github.com/max-moser/invenio-records-resources/tree/mm/failed-file-upload-cleanup) | https://github.com/max-moser/invenio-records-resources | mm/failed-file-upload-cleanup |
| [invenio-rdm-records](https://github.com/max-moser/invenio-rdm-records/tree/mm/revert-file-test) | https://github.com/max-moser/invenio-rdm-records | mm/revert-file-test |

## 🔄 Patched Packages

| Package | Patches Applied | Original | Patched | Result |
|---------|----------------|--------|-------|--------|

## 📦 Packages that do not depend on patched packages

| Package | Build Status |
|---------|--------------|
| `invenio-mail` | ⏭️  Skipped |
| `invenio-config` | ⏭️  Skipped |
| `invenio-queues` | ⏭️  Skipped |
| `invenio-oauthclient` | ⏭️  Skipped |
| `invenio-cache` | ⏭️  Skipped |
| `invenio-base` | ⏭️  Skipped |
| `invenio-app` | ⏭️  Skipped |
| `invenio-theme` | ⏭️  Skipped |
| `invenio-assets` | ⏭️  Skipped |
| `invenio-celery` | ⏭️  Skipped |
| `invenio-pidstore` | ⏭️  Skipped |
| `invenio-db` | ⏭️  Skipped |
| `invenio-indexer` | ⏭️  Skipped |
| `invenio-oaiserver` | ⏭️  Skipped |
| `invenio-access` | ⏭️  Skipped |
| `invenio-rest` | ⏭️  Skipped |
| `invenio-records-permissions` | ⏭️  Skipped |
| `invenio-records-ui` | ⏭️  Skipped |
| `invenio-userprofiles` | ⏭️  Skipped |
| `invenio-previewer` | ⏭️  Skipped |
| `invenio-search-ui` | ⏭️  Skipped |
| `invenio-records-files` | ⏭️  Skipped |
| `invenio-logging` | ⏭️  Skipped |
| `invenio-files-rest` | ⏭️  Skipped |
| `invenio-formatter` | ⏭️  Skipped |
| `invenio-records-rest` | ⏭️  Skipped |
| `invenio-i18n` | ⏭️  Skipped |
| `invenio-oauth2server` | ⏭️  Skipped |
| `invenio-jsonschemas` | ⏭️  Skipped |
| `invenio-search` | ⏭️  Skipped |
| `invenio-accounts` | ⏭️  Skipped |
| `invenio-webhooks` | ⏭️  Skipped |
| `invenio-records` | ⏭️  Skipped |

## 🔄 Packages that depend on patched packages

| Package | Patches Applied | Original | Patched | Result |
|---------|----------------|--------|-------|--------|
| `invenio-banners` | invenio-records-resources | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-banners/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-banners/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-banners/test-report-patched.xml)<br>[warnings](packages/invenio-banners/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-jobs` | invenio-records-resources | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-jobs/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-jobs/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-jobs/test-report-patched.xml)<br>[warnings](packages/invenio-jobs/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-pages` | invenio-records-resources | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-pages/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-pages/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-pages/test-report-patched.xml)<br>[warnings](packages/invenio-pages/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-audit-logs` | invenio-records-resources | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-audit-logs/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-audit-logs/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-audit-logs/test-report-patched.xml)<br>[warnings](packages/invenio-audit-logs/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-administration` | invenio-records-resources | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-administration/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-administration/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-administration/test-report-patched.xml)<br>[warnings](packages/invenio-administration/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-github` | invenio-records-resources | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-github/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-github/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-github/test-report-patched.xml)<br>[warnings](packages/invenio-github/warnings-patched.md) | ✅ Patch applied successfully, tests passed |

## Collected Warnings

### Patched

#### Warning 1 - 34 occurrences

DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).

| Package | Count |
|---------|-------|
| `invenio-jobs` | 7 |
| `invenio-audit-logs` | 6 |
| `invenio-banners` | 6 |
| `invenio-github` | 6 |
| `invenio-pages` | 6 |
| `invenio-administration` | 3 |

#### Warning 2 - 11 occurrences

RemovedInMarshmallow4Warning: The `context` parameter is deprecated and will be removed in marshmallow 4.0. Use `contextvars.ContextVar` to pass context instead.

| Package | Count |
|---------|-------|
| `invenio-jobs` | 4 |
| `invenio-audit-logs` | 3 |
| `invenio-banners` | 2 |
| `invenio-pages` | 2 |

#### Warning 3 - 10 occurrences

DeprecationWarning: Deprecated call to `pkg_resources.declare_namespace('fs')`.

| Package | Count |
|---------|-------|
| `invenio-administration` | 2 |
| `invenio-audit-logs` | 2 |
| `invenio-banners` | 2 |
| `invenio-jobs` | 2 |
| `invenio-pages` | 2 |

#### Warning 4 - 10 occurrences

DeprecationWarning: jsonschema.RefResolver is deprecated as of v4.18.0, in favor of the https://github.com/python-jsonschema/referencing library, which provides more compliant referencing behavior as well as more flexible APIs for customization. A future release will remove RefResolver. Please file a feature request (on referencing) if you are missing an API for the kind of customization you need.

| Package | Count |
|---------|-------|
| `invenio-administration` | 2 |
| `invenio-audit-logs` | 2 |
| `invenio-banners` | 2 |
| `invenio-jobs` | 2 |
| `invenio-pages` | 2 |

#### Warning 5 - 6 occurrences

DeprecationWarning: 'crypt' is deprecated and slated for removal in Python 3.13

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-banners` | 1 |
| `invenio-github` | 1 |
| `invenio-jobs` | 1 |
| `invenio-pages` | 1 |

#### Warning 6 - 6 occurrences

DeprecationWarning: Using the initialization functions in flask_caching.backend is deprecated.  Use the a full path to backend classes directly.

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-banners` | 1 |
| `invenio-github` | 1 |
| `invenio-jobs` | 1 |
| `invenio-pages` | 1 |

#### Warning 7 - 6 occurrences

FutureWarning: CSRF validation will be enabled by default in the version 1.3.x

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-banners` | 1 |
| `invenio-github` | 1 |
| `invenio-jobs` | 1 |
| `invenio-pages` | 1 |

#### Warning 8 - 6 occurrences

RemovedInMarshmallow4Warning: The 'default' argument to fields is deprecated. Use 'dump_default' instead.

| Package | Count |
|---------|-------|
| `invenio-jobs` | 2 |
| `invenio-administration` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-banners` | 1 |
| `invenio-pages` | 1 |

#### Warning 9 - 6 occurrences

SAWarning: nested transaction already deassociated from connection

| Package | Count |
|---------|-------|
| `invenio-pages` | 6 |

#### Warning 10 - 5 occurrences

DeprecationWarning: Deprecated call to `pkg_resources.declare_namespace('fs.opener')`.

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-banners` | 1 |
| `invenio-jobs` | 1 |
| `invenio-pages` | 1 |

#### Warning 11 - 5 occurrences

DeprecationWarning: Deprecated call to `pkg_resources.declare_namespace('sphinxcontrib')`.

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-banners` | 1 |
| `invenio-jobs` | 1 |
| `invenio-pages` | 1 |

#### Warning 12 - 5 occurrences

DeprecationWarning: The '__version_info__' attribute is deprecated and will be removed in in a future version. Use feature detection or 'packaging.Version(importlib.metadata.version("marshmallow")).release' instead.

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-banners` | 1 |
| `invenio-jobs` | 1 |
| `invenio-pages` | 1 |

#### Warning 13 - 5 occurrences

DeprecationWarning: jsonschema.exceptions.RefResolutionError is deprecated as of version 4.18.0. If you wish to catch potential reference resolution errors, directly catch referencing.exceptions.Unresolvable.

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-banners` | 1 |
| `invenio-jobs` | 1 |
| `invenio-pages` | 1 |

#### Warning 14 - 5 occurrences

UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-banners` | 1 |
| `invenio-jobs` | 1 |
| `invenio-pages` | 1 |

#### Warning 15 - 4 occurrences

DeprecationWarning: Link is deprecated and will be removed in v14.0. Use `ExternalLink` for third-party links and `EndpointLink` for InvenioRDM links.

| Package | Count |
|---------|-------|
| `invenio-audit-logs` | 1 |
| `invenio-banners` | 1 |
| `invenio-jobs` | 1 |
| `invenio-pages` | 1 |

#### Warning 16 - 3 occurrences

DeprecationWarning: datetime.datetime.utcfromtimestamp() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.fromtimestamp(timestamp, datetime.UTC).

| Package | Count |
|---------|-------|
| `invenio-banners` | 1 |
| `invenio-github` | 1 |
| `invenio-pages` | 1 |

#### Warning 17 - 2 occurrences

DeprecationWarning: get_user method is deprecated, user get_user_by_email/get_user_by_id

| Package | Count |
|---------|-------|
| `invenio-banners` | 1 |
| `invenio-pages` | 1 |

#### Warning 18 - 1 occurrence

ChangedInMarshmallow4Warning: `Field` should not be instantiated. Use `fields.Raw` or  another field subclass instead.

| Package | Count |
|---------|-------|
| `invenio-jobs` | 1 |

#### Warning 19 - 1 occurrence

DeprecationWarning: No path_separator found in configuration; falling back to legacy splitting on spaces/commas for version_locations.  Consider adding path_separator=os to Alembic config.

| Package | Count |
|---------|-------|
| `invenio-audit-logs` | 1 |

#### Warning 20 - 1 occurrence

DeprecationWarning: Remember me support has been removed.

| Package | Count |
|---------|-------|
| `invenio-audit-logs` | 1 |

#### Warning 21 - 1 occurrence

LegacyAPIWarning: The Query.get() method is considered legacy as of the 1.x series of SQLAlchemy and becomes a legacy construct in 2.0. The method is now available as Session.get() (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)

| Package | Count |
|---------|-------|
| `invenio-jobs` | 1 |

#### Warning 22 - 1 occurrence

PytestCollectionWarning: cannot collect test class 'TestCustomView' because it has a __init__ constructor (from: tests/test_base.py)

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |

#### Warning 23 - 1 occurrence

PytestCollectionWarning: cannot collect test class 'TestSchema' because it has a __init__ constructor (from: tests/test_marshmallow_utils.py)

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |

#### Warning 24 - 1 occurrence

SADeprecationWarning: The from_engine() method on Inspector is deprecated and will be removed in a future release.  Please use the sqlalchemy.inspect() function on an Engine or Connection in order to acquire an Inspector. (deprecated since: 1.4)

| Package | Count |
|---------|-------|
| `invenio-audit-logs` | 1 |

#### Warning 25 - 1 occurrence

SAWarning: Identity map already had an identity for (<class 'invenio_jobs.models.Run'>, (UUID('00f3f6f0-618f-4446-868c-2ee95bd1a5bd'),), None), replacing it with newly flushed object.   Are there load operations occurring inside of an event handler within the flush?

| Package | Count |
|---------|-------|
| `invenio-jobs` | 1 |

#### Warning 26 - 1 occurrence

SAWarning: Identity map already had an identity for (<class 'invenio_jobs.models.Run'>, (UUID('14597911-df8d-4478-96a3-62974b9e82fd'),), None), replacing it with newly flushed object.   Are there load operations occurring inside of an event handler within the flush?

| Package | Count |
|---------|-------|
| `invenio-jobs` | 1 |

#### Warning 27 - 1 occurrence

SAWarning: Identity map already had an identity for (<class 'invenio_jobs.models.Run'>, (UUID('427d3dd6-4b49-4df7-85a6-ff1b49cd91d6'),), None), replacing it with newly flushed object.   Are there load operations occurring inside of an event handler within the flush?

| Package | Count |
|---------|-------|
| `invenio-jobs` | 1 |

#### Warning 28 - 1 occurrence

SAWarning: Identity map already had an identity for (<class 'invenio_jobs.models.Run'>, (UUID('8c2aef9d-dbc0-402a-b68f-46837a516f34'),), None), replacing it with newly flushed object.   Are there load operations occurring inside of an event handler within the flush?

| Package | Count |
|---------|-------|
| `invenio-jobs` | 1 |

#### Warning 29 - 1 occurrence

SAWarning: Identity map already had an identity for (<class 'invenio_jobs.models.Run'>, (UUID('c5e93b6e-cb14-4fdf-9625-698068173a4f'),), None), replacing it with newly flushed object.   Are there load operations occurring inside of an event handler within the flush?

| Package | Count |
|---------|-------|
| `invenio-jobs` | 1 |

#### Warning 30 - 1 occurrence

SAWarning: Identity map already had an identity for (<class 'invenio_jobs.models.Run'>, (UUID('d2bb65fc-82f1-491b-b09b-edf6a46a6ea7'),), None), replacing it with newly flushed object.   Are there load operations occurring inside of an event handler within the flush?

| Package | Count |
|---------|-------|
| `invenio-jobs` | 1 |

#### Warning 31 - 1 occurrence

SAWarning: Identity map already had an identity for (<class 'invenio_jobs.models.Run'>, (UUID('e0387eea-6f89-4b27-be8c-7639d67d3aa1'),), None), replacing it with newly flushed object.   Are there load operations occurring inside of an event handler within the flush?

| Package | Count |
|---------|-------|
| `invenio-jobs` | 1 |

#### Warning 32 - 1 occurrence

UserWarning: autoincrement and existing_autoincrement only make sense for MySQL

| Package | Count |
|---------|-------|
| `invenio-audit-logs` | 1 |




---