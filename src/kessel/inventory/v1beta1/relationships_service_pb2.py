# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kessel/inventory/v1beta1/relationships_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from kessel.inventory.v1beta1 import policy_relationship_pb2 as kessel_dot_inventory_dot_v1beta1_dot_policy__relationship__pb2
from kessel.inventory.v1beta1 import update_resource_relationship_by_urnhs_resources_parameter_pb2 as kessel_dot_inventory_dot_v1beta1_dot_update__resource__relationship__by__urnhs__resources__parameter__pb2

from kessel.inventory.v1beta1.policy_relationship_pb2 import *
from kessel.inventory.v1beta1.update_resource_relationship_by_urnhs_resources_parameter_pb2 import *

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4kessel/inventory/v1beta1/relationships_service.proto\x12\x1c\x61pi.kessel.inventory.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x32kessel/inventory/v1beta1/policy_relationship.proto\x1aXkessel/inventory/v1beta1/update_resource_relationship_by_urnhs_resources_parameter.proto\"o\n\x1f\x43reatePolicyRelationshipRequest\x12L\n\x12policyRelationship\x18\x01 \x01(\x0b\x32\x30.api.kessel.inventory.v1beta1.PolicyRelationship\"p\n CreatePolicyRelationshipResponse\x12L\n\x12policyRelationship\x18\x01 \x01(\x0b\x32\x30.api.kessel.inventory.v1beta1.PolicyRelationship\"\xde\x01\n(UpdateResourceRelationshipByURNHsRequest\x12\x64\n\tresources\x18\x01 \x01(\x0b\x32Q.api.kessel.inventory.v1beta1.UpdateResourceRelationshipByURNHsResourcesParameter\x12L\n\x12policyRelationship\x18\x02 \x01(\x0b\x32\x30.api.kessel.inventory.v1beta1.PolicyRelationship\")\n\'UpdateResourceRelationshipByURNResponse\"\x8e\x01\n&DeleteResourceRelationshipByURNRequest\x12\x64\n\tresources\x18\x01 \x01(\x0b\x32Q.api.kessel.inventory.v1beta1.UpdateResourceRelationshipByURNHsResourcesParameter\")\n\'DeleteResourceRelationshipByURNResponse2\xb5\x05\n\x14RelationshipsService\x12\xd4\x01\n\x18\x43reatePolicyRelationship\x12=.api.kessel.inventory.v1beta1.CreatePolicyRelationshipRequest\x1a>.api.kessel.inventory.v1beta1.CreatePolicyRelationshipResponse\"9\x82\xd3\xe4\x93\x02\x33\"\x1d/v1beta1/policy_relationships:\x12policyRelationship\x12\xed\x01\n!UpdateResourceRelationshipByURNHs\x12\x46.api.kessel.inventory.v1beta1.UpdateResourceRelationshipByURNHsRequest\x1a\x45.api.kessel.inventory.v1beta1.UpdateResourceRelationshipByURNResponse\"9\x82\xd3\xe4\x93\x02\x33\x1a\x1d/v1beta1/policy_relationships:\x12policyRelationship\x12\xd5\x01\n\x1f\x44\x65leteResourceRelationshipByURN\x12\x44.api.kessel.inventory.v1beta1.DeleteResourceRelationshipByURNRequest\x1a\x45.api.kessel.inventory.v1beta1.DeleteResourceRelationshipByURNResponse\"%\x82\xd3\xe4\x93\x02\x1f*\x1d/v1beta1/policy_relationshipsBF\n\x1c\x61pi.kessel.inventory.v1beta1P\x01Z$api/kessel/inventory/v1beta1;v1beta1P\x01P\x02\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'kessel.inventory.v1beta1.relationships_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\034api.kessel.inventory.v1beta1P\001Z$api/kessel/inventory/v1beta1;v1beta1'
  _globals['_RELATIONSHIPSSERVICE'].methods_by_name['CreatePolicyRelationship']._loaded_options = None
  _globals['_RELATIONSHIPSSERVICE'].methods_by_name['CreatePolicyRelationship']._serialized_options = b'\202\323\344\223\0023\"\035/v1beta1/policy_relationships:\022policyRelationship'
  _globals['_RELATIONSHIPSSERVICE'].methods_by_name['UpdateResourceRelationshipByURNHs']._loaded_options = None
  _globals['_RELATIONSHIPSSERVICE'].methods_by_name['UpdateResourceRelationshipByURNHs']._serialized_options = b'\202\323\344\223\0023\032\035/v1beta1/policy_relationships:\022policyRelationship'
  _globals['_RELATIONSHIPSSERVICE'].methods_by_name['DeleteResourceRelationshipByURN']._loaded_options = None
  _globals['_RELATIONSHIPSSERVICE'].methods_by_name['DeleteResourceRelationshipByURN']._serialized_options = b'\202\323\344\223\002\037*\035/v1beta1/policy_relationships'
  _globals['_CREATEPOLICYRELATIONSHIPREQUEST']._serialized_start=258
  _globals['_CREATEPOLICYRELATIONSHIPREQUEST']._serialized_end=369
  _globals['_CREATEPOLICYRELATIONSHIPRESPONSE']._serialized_start=371
  _globals['_CREATEPOLICYRELATIONSHIPRESPONSE']._serialized_end=483
  _globals['_UPDATERESOURCERELATIONSHIPBYURNHSREQUEST']._serialized_start=486
  _globals['_UPDATERESOURCERELATIONSHIPBYURNHSREQUEST']._serialized_end=708
  _globals['_UPDATERESOURCERELATIONSHIPBYURNRESPONSE']._serialized_start=710
  _globals['_UPDATERESOURCERELATIONSHIPBYURNRESPONSE']._serialized_end=751
  _globals['_DELETERESOURCERELATIONSHIPBYURNREQUEST']._serialized_start=754
  _globals['_DELETERESOURCERELATIONSHIPBYURNREQUEST']._serialized_end=896
  _globals['_DELETERESOURCERELATIONSHIPBYURNRESPONSE']._serialized_start=898
  _globals['_DELETERESOURCERELATIONSHIPBYURNRESPONSE']._serialized_end=939
  _globals['_RELATIONSHIPSSERVICE']._serialized_start=942
  _globals['_RELATIONSHIPSSERVICE']._serialized_end=1635
# @@protoc_insertion_point(module_scope)
