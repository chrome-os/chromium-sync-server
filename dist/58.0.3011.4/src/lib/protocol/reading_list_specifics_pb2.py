# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: reading_list_specifics.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='reading_list_specifics.proto',
  package='sync_pb',
  syntax='proto2',
  serialized_options=_b('H\003'),
  serialized_pb=_b('\n\x1creading_list_specifics.proto\x12\x07sync_pb\"\xb2\x02\n\x14ReadingListSpecifics\x12\x10\n\x08\x65ntry_id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0b\n\x03url\x18\x03 \x01(\t\x12\x18\n\x10\x63reation_time_us\x18\x04 \x01(\x03\x12\x16\n\x0eupdate_time_us\x18\x05 \x01(\x03\x12\x1a\n\x12\x66irst_read_time_us\x18\x07 \x01(\x03\x12\x1c\n\x14update_title_time_us\x18\x08 \x01(\x03\x12\x44\n\x06status\x18\x06 \x01(\x0e\x32\x34.sync_pb.ReadingListSpecifics.ReadingListEntryStatus\":\n\x16ReadingListEntryStatus\x12\n\n\x06UNREAD\x10\x00\x12\x08\n\x04READ\x10\x01\x12\n\n\x06UNSEEN\x10\x02\x42\x02H\x03')
)



_READINGLISTSPECIFICS_READINGLISTENTRYSTATUS = _descriptor.EnumDescriptor(
  name='ReadingListEntryStatus',
  full_name='sync_pb.ReadingListSpecifics.ReadingListEntryStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNREAD', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='READ', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNSEEN', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=290,
  serialized_end=348,
)
_sym_db.RegisterEnumDescriptor(_READINGLISTSPECIFICS_READINGLISTENTRYSTATUS)


_READINGLISTSPECIFICS = _descriptor.Descriptor(
  name='ReadingListSpecifics',
  full_name='sync_pb.ReadingListSpecifics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entry_id', full_name='sync_pb.ReadingListSpecifics.entry_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='title', full_name='sync_pb.ReadingListSpecifics.title', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='url', full_name='sync_pb.ReadingListSpecifics.url', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='creation_time_us', full_name='sync_pb.ReadingListSpecifics.creation_time_us', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='update_time_us', full_name='sync_pb.ReadingListSpecifics.update_time_us', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='first_read_time_us', full_name='sync_pb.ReadingListSpecifics.first_read_time_us', index=5,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='update_title_time_us', full_name='sync_pb.ReadingListSpecifics.update_title_time_us', index=6,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='sync_pb.ReadingListSpecifics.status', index=7,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _READINGLISTSPECIFICS_READINGLISTENTRYSTATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=42,
  serialized_end=348,
)

_READINGLISTSPECIFICS.fields_by_name['status'].enum_type = _READINGLISTSPECIFICS_READINGLISTENTRYSTATUS
_READINGLISTSPECIFICS_READINGLISTENTRYSTATUS.containing_type = _READINGLISTSPECIFICS
DESCRIPTOR.message_types_by_name['ReadingListSpecifics'] = _READINGLISTSPECIFICS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ReadingListSpecifics = _reflection.GeneratedProtocolMessageType('ReadingListSpecifics', (_message.Message,), dict(
  DESCRIPTOR = _READINGLISTSPECIFICS,
  __module__ = 'reading_list_specifics_pb2'
  # @@protoc_insertion_point(class_scope:sync_pb.ReadingListSpecifics)
  ))
_sym_db.RegisterMessage(ReadingListSpecifics)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
