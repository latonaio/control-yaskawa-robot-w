#!/usr/bin/env python3
# coding: utf-8

# Copyright (c) 2019-2020 Latona. All rights reserved.

import os
import time

from google.protobuf.json_format import MessageToDict

from StatusJsonPythonModule import StatusJsonRest

from grpc_modules.control_yaskawa_robot_w_client import ControlYaskawaRobotWClient

def main():
    result_list = []
    statusObj = StatusJsonRest.StatusJsonRest(os.getcwd(), __file__)
    statusObj.initializeInputStatusJson()

    statusObj.initializeOutputStatusJson()
    statusObj.setNextService(
        "ServiceBroker",
        "/home/toyota/gaia/Data/service-broker",
        "go", "go run", "gaia")
    statusObj.setMetadataValue("end_service", "ControlYaskawaRobotR")
    statusObj.setResultStatus(True)
    statusObj.outputJsonFile()
    statusObj.resetOutputJsonFile()

    time.sleep(0.5)

    write_command_list = statusObj.getMetadataFromJson("write_command")

    for write_command in write_command_list:
        response = None

        with ControlYaskawaRobotWClient() as client:
            response = client.Write(write_command)

        if response:
            robot_data = MessageToDict(response.robot_data)
            timestamp = response.timestamp
            result_list.append({
                "RobotData": robot_data,
                "timestamp": timestamp
            })

    statusObj.initializeOutputStatusJson()
    statusObj.setNextService(
        "ServiceBroker",
        "/home/toyota/gaia/Data/service-broker",
        "go", "go run", "gaia")
    statusObj.setMetadataValue("start_service", "ControlYaskawaRobotR")
    #statusObj.setMetadataValue("result_list", result_list)
    statusObj.setResultStatus(True)
    statusObj.outputJsonFile()
    return

if __name__ == "__main__":
    main()

