import logging

import grpc

import demo_pb2
import demo_pb2_grpc


def run():
    with grpc.insecure_channel('127.0.0.1:50051') as channel:
        client = demo_pb2_grpc.DemoServiceStub(channel)

        response = client.ApiCreate(demo_pb2.RequestData(
            data="call ApiCreate from client",
        ))
        print(response.return_code, response.message, response.data)

        # response = client.ApiList(demo_pb2.RequestData(
        #     data="call ApiList from client",
        # ))
        # print(response.return_code, response.message, response.data)
        #
        # response = client.ApiUpdate(demo_pb2.RequestData(
        #     data="call ApiUpdate from client",
        # ))
        # print(response.return_code, response.message, response.data)
        #
        # response = client.ApiDelete(demo_pb2.RequestData(
        #     data="call ApiDelete from client",
        # ))
        # print(response.return_code, response.message, response.data)


async def async_run(index):
    with grpc.insecure_channel('127.0.0.1:50051') as channel:
        client = demo_pb2_grpc.DemoServiceStub(channel)

        response = client.ApiCreate(demo_pb2.RequestData(
            data="call ApiCreate from client " + str(index),
        ))
        print(response.return_code, response.message, response.data)


if __name__ == '__main__':
    import time
    import asyncio

    logging.basicConfig()
    now = lambda: time.time()

    start = now()

    loop = asyncio.get_event_loop()
    tasks = []
    for i in range(0, 100):
        tasks.append(asyncio.ensure_future(async_run(i)))

    loop.run_until_complete(asyncio.wait(tasks))

    print('TIME: ', now() - start)
