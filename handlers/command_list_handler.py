# Copyright Iress 2024

from controller.coordinate import Coordinate
from handlers.command_handler import ToyRobotCommandHandler

from models.constants import COMMANDS


class ToyRobotCommandListHandler:
    """
    A class to handle lists of commands for operating a toy robot.
    It processes multiple commands and directs them to the appropriate command handler.

    Attributes:
        _command_handler (ToyRobotCommandHandler): Handler that executes
                                                    individual commands.
    """

    _command_handler = None

    def __init__(self) -> None:
        """
        Initializes a new instance of ToyRobotCommandListHandler with a command handler.
        """
        self._command_handler = ToyRobotCommandHandler()

    def execute_command_list(self, command_list):
        """
        Executes a list of commands in sequence on a toy robot.

        Args:
          command_list (list of str): A list of command strings to be executed.

        Returns:
          Coordinate: The robot's coordinate after executing all commands in the list.

        Process:
          This method processes each command in the list, formats it,
          and determines if the commandinvolves placing the robot with
          specific coordinates. It then executes the command through
          the ToyRobotCommandHandler. The final robot location is
          reported after all commands have
          been processed.
        """
        for command in command_list:
            command = command.strip().upper()

            if COMMANDS.PLACE.name in command:
                # Extract command and coordinates for the PLACE command
                parts = command.split(" ")
                coordinates = parts[1].split(",")
                command = parts[0]
                coordinate = Coordinate(
                    int(coordinates[0]), int(coordinates[1]), coordinates[2]
                )

                self._command_handler.execute_command(command, coordinate)
            else:
                self._command_handler.execute_command(command)

        # Report the robot's final location after executing all commands
        return self._command_handler.execute_command("REPORT")
