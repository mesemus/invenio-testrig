# Invenio Bugfix Verification Results

> **⏳ Status: Running** - This report is being updated as tests complete.

_Last updated: 2025-12-08 19:08:44 UTC_

## 📊 Overall Status

| Metric | Count |
|--------|-------|
| **Total Packages** | 25 |
| **Patched Packages** | 3 |
| **Unpatched Packages** | 22 |

### Patch Results
| Result | Count |
|--------|-------|
| ✅ Fixed | 3 |
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

## 📦 Packages that do not depend on patched packages

| Package | Build Status |
|---------|--------------|
| `invenio-mail` | ⏭️  Skipped |
| `invenio-config` | ⏭️  Skipped |
| `invenio-queues` | ⏭️  Skipped |
| `invenio-cache` | ⏭️  Skipped |
| `invenio-base` | ⏭️  Skipped |
| `invenio-app` | ⏭️  Skipped |
| `invenio-theme` | ⏭️  Skipped |
| `invenio-assets` | ⏭️  Skipped |
| `invenio-pidstore` | ⏭️  Skipped |
| `invenio-indexer` | ⏭️  Skipped |
| `invenio-access` | ⏭️  Skipped |
| `invenio-records-ui` | ⏭️  Skipped |
| `invenio-userprofiles` | ⏭️  Skipped |
| `invenio-previewer` | ⏭️  Skipped |
| `invenio-search-ui` | ⏭️  Skipped |
| `invenio-logging` | ⏭️  Skipped |
| `invenio-formatter` | ⏭️  Skipped |
| `invenio-records-rest` | ⏭️  Skipped |
| `invenio-oauth2server` | ⏭️  Skipped |
| `invenio-jsonschemas` | ⏭️  Skipped |
| `invenio-accounts` | ⏭️  Skipped |
| `invenio-records` | ⏭️  Skipped |

## 🔄 Packages that depend on patched packages

| Package | Patches Applied | Original | Patched | Result |
|---------|----------------|--------|-------|--------|
| `invenio-banners` | invenio-records-resources | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-banners/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-banners/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-banners/test-report-patched.xml)<br>[warnings](packages/invenio-banners/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-jobs` | invenio-records-resources | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-jobs/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-jobs/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-jobs/test-report-patched.xml)<br>[warnings](packages/invenio-jobs/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-github` | invenio-records-resources | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-github/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-github/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-github/test-report-patched.xml)<br>[warnings](packages/invenio-github/warnings-patched.md) | ✅ Patch applied successfully, tests passed |

## Collected Warnings

### Patched

#### Warning 1 - 19 occurrences

DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).

| Package | Count |
|---------|-------|
| `invenio-jobs` | 7 |
| `invenio-banners` | 6 |
| `invenio-github` | 6 |

#### Warning 2 - 6 occurrences

RemovedInMarshmallow4Warning: The `context` parameter is deprecated and will be removed in marshmallow 4.0. Use `contextvars.ContextVar` to pass context instead.

| Package | Count |
|---------|-------|
| `invenio-jobs` | 4 |
| `invenio-banners` | 2 |

#### Warning 3 - 4 occurrences

DeprecationWarning: Deprecated call to `pkg_resources.declare_namespace('fs')`.

| Package | Count |
|---------|-------|
| `invenio-banners` | 2 |
| `invenio-jobs` | 2 |

#### Warning 4 - 4 occurrences

DeprecationWarning: jsonschema.RefResolver is deprecated as of v4.18.0, in favor of the https://github.com/python-jsonschema/referencing library, which provides more compliant referencing behavior as well as more flexible APIs for customization. A future release will remove RefResolver. Please file a feature request (on referencing) if you are missing an API for the kind of customization you need.

| Package | Count |
|---------|-------|
| `invenio-banners` | 2 |
| `invenio-jobs` | 2 |

#### Warning 5 - 3 occurrences

DeprecationWarning: 'crypt' is deprecated and slated for removal in Python 3.13

| Package | Count |
|---------|-------|
| `invenio-banners` | 1 |
| `invenio-github` | 1 |
| `invenio-jobs` | 1 |

#### Warning 6 - 3 occurrences

DeprecationWarning: Using the initialization functions in flask_caching.backend is deprecated.  Use the a full path to backend classes directly.

| Package | Count |
|---------|-------|
| `invenio-banners` | 1 |
| `invenio-github` | 1 |
| `invenio-jobs` | 1 |

#### Warning 7 - 3 occurrences

FutureWarning: CSRF validation will be enabled by default in the version 1.3.x

| Package | Count |
|---------|-------|
| `invenio-banners` | 1 |
| `invenio-github` | 1 |
| `invenio-jobs` | 1 |

#### Warning 8 - 3 occurrences

RemovedInMarshmallow4Warning: The 'default' argument to fields is deprecated. Use 'dump_default' instead.

| Package | Count |
|---------|-------|
| `invenio-jobs` | 2 |
| `invenio-banners` | 1 |

#### Warning 9 - 2 occurrences

DeprecationWarning: Deprecated call to `pkg_resources.declare_namespace('fs.opener')`.

| Package | Count |
|---------|-------|
| `invenio-banners` | 1 |
| `invenio-jobs` | 1 |

#### Warning 10 - 2 occurrences

