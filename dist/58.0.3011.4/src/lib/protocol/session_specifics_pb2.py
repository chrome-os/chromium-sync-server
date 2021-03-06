# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: session_specifics.proto

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
  name='session_specifics.proto',
  package='sync_pb',
  syntax='proto2',
  serialized_options=_b('H\003'),
  serialized_pb=_b('\n\x17session_specifics.proto\x12\x07sync_pb\x1a\x10sync_enums.proto\"\x8a\x01\n\x10SessionSpecifics\x12\x13\n\x0bsession_tag\x18\x01 \x01(\t\x12&\n\x06header\x18\x02 \x01(\x0b\x32\x16.sync_pb.SessionHeader\x12 \n\x03tab\x18\x03 \x01(\x0b\x32\x13.sync_pb.SessionTab\x12\x17\n\x0btab_node_id\x18\x04 \x01(\x05:\x02-1\"\x80\x01\n\rSessionHeader\x12&\n\x06window\x18\x02 \x03(\x0b\x32\x16.sync_pb.SessionWindow\x12\x13\n\x0b\x63lient_name\x18\x03 \x01(\t\x12\x32\n\x0b\x64\x65vice_type\x18\x04 \x01(\x0e\x32\x1d.sync_pb.SyncEnums.DeviceType\"\xdb\x01\n\rSessionWindow\x12\x11\n\twindow_id\x18\x01 \x01(\x05\x12\x1e\n\x12selected_tab_index\x18\x02 \x01(\x05:\x02-1\x12\x45\n\x0c\x62rowser_type\x18\x03 \x01(\x0e\x32\".sync_pb.SessionWindow.BrowserType:\x0bTYPE_TABBED\x12\x0b\n\x03tab\x18\x04 \x03(\x05\"C\n\x0b\x42rowserType\x12\x0f\n\x0bTYPE_TABBED\x10\x01\x12\x0e\n\nTYPE_POPUP\x10\x02\x12\x13\n\x0fTYPE_CUSTOM_TAB\x10\x03\"\xff\x02\n\nSessionTab\x12\x12\n\x06tab_id\x18\x01 \x01(\x05:\x02-1\x12\x11\n\twindow_id\x18\x02 \x01(\x05\x12\x1c\n\x10tab_visual_index\x18\x03 \x01(\x05:\x02-1\x12$\n\x18\x63urrent_navigation_index\x18\x04 \x01(\x05:\x02-1\x12\x15\n\x06pinned\x18\x05 \x01(\x08:\x05\x66\x61lse\x12\x18\n\x10\x65xtension_app_id\x18\x06 \x01(\t\x12*\n\nnavigation\x18\x07 \x03(\x0b\x32\x16.sync_pb.TabNavigation\x12\x13\n\x07\x66\x61vicon\x18\x08 \x01(\x0c\x42\x02\x18\x01\x12\x39\n\x0c\x66\x61vicon_type\x18\t \x01(\x0e\x32\x1f.sync_pb.SessionTab.FaviconTypeB\x02\x18\x01\x12\x1a\n\x0e\x66\x61vicon_source\x18\x0b \x01(\tB\x02\x18\x01\x12\x18\n\x0cvariation_id\x18\x0c \x03(\x04\x42\x02\x18\x01\"#\n\x0b\x46\x61viconType\x12\x14\n\x10TYPE_WEB_FAVICON\x10\x01\"\xd6\x08\n\rTabNavigation\x12\x13\n\x0bvirtual_url\x18\x02 \x01(\t\x12\x10\n\x08referrer\x18\x03 \x01(\t\x12\r\n\x05title\x18\x04 \x01(\t\x12@\n\x0fpage_transition\x18\x06 \x01(\x0e\x32!.sync_pb.SyncEnums.PageTransition:\x04LINK\x12\x44\n\rredirect_type\x18\x07 \x01(\x0e\x32-.sync_pb.SyncEnums.PageTransitionRedirectType\x12\x11\n\tunique_id\x18\x08 \x01(\x05\x12\x16\n\x0etimestamp_msec\x18\t \x01(\x03\x12\x1f\n\x17navigation_forward_back\x18\n \x01(\x08\x12#\n\x1bnavigation_from_address_bar\x18\x0b \x01(\x08\x12\x1c\n\x14navigation_home_page\x18\x0c \x01(\x08\x12\x1e\n\x16navigation_chain_start\x18\r \x01(\x08\x12\x1c\n\x14navigation_chain_end\x18\x0e \x01(\x08\x12\x11\n\tglobal_id\x18\x0f \x01(\x03\x12\x18\n\x0csearch_terms\x18\x10 \x01(\tB\x02\x18\x01\x12\x13\n\x0b\x66\x61vicon_url\x18\x11 \x01(\t\x12I\n\rblocked_state\x18\x12 \x01(\x0e\x32#.sync_pb.TabNavigation.BlockedState:\rSTATE_ALLOWED\x12\x1f\n\x17\x63ontent_pack_categories\x18\x13 \x03(\t\x12\x18\n\x10http_status_code\x18\x14 \x01(\x05\x12$\n\x18obsolete_referrer_policy\x18\x15 \x01(\x05\x42\x02\x18\x01\x12\x13\n\x0bis_restored\x18\x16 \x01(\x08\x12\x38\n\x13navigation_redirect\x18\x17 \x03(\x0b\x32\x1b.sync_pb.NavigationRedirect\x12$\n\x1clast_navigation_redirect_url\x18\x18 \x01(\t\x12\"\n\x17\x63orrect_referrer_policy\x18\x19 \x01(\x05:\x01\x31\x12<\n\x0epassword_state\x18\x1a \x01(\x0e\x32$.sync_pb.TabNavigation.PasswordState\x12\x0f\n\x07task_id\x18\x1b \x01(\x03\x12\x18\n\x10\x61ncestor_task_id\x18\x1c \x03(\x03\x12\x38\n\x13replaced_navigation\x18\x1d \x01(\x0b\x32\x1b.sync_pb.ReplacedNavigation\"4\n\x0c\x42lockedState\x12\x11\n\rSTATE_ALLOWED\x10\x01\x12\x11\n\rSTATE_BLOCKED\x10\x02\"Z\n\rPasswordState\x12\x1a\n\x16PASSWORD_STATE_UNKNOWN\x10\x00\x12\x15\n\x11NO_PASSWORD_FIELD\x10\x01\x12\x16\n\x12HAS_PASSWORD_FIELD\x10\x02\"!\n\x12NavigationRedirect\x12\x0b\n\x03url\x18\x01 \x01(\t\"\x91\x01\n\x12ReplacedNavigation\x12\x1b\n\x13\x66irst_committed_url\x18\x01 \x01(\t\x12\x1c\n\x14\x66irst_timestamp_msec\x18\x02 \x01(\x03\x12@\n\x15\x66irst_page_transition\x18\x03 \x01(\x0e\x32!.sync_pb.SyncEnums.PageTransitionB\x02H\x03')
  ,
  dependencies=[sync__enums__pb2.DESCRIPTOR,])



