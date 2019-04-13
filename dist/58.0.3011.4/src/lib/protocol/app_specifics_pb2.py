# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: app_specifics.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import extension_specifics_pb2 as extension__specifics__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='app_specifics.proto',
  package='sync_pb',
  syntax='proto2',
  serialized_options=_b('H\003'),
  serialized_pb=_b('\n\x13\x61pp_specifics.proto\x12\x07sync_pb\x1a\x19\x65xtension_specifics.proto\"`\n\x17\x41ppNotificationSettings\x12\x1a\n\x12initial_setup_done\x18\x01 \x01(\x08\x12\x10\n\x08\x64isabled\x18\x02 \x01(\x08\x12\x17\n\x0foauth_client_id\x18\x03 \x01(\t\".\n\x11LinkedAppIconInfo\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x0c\n\x04size\x18\x02 \x01(\r\"\xfc\x03\n\x0c\x41ppSpecifics\x12.\n\textension\x18\x01 \x01(\x0b\x32\x1b.sync_pb.ExtensionSpecifics\x12?\n\x15notification_settings\x18\x02 \x01(\x0b\x32 .sync_pb.AppNotificationSettings\x12\x1a\n\x12\x61pp_launch_ordinal\x18\x03 \x01(\t\x12\x14\n\x0cpage_ordinal\x18\x04 \x01(\t\x12\x35\n\x0blaunch_type\x18\x05 \x01(\x0e\x32 .sync_pb.AppSpecifics.LaunchType\x12\x18\n\x10\x62ookmark_app_url\x18\x06 \x01(\t\x12 \n\x18\x62ookmark_app_description\x18\x07 \x01(\t\x12\x1f\n\x17\x62ookmark_app_icon_color\x18\x08 \x01(\t\x12\x34\n\x10linked_app_icons\x18\t \x03(\x0b\x32\x1a.sync_pb.LinkedAppIconInfo\x12\x1a\n\x12\x62ookmark_app_scope\x18\n \x01(\t\x12 \n\x18\x62ookmark_app_theme_color\x18\x0b \x01(\r\"A\n\nLaunchType\x12\n\n\x06PINNED\x10\x00\x12\x0b\n\x07REGULAR\x10\x01\x12\x0e\n\nFULLSCREEN\x10\x02\x12\n\n\x06WINDOW\x10\x03\x42\x02H\x03')
  ,
  dependencies=[extension__specifics__pb2.DESCRIPTOR,])



_APPSPECIFICS_LAUNCHTYPE = _descriptor.EnumDescriptor(
  name='LaunchType',
  full_name='sync_pb.AppSpecifics.LaunchType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PINNED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REGULAR', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FULLSCREEN', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WINDOW', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=649,
  serialized_end=714,
)
_sym_db.RegisterEnumDescriptor(_APPSPECIFICS_LAUNCHTYPE)


_APPNOTIFICATIONSETTINGS = _descriptor.Descriptor(
  name='AppNotificationSettings',
  full_name='sync_pb.AppNotificationSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='initial_setup_done', full_name='sync_pb.AppNotificationSettings.initial_setup_done', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='disabled', full_name='sync_pb.AppNotificationSettings.disabled', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='oauth_client_id', full_name='sync_pb.AppNotificationSettings.oauth_client_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=59,
  serialized_end=155,
)


_LINKEDAPPICONINFO = _descriptor.Descriptor(
  name='LinkedAppIconInfo',
  full_name='sync_pb.LinkedAppIconInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='url', full_name='sync_pb.LinkedAppIconInfo.url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='size', full_name='sync_pb.LinkedAppIconInfo.size', index=1,
      number=2, type=13, cpp_type=3, label=1,
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
  serialized_start=157,
  serialized_end=203,
)


_APPSPECIFICS = _descriptor.Descriptor(
  name='AppSpecifics',
  full_name='sync_pb.AppSpecifics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='extension', full_name='sync_pb.AppSpecifics.extension', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='notification_settings', full_name='sync_pb.AppSpecifics.notification_settings', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='app_launch_ordinal', full_name='sync_pb.AppSpecifics.app_launch_ordinal', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_ordinal', full_name='sync_pb.AppSpecifics.page_ordinal', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='launch_type', full_name='sync_pb.AppSpecifics.launch_type', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bookmark_app_url', full_name='sync_pb.AppSpecifics.bookmark_app_url', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bookmark_app_description', full_name='sync_pb.AppSpecifics.bookmark_app_description', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bookmark_app_icon_color', full_name='sync_pb.AppSpecifics.bookmark_app_icon_color', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='linked_app_icons', full_name='sync_pb.AppSpecifics.linked_app_icons', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bookmark_app_scope', full_name='sync_pb.AppSpecifics.bookmark_app_scope', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bookmark_app_theme_color', full_name='sync_pb.AppSpecifics.bookmark_app_theme_color', index=10,
      number=11, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _APPSPECIFICS_LAUNCHTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=206,
  serialized_end=714,
)

_APPSPECIFICS.fields_by_name['extension'].message_type = extension__specifics__pb2._EXTENSIONSPECIFICS
_APPSPECIFICS.fields_by_name['notification_settings'].message_type = _APPNOTIFICATIONSETTINGS
_APPSPECIFICS.fields_by_name['launch_type'].enum_type = _APPSPECIFICS_LAUNCHTYPE
_APPSPECIFICS.fields_by_name['linked_app_icons'].message_type = _LINKEDAPPICONINFO
_APPSPECIFICS_LAUNCHTYPE.containing_type = _APPSPECIFICS
DESCRIPTOR.message_types_by_name['AppNotificationSettings'] = _APPNOTIFICATIONSETTINGS
DESCRIPTOR.message_types_by_name['LinkedAppIconInfo'] = _LINKEDAPPICONINFO
DESCRIPTOR.message_types_by_name['AppSpecifics'] = _APPSPECIFICS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AppNotificationSettings = _reflection.GeneratedProtocolMessageType('AppNotificationSettings', (_message.Message,), dict(
  DESCRIPTOR = _APPNOTIFICATIONSETTINGS,
  __module__ = 'app_specifics_pb2'
  # @@protoc_insertion_point(class_scope:sync_pb.AppNotificationSettings)
  ))
_sym_db.RegisterMessage(AppNotificationSettings)

LinkedAppIconInfo = _reflection.GeneratedProtocolMessageType('LinkedAppIconInfo', (_message.Message,), dict(
  DESCRIPTOR = _LINKEDAPPICONINFO,
  __module__ = 'app_specifics_pb2'
  # @@protoc_insertion_point(class_scope:sync_pb.LinkedAppIconInfo)
  ))
_sym_db.RegisterMessage(LinkedAppIconInfo)

AppSpecifics = _reflection.GeneratedProtocolMessageType('AppSpecifics', (_message.Message,), dict(
  DESCRIPTOR = _APPSPECIFICS,
  __module__ = 'app_specifics_pb2'
  # @@protoc_insertion_point(class_scope:sync_pb.AppSpecifics)
  ))
_sym_db.RegisterMessage(AppSpecifics)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
