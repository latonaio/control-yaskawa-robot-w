# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import control_yaskawa_robot_w_pb2 as control__yaskawa__robot__w__pb2


class ControlYaskawaRobotWStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Write = channel.unary_unary(
                '/controlyaskawarobotw.ControlYaskawaRobotW/Write',
                request_serializer=control__yaskawa__robot__w__pb2.WriteRequest.SerializeToString,
                response_deserializer=control__yaskawa__robot__w__pb2.WriteResponse.FromString,
                )


class ControlYaskawaRobotWServicer(object):
    """Missing associated documentation comment in .proto file"""

    def Write(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ControlYaskawaRobotWServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Write': grpc.unary_unary_rpc_method_handler(
                    servicer.Write,
                    request_deserializer=control__yaskawa__robot__w__pb2.WriteRequest.FromString,
                    response_serializer=control__yaskawa__robot__w__pb2.WriteResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'controlyaskawarobotw.ControlYaskawaRobotW', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ControlYaskawaRobotW(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def Write(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/controlyaskawarobotw.ControlYaskawaRobotW/Write',
            control__yaskawa__robot__w__pb2.WriteRequest.SerializeToString,
            control__yaskawa__robot__w__pb2.WriteResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
