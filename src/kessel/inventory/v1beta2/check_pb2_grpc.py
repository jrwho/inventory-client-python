# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from kessel.inventory.v1beta2 import check_pb2 as kessel_dot_inventory_dot_v1beta2_dot_check__pb2


class KesselCheckServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Check = channel.unary_unary(
                '/kessel.inventory.v1beta2.KesselCheckService/Check',
                request_serializer=kessel_dot_inventory_dot_v1beta2_dot_check__pb2.CheckRequest.SerializeToString,
                response_deserializer=kessel_dot_inventory_dot_v1beta2_dot_check__pb2.CheckResponse.FromString,
                _registered_method=True)
        self.CheckForUpdate = channel.unary_unary(
                '/kessel.inventory.v1beta2.KesselCheckService/CheckForUpdate',
                request_serializer=kessel_dot_inventory_dot_v1beta2_dot_check__pb2.CheckForUpdateRequest.SerializeToString,
                response_deserializer=kessel_dot_inventory_dot_v1beta2_dot_check__pb2.CheckForUpdateResponse.FromString,
                _registered_method=True)


class KesselCheckServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Check(self, request, context):
        """Checks for the existence of a single Relationship
        (a Relation between a Resource and a Subject or Subject Set).
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckForUpdate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_KesselCheckServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Check': grpc.unary_unary_rpc_method_handler(
                    servicer.Check,
                    request_deserializer=kessel_dot_inventory_dot_v1beta2_dot_check__pb2.CheckRequest.FromString,
                    response_serializer=kessel_dot_inventory_dot_v1beta2_dot_check__pb2.CheckResponse.SerializeToString,
            ),
            'CheckForUpdate': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckForUpdate,
                    request_deserializer=kessel_dot_inventory_dot_v1beta2_dot_check__pb2.CheckForUpdateRequest.FromString,
                    response_serializer=kessel_dot_inventory_dot_v1beta2_dot_check__pb2.CheckForUpdateResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'kessel.inventory.v1beta2.KesselCheckService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('kessel.inventory.v1beta2.KesselCheckService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class KesselCheckService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Check(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/kessel.inventory.v1beta2.KesselCheckService/Check',
            kessel_dot_inventory_dot_v1beta2_dot_check__pb2.CheckRequest.SerializeToString,
            kessel_dot_inventory_dot_v1beta2_dot_check__pb2.CheckResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def CheckForUpdate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/kessel.inventory.v1beta2.KesselCheckService/CheckForUpdate',
            kessel_dot_inventory_dot_v1beta2_dot_check__pb2.CheckForUpdateRequest.SerializeToString,
            kessel_dot_inventory_dot_v1beta2_dot_check__pb2.CheckForUpdateResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