_SESSIONWINDOW_BROWSERTYPE = _descriptor.EnumDescriptor(
  name='BrowserType',
  full_name='sync_pb.SessionWindow.BrowserType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TYPE_TABBED', index=0, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_POPUP', index=1, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_CUSTOM_TAB', index=2, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=479,
  serialized_end=546,
)
_sym_db.RegisterEnumDescriptor(_SESSIONWINDOW_BROWSERTYPE)

_SESSIONTAB_FAVICONTYPE = _descriptor.EnumDescriptor(
  name='FaviconType',
  full_name='sync_pb.SessionTab.FaviconType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TYPE_WEB_FAVICON', index=0, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=897,
  serialized_end=932,
)
_sym_db.RegisterEnumDescriptor(_SESSIONTAB_FAVICONTYPE)

_TABNAVIGATION_BLOCKEDSTATE = _descriptor.EnumDescriptor(
  name='BlockedState',
  full_name='sync_pb.TabNavigation.BlockedState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STATE_ALLOWED', index=0, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATE_BLOCKED', index=1, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1901,
  serialized_end=1953,
)
_sym_db.RegisterEnumDescriptor(_TABNAVIGATION_BLOCKEDSTATE)

_TABNAVIGATION_PASSWORDSTATE = _descriptor.EnumDescriptor(
  name='PasswordState',
  full_name='sync_pb.TabNavigation.PasswordState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PASSWORD_STATE_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NO_PASSWORD_FIELD', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HAS_PASSWORD_FIELD', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1955,
  serialized_end=2045,
)
_sym_db.RegisterEnumDescriptor(_TABNAVIGATION_PASSWORDSTATE)


