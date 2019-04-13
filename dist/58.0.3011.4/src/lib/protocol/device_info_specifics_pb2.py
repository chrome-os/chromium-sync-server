# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: device_info_specifics.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import sync_enums_pb2 as sync__enums__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='device_info_specifics.proto',
  package='sync_pb',
  syntax='proto2',
  serialized_options=_b('H\003'),
  serialized_pb=_b('\n\x1b\x64\x65vice_info_specifics.proto\x12\x07sync_pb\x1a\x10sync_enums.proto\"\x8d\x02\n\x13\x44\x65viceInfoSpecifics\x12\x12\n\ncache_guid\x18\x01 \x01(\t\x12\x13\n\x0b\x63lient_name\x18\x02 \x01(\t\x12\x32\n\x0b\x64\x65vice_type\x18\x03 \x01(\x0e\x32\x1d.sync_pb.SyncEnums.DeviceType\x12\x17\n\x0fsync_user_agent\x18\x04 \x01(\t\x12\x16\n\x0e\x63hrome_version\x18\x05 \x01(\t\x12\'\n\x1b\x64\x65precated_backup_timestamp\x18\x06 \x01(\x03\x42\x02\x18\x01\x12\x1f\n\x17signin_scoped_device_id\x18\x07 \x01(\t\x12\x1e\n\x16last_updated_timestamp\x18\x08 \x01(\x03\x42\x02H\x03')
  ,
  dependencies=[sync__enums__pb2.DESCRIPTOR,])




_DEVICEINFOSPECIFICS = _descriptor.Descriptor(
  name='DeviceInfoSpecifics',
  full_name='sync_pb.DeviceInfoSpecifics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cache_guid', full_name='sync_pb.DeviceInfoSpecifics.cache_guid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='client_name', full_name='sync_pb.DeviceInfoSpecifics.client_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='device_type', full_name='sync_pb.DeviceInfoSpecifics.device_type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sync_user_agent', full_name='sync_pb.DeviceInfoSpecifics.sync_user_agent', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chrome_version', full_name='sync_pb.DeviceInfoSpecifics.chrome_version', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deprecated_backup_timestamp', full_name='sync_pb.DeviceInfoSpecifics.deprecated_backup_timestamp', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\030\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signin_scoped_device_id', full_name='sync_pb.DeviceInfoSpecifics.signin_scoped_device_id', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_updated_timestamp', full_name='sync_pb.DeviceInfoSpecifics.last_updated_timestamp', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=59,
  serialized_end=328,
)

_DEVICEINFOSPECIFICS.fields_by_name['device_type'].enum_type = sync__enums__pb2._SYNCENUMS_DEVICETYPE
DESCRIPTOR.message_types_by_name['DeviceInfoSpecifics'] = _DEVICEINFOSPECIFICS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DeviceInfoSpecifics = _reflection.GeneratedProtocolMessageType('DeviceInfoSpecifics', (_message.Message,), dict(
  DESCRIPTOR = _DEVICEINFOSPECIFICS,
  __module__ = 'device_info_specifics_pb2'
  # @@protoc_insertion_point(class_scope:sync_pb.DeviceInfoSpecifics)
  ))
_sym_db.RegisterMessage(DeviceInfoSpecifics)


DESCRIPTOR._options = None
_DEVICEINFOSPECIFICS.fields_by_name['deprecated_backup_timestamp']._options = None
# @@protoc_insertion_point(module_scope)