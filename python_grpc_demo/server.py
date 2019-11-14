import logging
import time
from concurrent import futures

import grpc

import demo_pb2
import demo_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class DemoService(demo_pb2_grpc.DemoServiceServicer):

    def __init__(self):
        pass

    def ApiCreate(self, request, context):

        print("C_2_S ApiCreate: >>>>> ", request)

        response = demo_pb2.ResponseData(
            return_code=0,
            message="success",
            data=""
        )

        print("S_2_C ApiCreate: <<<<< ", response)

        return response

    def ApiList(self, request, context):

        print("C_2_S ApiList: >>>>> ", request)

        response = demo_pb2.ResponseData(
            return_code=0,
            message="success",
            data=""
        )

        print("S_2_C ApiList: <<<<< ", response)

        return response

    def ApiUpdate(self, request, context):

        print("C_2_S ApiUpdate: >>>>> ", request)

        response = demo_pb2.ResponseData(
            return_code=0,
            message="success",
            data=""
        )

        print("S_2_C ApiUpdate: <<<<< ", response)

        return response

    def ApiDelete(self, request, context):

        print("C_2_S ApiDelete: >>>>> ", request)

        response = demo_pb2.ResponseData(
            return_code=0,
            message="success",
            data=""
        )

        print("S_2_C ApiDelete: <<<<< ", response)

        return response


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    demo_pb2_grpc.add_DemoServiceServicer_to_server(DemoService(), server)
    server.add_insecure_port('[::]:9000')
    server.start()

    print("listen: 9000")

    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    logging.basicConfig()
    serve()
