# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: kessel/inventory/v1beta1/relationships/metadata.proto
# Protobuf Python Version: 6.30.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    6,
    30,
    2,
    '',
    'kessel/inventory/v1beta1/relationships/metadata.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from buf.validate import validate_pb2 as buf_dot_validate_dot_validate__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5kessel/inventory/v1beta1/relationships/metadata.proto\x12&kessel.inventory.v1beta1.relationships\x1a\x1b\x62uf/validate/validate.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xbe\x02\n\x08Metadata\x12\x14\n\x02id\x18\x9c\x1a \x01(\tB\x03\xe0\x41\x03R\x02id\x12\x34\n\x11relationship_type\x18\xe4\xe9\xd7w \x01(\tB\x03\xe0\x41\x03R\x11relationship_type\x12@\n\ncreated_at\x18\xc8\x1a \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x03\xe0\x41\x03R\ncreated_at\x12@\n\nupdated_at\x18\xc9\x1a \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x03\xe0\x41\x03R\nupdated_at\x12@\n\ndeleted_at\x18\xca\x1a \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x03\xe0\x41\x03R\ndeleted_at\x12 \n\x06org_id\x18\xac\x1b \x01(\tB\x07\xbaH\x04r\x02\x10\x01R\x06org_idB\x8e\x01\n6org.project_kessel.api.inventory.v1beta1.relationshipsP\x01ZRgithub.com/project-kessel/inventory-api/api/kessel/inventory/v1beta1/relationshipsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'kessel.inventory.v1beta1.relationships.metadata_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n6org.project_kessel.api.inventory.v1beta1.relationshipsP\001ZRgithub.com/project-kessel/inventory-api/api/kessel/inventory/v1beta1/relationships'
  _globals['_METADATA'].fields_by_name['id']._loaded_options = None
  _globals['_METADATA'].fields_by_name['id']._serialized_options = b'\340A\003'
  _globals['_METADATA'].fields_by_name['relationship_type']._loaded_options = None
  _globals['_METADATA'].fields_by_name['relationship_type']._serialized_options = b'\340A\003'
  _globals['_METADATA'].fields_by_name['created_at']._loaded_options = None
  _globals['_METADATA'].fields_by_name['created_at']._serialized_options = b'\340A\003'
  _globals['_METADATA'].fields_by_name['updated_at']._loaded_options = None
  _globals['_METADATA'].fields_by_name['updated_at']._serialized_options = b'\340A\003'
  _globals['_METADATA'].fields_by_name['deleted_at']._loaded_options = None
  _globals['_METADATA'].fields_by_name['deleted_at']._serialized_options = b'\340A\003'
  _globals['_METADATA'].fields_by_name['org_id']._loaded_options = None
  _globals['_METADATA'].fields_by_name['org_id']._serialized_options = b'\272H\004r\002\020\001'
  _globals['_METADATA']._serialized_start=193
  _globals['_METADATA']._serialized_end=511
# @@protoc_insertion_point(module_scope)
