## Collected Warnings

### Patched

#### Warning 1 - 21 occurrences

SAWarning: nested transaction already deassociated from connection

| Package | Count |
|---------|-------|
| `invenio-records` | 21 |

#### Warning 2 - 11 occurrences

DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).

| Package | Count |
|---------|-------|
| `invenio-audit-logs` | 6 |
| `invenio-records` | 3 |
| `invenio-cache` | 1 |
| `invenio-rest` | 1 |

#### Warning 3 - 7 occurrences

DeprecationWarning: jsonschema.RefResolver is deprecated as of v4.18.0, in favor of the https://github.com/python-jsonschema/referencing library, which provides more compliant referencing behavior as well as more flexible APIs for customization. A future release will remove RefResolver. Please file a feature request (on referencing) if you are missing an API for the kind of customization you need.

| Package | Count |
|---------|-------|
| `invenio-audit-logs` | 2 |
| `invenio-checks` | 2 |
| `invenio-records` | 2 |
| `invenio-jsonschemas` | 1 |

#### Warning 4 - 5 occurrences

RemovedInMarshmallow4Warning: The `context` parameter is deprecated and will be removed in marshmallow 4.0. Use `contextvars.ContextVar` to pass context instead.

| Package | Count |
|---------|-------|
| `invenio-audit-logs` | 3 |
| `invenio-checks` | 2 |

#### Warning 5 - 4 occurrences

DeprecationWarning: Deprecated call to `pkg_resources.declare_namespace('fs')`.

| Package | Count |
|---------|-------|
| `invenio-audit-logs` | 2 |
| `invenio-checks` | 2 |

#### Warning 6 - 4 occurrences

PytestMockWarning: Mocks returned by pytest-mock do not need to be used as context managers. The mocker fixture automatically undoes mocking at the end of a test. This warning can be ignored if it was triggered by mocking a context manager. https://pytest-mock.readthedocs.io/en/latest/usage.html#usage-as-context-manager

| Package | Count |
|---------|-------|
| `invenio-cache` | 4 |

#### Warning 7 - 3 occurrences

DeprecationWarning: 'crypt' is deprecated and slated for removal in Python 3.13

| Package | Count |
|---------|-------|
| `invenio-audit-logs` | 1 |
| `invenio-checks` | 1 |
| `invenio-records` | 1 |

#### Warning 8 - 3 occurrences

DeprecationWarning: Using the initialization functions in flask_caching.backend is deprecated.  Use the a full path to backend classes directly.

| Package | Count |
|---------|-------|
| `invenio-audit-logs` | 1 |
| `invenio-cache` | 1 |
| `invenio-sitemap` | 1 |

#### Warning 9 - 3 occurrences

DeprecationWarning: jsonschema.exceptions.RefResolutionError is deprecated as of version 4.18.0. If you wish to catch potential reference resolution errors, directly catch referencing.exceptions.Unresolvable.

| Package | Count |
|---------|-------|
| `invenio-audit-logs` | 1 |
| `invenio-checks` | 1 |
| `invenio-records` | 1 |

#### Warning 10 - 3 occurrences

FutureWarning: CSRF validation will be enabled by default in the version 1.3.x

| Package | Count |
|---------|-------|
| `invenio-rest` | 2 |
| `invenio-audit-logs` | 1 |

#### Warning 11 - 3 occurrences

PendingDeprecationWarning: Schema().dump().data and Schema().dump().errors as well as Schema().load().data and Schema().loads().dataattributes are deprecated in marshmallow v3.x.

| Package | Count |
|---------|-------|
| `invenio-rest` | 3 |

#### Warning 12 - 3 occurrences

RemovedInMarshmallow4Warning: The 'default' argument to fields is deprecated. Use 'dump_default' instead.

| Package | Count |
|---------|-------|
| `invenio-checks` | 2 |
| `invenio-audit-logs` | 1 |

#### Warning 13 - 2 occurrences

DeprecationWarning: Deprecated call to `pkg_resources.declare_namespace('fs.opener')`.

| Package | Count |
|---------|-------|
| `invenio-audit-logs` | 1 |
| `invenio-checks` | 1 |

#### Warning 14 - 2 occurrences

DeprecationWarning: Deprecated call to `pkg_resources.declare_namespace('sphinxcontrib')`.

| Package | Count |
|---------|-------|
| `invenio-audit-logs` | 1 |
| `invenio-checks` | 1 |

#### Warning 15 - 2 occurrences

