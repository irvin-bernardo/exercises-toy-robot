# Copyright Iress 2024

import sys

from controller.coordinate import Coordinate

from handlers.command_list_handler import ToyRobotCommandListHandler
from handlers.command_handler import ToyRobotCommandHandler
from models.constants import EXECUTIONTYPE
from models.constants import COMMANDS

if len(sys.argv) <= 1:
    print("Unrecognized execution mode")
    exit()

arg_command = sys.argv[1]

if arg_command == EXECUTIONTYPE.COMMANDLIST.value:
    if len(sys.argv) <= 2:
        print("Missing command list location")
    try:
        file_path = sys.argv[2]
        with open(file_path, "r") as file:
            command_list = file.readlines()

            command_list_handler = ToyRobotCommandListHandler()
            command_list_handler.execute_command_list(command_list)
    except Exception as exc:
        print(f"Exception encountered while executing command list: {exc}")
elif arg_command == EXECUTIONTYPE.CONSOLE.value:
    command_handler = ToyRobotCommandHandler()
    while 1:
        try:
            command = input("COMMAND: ")
            command = command.upper()
            if COMMANDS.PLACE.name in command:
                coordinates = command.split(" ")[1].split(",")
                command = command.split(" ")[0]
                coordinate = Coordinate(coordinates[0], coordinates[1], coordinates[2])

                result = command_handler.execute_command(command, coordinate)
            else:
                result = command_handler.execute_command(command)
        except Exception as exc:
            print(f"Exception encountered while executing command: {exc}")
