# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: kessel/inventory/v1beta2/resource.proto
# Protobuf Python Version: 6.30.1
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
    1,
    '',
    'kessel/inventory/v1beta2/resource.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from kessel.inventory.v1beta2 import reporter_data_pb2 as kessel_dot_inventory_dot_v1beta2_dot_reporter__data__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from buf.validate import validate_pb2 as buf_dot_validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'kessel/inventory/v1beta2/resource.proto\x12\x18kessel.inventory.v1beta2\x1a,kessel/inventory/v1beta2/reporter_data.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1b\x62uf/validate/validate.proto\"\x83\x02\n\x08Resource\x12!\n\x0cinventory_id\x18\x01 \x01(\tR\x0binventoryId\x12,\n\rresource_type\x18\x02 \x01(\tB\x07\xbaH\x04r\x02\x10\x01R\x0cresourceType\x12S\n\rreporter_data\x18\x03 \x01(\x0b\x32&.kessel.inventory.v1beta2.ReporterDataB\x06\xbaH\x03\xc8\x01\x01R\x0creporterData\x12Q\n\x14\x63ommon_resource_data\x18\x04 \x01(\x0b\x32\x17.google.protobuf.StructB\x06\xbaH\x03\xc8\x01\x01R\x12\x63ommonResourceDataBr\n(org.project_kessel.api.inventory.v1beta2P\x01ZDgithub.com/project-kessel/inventory-api/api/kessel/inventory/v1beta2b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'kessel.inventory.v1beta2.resource_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n(org.project_kessel.api.inventory.v1beta2P\001ZDgithub.com/project-kessel/inventory-api/api/kessel/inventory/v1beta2'
  _globals['_RESOURCE'].fields_by_name['resource_type']._loaded_options = None
  _globals['_RESOURCE'].fields_by_name['resource_type']._serialized_options = b'\272H\004r\002\020\001'
  _globals['_RESOURCE'].fields_by_name['reporter_data']._loaded_options = None
  _globals['_RESOURCE'].fields_by_name['reporter_data']._serialized_options = b'\272H\003\310\001\001'
  _globals['_RESOURCE'].fields_by_name['common_resource_data']._loaded_options = None
  _globals['_RESOURCE'].fields_by_name['common_resource_data']._serialized_options = b'\272H\003\310\001\001'
  _globals['_RESOURCE']._serialized_start=175
  _globals['_RESOURCE']._serialized_end=434
# @@protoc_insertion_point(module_scope)
