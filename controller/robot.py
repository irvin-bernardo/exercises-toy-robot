# Copyright Iress 2024

from controller.coordinate import Coordinate
from controller.grid import Grid

from models.constants import FACEDIRECTION
from models.constants import FACEICONMAPPING
from models.constants import MOVESPEED


class Robot:
    """A class that simulates a robot's movement and operations within a grid."""

    _cur_x_location: int = None
    _cur_y_location: int = None
    _cur_face: FACEDIRECTION = None
    _grid = None

    def __init__(self, grid: Grid):
        """
        Initializes a new Robot instance.

        Args:
          grid (Grid): The grid on which the robot will operate.
        """
        self._grid = grid

    def get_present_location(self) -> Coordinate:
        """
        Retrieves the current location of the robot as a Coordinate object.

        Returns:
          Coordinate: The current location of the robot or None if not placed.
        """
        if self._cur_x_location is None or self._cur_y_location is None:
            return None
        else:
            return Coordinate(
                self._cur_x_location, self._cur_y_location, self._cur_face
            )

    def _check_and_save_location(self, coordinate: Coordinate) -> Coordinate:
        """
        Validates and updates the robot's location based on the provided coordinate.

        Args:
          coordinate (Coordinate): The new location to validate and set.

        Returns:
          Coordinate: The updated location of the robot.

        Raises:
          Exception: If the provided location is out of grid bounds.
        """
        x = coordinate.get_x_location()
        y = coordinate.get_y_location()

        if x < self._grid.get_max_x() and x >= self._grid.get_min_x():
            self._cur_x_location = x
        else:
            raise Exception("X Location is out of bounds")

        if y < self._grid.get_max_y() and y >= self._grid.get_min_y():
            self._cur_y_location = y
        else:
            raise Exception("Y Location is out of bounds")

        return self.get_present_location()

    def place(self, coordinate: Coordinate) -> Coordinate:
        """
        Places the robot at the specified coordinate and orientation.

        Args:
          coordinate (Coordinate): The initial placement and orientation of the robot.

        Returns:
          Coordinate: The placement location of the robot.

        Raises:
          Exception: If the specified location is invalid.
        """
        # Check Coordinates
        self._check_and_save_location(coordinate)

        # Check Face
        face = coordinate.get_face_location()
        if face:
            self._cur_face = FACEDIRECTION(face)
        else:
            raise Exception("Invalid Face Value")

        return self.get_present_location()

    def move(self) -> Coordinate:
        """
        Moves the robot one step in the direction it is currently facing.

        Returns:
          Coordinate: The new location after the move.

        Raises:
          Exception: If the robot is unplaced or if the move is invalid.
        """
        if self.get_present_location() is None:
            raise Exception("Unplaced robot")

        # Compute new destination based on current facing
        x_destination = self._cur_x_location
        y_destination = self._cur_y_location

        # Adjust destination based on facing direction
        if self._cur_face == FACEDIRECTION.NORTH:
            y_destination += MOVESPEED
        elif self._cur_face == FACEDIRECTION.SOUTH:
            y_destination -= MOVESPEED
        elif self._cur_face == FACEDIRECTION.EAST:
            x_destination += MOVESPEED
        elif self._cur_face == FACEDIRECTION.WEST:
            x_destination -= MOVESPEED
        else:
            raise Exception("Invalid Current Face State")

        # Validate and update location
        new_coordinate = Coordinate(x_destination, y_destination, self._cur_face)
        return self._check_and_save_location(new_coordinate)

    def rotate_right(self) -> Coordinate:
        """
        Rotates the robot 90 degrees to the right.

        Returns:
          Coordinate: The new facing direction of the robot.

        Raises:
          Exception: If the robot is unplaced or the rotation is invalid.
        """
        if self.get_present_location() is None:
            raise Exception("Unplaced robot")

        # For simplicity and readability, use direct mapping
        # instead of mathematically adding indexes and getting
        # the next face
        if self._cur_face == FACEDIRECTION.NORTH:
            self._cur_face = FACEDIRECTION.EAST
        elif self._cur_face == FACEDIRECTION.EAST:
            self._cur_face = FACEDIRECTION.SOUTH
        elif self._cur_face == FACEDIRECTION.SOUTH:
            self._cur_face = FACEDIRECTION.WEST
        elif self._cur_face == FACEDIRECTION.WEST:
            self._cur_face = FACEDIRECTION.NORTH
        else:
            raise Exception("Invalid Current Face State")

        return self.get_present_location()

    def rotate_left(self) -> Coordinate:
        """
        Rotates the robot 90 degrees to the left.

        Returns:
          Coordinate: The new facing direction of the robot.

        Raises:
          Exception: If the robot is unplaced or the rotation is invalid.
        """
        if self.get_present_location() is None:
            raise Exception("Unplaced robot")

        # For simplicity and readability, use direct mapping
        # instead of mathematically adding indexes and getting
        # the next face
        if self._cur_face == FACEDIRECTION.NORTH:
            self._cur_face = FACEDIRECTION.WEST
        elif self._cur_face == FACEDIRECTION.WEST:
            self._cur_face = FACEDIRECTION.SOUTH
        elif self._cur_face == FACEDIRECTION.SOUTH:
            self._cur_face = FACEDIRECTION.EAST
        elif self._cur_face == FACEDIRECTION.EAST:
            self._cur_face = FACEDIRECTION.NORTH
        else:
            raise Exception("Invalid Current Face State")
        return self.get_present_location()

    def print_robot_location(self):
        """
        Prints the current grid with the robot's location marked on it.

        Returns:
          None
        """
        grid = self._grid.get_grid()

        if self.get_present_location() is not None:
            # Mark the robot's position on the grid
            grid[self._cur_y_location][self._cur_x_location] = FACEICONMAPPING[
                self._cur_face.value
            ]

        # Print the grid
        for y in reversed(range(self._grid.get_min_y(), self._grid.get_max_y())):
            for x in range(self._grid.get_min_x(), self._grid.get_max_x()):
                print(f" {grid[y][x]} ", end=" ")
            print(" ")
        return None
