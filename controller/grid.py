# Copyright Iress 2024
from models.constants import GRID_SIZE


class Grid:
    """A class to represent a grid layout.

    Attributes:
        _min_x (int): The minimum x-coordinate of the grid, set to 0.
        _min_y (int): The minimum y-coordinate of the grid, set to 0.
        _max_x (int): The maximum x-coordinate of the grid, derived from grid size.
        _max_y (int): The maximum y-coordinate of the grid, derived from grid size.
        _grid (list): A 2D list representation of the grid (optional).
    """

    _min_y = None
    _min_x = None
    _max_y = None
    _max_x = None
    _grid = None

    def __init__(self, size=GRID_SIZE):
        """
        Initializes a new Grid instance with a specified size.

        Args:
          size (int): The size for both the width and height of the grid.
            Defaults to GRID_SIZE.
        """
        self._min_x = 0
        self._min_y = 0
        self._max_x = size
        self._max_y = size

    def get_min_x(self):
        """
        Returns the minimum x-coordinate of the grid.

        Returns:
          int: The minimum x-coordinate.
        """
        return self._min_x

    def get_min_y(self):
        """
        Returns the minimum y-coordinate of the grid.

        Returns:
          int: The minimum y-coordinate.
        """
        return self._min_y

    def get_max_x(self):
        """
        Returns the maximum x-coordinate of the grid.

        Returns:
          int: The maximum x-coordinate.
        """
        return self._max_x

    def get_max_y(self):
        """
        Returns the maximum y-coordinate of the grid.

        Returns:
          int: The maximum y-coordinate.
        """
        return self._max_y

    def get_grid(self):
        """
        Generates and returns a 2D list representing the grid layout.
        Each cell in the grid is initialized to '.' indicating an empty space.

        Returns:
          list: A 2D list of strings representing the grid.
        """
        grid = [["." for x in range(self._max_x)] for y in range(self._max_y)]
        return grid
