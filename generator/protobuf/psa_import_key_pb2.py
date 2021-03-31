# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: psa_import_key.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import psa_key_attributes_pb2 as psa__key__attributes__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='psa_import_key.proto',
  package='psa_import_key',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x14psa_import_key.proto\x12\x0epsa_import_key\x1a\x18psa_key_attributes.proto\"b\n\tOperation\x12\x10\n\x08key_name\x18\x01 \x01(\t\x12\x35\n\nattributes\x18\x02 \x01(\x0b\x32!.psa_key_attributes.KeyAttributes\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\"\x08\n\x06Resultb\x06proto3')
  ,
  dependencies=[psa__key__attributes__pb2.DESCRIPTOR,])




_OPERATION = _descriptor.Descriptor(
  name='Operation',
  full_name='psa_import_key.Operation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key_name', full_name='psa_import_key.Operation.key_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='attributes', full_name='psa_import_key.Operation.attributes', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='psa_import_key.Operation.data', index=2,
      number=3, type=12, cpp_type=9, label=1,
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
  serialized_start=66,
  serialized_end=164,
)


_RESULT = _descriptor.Descriptor(
  name='Result',
  full_name='psa_import_key.Result',
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=166,
  serialized_end=174,
)

_OPERATION.fields_by_name['attributes'].message_type = psa__key__attributes__pb2._KEYATTRIBUTES
DESCRIPTOR.message_types_by_name['Operation'] = _OPERATION
DESCRIPTOR.message_types_by_name['Result'] = _RESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Operation = _reflection.GeneratedProtocolMessageType('Operation', (_message.Message,), dict(
  DESCRIPTOR = _OPERATION,
  __module__ = 'psa_import_key_pb2'
  # @@protoc_insertion_point(class_scope:psa_import_key.Operation)
  ))
_sym_db.RegisterMessage(Operation)

Result = _reflection.GeneratedProtocolMessageType('Result', (_message.Message,), dict(
  DESCRIPTOR = _RESULT,
  __module__ = 'psa_import_key_pb2'
  # @@protoc_insertion_point(class_scope:psa_import_key.Result)
  ))
_sym_db.RegisterMessage(Result)


# @@protoc_insertion_point(module_scope)