DeprecationWarning: Link is deprecated and will be removed in v14.0. Use `ExternalLink` for third-party links and `EndpointLink` for InvenioRDM links.

| Package | Count |
|---------|-------|
| `invenio-audit-logs` | 1 |
| `invenio-checks` | 1 |

#### Warning 16 - 2 occurrences

DeprecationWarning: The '__version_info__' attribute is deprecated and will be removed in in a future version. Use feature detection or 'packaging.Version(importlib.metadata.version("marshmallow")).release' instead.

| Package | Count |
|---------|-------|
| `invenio-audit-logs` | 1 |
| `invenio-checks` | 1 |

#### Warning 17 - 2 occurrences

SAWarning: On mapper Mapper[RecordMetadataVersion(records_metadata_version)], primary key column 'records_metadata_version.transaction_id' is being combined with distinct primary key column 'records_metadata_version.transaction_id' in attribute 'transaction_id'. Use explicit properties to give each column its own mapped attribute name. (This warning originated from the `configure_mappers()` process, which was invoked automatically in response to a user-initiated operation.)

| Package | Count |
|---------|-------|
| `invenio-records` | 2 |

#### Warning 18 - 2 occurrences

UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.

| Package | Count |
|---------|-------|
| `invenio-audit-logs` | 1 |
| `invenio-checks` | 1 |

#### Warning 19 - 1 occurrence

ChangedInMarshmallow4Warning: `Field` should not be instantiated. Use `fields.Raw` or  another field subclass instead.

| Package | Count |
|---------|-------|
| `invenio-checks` | 1 |

#### Warning 20 - 1 occurrence

DeprecationWarning: Implicit imports (e.g., 'import idutils; idutils.function;') might be removed in the next major version. Please use explicit imports (e.g., 'from idutils import function;') instead.

| Package | Count |
|---------|-------|
| `invenio-checks` | 1 |

#### Warning 21 - 1 occurrence

DeprecationWarning: No path_separator found in configuration; falling back to legacy splitting on spaces/commas for version_locations.  Consider adding path_separator=os to Alembic config.

| Package | Count |
|---------|-------|
| `invenio-audit-logs` | 1 |

#### Warning 22 - 1 occurrence

DeprecationWarning: Remember me support has been removed.

| Package | Count |
|---------|-------|
| `invenio-audit-logs` | 1 |

#### Warning 23 - 1 occurrence

DeprecationWarning: The patch() method is deprecated and will be removed.

| Package | Count |
|---------|-------|
| `invenio-records` | 1 |

#### Warning 24 - 1 occurrence

DeprecationWarning: The post_load hook must take a positional argument data.

| Package | Count |
|---------|-------|
| `invenio-records` | 1 |

#### Warning 25 - 1 occurrence

DeprecationWarning: The pre_dump hook must take a positional argument data.

| Package | Count |
|---------|-------|
| `invenio-records` | 1 |

#### Warning 26 - 1 occurrence

PendingDeprecationWarning: The WSGI_PROXIES configuration is deprecated and it will be removed, use PROXYFIX_CONFIG instead

| Package | Count |
|---------|-------|
| `invenio-base` | 1 |

#### Warning 27 - 1 occurrence

PytestConfigWarning: Unknown config option: pep8ignore

| Package | Count |
|---------|-------|
| `invenio-jsonschemas` | 1 |

#### Warning 28 - 1 occurrence

SADeprecationWarning: The from_engine() method on Inspector is deprecated and will be removed in a future release.  Please use the sqlalchemy.inspect() function on an Engine or Connection in order to acquire an Inspector. (deprecated since: 1.4)

| Package | Count |
|---------|-------|
| `invenio-audit-logs` | 1 |

#### Warning 29 - 1 occurrence

SAWarning: This declarative base already contains a class with the same class name and module name as sqlalchemy_continuum.model_builder.RecordMetadataVersion, and will be replaced in the string-lookup table. (This warning originated from the `configure_mappers()` process, which was invoked automatically in response to a user-initiated operation.)

| Package | Count |
|---------|-------|
| `invenio-records` | 1 |

#### Warning 30 - 1 occurrence