_SESSIONSPECIFICS = _descriptor.Descriptor(
  name='SessionSpecifics',
  full_name='sync_pb.SessionSpecifics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session_tag', full_name='sync_pb.SessionSpecifics.session_tag', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='header', full_name='sync_pb.SessionSpecifics.header', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tab', full_name='sync_pb.SessionSpecifics.tab', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tab_node_id', full_name='sync_pb.SessionSpecifics.tab_node_id', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=-1,
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
  serialized_start=55,
  serialized_end=193,
)


_SESSIONHEADER = _descriptor.Descriptor(
  name='SessionHeader',
  full_name='sync_pb.SessionHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='window', full_name='sync_pb.SessionHeader.window', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='client_name', full_name='sync_pb.SessionHeader.client_name', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='device_type', full_name='sync_pb.SessionHeader.device_type', index=2,
      number=4, type=14, cpp_type=8, label=1,
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
  serialized_start=196,
  serialized_end=324,
)


_SESSIONWINDOW = _descriptor.Descriptor(
  name='SessionWindow',
  full_name='sync_pb.SessionWindow',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='window_id', full_name='sync_pb.SessionWindow.window_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='selected_tab_index', full_name='sync_pb.SessionWindow.selected_tab_index', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='browser_type', full_name='sync_pb.SessionWindow.browser_type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tab', full_name='sync_pb.SessionWindow.tab', index=3,
      number=4, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SESSIONWINDOW_BROWSERTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=327,
  serialized_end=546,
)


_SESSIONTAB = _descriptor.Descriptor(
  name='SessionTab',
  full_name='sync_pb.SessionTab',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tab_id', full_name='sync_pb.SessionTab.tab_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='window_id', full_name='sync_pb.SessionTab.window_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tab_visual_index', full_name='sync_pb.SessionTab.tab_visual_index', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='current_navigation_index', full_name='sync_pb.SessionTab.current_navigation_index', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pinned', full_name='sync_pb.SessionTab.pinned', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='extension_app_id', full_name='sync_pb.SessionTab.extension_app_id', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='navigation', full_name='sync_pb.SessionTab.navigation', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='favicon', full_name='sync_pb.SessionTab.favicon', index=7,
      number=8, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\030\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='favicon_type', full_name='sync_pb.SessionTab.favicon_type', index=8,
      number=9, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\030\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='favicon_source', full_name='sync_pb.SessionTab.favicon_source', index=9,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\030\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='variation_id', full_name='sync_pb.SessionTab.variation_id', index=10,
      number=12, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\030\001'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SESSIONTAB_FAVICONTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=549,
  serialized_end=932,
)


