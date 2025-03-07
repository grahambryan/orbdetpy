# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
import orbdetpy.rpc.messages_pb2 as messages__pb2


class ConversionStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.transformFrame = channel.unary_unary(
                '/Conversion/transformFrame',
                request_serializer=messages__pb2.TransformFrameInput.SerializeToString,
                response_deserializer=messages__pb2.Double2DArray.FromString,
                )
        self.convertAzElToRaDec = channel.unary_unary(
                '/Conversion/convertAzElToRaDec',
                request_serializer=messages__pb2.AnglesInput.SerializeToString,
                response_deserializer=messages__pb2.DoubleArray.FromString,
                )
        self.convertRaDecToAzEl = channel.unary_unary(
                '/Conversion/convertRaDecToAzEl',
                request_serializer=messages__pb2.AnglesInput.SerializeToString,
                response_deserializer=messages__pb2.DoubleArray.FromString,
                )
        self.convertLLAToPos = channel.unary_unary(
                '/Conversion/convertLLAToPos',
                request_serializer=messages__pb2.TransformFrameInput.SerializeToString,
                response_deserializer=messages__pb2.Double2DArray.FromString,
                )
        self.convertPosToLLA = channel.unary_unary(
                '/Conversion/convertPosToLLA',
                request_serializer=messages__pb2.TransformFrameInput.SerializeToString,
                response_deserializer=messages__pb2.Double2DArray.FromString,
                )
        self.convertElemToPv = channel.unary_unary(
                '/Conversion/convertElemToPv',
                request_serializer=messages__pb2.TransformFrameInput.SerializeToString,
                response_deserializer=messages__pb2.Double2DArray.FromString,
                )
        self.convertPvToElem = channel.unary_unary(
                '/Conversion/convertPvToElem',
                request_serializer=messages__pb2.TransformFrameInput.SerializeToString,
                response_deserializer=messages__pb2.Double2DArray.FromString,
                )
        self.getUTCString = channel.unary_unary(
                '/Conversion/getUTCString',
                request_serializer=messages__pb2.DoubleArray.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_wrappers__pb2.StringValue.FromString,
                )
        self.getJ2000EpochOffset = channel.unary_unary(
                '/Conversion/getJ2000EpochOffset',
                request_serializer=google_dot_protobuf_dot_wrappers__pb2.StringValue.SerializeToString,
                response_deserializer=messages__pb2.DoubleArray.FromString,
                )
        self.getEpochDifference = channel.unary_unary(
                '/Conversion/getEpochDifference',
                request_serializer=messages__pb2.IntegerArray.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_wrappers__pb2.DoubleValue.FromString,
                )


class ConversionServicer(object):
    """Missing associated documentation comment in .proto file."""

    def transformFrame(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def convertAzElToRaDec(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def convertRaDecToAzEl(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def convertLLAToPos(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def convertPosToLLA(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def convertElemToPv(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def convertPvToElem(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getUTCString(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getJ2000EpochOffset(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getEpochDifference(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ConversionServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'transformFrame': grpc.unary_unary_rpc_method_handler(
                    servicer.transformFrame,
                    request_deserializer=messages__pb2.TransformFrameInput.FromString,
                    response_serializer=messages__pb2.Double2DArray.SerializeToString,
            ),
            'convertAzElToRaDec': grpc.unary_unary_rpc_method_handler(
                    servicer.convertAzElToRaDec,
                    request_deserializer=messages__pb2.AnglesInput.FromString,
                    response_serializer=messages__pb2.DoubleArray.SerializeToString,
            ),
            'convertRaDecToAzEl': grpc.unary_unary_rpc_method_handler(
                    servicer.convertRaDecToAzEl,
                    request_deserializer=messages__pb2.AnglesInput.FromString,
                    response_serializer=messages__pb2.DoubleArray.SerializeToString,
            ),
            'convertLLAToPos': grpc.unary_unary_rpc_method_handler(
                    servicer.convertLLAToPos,
                    request_deserializer=messages__pb2.TransformFrameInput.FromString,
                    response_serializer=messages__pb2.Double2DArray.SerializeToString,
            ),
            'convertPosToLLA': grpc.unary_unary_rpc_method_handler(
                    servicer.convertPosToLLA,
                    request_deserializer=messages__pb2.TransformFrameInput.FromString,
                    response_serializer=messages__pb2.Double2DArray.SerializeToString,
            ),
            'convertElemToPv': grpc.unary_unary_rpc_method_handler(
                    servicer.convertElemToPv,
                    request_deserializer=messages__pb2.TransformFrameInput.FromString,
                    response_serializer=messages__pb2.Double2DArray.SerializeToString,
            ),
            'convertPvToElem': grpc.unary_unary_rpc_method_handler(
                    servicer.convertPvToElem,
                    request_deserializer=messages__pb2.TransformFrameInput.FromString,
                    response_serializer=messages__pb2.Double2DArray.SerializeToString,
            ),
            'getUTCString': grpc.unary_unary_rpc_method_handler(
                    servicer.getUTCString,
                    request_deserializer=messages__pb2.DoubleArray.FromString,
                    response_serializer=google_dot_protobuf_dot_wrappers__pb2.StringValue.SerializeToString,
            ),
            'getJ2000EpochOffset': grpc.unary_unary_rpc_method_handler(
                    servicer.getJ2000EpochOffset,
                    request_deserializer=google_dot_protobuf_dot_wrappers__pb2.StringValue.FromString,
                    response_serializer=messages__pb2.DoubleArray.SerializeToString,
            ),
            'getEpochDifference': grpc.unary_unary_rpc_method_handler(
                    servicer.getEpochDifference,
                    request_deserializer=messages__pb2.IntegerArray.FromString,
                    response_serializer=google_dot_protobuf_dot_wrappers__pb2.DoubleValue.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Conversion', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Conversion(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def transformFrame(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Conversion/transformFrame',
            messages__pb2.TransformFrameInput.SerializeToString,
            messages__pb2.Double2DArray.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def convertAzElToRaDec(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Conversion/convertAzElToRaDec',
            messages__pb2.AnglesInput.SerializeToString,
            messages__pb2.DoubleArray.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def convertRaDecToAzEl(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Conversion/convertRaDecToAzEl',
            messages__pb2.AnglesInput.SerializeToString,
            messages__pb2.DoubleArray.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def convertLLAToPos(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Conversion/convertLLAToPos',
            messages__pb2.TransformFrameInput.SerializeToString,
            messages__pb2.Double2DArray.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def convertPosToLLA(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Conversion/convertPosToLLA',
            messages__pb2.TransformFrameInput.SerializeToString,
            messages__pb2.Double2DArray.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def convertElemToPv(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Conversion/convertElemToPv',
            messages__pb2.TransformFrameInput.SerializeToString,
            messages__pb2.Double2DArray.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def convertPvToElem(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Conversion/convertPvToElem',
            messages__pb2.TransformFrameInput.SerializeToString,
            messages__pb2.Double2DArray.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getUTCString(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Conversion/getUTCString',
            messages__pb2.DoubleArray.SerializeToString,
            google_dot_protobuf_dot_wrappers__pb2.StringValue.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getJ2000EpochOffset(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Conversion/getJ2000EpochOffset',
            google_dot_protobuf_dot_wrappers__pb2.StringValue.SerializeToString,
            messages__pb2.DoubleArray.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getEpochDifference(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Conversion/getEpochDifference',
            messages__pb2.IntegerArray.SerializeToString,
            google_dot_protobuf_dot_wrappers__pb2.DoubleValue.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
