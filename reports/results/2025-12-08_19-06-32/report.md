# Invenio Bugfix Verification Results

> **⏳ Status: Running** - This report is being updated as tests complete.

_Last updated: 2025-12-08 19:11:38 UTC_

## 📊 Overall Status

| Metric | Count |
|--------|-------|
| **Total Packages** | 47 |
| **Patched Packages** | 12 |
| **Unpatched Packages** | 35 |

### Patch Results
| Result | Count |
|--------|-------|
| ✅ Fixed | 12 |
| ❌ Regressions | 0 |
| ⚠️  Still Failing | 0 |
| ℹ️  No Change | 0 |

## 🔧 Configured Patches

| Patched Package | Repository | Branch |
|----------------|------------|--------|
| [invenio-records-resources](https://github.com/max-moser/invenio-records-resources/tree/mm/failed-file-upload-cleanup) | https://github.com/max-moser/invenio-records-resources | mm/failed-file-upload-cleanup |

## 🔄 Patched Packages

| Package | Patches Applied | Original | Patched | Result |
|---------|----------------|--------|-------|--------|
| `invenio-records-resources` |  | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-records-resources/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-records-resources/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-records-resources/test-report-patched.xml)<br>[warnings](packages/invenio-records-resources/warnings-patched.md) | ✅ Patch applied successfully, tests passed |

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
| `invenio-stats` | ⏭️  Skipped |
| `invenio-userprofiles` | ⏭️  Skipped |
| `invenio-previewer` | ⏭️  Skipped |
| `invenio-search-ui` | ⏭️  Skipped |
| `invenio-records-files` | ⏭️  Skipped |
| `invenio-logging` | ⏭️  Skipped |
| `invenio-sitemap` | ⏭️  Skipped |
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
| `invenio-notifications` | invenio-records-resources | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-notifications/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-notifications/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-notifications/test-report-patched.xml)<br>[warnings](packages/invenio-notifications/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-jobs` | invenio-records-resources | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-jobs/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-jobs/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-jobs/test-report-patched.xml)<br>[warnings](packages/invenio-jobs/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-drafts-resources` | invenio-records-resources | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-drafts-resources/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-drafts-resources/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-drafts-resources/test-report-patched.xml)<br>[warnings](packages/invenio-drafts-resources/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-pages` | invenio-records-resources | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-pages/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-pages/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-pages/test-report-patched.xml)<br>[warnings](packages/invenio-pages/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-collections` | invenio-records-resources | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-collections/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-collections/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-collections/test-report-patched.xml)<br>[warnings](packages/invenio-collections/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-checks` | invenio-records-resources | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-checks/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-checks/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-checks/test-report-patched.xml)<br>[warnings](packages/invenio-checks/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-audit-logs` | invenio-records-resources | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-audit-logs/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-audit-logs/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-audit-logs/test-report-patched.xml)<br>[warnings](packages/invenio-audit-logs/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-administration` | invenio-records-resources | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-administration/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-administration/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-administration/test-report-patched.xml)<br>[warnings](packages/invenio-administration/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-github` | invenio-records-resources | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-github/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-github/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-github/test-report-patched.xml)<br>[warnings](packages/invenio-github/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-users-resources` | invenio-records-resources | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-users-resources/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-users-resources/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-users-resources/test-report-patched.xml)<br>[warnings](packages/invenio-users-resources/warnings-patched.md) | ✅ Patch applied successfully, tests passed |

## Collected Warnings

### Patched

#### Warning 1 - 65 occurrences

DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).

| Package | Count |
|---------|-------|
| `invenio-users-resources` | 11 |
| `invenio-drafts-resources` | 7 |
| `invenio-jobs` | 7 |
| `invenio-records-resources` | 7 |
| `invenio-audit-logs` | 6 |
| `invenio-banners` | 6 |
| `invenio-collections` | 6 |
| `invenio-github` | 6 |
| `invenio-pages` | 6 |
| `invenio-administration` | 3 |

#### Warning 2 - 25 occurrences

RemovedInMarshmallow4Warning: The `context` parameter is deprecated and will be removed in marshmallow 4.0. Use `contextvars.ContextVar` to pass context instead.

| Package | Count |
|---------|-------|
| `invenio-jobs` | 4 |
| `invenio-audit-logs` | 3 |
| `invenio-collections` | 3 |
| `invenio-drafts-resources` | 3 |
| `invenio-records-resources` | 3 |
| `invenio-users-resources` | 3 |
| `invenio-banners` | 2 |
| `invenio-checks` | 2 |
| `invenio-pages` | 2 |

#### Warning 3 - 23 occurrences

DeprecationWarning: jsonschema.RefResolver is deprecated as of v4.18.0, in favor of the https://github.com/python-jsonschema/referencing library, which provides more compliant referencing behavior as well as more flexible APIs for customization. A future release will remove RefResolver. Please file a feature request (on referencing) if you are missing an API for the kind of customization you need.

| Package | Count |
|---------|-------|
| `invenio-collections` | 3 |
| `invenio-administration` | 2 |
| `invenio-audit-logs` | 2 |
| `invenio-banners` | 2 |
| `invenio-checks` | 2 |
| `invenio-drafts-resources` | 2 |
| `invenio-jobs` | 2 |
| `invenio-notifications` | 2 |
| `invenio-pages` | 2 |
| `invenio-records-resources` | 2 |
| `invenio-users-resources` | 2 |

#### Warning 4 - 22 occurrences

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
| `invenio-records-resources` | 2 |
| `invenio-users-resources` | 2 |

#### Warning 5 - 12 occurrences

DeprecationWarning: 'crypt' is deprecated and slated for removal in Python 3.13

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-banners` | 1 |
| `invenio-checks` | 1 |
| `invenio-collections` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-github` | 1 |
| `invenio-jobs` | 1 |
| `invenio-notifications` | 1 |
| `invenio-pages` | 1 |
| `invenio-records-resources` | 1 |
| `invenio-users-resources` | 1 |

#### Warning 6 - 12 occurrences

RemovedInMarshmallow4Warning: The 'default' argument to fields is deprecated. Use 'dump_default' instead.

| Package | Count |
|---------|-------|
| `invenio-checks` | 2 |
| `invenio-jobs` | 2 |
| `invenio-administration` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-banners` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-notifications` | 1 |
| `invenio-pages` | 1 |
| `invenio-records-resources` | 1 |
| `invenio-users-resources` | 1 |

#### Warning 7 - 12 occurrences

UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.

| Package | Count |
|---------|-------|
| `invenio-collections` | 2 |
| `invenio-administration` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-banners` | 1 |
| `invenio-checks` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-jobs` | 1 |
| `invenio-notifications` | 1 |
| `invenio-pages` | 1 |
| `invenio-records-resources` | 1 |
| `invenio-users-resources` | 1 |

#### Warning 8 - 11 occurrences

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
| `invenio-records-resources` | 1 |
| `invenio-users-resources` | 1 |

#### Warning 9 - 11 occurrences

DeprecationWarning: Deprecated call to `pkg_resources.declare_namespace('sphinxcontrib')`.

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
| `invenio-records-resources` | 1 |
| `invenio-users-resources` | 1 |

#### Warning 10 - 11 occurrences

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
| `invenio-records-resources` | 1 |
| `invenio-users-resources` | 1 |

#### Warning 11 - 11 occurrences

DeprecationWarning: jsonschema.exceptions.RefResolutionError is deprecated as of version 4.18.0. If you wish to catch potential reference resolution errors, directly catch referencing.exceptions.Unresolvable.

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
| `invenio-records-resources` | 1 |
| `invenio-users-resources` | 1 |

#### Warning 12 - 10 occurrences

DeprecationWarning: Using the initialization functions in flask_caching.backend is deprecated.  Use the a full path to backend classes directly.

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-banners` | 1 |
| `invenio-collections` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-github` | 1 |
| `invenio-jobs` | 1 |
| `invenio-pages` | 1 |
| `invenio-records-resources` | 1 |
| `invenio-users-resources` | 1 |

#### Warning 13 - 10 occurrences

FutureWarning: CSRF validation will be enabled by default in the version 1.3.x

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-banners` | 1 |
| `invenio-collections` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-github` | 1 |
| `invenio-jobs` | 1 |
| `invenio-pages` | 1 |
| `invenio-records-resources` | 1 |
| `invenio-users-resources` | 1 |

#### Warning 14 - 9 occurrences

DeprecationWarning: Link is deprecated and will be removed in v14.0. Use `ExternalLink` for third-party links and `EndpointLink` for InvenioRDM links.

| Package | Count |
|---------|-------|
| `invenio-audit-logs` | 1 |
| `invenio-banners` | 1 |
| `invenio-checks` | 1 |
| `invenio-collections` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-jobs` | 1 |
| `invenio-pages` | 1 |
| `invenio-records-resources` | 1 |
| `invenio-users-resources` | 1 |

#### Warning 15 - 8 occurrences

SAWarning: nested transaction already deassociated from connection

| Package | Count |
|---------|-------|
| `invenio-pages` | 6 |
| `invenio-collections` | 2 |

#### Warning 16 - 5 occurrences

LegacyAPIWarning: The Query.get() method is considered legacy as of the 1.x series of SQLAlchemy and becomes a legacy construct in 2.0. The method is now available as Session.get() (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)

| Package | Count |
|---------|-------|
| `invenio-collections` | 2 |
| `invenio-jobs` | 1 |
| `invenio-records-resources` | 1 |
| `invenio-users-resources` | 1 |

#### Warning 17 - 4 occurrences

DeprecationWarning: The 'warn' method is deprecated, use 'warning' instead

| Package | Count |
|---------|-------|
| `invenio-users-resources` | 2 |
| `invenio-drafts-resources` | 1 |
| `invenio-records-resources` | 1 |

#### Warning 18 - 4 occurrences

DeprecationWarning: datetime.datetime.utcfromtimestamp() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.fromtimestamp(timestamp, datetime.UTC).

| Package | Count |
|---------|-------|
| `invenio-banners` | 1 |
| `invenio-github` | 1 |
| `invenio-pages` | 1 |
| `invenio-users-resources` | 1 |

#### Warning 19 - 3 occurrences

ChangedInMarshmallow4Warning: `Field` should not be instantiated. Use `fields.Raw` or  another field subclass instead.

| Package | Count |
|---------|-------|
| `invenio-checks` | 1 |
| `invenio-collections` | 1 |
| `invenio-jobs` | 1 |

#### Warning 20 - 3 occurrences

DeprecationWarning: get_user method is deprecated, user get_user_by_email/get_user_by_id

| Package | Count |
|---------|-------|
| `invenio-banners` | 1 |
| `invenio-pages` | 1 |
| `invenio-users-resources` | 1 |

#### Warning 21 - 2 occurrences

DeprecationWarning: Implicit imports (e.g., 'import idutils; idutils.function;') might be removed in the next major version. Please use explicit imports (e.g., 'from idutils import function;') instead.

| Package | Count |
|---------|-------|
| `invenio-checks` | 1 |
| `invenio-collections` | 1 |

#### Warning 22 - 2 occurrences

DeprecationWarning: The 'record_to_index' function is no longer expected to return a tuple (index, doc_type), instead it should only return the index. Support for the tuple will be removed in a future version of 'invenio-indexer'.

| Package | Count |
|---------|-------|
| `invenio-drafts-resources` | 1 |
| `invenio-records-resources` | 1 |

#### Warning 23 - 2 occurrences

DeprecationWarning: distutils Version classes are deprecated. Use packaging.version instead.

| Package | Count |
|---------|-------|
| `invenio-collections` | 2 |

#### Warning 24 - 2 occurrences

RemovedInMarshmallow4Warning: The 'missing' argument to fields is deprecated. Use 'load_default' instead.

| Package | Count |
|---------|-------|
| `invenio-drafts-resources` | 1 |
| `invenio-records-resources` | 1 |

#### Warning 25 - 2 occurrences

SAWarning: Object of type <ObjectVersion> not in session, add operation along 'Bucket.objects' will not proceed (This warning originated from the Session 'autoflush' process, which was invoked automatically in response to a user-initiated operation. Consider using ``no_autoflush`` context manager if this warning happened while initializing objects.)

| Package | Count |
|---------|-------|
| `invenio-drafts-resources` | 1 |
| `invenio-records-resources` | 1 |

#### Warning 26 - 1 occurrence

DeprecationWarning: No path_separator found in configuration; falling back to legacy splitting on spaces/commas for version_locations.  Consider adding path_separator=os to Alembic config.

| Package | Count |
|---------|-------|
| `invenio-audit-logs` | 1 |

#### Warning 27 - 1 occurrence

DeprecationWarning: Remember me support has been removed.

| Package | Count |
|---------|-------|
| `invenio-audit-logs` | 1 |

#### Warning 28 - 1 occurrence

DeprecationWarning: The '__version__' attribute is deprecated and will be removed in in a future version. Use feature detection or 'importlib.metadata.version("marshmallow")' instead.

| Package | Count |
|---------|-------|
| `invenio-collections` | 1 |

#### Warning 29 - 1 occurrence

DeprecationWarning: The configuration value 'RDM_FILES_DEFAULT_MAX_FILE_SIZE' is not set. In future, please set it explicitly to define your max file size, or be aware that the default value used i.e. FILES_REST_DEFAULT_MAX_FILE_SIZE will be 10 * (10**9) (10 GB).

| Package | Count |
|---------|-------|
| `invenio-collections` | 1 |

#### Warning 30 - 1 occurrence

DeprecationWarning: The configuration value 'RDM_FILES_DEFAULT_QUOTA_SIZE' is not set. In future, please set it explicitly to define your quota size, or be aware that the default value used i.e. FILES_REST_DEFAULT_QUOTA_SIZE will be 10 * (10**9) (10 GB).

| Package | Count |
|---------|-------|
| `invenio-collections` | 1 |

#### Warning 31 - 1 occurrence

DeprecationWarning: subject_nested is deprecated. Use subject_combined instead.

| Package | Count |
|---------|-------|
| `invenio-collections` | 1 |

#### Warning 32 - 1 occurrence

PytestCollectionWarning: cannot collect test class 'TestCustomView' because it has a __init__ constructor (from: tests/test_base.py)

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |

#### Warning 33 - 1 occurrence

PytestCollectionWarning: cannot collect test class 'TestSchema' because it has a __init__ constructor (from: tests/test_marshmallow_utils.py)

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |

#### Warning 34 - 1 occurrence

SADeprecationWarning: The from_engine() method on Inspector is deprecated and will be removed in a future release.  Please use the sqlalchemy.inspect() function on an Engine or Connection in order to acquire an Inspector. (deprecated since: 1.4)

| Package | Count |
|---------|-------|
| `invenio-audit-logs` | 1 |

#### Warning 35 - 1 occurrence

SAWarning: Identity map already had an identity for (<class 'invenio_jobs.models.Run'>, (UUID('0c18692c-9c22-4eb2-9d9e-2758fa7ecbf2'),), None), replacing it with newly flushed object.   Are there load operations occurring inside of an event handler within the flush?

| Package | Count |
|---------|-------|
| `invenio-jobs` | 1 |

#### Warning 36 - 1 occurrence

SAWarning: Identity map already had an identity for (<class 'invenio_jobs.models.Run'>, (UUID('1ec37309-a725-40fa-b6f5-226cc4779184'),), None), replacing it with newly flushed object.   Are there load operations occurring inside of an event handler within the flush?

| Package | Count |
|---------|-------|
| `invenio-jobs` | 1 |

#### Warning 37 - 1 occurrence

SAWarning: Identity map already had an identity for (<class 'invenio_jobs.models.Run'>, (UUID('2bd0a543-d6f3-4859-ad47-9bfcb1841fee'),), None), replacing it with newly flushed object.   Are there load operations occurring inside of an event handler within the flush?

| Package | Count |
|---------|-------|
| `invenio-jobs` | 1 |

#### Warning 38 - 1 occurrence

SAWarning: Identity map already had an identity for (<class 'invenio_jobs.models.Run'>, (UUID('4232d756-47d1-416a-856f-a72837f288db'),), None), replacing it with newly flushed object.   Are there load operations occurring inside of an event handler within the flush?

| Package | Count |
|---------|-------|
| `invenio-jobs` | 1 |

#### Warning 39 - 1 occurrence

SAWarning: Identity map already had an identity for (<class 'invenio_jobs.models.Run'>, (UUID('70e32b8c-9b27-4d8e-8c6a-3d1f20bbf211'),), None), replacing it with newly flushed object.   Are there load operations occurring inside of an event handler within the flush?

| Package | Count |
|---------|-------|
| `invenio-jobs` | 1 |

#### Warning 40 - 1 occurrence

SAWarning: Identity map already had an identity for (<class 'invenio_jobs.models.Run'>, (UUID('8c58b727-d2fa-4d82-83c2-0aa6ae9d19b1'),), None), replacing it with newly flushed object.   Are there load operations occurring inside of an event handler within the flush?

| Package | Count |
|---------|-------|
| `invenio-jobs` | 1 |

#### Warning 41 - 1 occurrence

SAWarning: Identity map already had an identity for (<class 'invenio_jobs.models.Run'>, (UUID('e3f58fe3-a3ed-46fb-b581-d6c92c1f4a9e'),), None), replacing it with newly flushed object.   Are there load operations occurring inside of an event handler within the flush?

| Package | Count |
|---------|-------|
| `invenio-jobs` | 1 |

#### Warning 42 - 1 occurrence

SAWarning: This declarative base already contains a class with the same class name and module name as invenio_records_resources.factories.factory.MyRecordMetadata, and will be replaced in the string-lookup table.

| Package | Count |
|---------|-------|
| `invenio-records-resources` | 1 |

#### Warning 43 - 1 occurrence

UserWarning: Please specify the OAISERVER_ID_PREFIX configuration.default value is: oai:runnervmoqczp:

| Package | Count |
|---------|-------|
| `invenio-collections` | 1 |

#### Warning 44 - 1 occurrence

UserWarning: autoincrement and existing_autoincrement only make sense for MySQL

| Package | Count |
|---------|-------|
| `invenio-audit-logs` | 1 |




---