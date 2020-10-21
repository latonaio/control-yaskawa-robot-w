#!/usr/bin/env python3
# coding: utf-8

# Copyright (c) 2019-2020 Latona. All rights reserved.

from concurrent import futures

import datetime
import grpc

from google.protobuf.struct_pb2 import Struct
from google.protobuf.json_format import MessageToDict

import control_yaskawa_robot_w_pb2
import control_yaskawa_robot_w_pb2_grpc

SERVER_PORT = 50053


class ControlYaskawaRobotWServicer(control_yaskawa_robot_w_pb2_grpc.ControlYaskawaRobotWServicer):
    def __init__(self, y):
        super().__init__()
        self.y = y

    def Write(self, request, context):
        write_command = MessageToDict(request.write_command)

        robot_data, timestamp = await self.y.write_command(write_command)

        #robot_data = MessageToDict(request.write_command)
        #timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        
        s = Struct()
        s.update(robot_data)
        return control_yaskawa_robot_w_pb2.WriteResponse(
            robot_data=s, timestamp=timestamp)


def start_server(y):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    control_yaskawa_robot_w_pb2_grpc.add_ControlYaskawaRobotWServicer_to_server(
        ControlYaskawaRobotWServicer(y), server
    )
    server.add_insecure_port(f'[::]:{SERVER_PORT}')
    server.start()
    y.start_to_send()
    server.wait_for_termination()
    return


if __name__ == "__main__":
    start_server()