SAWarning: relationship 'RecordMetadataVersion.transaction' will copy column transaction.id to column records_metadata_version.transaction_id, which conflicts with relationship(s): 'RecordMetadataVersion.transaction' (copies transaction.id to records_metadata_version.transaction_id), 'RecordMetadataVersion.transaction' (copies transaction.id to records_metadata_version.transaction_id), 'RecordMetadataVersion.transaction' (copies transaction.id to records_metadata_version.transaction_id), 'RecordMetadataVersion.transaction' (copies transaction.id to records_metadata_version.transaction_id). If this is not the intention, consider if these relationships should be linked with back_populates, or if viewonly=True should be applied to one or more if they are read-only. For the less common case that foreign key constraints are partially overlapping, the orm.foreign() annotation can be used to isolate the columns that should be written towards.   To silence this warning, add the parameter 'overlaps="transaction,transaction,transaction,transaction"' to the 'RecordMetadataVersion.transaction' relationship. (Background on this warning at: https://sqlalche.me/e/20/qzyx) (This warning originated from the `configure_mappers()` process, which was invoked automatically in response to a user-initiated operation.)

| Package | Count |
|---------|-------|
| `invenio-records` | 1 |

#### Warning 31 - 1 occurrence

SAWarning: relationship 'RecordMetadataVersion.transaction' will copy column transaction.id to column records_metadata_version.transaction_id, which conflicts with relationship(s): 'RecordMetadataVersion.transaction' (copies transaction.id to records_metadata_version.transaction_id), 'RecordMetadataVersion.transaction' (copies transaction.id to records_metadata_version.transaction_id), 'RecordMetadataVersion.transaction' (copies transaction.id to records_metadata_version.transaction_id). If this is not the intention, consider if these relationships should be linked with back_populates, or if viewonly=True should be applied to one or more if they are read-only. For the less common case that foreign key constraints are partially overlapping, the orm.foreign() annotation can be used to isolate the columns that should be written towards.   To silence this warning, add the parameter 'overlaps="transaction,transaction,transaction"' to the 'RecordMetadataVersion.transaction' relationship. (Background on this warning at: https://sqlalche.me/e/20/qzyx) (This warning originated from the `configure_mappers()` process, which was invoked automatically in response to a user-initiated operation.)

| Package | Count |
|---------|-------|
| `invenio-records` | 1 |

#### Warning 32 - 1 occurrence

SAWarning: relationship 'RecordMetadataVersion.transaction' will copy column transaction.id to column records_metadata_version.transaction_id, which conflicts with relationship(s): 'RecordMetadataVersion.transaction' (copies transaction.id to records_metadata_version.transaction_id), 'RecordMetadataVersion.transaction' (copies transaction.id to records_metadata_version.transaction_id). If this is not the intention, consider if these relationships should be linked with back_populates, or if viewonly=True should be applied to one or more if they are read-only. For the less common case that foreign key constraints are partially overlapping, the orm.foreign() annotation can be used to isolate the columns that should be written towards.   To silence this warning, add the parameter 'overlaps="transaction,transaction"' to the 'RecordMetadataVersion.transaction' relationship. (Background on this warning at: https://sqlalche.me/e/20/qzyx) (This warning originated from the `configure_mappers()` process, which was invoked automatically in response to a user-initiated operation.)

| Package | Count |
|---------|-------|
| `invenio-records` | 1 |

#### Warning 33 - 1 occurrence

SAWarning: relationship 'RecordMetadataVersion.transaction' will copy column transaction.id to column records_metadata_version.transaction_id, which conflicts with relationship(s): 'RecordMetadataVersion.transaction' (copies transaction.id to records_metadata_version.transaction_id). If this is not the intention, consider if these relationships should be linked with back_populates, or if viewonly=True should be applied to one or more if they are read-only. For the less common case that foreign key constraints are partially overlapping, the orm.foreign() annotation can be used to isolate the columns that should be written towards.   To silence this warning, add the parameter 'overlaps="transaction"' to the 'RecordMetadataVersion.transaction' relationship. (Background on this warning at: https://sqlalche.me/e/20/qzyx) (This warning originated from the `configure_mappers()` process, which was invoked automatically in response to a user-initiated operation.)

| Package | Count |
|---------|-------|
| `invenio-records` | 1 |

#### Warning 34 - 1 occurrence

UserWarning: Set configuration variable SECRET_KEY with random string

| Package | Count |
|---------|-------|
| `invenio-config` | 1 |

#### Warning 35 - 1 occurrence

UserWarning: Test

| Package | Count |
|---------|-------|
| `invenio-base` | 1 |

#### Warning 36 - 1 occurrence

UserWarning: autoincrement and existing_autoincrement only make sense for MySQL

| Package | Count |
|---------|-------|
| `invenio-audit-logs` | 1 |


