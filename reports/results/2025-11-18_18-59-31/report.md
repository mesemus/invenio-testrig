# Invenio Bugfix Verification Results

_Last updated: 2025-11-18 19:03:04 UTC_

## 📊 Overall Status

| Metric | Count |
|--------|-------|
| **Total Packages** | 22 |
| **Patched Packages** | 22 |
| **Unpatched Packages** | 0 |

### Patch Results
| Result | Count |
|--------|-------|
| ✅ Fixed | 0 |
| ❌ Regressions | 0 |
| ⚠️  Still Failing | 1 |
| ℹ️  No Change | 21 |

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
| `invenio-mail` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-mail/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-mail/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-mail/test-report-patched.xml)<br>[warnings](packages/invenio-mail/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-config` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-config/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-config/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-config/test-report-patched.xml)<br>[warnings](packages/invenio-config/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-queues` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-queues/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-queues/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-queues/test-report-patched.xml) | ✅ Patch applied successfully, tests passed |
| `invenio-oauthclient` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-oauthclient/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-oauthclient/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-oauthclient/test-report-patched.xml)<br>[warnings](packages/invenio-oauthclient/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-cache` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-cache/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-cache/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-cache/test-report-patched.xml)<br>[warnings](packages/invenio-cache/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-base` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-base/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-base/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-base/test-report-patched.xml)<br>[warnings](packages/invenio-base/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-app` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-app/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-app/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-app/test-report-patched.xml)<br>[warnings](packages/invenio-app/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-theme` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-theme/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-theme/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-theme/test-report-patched.xml) | ✅ Patch applied successfully, tests passed |
| `invenio-assets` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-assets/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-assets/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-assets/test-report-patched.xml) | ✅ Patch applied successfully, tests passed |
| `invenio-pidstore` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-pidstore/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-pidstore/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-pidstore/test-report-patched.xml)<br>[warnings](packages/invenio-pidstore/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-db` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-db/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-db/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-db/test-report-patched.xml)<br>[warnings](packages/invenio-db/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-oaiserver` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-oaiserver/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-oaiserver/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-oaiserver/test-report-patched.xml)<br>[warnings](packages/invenio-oaiserver/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-drafts-resources` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-drafts-resources/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-drafts-resources/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-drafts-resources/test-report-patched.xml)<br>[warnings](packages/invenio-drafts-resources/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-pages` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-pages/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-pages/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-pages/test-report-patched.xml)<br>[warnings](packages/invenio-pages/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-search-ui` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-search-ui/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-search-ui/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-search-ui/test-report-patched.xml) | ✅ Patch applied successfully, tests passed |
| `invenio-records-files` | pytest-invenio | ❌ Fail<br>[output](packages/invenio-records-files/test-output-original.txt)<br>[output-no-warnings](packages/invenio-records-files/test-output-no-warnings-original.txt) | ❌ Fail<br>[output](packages/invenio-records-files/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-records-files/test-output-no-warnings-patched.txt) | ⚠️ Tests still failing after patch |
| `invenio-logging` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-logging/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-logging/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-logging/test-report-patched.xml)<br>[warnings](packages/invenio-logging/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-formatter` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-formatter/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-formatter/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-formatter/test-report-patched.xml)<br>[warnings](packages/invenio-formatter/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-administration` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-administration/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-administration/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-administration/test-report-patched.xml)<br>[warnings](packages/invenio-administration/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-github` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-github/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-github/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-github/test-report-patched.xml)<br>[warnings](packages/invenio-github/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-accounts` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-accounts/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-accounts/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-accounts/test-report-patched.xml)<br>[warnings](packages/invenio-accounts/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-webhooks` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-webhooks/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-webhooks/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-webhooks/test-report-patched.xml)<br>[warnings](packages/invenio-webhooks/warnings-patched.md) | ✅ Patch applied successfully, tests passed |

## Collected Warnings

### Patched

#### Warning 1 - 57 occurrences

DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).

| Package | Count |
|---------|-------|
| `invenio-accounts` | 13 |
| `invenio-oauthclient` | 8 |
| `invenio-drafts-resources` | 7 |
| `invenio-github` | 6 |
| `invenio-pages` | 6 |
| `invenio-oaiserver` | 5 |
| `invenio-webhooks` | 5 |
| `invenio-administration` | 3 |
| `invenio-pidstore` | 2 |
| `invenio-cache` | 1 |
| `invenio-formatter` | 1 |

#### Warning 2 - 10 occurrences

SAWarning: nested transaction already deassociated from connection

| Package | Count |
|---------|-------|
| `invenio-oaiserver` | 5 |
| `invenio-pages` | 5 |

