# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: psa_export_public_key.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='psa_export_public_key.proto',
  package='psa_export_public_key',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1bpsa_export_public_key.proto\x12\x15psa_export_public_key\"\x1d\n\tOperation\x12\x10\n\x08key_name\x18\x01 \x01(\t\"\x16\n\x06Result\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\x62\x06proto3')
)




_OPERATION = _descriptor.Descriptor(
  name='Operation',
  full_name='psa_export_public_key.Operation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key_name', full_name='psa_export_public_key.Operation.key_name', index=0,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=54,
  serialized_end=83,
)


_RESULT = _descriptor.Descriptor(
  name='Result',
  full_name='psa_export_public_key.Result',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='psa_export_public_key.Result.data', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_end=107,
)

DESCRIPTOR.message_types_by_name['Operation'] = _OPERATION
DESCRIPTOR.message_types_by_name['Result'] = _RESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Operation = _reflection.GeneratedProtocolMessageType('Operation', (_message.Message,), dict(
  DESCRIPTOR = _OPERATION,
  __module__ = 'psa_export_public_key_pb2'
  # @@protoc_insertion_point(class_scope:psa_export_public_key.Operation)
  ))
_sym_db.RegisterMessage(Operation)

Result = _reflection.GeneratedProtocolMessageType('Result', (_message.Message,), dict(
  DESCRIPTOR = _RESULT,
  __module__ = 'psa_export_public_key_pb2'
  # @@protoc_insertion_point(class_scope:psa_export_public_key.Result)
  ))
_sym_db.RegisterMessage(Result)


# @@protoc_insertion_point(module_scope)
