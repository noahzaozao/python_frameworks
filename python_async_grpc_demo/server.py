import asyncio
import logging

from grpclib.server import Server
from grpclib.utils import graceful_exit

import demo_pb2
from demo_grpc import DemoServiceBase

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class DemoService(DemoServiceBase):

    async def ApiCreate(self, stream):

        request = await stream.recv_message()

        print("C_2_S ApiCreate: >>>>> ", request)

        response = demo_pb2.ResponseData(
            return_code=0,
            message="success",
            data=""
        )

        print("S_2_C ApiCreate: <<<<< ", response)

        await stream.send_message(response)

    async def ApiList(self, stream):

        request = await stream.recv_message()

        print("C_2_S ApiList: >>>>> ", request)

        response = demo_pb2.ResponseData(
            return_code=0,
            message="success",
            data=""
        )

        print("S_2_C ApiList: <<<<< ", response)

        await stream.send_message(response)

    async def ApiUpdate(self, stream):

        request = await stream.recv_message()

        print("C_2_S ApiUpdate: >>>>> ", request)

        response = demo_pb2.ResponseData(
            return_code=0,
            message="success",
            data=""
        )

        print("S_2_C ApiUpdate: <<<<< ", response)

        await stream.send_message(response)

    async def ApiDelete(self, stream):

        request = await stream.recv_message()

        print("C_2_S ApiDelete: >>>>> ", request)

        response = demo_pb2.ResponseData(
            return_code=0,
            message="success",
            data=""
        )

        print("S_2_C ApiDelete: <<<<< ", response)

        await stream.send_message(response)


async def main(host='127.0.0.1', port=50051):
    server = Server([DemoService()])
    with graceful_exit([server]):
        await server.start(host, port)
        print(f'Serving on {host}:{port}')
        await server.wait_closed()


if __name__ == '__main__':
    logging.basicConfig()
    asyncio.run(main())
