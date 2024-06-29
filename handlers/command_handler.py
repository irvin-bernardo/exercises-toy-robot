# Copyright Iress 2024

from controller.grid import Grid
from controller.robot import Robot
from controller.coordinate import Coordinate

from models.constants import COMMANDS


class ToyRobotCommandHandler:
    """
    A command handler class for operating a toy robot on a grid based on commands.

    Attributes:
        grid (Grid): The grid on which the robot operates.
        robot (Robot): The robot that executes commands on the grid.
    """

    _grid = None
    _robot = None

    def __init__(self) -> None:
        """
        Initializes a new instance of ToyRobotCommandHandler,
        setting up a grid and a robot.
        """
        self.grid = Grid()
        self.robot = Robot(self.grid)

    def execute_command(self, command, coordinate: Coordinate = None) -> Coordinate:
        """
        Executes a command for the robot to perform an action on the grid.

        Args:
          command (str): A command to execute, derived from COMMANDS enum values.
          coordinate (Coordinate, optional): The coordinate used for the PLACE command.
                                             Default is None.

        Returns:
          Coordinate: The robot's coordinate after executing the command,
          or None for PRINT command.

        Raises:
          Exception: If an unrecognized command is passed or
            if required parameters are missing.

        Notes:
          If the command is PRINT, it prints the robot's locationand returns None.
          For all other commands, it performs the respective robot actions
        """
        if command == COMMANDS.PLACE.value:
            result = self.robot.place(coordinate)
        elif command == COMMANDS.MOVE.value:
            result = self.robot.move()
        elif command == COMMANDS.RIGHT.value:
            result = self.robot.rotate_right()
        elif command == COMMANDS.LEFT.value:
            result = self.robot.rotate_left()
        elif command == COMMANDS.REPORT.value:
            result = self.robot.get_present_location()
        elif command == COMMANDS.PRINT.value:
            self.robot.print_robot_location()
            return None  # Explicitly return None after printing the grid
        else:
            raise Exception("Unrecognized Command")

        if result:
            print(result.get_string_coordinate())

        return result