DeprecationWarning: Deprecated call to `pkg_resources.declare_namespace('sphinxcontrib')`.

| Package | Count |
|---------|-------|
| `invenio-banners` | 1 |
| `invenio-jobs` | 1 |

#### Warning 11 - 2 occurrences

DeprecationWarning: Link is deprecated and will be removed in v14.0. Use `ExternalLink` for third-party links and `EndpointLink` for InvenioRDM links.

| Package | Count |
|---------|-------|
| `invenio-banners` | 1 |
| `invenio-jobs` | 1 |

#### Warning 12 - 2 occurrences

DeprecationWarning: The '__version_info__' attribute is deprecated and will be removed in in a future version. Use feature detection or 'packaging.Version(importlib.metadata.version("marshmallow")).release' instead.

| Package | Count |
|---------|-------|
| `invenio-banners` | 1 |
| `invenio-jobs` | 1 |

#### Warning 13 - 2 occurrences

DeprecationWarning: datetime.datetime.utcfromtimestamp() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.fromtimestamp(timestamp, datetime.UTC).

| Package | Count |
|---------|-------|
| `invenio-banners` | 1 |
| `invenio-github` | 1 |

#### Warning 14 - 2 occurrences

DeprecationWarning: jsonschema.exceptions.RefResolutionError is deprecated as of version 4.18.0. If you wish to catch potential reference resolution errors, directly catch referencing.exceptions.Unresolvable.

| Package | Count |
|---------|-------|
| `invenio-banners` | 1 |
| `invenio-jobs` | 1 |

#### Warning 15 - 2 occurrences

UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.

| Package | Count |
|---------|-------|
| `invenio-banners` | 1 |
| `invenio-jobs` | 1 |

#### Warning 16 - 1 occurrence

ChangedInMarshmallow4Warning: `Field` should not be instantiated. Use `fields.Raw` or  another field subclass instead.

| Package | Count |
|---------|-------|
| `invenio-jobs` | 1 |

#### Warning 17 - 1 occurrence

DeprecationWarning: get_user method is deprecated, user get_user_by_email/get_user_by_id

| Package | Count |
|---------|-------|
| `invenio-banners` | 1 |

#### Warning 18 - 1 occurrence

LegacyAPIWarning: The Query.get() method is considered legacy as of the 1.x series of SQLAlchemy and becomes a legacy construct in 2.0. The method is now available as Session.get() (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)

| Package | Count |
|---------|-------|
| `invenio-jobs` | 1 |

#### Warning 19 - 1 occurrence

SAWarning: Identity map already had an identity for (<class 'invenio_jobs.models.Run'>, (UUID('0c18692c-9c22-4eb2-9d9e-2758fa7ecbf2'),), None), replacing it with newly flushed object.   Are there load operations occurring inside of an event handler within the flush?

| Package | Count |
|---------|-------|
| `invenio-jobs` | 1 |

#### Warning 20 - 1 occurrence

SAWarning: Identity map already had an identity for (<class 'invenio_jobs.models.Run'>, (UUID('1ec37309-a725-40fa-b6f5-226cc4779184'),), None), replacing it with newly flushed object.   Are there load operations occurring inside of an event handler within the flush?

| Package | Count |
|---------|-------|
| `invenio-jobs` | 1 |

#### Warning 21 - 1 occurrence

SAWarning: Identity map already had an identity for (<class 'invenio_jobs.models.Run'>, (UUID('2bd0a543-d6f3-4859-ad47-9bfcb1841fee'),), None), replacing it with newly flushed object.   Are there load operations occurring inside of an event handler within the flush?

| Package | Count |
|---------|-------|
| `invenio-jobs` | 1 |

#### Warning 22 - 1 occurrence

SAWarning: Identity map already had an identity for (<class 'invenio_jobs.models.Run'>, (UUID('4232d756-47d1-416a-856f-a72837f288db'),), None), replacing it with newly flushed object.   Are there load operations occurring inside of an event handler within the flush?

| Package | Count |
|---------|-------|
| `invenio-jobs` | 1 |

#### Warning 23 - 1 occurrence

SAWarning: Identity map already had an identity for (<class 'invenio_jobs.models.Run'>, (UUID('70e32b8c-9b27-4d8e-8c6a-3d1f20bbf211'),), None), replacing it with newly flushed object.   Are there load operations occurring inside of an event handler within the flush?

| Package | Count |
|---------|-------|
| `invenio-jobs` | 1 |

#### Warning 24 - 1 occurrence

SAWarning: Identity map already had an identity for (<class 'invenio_jobs.models.Run'>, (UUID('8c58b727-d2fa-4d82-83c2-0aa6ae9d19b1'),), None), replacing it with newly flushed object.   Are there load operations occurring inside of an event handler within the flush?

| Package | Count |
|---------|-------|
| `invenio-jobs` | 1 |

#### Warning 25 - 1 occurrence

SAWarning: Identity map already had an identity for (<class 'invenio_jobs.models.Run'>, (UUID('e3f58fe3-a3ed-46fb-b581-d6c92c1f4a9e'),), None), replacing it with newly flushed object.   Are there load operations occurring inside of an event handler within the flush?

| Package | Count |
|---------|-------|
| `invenio-jobs` | 1 |




---