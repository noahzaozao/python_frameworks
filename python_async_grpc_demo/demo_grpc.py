import abc
import typing

import grpclib.client
import grpclib.const
import grpclib.server

import demo_pb2

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class DemoServiceBase(abc.ABC):

    @abc.abstractmethod
    async def ApiCreate(self, stream: 'grpclib.server.Stream[demo_pb2.RequestData, demo_pb2.ResponseData]') -> None:
        pass

    @abc.abstractmethod
    async def ApiList(self, stream: 'grpclib.server.Stream[demo_pb2.RequestData, demo_pb2.ResponseData]') -> None:
        pass

    @abc.abstractmethod
    async def ApiUpdate(self, stream: 'grpclib.server.Stream[demo_pb2.RequestData, demo_pb2.ResponseData]') -> None:
        pass

    @abc.abstractmethod
    async def ApiDelete(self, stream: 'grpclib.server.Stream[demo_pb2.RequestData, demo_pb2.ResponseData]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/demo.DemoService/ApiCreate': grpclib.const.Handler(
                self.ApiCreate,
                grpclib.const.Cardinality.UNARY_UNARY,
                demo_pb2.RequestData,
                demo_pb2.ResponseData,
            ),
            '/demo.DemoService/ApiList': grpclib.const.Handler(
                self.ApiList,
                grpclib.const.Cardinality.UNARY_UNARY,
                demo_pb2.RequestData,
                demo_pb2.ResponseData,
            ),
            '/demo.DemoService/ApiUpdate': grpclib.const.Handler(
                self.ApiUpdate,
                grpclib.const.Cardinality.UNARY_UNARY,
                demo_pb2.RequestData,
                demo_pb2.ResponseData,
            ),
            '/demo.DemoService/ApiDelete': grpclib.const.Handler(
                self.ApiDelete,
                grpclib.const.Cardinality.UNARY_UNARY,
                demo_pb2.RequestData,
                demo_pb2.ResponseData,
            ),
        }


class DemoServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.ApiCreate = grpclib.client.UnaryUnaryMethod(
            channel,
            '/demo.DemoService/ApiCreate',
            demo_pb2.RequestData,
            demo_pb2.ResponseData,
        )
        self.ApiList = grpclib.client.UnaryUnaryMethod(
            channel,
            '/demo.DemoService/ApiList',
            demo_pb2.RequestData,
            demo_pb2.ResponseData,
        )
        self.ApiUpdate = grpclib.client.UnaryUnaryMethod(
            channel,
            '/demo.DemoService/ApiUpdate',
            demo_pb2.RequestData,
            demo_pb2.ResponseData,
        )
        self.ApiDelete = grpclib.client.UnaryUnaryMethod(
            channel,
            '/demo.DemoService/ApiDelete',
            demo_pb2.RequestData,
            demo_pb2.ResponseData,
        )
