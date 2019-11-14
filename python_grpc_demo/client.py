import logging

import grpc

import demo_pb2
import demo_pb2_grpc


def run():
    with grpc.insecure_channel('127.0.0.1:9000') as channel:
        client = demo_pb2_grpc.DemoServiceStub(channel)

        response = client.ApiCreate(demo_pb2.RequestData(
            data="call ApiCreate from client",
        ))
        print(response.return_code, response.message, response.data)

        response = client.ApiList(demo_pb2.RequestData(
            data="call ApiList from client",
        ))
        print(response.return_code, response.message, response.data)

        response = client.ApiUpdate(demo_pb2.RequestData(
            data="call ApiUpdate from client",
        ))
        print(response.return_code, response.message, response.data)

        response = client.ApiDelete(demo_pb2.RequestData(
            data="call ApiDelete from client",
        ))
        print(response.return_code, response.message, response.data)


if __name__ == '__main__':
    logging.basicConfig()
    run()
