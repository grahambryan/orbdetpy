# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import orbdetpy.rpc.messages_pb2 as messages__pb2


class UtilitiesStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.importTDM = channel.unary_unary(
                '/Utilities/importTDM',
                request_serializer=messages__pb2.ImportTDMInput.SerializeToString,
                response_deserializer=messages__pb2.Measurement2DArray.FromString,
                )
        self.interpolateEphemeris = channel.unary_unary(
                '/Utilities/interpolateEphemeris',
                request_serializer=messages__pb2.InterpolateEphemerisInput.SerializeToString,
                response_deserializer=messages__pb2.MeasurementArray.FromString,
                )
        self.getDensity = channel.unary_unary(
                '/Utilities/getDensity',
                request_serializer=messages__pb2.TransformFrameInput.SerializeToString,
                response_deserializer=messages__pb2.DoubleArray.FromString,
                )


class UtilitiesServicer(object):
    """Missing associated documentation comment in .proto file."""

    def importTDM(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def interpolateEphemeris(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getDensity(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UtilitiesServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'importTDM': grpc.unary_unary_rpc_method_handler(
                    servicer.importTDM,
                    request_deserializer=messages__pb2.ImportTDMInput.FromString,
                    response_serializer=messages__pb2.Measurement2DArray.SerializeToString,
            ),
            'interpolateEphemeris': grpc.unary_unary_rpc_method_handler(
                    servicer.interpolateEphemeris,
                    request_deserializer=messages__pb2.InterpolateEphemerisInput.FromString,
                    response_serializer=messages__pb2.MeasurementArray.SerializeToString,
            ),
            'getDensity': grpc.unary_unary_rpc_method_handler(
                    servicer.getDensity,
                    request_deserializer=messages__pb2.TransformFrameInput.FromString,
                    response_serializer=messages__pb2.DoubleArray.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Utilities', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Utilities(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def importTDM(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Utilities/importTDM',
            messages__pb2.ImportTDMInput.SerializeToString,
            messages__pb2.Measurement2DArray.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def interpolateEphemeris(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Utilities/interpolateEphemeris',
            messages__pb2.InterpolateEphemerisInput.SerializeToString,
            messages__pb2.MeasurementArray.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getDensity(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Utilities/getDensity',
            messages__pb2.TransformFrameInput.SerializeToString,
            messages__pb2.DoubleArray.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
