# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: kessel/inventory/v1beta1/resources/k8s_clusters_service.proto
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
    'kessel/inventory/v1beta1/resources/k8s_clusters_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from buf.validate import validate_pb2 as buf_dot_validate_dot_validate__pb2
from kessel.inventory.v1beta1.resources import k8s_cluster_pb2 as kessel_dot_inventory_dot_v1beta1_dot_resources_dot_k8s__cluster__pb2
from kessel.inventory.v1beta1.resources import reporter_data_pb2 as kessel_dot_inventory_dot_v1beta1_dot_resources_dot_reporter__data__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=kessel/inventory/v1beta1/resources/k8s_clusters_service.proto\x12\"kessel.inventory.v1beta1.resources\x1a\x1cgoogle/api/annotations.proto\x1a\x1b\x62uf/validate/validate.proto\x1a\x34kessel/inventory/v1beta1/resources/k8s_cluster.proto\x1a\x36kessel/inventory/v1beta1/resources/reporter_data.proto\"k\n\x17\x43reateK8sClusterRequest\x12P\n\x0bk8s_cluster\x18\x01 \x01(\x0b\x32..kessel.inventory.v1beta1.resources.K8sClusterR\x0bk8s_cluster\"\x1a\n\x18\x43reateK8sClusterResponse\"k\n\x17UpdateK8sClusterRequest\x12P\n\x0bk8s_cluster\x18\x01 \x01(\x0b\x32..kessel.inventory.v1beta1.resources.K8sClusterR\x0bk8s_cluster\"\x1a\n\x18UpdateK8sClusterResponse\"y\n\x17\x44\x65leteK8sClusterRequest\x12^\n\rreporter_data\x18\x01 \x01(\x0b\x32\x30.kessel.inventory.v1beta1.resources.ReporterDataB\x06\xbaH\x03\xc8\x01\x01R\rreporter_data\"\x1a\n\x18\x44\x65leteK8sClusterResponse2\xf7\x04\n\x17KesselK8sClusterService\x12\xc7\x01\n\x10\x43reateK8sCluster\x12;.kessel.inventory.v1beta1.resources.CreateK8sClusterRequest\x1a<.kessel.inventory.v1beta1.resources.CreateK8sClusterResponse\"8\x82\xd3\xe4\x93\x02\x32\"-/api/inventory/v1beta1/resources/k8s-clusters:\x01*\x12\xc7\x01\n\x10UpdateK8sCluster\x12;.kessel.inventory.v1beta1.resources.UpdateK8sClusterRequest\x1a<.kessel.inventory.v1beta1.resources.UpdateK8sClusterResponse\"8\x82\xd3\xe4\x93\x02\x32\x1a-/api/inventory/v1beta1/resources/k8s-clusters:\x01*\x12\xc7\x01\n\x10\x44\x65leteK8sCluster\x12;.kessel.inventory.v1beta1.resources.DeleteK8sClusterRequest\x1a<.kessel.inventory.v1beta1.resources.DeleteK8sClusterResponse\"8\x82\xd3\xe4\x93\x02\x32*-/api/inventory/v1beta1/resources/k8s-clusters:\x01*B\x86\x01\n2org.project_kessel.api.inventory.v1beta1.resourcesP\x01ZNgithub.com/project-kessel/inventory-api/api/kessel/inventory/v1beta1/resourcesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'kessel.inventory.v1beta1.resources.k8s_clusters_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n2org.project_kessel.api.inventory.v1beta1.resourcesP\001ZNgithub.com/project-kessel/inventory-api/api/kessel/inventory/v1beta1/resources'
  _globals['_DELETEK8SCLUSTERREQUEST'].fields_by_name['reporter_data']._loaded_options = None
  _globals['_DELETEK8SCLUSTERREQUEST'].fields_by_name['reporter_data']._serialized_options = b'\272H\003\310\001\001'
  _globals['_KESSELK8SCLUSTERSERVICE'].methods_by_name['CreateK8sCluster']._loaded_options = None
  _globals['_KESSELK8SCLUSTERSERVICE'].methods_by_name['CreateK8sCluster']._serialized_options = b'\202\323\344\223\0022\"-/api/inventory/v1beta1/resources/k8s-clusters:\001*'
  _globals['_KESSELK8SCLUSTERSERVICE'].methods_by_name['UpdateK8sCluster']._loaded_options = None
  _globals['_KESSELK8SCLUSTERSERVICE'].methods_by_name['UpdateK8sCluster']._serialized_options = b'\202\323\344\223\0022\032-/api/inventory/v1beta1/resources/k8s-clusters:\001*'
  _globals['_KESSELK8SCLUSTERSERVICE'].methods_by_name['DeleteK8sCluster']._loaded_options = None
  _globals['_KESSELK8SCLUSTERSERVICE'].methods_by_name['DeleteK8sCluster']._serialized_options = b'\202\323\344\223\0022*-/api/inventory/v1beta1/resources/k8s-clusters:\001*'
  _globals['_CREATEK8SCLUSTERREQUEST']._serialized_start=270
  _globals['_CREATEK8SCLUSTERREQUEST']._serialized_end=377
  _globals['_CREATEK8SCLUSTERRESPONSE']._serialized_start=379
  _globals['_CREATEK8SCLUSTERRESPONSE']._serialized_end=405
  _globals['_UPDATEK8SCLUSTERREQUEST']._serialized_start=407
  _globals['_UPDATEK8SCLUSTERREQUEST']._serialized_end=514
  _globals['_UPDATEK8SCLUSTERRESPONSE']._serialized_start=516
  _globals['_UPDATEK8SCLUSTERRESPONSE']._serialized_end=542
  _globals['_DELETEK8SCLUSTERREQUEST']._serialized_start=544
  _globals['_DELETEK8SCLUSTERREQUEST']._serialized_end=665
  _globals['_DELETEK8SCLUSTERRESPONSE']._serialized_start=667
  _globals['_DELETEK8SCLUSTERRESPONSE']._serialized_end=693
  _globals['_KESSELK8SCLUSTERSERVICE']._serialized_start=696
  _globals['_KESSELK8SCLUSTERSERVICE']._serialized_end=1327
# @@protoc_insertion_point(module_scope)