#### Warning 3 - 9 occurrences

DeprecationWarning: 'crypt' is deprecated and slated for removal in Python 3.13

| Package | Count |
|---------|-------|
| `invenio-accounts` | 1 |
| `invenio-administration` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-github` | 1 |
| `invenio-oaiserver` | 1 |
| `invenio-oauthclient` | 1 |
| `invenio-pages` | 1 |
| `invenio-pidstore` | 1 |
| `invenio-webhooks` | 1 |

#### Warning 4 - 8 occurrences

DeprecationWarning: ast.Str is deprecated and will be removed in Python 3.14; use ast.Constant instead

| Package | Count |
|---------|-------|
| `invenio-mail` | 8 |

#### Warning 5 - 8 occurrences

DeprecationWarning: jsonschema.RefResolver is deprecated as of v4.18.0, in favor of the https://github.com/python-jsonschema/referencing library, which provides more compliant referencing behavior as well as more flexible APIs for customization. A future release will remove RefResolver. Please file a feature request (on referencing) if you are missing an API for the kind of customization you need.

| Package | Count |
|---------|-------|
| `invenio-administration` | 2 |
| `invenio-drafts-resources` | 2 |
| `invenio-oaiserver` | 2 |
| `invenio-pages` | 2 |

#### Warning 6 - 6 occurrences

DeprecationWarning: Deprecated call to `pkg_resources.declare_namespace('fs')`.

| Package | Count |
|---------|-------|
| `invenio-administration` | 2 |
| `invenio-drafts-resources` | 2 |
| `invenio-pages` | 2 |

#### Warning 7 - 6 occurrences

DeprecationWarning: Using the initialization functions in flask_caching.backend is deprecated.  Use the a full path to backend classes directly.

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |
| `invenio-app` | 1 |
| `invenio-cache` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-github` | 1 |
| `invenio-pages` | 1 |

#### Warning 8 - 5 occurrences

DeprecationWarning: Deprecated call to `pkg_resources.declare_namespace('sphinxcontrib')`.

| Package | Count |
|---------|-------|
| `invenio-accounts` | 1 |
| `invenio-administration` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-oauthclient` | 1 |
| `invenio-pages` | 1 |

#### Warning 9 - 5 occurrences

DeprecationWarning: datetime.datetime.utcfromtimestamp() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.fromtimestamp(timestamp, datetime.UTC).

| Package | Count |
|---------|-------|
| `invenio-accounts` | 1 |
| `invenio-github` | 1 |
| `invenio-oauthclient` | 1 |
| `invenio-pages` | 1 |
| `invenio-webhooks` | 1 |

#### Warning 10 - 5 occurrences

FutureWarning: CSRF validation will be enabled by default in the version 1.3.x

| Package | Count |
|---------|-------|
| `invenio-accounts` | 1 |
| `invenio-administration` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-github` | 1 |
| `invenio-pages` | 1 |

#### Warning 11 - 5 occurrences

RemovedInMarshmallow4Warning: The `context` parameter is deprecated and will be removed in marshmallow 4.0. Use `contextvars.ContextVar` to pass context instead.

| Package | Count |
|---------|-------|
| `invenio-drafts-resources` | 3 |
| `invenio-pages` | 2 |

#### Warning 12 - 5 occurrences

UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.

| Package | Count |
|---------|-------|
| `invenio-accounts` | 1 |
| `invenio-administration` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-oauthclient` | 1 |
| `invenio-pages` | 1 |

#### Warning 13 - 4 occurrences

DeprecationWarning: distutils Version classes are deprecated. Use packaging.version instead.

| Package | Count |
|---------|-------|
| `invenio-accounts` | 2 |
| `invenio-oaiserver` | 2 |

#### Warning 14 - 4 occurrences

DeprecationWarning: jsonschema.exceptions.RefResolutionError is deprecated as of version 4.18.0. If you wish to catch potential reference resolution errors, directly catch referencing.exceptions.Unresolvable.

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-oaiserver` | 1 |
| `invenio-pages` | 1 |

#### Warning 15 - 4 occurrences

PendingDeprecationWarning: Schema().dump().data and Schema().dump().errors as well as Schema().load().data and Schema().loads().dataattributes are deprecated in marshmallow v3.x.

| Package | Count |
|---------|-------|
| `invenio-oaiserver` | 4 |

#### Warning 16 - 4 occurrences

PytestMockWarning: Mocks returned by pytest-mock do not need to be used as context managers. The mocker fixture automatically undoes mocking at the end of a test. This warning can be ignored if it was triggered by mocking a context manager. https://pytest-mock.readthedocs.io/en/latest/usage.html#usage-as-context-manager

