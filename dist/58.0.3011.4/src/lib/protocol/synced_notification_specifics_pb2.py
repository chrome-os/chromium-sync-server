# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: synced_notification_specifics.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='synced_notification_specifics.proto',
  package='sync_pb',
  syntax='proto2',
  serialized_options=_b('H\003'),
  serialized_pb=_b('\n#synced_notification_specifics.proto\x12\x07sync_pb\"\x1d\n\x1bSyncedNotificationSpecificsB\x02H\x03')
)




_SYNCEDNOTIFICATIONSPECIFICS = _descriptor.Descriptor(
  name='SyncedNotificationSpecifics',
  full_name='sync_pb.SyncedNotificationSpecifics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=48,
  serialized_end=77,
)

DESCRIPTOR.message_types_by_name['SyncedNotificationSpecifics'] = _SYNCEDNOTIFICATIONSPECIFICS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SyncedNotificationSpecifics = _reflection.GeneratedProtocolMessageType('SyncedNotificationSpecifics', (_message.Message,), dict(
  DESCRIPTOR = _SYNCEDNOTIFICATIONSPECIFICS,
  __module__ = 'synced_notification_specifics_pb2'
  # @@protoc_insertion_point(class_scope:sync_pb.SyncedNotificationSpecifics)
  ))
_sym_db.RegisterMessage(SyncedNotificationSpecifics)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
