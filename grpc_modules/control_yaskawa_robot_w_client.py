#!/usr/bin/env python3
# coding: utf-8

# Copyright (c) 2019-2020 Latona. All rights reserved.

import grpc

from google.protobuf.struct_pb2 import Struct
from google.protobuf.json_format import MessageToDict

from . import control_yaskawa_robot_w_pb2
from . import control_yaskawa_robot_w_pb2_grpc

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 50053


class ControlYaskawaRobotWClient():
    def __init__(self):
        self.channel = None
        self.stub = None

    def __enter__(self):
        self.channel = grpc.insecure_channel(f'{SERVER_HOST}:{SERVER_PORT}')
        self.stub = control_yaskawa_robot_w_pb2_grpc.ControlYaskawaRobotWStub(self.channel)
        return self

    def __exit__(self, exc_type, exe_value, traceback):
        if self.channel is not None:
            self.channel.close()
        self.channel = None
        self.stub = None

        if exc_type is not None:
            raise RuntimeError(exe_value)
        return

    def Write(self, write_command):
        if self.stub is None:
            raise RuntimeError('Not open channel.')

        s = Struct()
        s.update(write_command)
        request_data = control_yaskawa_robot_w_pb2.WriteRequest(
            write_command = s
        )
        detection = self.stub.Write(request_data)
        return detection


def test_client():
    print('start')
    write_command = {
        "command": "7f",
        "arrayNo": 0,
        "elementNo": "00",
        "processNo": "02",
        "property": {
            "AXES_01": 122,
            "AXES_02": 122,
            "AXES_03": 12,
            "AXES_04": 12,
            "AXES_05": 12,
            "AXES_06": 12,
            "AXES_07": 0,
            "AXES_08": 0
        },
        "expire_time": 1000
    }
    with ControlYaskawaRobotWClient() as client:
        print('send')
        result = client.Write(write_command)
        print(result)
    return


if __name__ == "__main__":
    test_client()

