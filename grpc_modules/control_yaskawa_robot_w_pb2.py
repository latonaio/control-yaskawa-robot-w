# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: control_yaskawa_robot_w.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='control_yaskawa_robot_w.proto',
  package='controlyaskawarobotw',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x1d\x63ontrol_yaskawa_robot_w.proto\x12\x14\x63ontrolyaskawarobotw\x1a\x1cgoogle/protobuf/struct.proto\">\n\x0cWriteRequest\x12.\n\rwrite_command\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\"O\n\rWriteResponse\x12+\n\nrobot_data\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x11\n\ttimestamp\x18\x02 \x01(\t2j\n\x14\x43ontrolYaskawaRobotW\x12R\n\x05Write\x12\".controlyaskawarobotw.WriteRequest\x1a#.controlyaskawarobotw.WriteResponse\"\x00\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_WRITEREQUEST = _descriptor.Descriptor(
  name='WriteRequest',
  full_name='controlyaskawarobotw.WriteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='write_command', full_name='controlyaskawarobotw.WriteRequest.write_command', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=85,
  serialized_end=147,
)


_WRITERESPONSE = _descriptor.Descriptor(
  name='WriteResponse',
  full_name='controlyaskawarobotw.WriteResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='robot_data', full_name='controlyaskawarobotw.WriteResponse.robot_data', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='controlyaskawarobotw.WriteResponse.timestamp', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=149,
  serialized_end=228,
)

_WRITEREQUEST.fields_by_name['write_command'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_WRITERESPONSE.fields_by_name['robot_data'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
DESCRIPTOR.message_types_by_name['WriteRequest'] = _WRITEREQUEST
DESCRIPTOR.message_types_by_name['WriteResponse'] = _WRITERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

WriteRequest = _reflection.GeneratedProtocolMessageType('WriteRequest', (_message.Message,), {
  'DESCRIPTOR' : _WRITEREQUEST,
  '__module__' : 'control_yaskawa_robot_w_pb2'
  # @@protoc_insertion_point(class_scope:controlyaskawarobotw.WriteRequest)
  })
_sym_db.RegisterMessage(WriteRequest)

WriteResponse = _reflection.GeneratedProtocolMessageType('WriteResponse', (_message.Message,), {
  'DESCRIPTOR' : _WRITERESPONSE,
  '__module__' : 'control_yaskawa_robot_w_pb2'
  # @@protoc_insertion_point(class_scope:controlyaskawarobotw.WriteResponse)
  })
_sym_db.RegisterMessage(WriteResponse)



_CONTROLYASKAWAROBOTW = _descriptor.ServiceDescriptor(
  name='ControlYaskawaRobotW',
  full_name='controlyaskawarobotw.ControlYaskawaRobotW',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=230,
  serialized_end=336,
  methods=[
  _descriptor.MethodDescriptor(
    name='Write',
    full_name='controlyaskawarobotw.ControlYaskawaRobotW.Write',
    index=0,
    containing_service=None,
    input_type=_WRITEREQUEST,
    output_type=_WRITERESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CONTROLYASKAWAROBOTW)

DESCRIPTOR.services_by_name['ControlYaskawaRobotW'] = _CONTROLYASKAWAROBOTW

# @@protoc_insertion_point(module_scope)
