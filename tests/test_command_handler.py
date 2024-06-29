# Copyright Iress 2024

from unittest import TestCase

from controller.coordinate import Coordinate
from handlers.command_handler import ToyRobotCommandHandler


class CommandListTest(TestCase):
    def test_execute_command(self):
        command_handler = ToyRobotCommandHandler()
        coordinate = Coordinate(1, 1, "NORTH")
        result = command_handler.execute_command("PLACE", coordinate)

        assert result is not None
        assert result.get_x_location() == 1
        assert result.get_y_location() == 1
        assert result.get_face_location() == "NORTH"

    def test_invalid_command(self):
        command_handler = ToyRobotCommandHandler()
        with self.assertRaises(Exception) as exc:
            command_handler.execute_command("NOT_A_REAL_COMMAND")

        self.assertTrue("Unrecognized Command" in str(exc.exception))