_TABNAVIGATION = _descriptor.Descriptor(
  name='TabNavigation',
  full_name='sync_pb.TabNavigation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='virtual_url', full_name='sync_pb.TabNavigation.virtual_url', index=0,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='referrer', full_name='sync_pb.TabNavigation.referrer', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='title', full_name='sync_pb.TabNavigation.title', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_transition', full_name='sync_pb.TabNavigation.page_transition', index=3,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='redirect_type', full_name='sync_pb.TabNavigation.redirect_type', index=4,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unique_id', full_name='sync_pb.TabNavigation.unique_id', index=5,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp_msec', full_name='sync_pb.TabNavigation.timestamp_msec', index=6,
      number=9, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='navigation_forward_back', full_name='sync_pb.TabNavigation.navigation_forward_back', index=7,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='navigation_from_address_bar', full_name='sync_pb.TabNavigation.navigation_from_address_bar', index=8,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='navigation_home_page', full_name='sync_pb.TabNavigation.navigation_home_page', index=9,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='navigation_chain_start', full_name='sync_pb.TabNavigation.navigation_chain_start', index=10,
      number=13, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='navigation_chain_end', full_name='sync_pb.TabNavigation.navigation_chain_end', index=11,
      number=14, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='global_id', full_name='sync_pb.TabNavigation.global_id', index=12,
      number=15, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='search_terms', full_name='sync_pb.TabNavigation.search_terms', index=13,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\030\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='favicon_url', full_name='sync_pb.TabNavigation.favicon_url', index=14,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='blocked_state', full_name='sync_pb.TabNavigation.blocked_state', index=15,
      number=18, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content_pack_categories', full_name='sync_pb.TabNavigation.content_pack_categories', index=16,
      number=19, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='http_status_code', full_name='sync_pb.TabNavigation.http_status_code', index=17,
      number=20, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='obsolete_referrer_policy', full_name='sync_pb.TabNavigation.obsolete_referrer_policy', index=18,
      number=21, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\030\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_restored', full_name='sync_pb.TabNavigation.is_restored', index=19,
      number=22, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='navigation_redirect', full_name='sync_pb.TabNavigation.navigation_redirect', index=20,
      number=23, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_navigation_redirect_url', full_name='sync_pb.TabNavigation.last_navigation_redirect_url', index=21,
      number=24, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='correct_referrer_policy', full_name='sync_pb.TabNavigation.correct_referrer_policy', index=22,
      number=25, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='password_state', full_name='sync_pb.TabNavigation.password_state', index=23,
      number=26, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='task_id', full_name='sync_pb.TabNavigation.task_id', index=24,
      number=27, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ancestor_task_id', full_name='sync_pb.TabNavigation.ancestor_task_id', index=25,
      number=28, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='replaced_navigation', full_name='sync_pb.TabNavigation.replaced_navigation', index=26,
      number=29, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TABNAVIGATION_BLOCKEDSTATE,
    _TABNAVIGATION_PASSWORDSTATE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=935,
  serialized_end=2045,
)


_NAVIGATIONREDIRECT = _descriptor.Descriptor(
  name='NavigationRedirect',
  full_name='sync_pb.NavigationRedirect',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='url', full_name='sync_pb.NavigationRedirect.url', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=2047,
  serialized_end=2080,
)


_REPLACEDNAVIGATION = _descriptor.Descriptor(
  name='ReplacedNavigation',
  full_name='sync_pb.ReplacedNavigation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='first_committed_url', full_name='sync_pb.ReplacedNavigation.first_committed_url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='first_timestamp_msec', full_name='sync_pb.ReplacedNavigation.first_timestamp_msec', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='first_page_transition', full_name='sync_pb.ReplacedNavigation.first_page_transition', index=2,
      number=3, type=14, cpp_type=8, label=1,
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
  serialized_start=2083,
  serialized_end=2228,
)

_SESSIONSPECIFICS.fields_by_name['header'].message_type = _SESSIONHEADER
_SESSIONSPECIFICS.fields_by_name['tab'].message_type = _SESSIONTAB
_SESSIONHEADER.fields_by_name['window'].message_type = _SESSIONWINDOW
_SESSIONHEADER.fields_by_name['device_type'].enum_type = sync__enums__pb2._SYNCENUMS_DEVICETYPE
_SESSIONWINDOW.fields_by_name['browser_type'].enum_type = _SESSIONWINDOW_BROWSERTYPE
_SESSIONWINDOW_BROWSERTYPE.containing_type = _SESSIONWINDOW
_SESSIONTAB.fields_by_name['navigation'].message_type = _TABNAVIGATION
_SESSIONTAB.fields_by_name['favicon_type'].enum_type = _SESSIONTAB_FAVICONTYPE
_SESSIONTAB_FAVICONTYPE.containing_type = _SESSIONTAB
_TABNAVIGATION.fields_by_name['page_transition'].enum_type = sync__enums__pb2._SYNCENUMS_PAGETRANSITION
_TABNAVIGATION.fields_by_name['redirect_type'].enum_type = sync__enums__pb2._SYNCENUMS_PAGETRANSITIONREDIRECTTYPE
_TABNAVIGATION.fields_by_name['blocked_state'].enum_type = _TABNAVIGATION_BLOCKEDSTATE
_TABNAVIGATION.fields_by_name['navigation_redirect'].message_type = _NAVIGATIONREDIRECT
_TABNAVIGATION.fields_by_name['password_state'].enum_type = _TABNAVIGATION_PASSWORDSTATE
_TABNAVIGATION.fields_by_name['replaced_navigation'].message_type = _REPLACEDNAVIGATION
_TABNAVIGATION_BLOCKEDSTATE.containing_type = _TABNAVIGATION
_TABNAVIGATION_PASSWORDSTATE.containing_type = _TABNAVIGATION
_REPLACEDNAVIGATION.fields_by_name['first_page_transition'].enum_type = sync__enums__pb2._SYNCENUMS_PAGETRANSITION
DESCRIPTOR.message_types_by_name['SessionSpecifics'] = _SESSIONSPECIFICS
DESCRIPTOR.message_types_by_name['SessionHeader'] = _SESSIONHEADER
DESCRIPTOR.message_types_by_name['SessionWindow'] = _SESSIONWINDOW
DESCRIPTOR.message_types_by_name['SessionTab'] = _SESSIONTAB
DESCRIPTOR.message_types_by_name['TabNavigation'] = _TABNAVIGATION
DESCRIPTOR.message_types_by_name['NavigationRedirect'] = _NAVIGATIONREDIRECT
DESCRIPTOR.message_types_by_name['ReplacedNavigation'] = _REPLACEDNAVIGATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SessionSpecifics = _reflection.GeneratedProtocolMessageType('SessionSpecifics', (_message.Message,), dict(
  DESCRIPTOR = _SESSIONSPECIFICS,
  __module__ = 'session_specifics_pb2'
  # @@protoc_insertion_point(class_scope:sync_pb.SessionSpecifics)
  ))
