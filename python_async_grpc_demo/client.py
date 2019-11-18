import asyncio
import logging
import time

from grpclib.client import Channel

import demo_pb2
from demo_grpc import DemoServiceStub


async def main(index):
    channel = Channel('127.0.0.1', 50051)
    client = DemoServiceStub(channel)

    response: demo_pb2.ResponseData = await client.ApiCreate(demo_pb2.RequestData(
        data="call ApiCreate from client " + str(index),
    ))
    print(response.return_code, response.message, response.data)

    # response: demo_pb2.ResponseData = await client.ApiList(demo_pb2.RequestData(
    #     data="call ApiList from client",
    # ))
    # print(response.return_code, response.message, response.data)
    #
    # response: demo_pb2.ResponseData = await client.ApiUpdate(demo_pb2.RequestData(
    #     data="call ApiUpdate from client",
    # ))
    # print(response.return_code, response.message, response.data)
    #
    # response: demo_pb2.ResponseData = await client.ApiDelete(demo_pb2.RequestData(
    #     data="call ApiDelete from client",
    # ))
    # print(response.return_code, response.message, response.data)

    channel.close()


if __name__ == '__main__':
    logging.basicConfig()

    now = lambda: time.time()

    start = now()

    loop = asyncio.get_event_loop()
    tasks = []
    for i in range(0, 100):
        tasks.append(asyncio.ensure_future(main(i)))

    loop.run_until_complete(asyncio.wait(tasks))

    print('TIME: ', now() - start)
