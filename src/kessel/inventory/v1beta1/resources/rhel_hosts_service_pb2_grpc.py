# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from kessel.inventory.v1beta1.resources import rhel_hosts_service_pb2 as kessel_dot_inventory_dot_v1beta1_dot_resources_dot_rhel__hosts__service__pb2


class KesselRhelHostServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateRhelHost = channel.unary_unary(
                '/kessel.inventory.v1beta1.resources.KesselRhelHostService/CreateRhelHost',
                request_serializer=kessel_dot_inventory_dot_v1beta1_dot_resources_dot_rhel__hosts__service__pb2.CreateRhelHostRequest.SerializeToString,
                response_deserializer=kessel_dot_inventory_dot_v1beta1_dot_resources_dot_rhel__hosts__service__pb2.CreateRhelHostResponse.FromString,
                _registered_method=True)
        self.UpdateRhelHost = channel.unary_unary(
                '/kessel.inventory.v1beta1.resources.KesselRhelHostService/UpdateRhelHost',
                request_serializer=kessel_dot_inventory_dot_v1beta1_dot_resources_dot_rhel__hosts__service__pb2.UpdateRhelHostRequest.SerializeToString,
                response_deserializer=kessel_dot_inventory_dot_v1beta1_dot_resources_dot_rhel__hosts__service__pb2.UpdateRhelHostResponse.FromString,
                _registered_method=True)
        self.DeleteRhelHost = channel.unary_unary(
                '/kessel.inventory.v1beta1.resources.KesselRhelHostService/DeleteRhelHost',
                request_serializer=kessel_dot_inventory_dot_v1beta1_dot_resources_dot_rhel__hosts__service__pb2.DeleteRhelHostRequest.SerializeToString,
                response_deserializer=kessel_dot_inventory_dot_v1beta1_dot_resources_dot_rhel__hosts__service__pb2.DeleteRhelHostResponse.FromString,
                _registered_method=True)


class KesselRhelHostServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateRhelHost(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateRhelHost(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteRhelHost(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_KesselRhelHostServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateRhelHost': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateRhelHost,
                    request_deserializer=kessel_dot_inventory_dot_v1beta1_dot_resources_dot_rhel__hosts__service__pb2.CreateRhelHostRequest.FromString,
                    response_serializer=kessel_dot_inventory_dot_v1beta1_dot_resources_dot_rhel__hosts__service__pb2.CreateRhelHostResponse.SerializeToString,
            ),
            'UpdateRhelHost': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateRhelHost,
                    request_deserializer=kessel_dot_inventory_dot_v1beta1_dot_resources_dot_rhel__hosts__service__pb2.UpdateRhelHostRequest.FromString,
                    response_serializer=kessel_dot_inventory_dot_v1beta1_dot_resources_dot_rhel__hosts__service__pb2.UpdateRhelHostResponse.SerializeToString,
            ),
            'DeleteRhelHost': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteRhelHost,
                    request_deserializer=kessel_dot_inventory_dot_v1beta1_dot_resources_dot_rhel__hosts__service__pb2.DeleteRhelHostRequest.FromString,
                    response_serializer=kessel_dot_inventory_dot_v1beta1_dot_resources_dot_rhel__hosts__service__pb2.DeleteRhelHostResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'kessel.inventory.v1beta1.resources.KesselRhelHostService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('kessel.inventory.v1beta1.resources.KesselRhelHostService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class KesselRhelHostService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateRhelHost(request,
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
            '/kessel.inventory.v1beta1.resources.KesselRhelHostService/CreateRhelHost',
            kessel_dot_inventory_dot_v1beta1_dot_resources_dot_rhel__hosts__service__pb2.CreateRhelHostRequest.SerializeToString,
            kessel_dot_inventory_dot_v1beta1_dot_resources_dot_rhel__hosts__service__pb2.CreateRhelHostResponse.FromString,
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
    def UpdateRhelHost(request,
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
            '/kessel.inventory.v1beta1.resources.KesselRhelHostService/UpdateRhelHost',
            kessel_dot_inventory_dot_v1beta1_dot_resources_dot_rhel__hosts__service__pb2.UpdateRhelHostRequest.SerializeToString,
            kessel_dot_inventory_dot_v1beta1_dot_resources_dot_rhel__hosts__service__pb2.UpdateRhelHostResponse.FromString,
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
    def DeleteRhelHost(request,
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
            '/kessel.inventory.v1beta1.resources.KesselRhelHostService/DeleteRhelHost',
            kessel_dot_inventory_dot_v1beta1_dot_resources_dot_rhel__hosts__service__pb2.DeleteRhelHostRequest.SerializeToString,
            kessel_dot_inventory_dot_v1beta1_dot_resources_dot_rhel__hosts__service__pb2.DeleteRhelHostResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
