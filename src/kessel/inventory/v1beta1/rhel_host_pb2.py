# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kessel/inventory/v1beta1/rhel_host.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from kessel.inventory.v1beta1 import metadata_pb2 as kessel_dot_inventory_dot_v1beta1_dot_metadata__pb2
try:
  kessel_dot_inventory_dot_v1beta1_dot_resource__tag__pb2 = kessel_dot_inventory_dot_v1beta1_dot_metadata__pb2.kessel_dot_inventory_dot_v1beta1_dot_resource__tag__pb2
except AttributeError:
  kessel_dot_inventory_dot_v1beta1_dot_resource__tag__pb2 = kessel_dot_inventory_dot_v1beta1_dot_metadata__pb2.kessel.inventory.v1beta1.resource_tag_pb2
from kessel.inventory.v1beta1 import reporter_data_pb2 as kessel_dot_inventory_dot_v1beta1_dot_reporter__data__pb2

from kessel.inventory.v1beta1.metadata_pb2 import *
from kessel.inventory.v1beta1.reporter_data_pb2 import *

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(kessel/inventory/v1beta1/rhel_host.proto\x12\x1c\x61pi.kessel.inventory.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\'kessel/inventory/v1beta1/metadata.proto\x1a,kessel/inventory/v1beta1/reporter_data.proto\"\xdf\x01\n\x08RHELHost\x12>\n\x08metadata\x18\x01 \x01(\x0b\x32&.api.kessel.inventory.v1beta1.MetadataB\x04\xe2\x41\x01\x02\x12J\n\rreporter_data\x18\xc8\xd0\xfat \x01(\x0b\x32*.api.kessel.inventory.v1beta1.ReporterDataB\x04\xe2\x41\x01\x04\x12G\n\treporters\x18\xce\x90\xbd\xa8\x01 \x03(\x0b\x32*.api.kessel.inventory.v1beta1.ReporterDataB\x04\xe2\x41\x01\x03\x42\x46\n\x1c\x61pi.kessel.inventory.v1beta1P\x01Z$api/kessel/inventory/v1beta1;v1beta1P\x01P\x02\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'kessel.inventory.v1beta1.rhel_host_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\034api.kessel.inventory.v1beta1P\001Z$api/kessel/inventory/v1beta1;v1beta1'
  _globals['_RHELHOST'].fields_by_name['metadata']._loaded_options = None
  _globals['_RHELHOST'].fields_by_name['metadata']._serialized_options = b'\342A\001\002'
  _globals['_RHELHOST'].fields_by_name['reporter_data']._loaded_options = None
  _globals['_RHELHOST'].fields_by_name['reporter_data']._serialized_options = b'\342A\001\004'
  _globals['_RHELHOST'].fields_by_name['reporters']._loaded_options = None
  _globals['_RHELHOST'].fields_by_name['reporters']._serialized_options = b'\342A\001\003'
  _globals['_RHELHOST']._serialized_start=195
  _globals['_RHELHOST']._serialized_end=418
# @@protoc_insertion_point(module_scope)
