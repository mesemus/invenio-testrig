# Warnings (patched)

## Warning 1 - 21 occurrences

SAWarning: nested transaction already deassociated from connection

## Warning 2 - 3 occurrences

DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).

## Warning 3 - 2 occurrences

DeprecationWarning: jsonschema.RefResolver is deprecated as of v4.18.0, in favor of the https://github.com/python-jsonschema/referencing library, which provides more compliant referencing behavior as well as more flexible APIs for customization. A future release will remove RefResolver. Please file a feature request (on referencing) if you are missing an API for the kind of customization you need.

## Warning 4 - 2 occurrences

SAWarning: On mapper Mapper[RecordMetadataVersion(records_metadata_version)], primary key column 'records_metadata_version.transaction_id' is being combined with distinct primary key column 'records_metadata_version.transaction_id' in attribute 'transaction_id'. Use explicit properties to give each column its own mapped attribute name. (This warning originated from the `configure_mappers()` process, which was invoked automatically in response to a user-initiated operation.)

## Warning 5 - 1 occurrence

DeprecationWarning: 'crypt' is deprecated and slated for removal in Python 3.13

## Warning 6 - 1 occurrence

DeprecationWarning: The patch() method is deprecated and will be removed.

## Warning 7 - 1 occurrence

DeprecationWarning: The post_load hook must take a positional argument data.

## Warning 8 - 1 occurrence

DeprecationWarning: The pre_dump hook must take a positional argument data.

## Warning 9 - 1 occurrence

DeprecationWarning: jsonschema.exceptions.RefResolutionError is deprecated as of version 4.18.0. If you wish to catch potential reference resolution errors, directly catch referencing.exceptions.Unresolvable.

## Warning 10 - 1 occurrence

SAWarning: This declarative base already contains a class with the same class name and module name as sqlalchemy_continuum.model_builder.RecordMetadataVersion, and will be replaced in the string-lookup table. (This warning originated from the `configure_mappers()` process, which was invoked automatically in response to a user-initiated operation.)

## Warning 11 - 1 occurrence

SAWarning: relationship 'RecordMetadataVersion.transaction' will copy column transaction.id to column records_metadata_version.transaction_id, which conflicts with relationship(s): 'RecordMetadataVersion.transaction' (copies transaction.id to records_metadata_version.transaction_id), 'RecordMetadataVersion.transaction' (copies transaction.id to records_metadata_version.transaction_id), 'RecordMetadataVersion.transaction' (copies transaction.id to records_metadata_version.transaction_id), 'RecordMetadataVersion.transaction' (copies transaction.id to records_metadata_version.transaction_id). If this is not the intention, consider if these relationships should be linked with back_populates, or if viewonly=True should be applied to one or more if they are read-only. For the less common case that foreign key constraints are partially overlapping, the orm.foreign() annotation can be used to isolate the columns that should be written towards.   To silence this warning, add the parameter 'overlaps="transaction,transaction,transaction,transaction"' to the 'RecordMetadataVersion.transaction' relationship. (Background on this warning at: https://sqlalche.me/e/20/qzyx) (This warning originated from the `configure_mappers()` process, which was invoked automatically in response to a user-initiated operation.)

## Warning 12 - 1 occurrence

SAWarning: relationship 'RecordMetadataVersion.transaction' will copy column transaction.id to column records_metadata_version.transaction_id, which conflicts with relationship(s): 'RecordMetadataVersion.transaction' (copies transaction.id to records_metadata_version.transaction_id), 'RecordMetadataVersion.transaction' (copies transaction.id to records_metadata_version.transaction_id), 'RecordMetadataVersion.transaction' (copies transaction.id to records_metadata_version.transaction_id). If this is not the intention, consider if these relationships should be linked with back_populates, or if viewonly=True should be applied to one or more if they are read-only. For the less common case that foreign key constraints are partially overlapping, the orm.foreign() annotation can be used to isolate the columns that should be written towards.   To silence this warning, add the parameter 'overlaps="transaction,transaction,transaction"' to the 'RecordMetadataVersion.transaction' relationship. (Background on this warning at: https://sqlalche.me/e/20/qzyx) (This warning originated from the `configure_mappers()` process, which was invoked automatically in response to a user-initiated operation.)

## Warning 13 - 1 occurrence

SAWarning: relationship 'RecordMetadataVersion.transaction' will copy column transaction.id to column records_metadata_version.transaction_id, which conflicts with relationship(s): 'RecordMetadataVersion.transaction' (copies transaction.id to records_metadata_version.transaction_id), 'RecordMetadataVersion.transaction' (copies transaction.id to records_metadata_version.transaction_id). If this is not the intention, consider if these relationships should be linked with back_populates, or if viewonly=True should be applied to one or more if they are read-only. For the less common case that foreign key constraints are partially overlapping, the orm.foreign() annotation can be used to isolate the columns that should be written towards.   To silence this warning, add the parameter 'overlaps="transaction,transaction"' to the 'RecordMetadataVersion.transaction' relationship. (Background on this warning at: https://sqlalche.me/e/20/qzyx) (This warning originated from the `configure_mappers()` process, which was invoked automatically in response to a user-initiated operation.)

## Warning 14 - 1 occurrence

SAWarning: relationship 'RecordMetadataVersion.transaction' will copy column transaction.id to column records_metadata_version.transaction_id, which conflicts with relationship(s): 'RecordMetadataVersion.transaction' (copies transaction.id to records_metadata_version.transaction_id). If this is not the intention, consider if these relationships should be linked with back_populates, or if viewonly=True should be applied to one or more if they are read-only. For the less common case that foreign key constraints are partially overlapping, the orm.foreign() annotation can be used to isolate the columns that should be written towards.   To silence this warning, add the parameter 'overlaps="transaction"' to the 'RecordMetadataVersion.transaction' relationship. (Background on this warning at: https://sqlalche.me/e/20/qzyx) (This warning originated from the `configure_mappers()` process, which was invoked automatically in response to a user-initiated operation.)

