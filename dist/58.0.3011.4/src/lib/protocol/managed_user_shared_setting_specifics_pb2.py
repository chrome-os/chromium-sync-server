# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: managed_user_shared_setting_specifics.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='managed_user_shared_setting_specifics.proto',
  package='sync_pb',
  syntax='proto2',
  serialized_options=_b('H\003'),
  serialized_pb=_b('\n+managed_user_shared_setting_specifics.proto\x12\x07sync_pb\"k\n!ManagedUserSharedSettingSpecifics\x12\r\n\x05mu_id\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\t\x12\x1b\n\x0c\x61\x63knowledged\x18\x04 \x01(\x08:\x05\x66\x61lseB\x02H\x03')
)




_MANAGEDUSERSHAREDSETTINGSPECIFICS = _descriptor.Descriptor(
  name='ManagedUserSharedSettingSpecifics',
  full_name='sync_pb.ManagedUserSharedSettingSpecifics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mu_id', full_name='sync_pb.ManagedUserSharedSettingSpecifics.mu_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='key', full_name='sync_pb.ManagedUserSharedSettingSpecifics.key', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='sync_pb.ManagedUserSharedSettingSpecifics.value', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='acknowledged', full_name='sync_pb.ManagedUserSharedSettingSpecifics.acknowledged', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
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
  serialized_start=56,
  serialized_end=163,
)

DESCRIPTOR.message_types_by_name['ManagedUserSharedSettingSpecifics'] = _MANAGEDUSERSHAREDSETTINGSPECIFICS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ManagedUserSharedSettingSpecifics = _reflection.GeneratedProtocolMessageType('ManagedUserSharedSettingSpecifics', (_message.Message,), dict(
  DESCRIPTOR = _MANAGEDUSERSHAREDSETTINGSPECIFICS,
  __module__ = 'managed_user_shared_setting_specifics_pb2'
  # @@protoc_insertion_point(class_scope:sync_pb.ManagedUserSharedSettingSpecifics)
  ))
_sym_db.RegisterMessage(ManagedUserSharedSettingSpecifics)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
