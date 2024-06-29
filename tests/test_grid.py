# Copyright Iress 2024

from unittest import TestCase

from controller.grid import Grid


class GridTest(TestCase):
    def test_create_default_grid(self):
        grid = Grid()

        assert grid.get_max_x() == 5
        assert grid.get_max_y() == 5
        assert grid.get_min_x() == 0
        assert grid.get_min_y() == 0
        assert grid.get_grid() == [
            [".", ".", ".", ".", "."],
            [".", ".", ".", ".", "."],
            [".", ".", ".", ".", "."],
            [".", ".", ".", ".", "."],
            [".", ".", ".", ".", "."],
        ]

    def test_create_bigger_grid(self):
        grid = Grid(10)
        assert grid.get_max_x() == 10
        assert grid.get_max_y() == 10
        assert grid.get_min_x() == 0
        assert grid.get_min_y() == 0
        assert grid.get_grid() == [
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        ]