| Package | Count |
|---------|-------|
| `invenio-cache` | 4 |

#### Warning 17 - 4 occurrences

SyntaxWarning: invalid escape sequence '\_'

| Package | Count |
|---------|-------|
| `invenio-mail` | 4 |

#### Warning 18 - 3 occurrences

DeprecationWarning: Deprecated call to `pkg_resources.declare_namespace('fs.opener')`.

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-pages` | 1 |

#### Warning 19 - 3 occurrences

DeprecationWarning: The '__version_info__' attribute is deprecated and will be removed in in a future version. Use feature detection or 'packaging.Version(importlib.metadata.version("marshmallow")).release' instead.

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-pages` | 1 |

#### Warning 20 - 3 occurrences

DeprecationWarning: get_user method is deprecated, user get_user_by_email/get_user_by_id

| Package | Count |
|---------|-------|
| `invenio-accounts` | 1 |
| `invenio-pages` | 1 |
| `invenio-webhooks` | 1 |

#### Warning 21 - 3 occurrences

RemovedInMarshmallow4Warning: The 'default' argument to fields is deprecated. Use 'dump_default' instead.

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-pages` | 1 |

#### Warning 22 - 3 occurrences

SyntaxWarning: invalid escape sequence '\*'

| Package | Count |
|---------|-------|
| `invenio-mail` | 3 |

#### Warning 23 - 2 occurrences

DeprecationWarning: 'pkgutil.get_loader' is deprecated and slated for removal in Python 3.14; use importlib.util.find_spec() instead

| Package | Count |
|---------|-------|
| `invenio-mail` | 2 |

#### Warning 24 - 2 occurrences

DeprecationWarning: Link is deprecated and will be removed in v14.0. Use `ExternalLink` for third-party links and `EndpointLink` for InvenioRDM links.

| Package | Count |
|---------|-------|
| `invenio-drafts-resources` | 1 |
| `invenio-pages` | 1 |

#### Warning 25 - 2 occurrences

DeprecationWarning: The '__version__' attribute is deprecated and will be removed in in a future version. Use feature detection or 'importlib.metadata.version("marshmallow")' instead.

| Package | Count |
|---------|-------|
| `invenio-accounts` | 1 |
| `invenio-oaiserver` | 1 |

#### Warning 26 - 2 occurrences

DeprecationWarning: The 'warn' method is deprecated, use 'warning' instead

| Package | Count |
|---------|-------|
| `invenio-drafts-resources` | 1 |
| `invenio-logging` | 1 |

#### Warning 27 - 2 occurrences

LegacyAPIWarning: The Query.get() method is considered legacy as of the 1.x series of SQLAlchemy and becomes a legacy construct in 2.0. The method is now available as Session.get() (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)

| Package | Count |
|---------|-------|
| `invenio-webhooks` | 2 |

#### Warning 28 - 2 occurrences

PytestDeprecationWarning: @pytest.yield_fixture is deprecated.

| Package | Count |
|---------|-------|
| `invenio-pidstore` | 2 |

#### Warning 29 - 2 occurrences

UserWarning: Set configuration variable SECRET_KEY with random string

| Package | Count |
|---------|-------|
| `invenio-app` | 1 |
| `invenio-config` | 1 |

#### Warning 30 - 1 occurrence

DeprecationWarning: 'pkgutil.find_loader' is deprecated and slated for removal in Python 3.14; use importlib.util.find_spec() instead

| Package | Count |
|---------|-------|
| `invenio-mail` | 1 |

#### Warning 31 - 1 occurrence

DeprecationWarning: Attribute s is deprecated and will be removed in Python 3.14; use value instead

| Package | Count |
|---------|-------|
| `invenio-mail` | 1 |

#### Warning 32 - 1 occurrence

DeprecationWarning: CryptContext.hash(): 'scheme' keyword is deprecated as of Passlib 1.7, and will be removed in Passlib 2.0

| Package | Count |
|---------|-------|
| `invenio-accounts` | 1 |

#### Warning 33 - 1 occurrence

DeprecationWarning: Implicit imports (e.g., 'import idutils; idutils.function;') might be removed in the next major version. Please use explicit imports (e.g., 'from idutils import function;') instead.

| Package | Count |
|---------|-------|
| `invenio-pidstore` | 1 |

#### Warning 34 - 1 occurrence

DeprecationWarning: No path_separator found in configuration; falling back to legacy splitting on spaces/commas for version_locations.  Consider adding path_separator=os to Alembic config.

| Package | Count |
|---------|-------|
| `invenio-db` | 1 |

#### Warning 35 - 1 occurrence

DeprecationWarning: The 'record_to_index' function is no longer expected to return a tuple (index, doc_type), instead it should only return the index. Support for the tuple will be removed in a future version of 'invenio-indexer'.

| Package | Count |
|---------|-------|
| `invenio-drafts-resources` | 1 |

#### Warning 36 - 1 occurrence

DeprecationWarning: The cern contrib is deprecated. Please use the generic keycloak instead.

| Package | Count |
|---------|-------|
| `invenio-oauthclient` | 1 |

#### Warning 37 - 1 occurrence

DeprecationWarning: ast.NameConstant is deprecated and will be removed in Python 3.14; use ast.Constant instead

| Package | Count |
|---------|-------|
| `invenio-mail` | 1 |

#### Warning 38 - 1 occurrence

DeprecationWarning: passing settings to invenio_aes_encrypted_email.hash() is deprecated, and won't be supported in Passlib 2.0; use 'invenio_aes_encrypted_email.using(**settings).hash(secret)' instead

| Package | Count |
|---------|-------|
| `invenio-accounts` | 1 |

#### Warning 39 - 1 occurrence

DeprecationWarning: the method passlib.context.CryptContext.encrypt() is deprecated as of Passlib 1.7, and will be removed in Passlib 2.0, use CryptContext.hash() instead.

| Package | Count |
|---------|-------|
| `invenio-accounts` | 1 |

#### Warning 40 - 1 occurrence

PendingDeprecationWarning: The WSGI_PROXIES configuration is deprecated and it will be removed, use PROXYFIX_CONFIG instead

| Package | Count |
|---------|-------|
| `invenio-base` | 1 |

#### Warning 41 - 1 occurrence

PendingDeprecationWarning: This feature is deprecated.

| Package | Count |
|---------|-------|
| `invenio-logging` | 1 |

#### Warning 42 - 1 occurrence

PytestCollectionWarning: cannot collect test class 'TestCustomView' because it has a __init__ constructor (from: tests/test_base.py)

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |

#### Warning 43 - 1 occurrence

PytestCollectionWarning: cannot collect test class 'TestSchema' because it has a __init__ constructor (from: tests/test_marshmallow_utils.py)

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |

#### Warning 44 - 1 occurrence

RemovedInMarshmallow4Warning: The 'missing' argument to fields is deprecated. Use 'load_default' instead.

| Package | Count |
|---------|-------|
| `invenio-drafts-resources` | 1 |

#### Warning 45 - 1 occurrence

RuntimeWarning: Results are not stored in backend and should not be retrieved when task_always_eager is enabled, unless task_store_eager_result is enabled.

| Package | Count |
|---------|-------|
| `invenio-webhooks` | 1 |

#### Warning 46 - 1 occurrence

RuntimeWarning: You are overriding the default OAuthlib "URL encoded" set of valid characters. Make sure that the characters defined in oauthlib.common.urlencoded are indeed limitting your needs.

| Package | Count |
|---------|-------|
| `invenio-webhooks` | 1 |

#### Warning 47 - 1 occurrence

SAWarning: Object of type <ObjectVersion> not in session, add operation along 'Bucket.objects' will not proceed (This warning originated from the Session 'autoflush' process, which was invoked automatically in response to a user-initiated operation. Consider using ``no_autoflush`` context manager if this warning happened while initializing objects.)

| Package | Count |
|---------|-------|
| `invenio-drafts-resources` | 1 |

#### Warning 48 - 1 occurrence

SyntaxWarning: "is" with 'str' literal. Did you mean "=="?

| Package | Count |
|---------|-------|
| `invenio-mail` | 1 |

#### Warning 49 - 1 occurrence

SyntaxWarning: invalid escape sequence '\ '

| Package | Count |
|---------|-------|
| `invenio-mail` | 1 |

#### Warning 50 - 1 occurrence

UserWarning: Please specify the OAISERVER_ID_PREFIX configuration.default value is: oai:runnervmg1sw1:

| Package | Count |
|---------|-------|
| `invenio-oaiserver` | 1 |

#### Warning 51 - 1 occurrence

UserWarning: Test

| Package | Count |
|---------|-------|
| `invenio-base` | 1 |

#### Warning 52 - 1 occurrence

UserWarning: Using the in-memory storage for tracking rate limits as no storage was explicitly specified. This is not recommended for production use. See: https://flask-limiter.readthedocs.io#configuring-a-storage-backend for documentation about configuring the storage backend.

| Package | Count |
|---------|-------|
| `invenio-app` | 1 |




---

_For detailed test outputs and diffs, see the [full report](https://mesemus.github.io/invenio-bug-verification/)._