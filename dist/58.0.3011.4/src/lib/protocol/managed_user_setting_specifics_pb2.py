# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: managed_user_setting_specifics.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='managed_user_setting_specifics.proto',
  package='sync_pb',
  syntax='proto2',
  serialized_options=_b('H\003'),
  serialized_pb=_b('\n$managed_user_setting_specifics.proto\x12\x07sync_pb\":\n\x1bManagedUserSettingSpecifics\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\tB\x02H\x03')
)




_MANAGEDUSERSETTINGSPECIFICS = _descriptor.Descriptor(
  name='ManagedUserSettingSpecifics',
  full_name='sync_pb.ManagedUserSettingSpecifics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='sync_pb.ManagedUserSettingSpecifics.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='sync_pb.ManagedUserSettingSpecifics.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=49,
  serialized_end=107,
)

DESCRIPTOR.message_types_by_name['ManagedUserSettingSpecifics'] = _MANAGEDUSERSETTINGSPECIFICS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ManagedUserSettingSpecifics = _reflection.GeneratedProtocolMessageType('ManagedUserSettingSpecifics', (_message.Message,), dict(
  DESCRIPTOR = _MANAGEDUSERSETTINGSPECIFICS,
  __module__ = 'managed_user_setting_specifics_pb2'
  # @@protoc_insertion_point(class_scope:sync_pb.ManagedUserSettingSpecifics)
  ))
_sym_db.RegisterMessage(ManagedUserSettingSpecifics)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