_sym_db.RegisterMessage(SessionSpecifics)

SessionHeader = _reflection.GeneratedProtocolMessageType('SessionHeader', (_message.Message,), dict(
  DESCRIPTOR = _SESSIONHEADER,
  __module__ = 'session_specifics_pb2'
  # @@protoc_insertion_point(class_scope:sync_pb.SessionHeader)
  ))
_sym_db.RegisterMessage(SessionHeader)

SessionWindow = _reflection.GeneratedProtocolMessageType('SessionWindow', (_message.Message,), dict(
  DESCRIPTOR = _SESSIONWINDOW,
  __module__ = 'session_specifics_pb2'
  # @@protoc_insertion_point(class_scope:sync_pb.SessionWindow)
  ))
_sym_db.RegisterMessage(SessionWindow)

SessionTab = _reflection.GeneratedProtocolMessageType('SessionTab', (_message.Message,), dict(
  DESCRIPTOR = _SESSIONTAB,
  __module__ = 'session_specifics_pb2'
  # @@protoc_insertion_point(class_scope:sync_pb.SessionTab)
  ))
_sym_db.RegisterMessage(SessionTab)

TabNavigation = _reflection.GeneratedProtocolMessageType('TabNavigation', (_message.Message,), dict(
  DESCRIPTOR = _TABNAVIGATION,
  __module__ = 'session_specifics_pb2'
  # @@protoc_insertion_point(class_scope:sync_pb.TabNavigation)
  ))
_sym_db.RegisterMessage(TabNavigation)

NavigationRedirect = _reflection.GeneratedProtocolMessageType('NavigationRedirect', (_message.Message,), dict(
  DESCRIPTOR = _NAVIGATIONREDIRECT,
  __module__ = 'session_specifics_pb2'
  # @@protoc_insertion_point(class_scope:sync_pb.NavigationRedirect)
  ))
_sym_db.RegisterMessage(NavigationRedirect)

ReplacedNavigation = _reflection.GeneratedProtocolMessageType('ReplacedNavigation', (_message.Message,), dict(
  DESCRIPTOR = _REPLACEDNAVIGATION,
  __module__ = 'session_specifics_pb2'
  # @@protoc_insertion_point(class_scope:sync_pb.ReplacedNavigation)
  ))
_sym_db.RegisterMessage(ReplacedNavigation)


DESCRIPTOR._options = None
_SESSIONTAB.fields_by_name['favicon']._options = None
_SESSIONTAB.fields_by_name['favicon_type']._options = None
_SESSIONTAB.fields_by_name['favicon_source']._options = None
_SESSIONTAB.fields_by_name['variation_id']._options = None
_TABNAVIGATION.fields_by_name['search_terms']._options = None
_TABNAVIGATION.fields_by_name['obsolete_referrer_policy']._options = None
# @@protoc_insertion_point(module_scope)
