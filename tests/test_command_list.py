# Copyright Iress 2024

from unittest import TestCase

from handlers.command_list_handler import ToyRobotCommandListHandler
from models.constants import FACEDIRECTION


class CommandListTest(TestCase):
    def test_import_from_command_list(self):
        file_path = "tests\\fixtures\\example_1.txt"
        with open(file_path, "r") as file:
            command_list = file.readlines()

            command_list_handler = ToyRobotCommandListHandler()
            result = command_list_handler.execute_command_list(command_list)

            assert result is not None
            assert result.get_x_location() == 0
            assert result.get_y_location() == 1
            assert result.get_face_location() == FACEDIRECTION.NORTH.value

    def test_import_from_command_list_2(self):
        file_path = "tests\\fixtures\\example_2.txt"
        with open(file_path, "r") as file:
            command_list = file.readlines()

            command_list_handler = ToyRobotCommandListHandler()
            result = command_list_handler.execute_command_list(command_list)

            assert result is not None
            assert result.get_x_location() == 0
            assert result.get_y_location() == 0
            assert result.get_face_location() == FACEDIRECTION.WEST.value

    def test_import_from_command_list_3(self):
        file_path = "tests\\fixtures\\example_3.txt"
        with open(file_path, "r") as file:
            command_list = file.readlines()

            command_list_handler = ToyRobotCommandListHandler()
            result = command_list_handler.execute_command_list(command_list)

            assert result is not None
            assert result.get_x_location() == 3
            assert result.get_y_location() == 3
            assert result.get_face_location() == FACEDIRECTION.NORTH.value
