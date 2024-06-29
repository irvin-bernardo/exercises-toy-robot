# Copyright Iress 2024

from unittest import TestCase

from controller.grid import Grid
from controller.robot import Robot
from controller.coordinate import Coordinate

from models.constants import FACEDIRECTION


class RobotTest(TestCase):
    def test_robot_create(self):
        grid = Grid()
        robot = Robot(grid)

        assert robot is not None
        assert robot.get_present_location() is None

    def test_robot_place(self):
        grid = Grid()
        robot = Robot(grid)
        coordinate = Coordinate(1, 2, FACEDIRECTION.NORTH.value)

        assert robot is not None

        result = robot.place(coordinate)

        assert result is not None
        assert result.get_x_location() == 1
        assert result.get_y_location() == 2
        assert result.get_face_location() == FACEDIRECTION.NORTH.value
        assert result.get_string_coordinate() == "1,2,NORTH"

    def test_robot_place_bounds(self):
        grid = Grid()
        robot = Robot(grid)

        # Invalid x min bound
        with self.assertRaises(Exception) as exc:
            coordinate = Coordinate(-1, 2, FACEDIRECTION.NORTH.value)
            robot.place(coordinate)

        self.assertTrue("X Location is out of bounds" in str(exc.exception))

        # Invalid x max bound
        with self.assertRaises(Exception) as exc:
            coordinate = Coordinate(6, 2, FACEDIRECTION.NORTH.value)
            robot.place(coordinate)

        self.assertTrue("X Location is out of bounds" in str(exc.exception))

        # Invalid y min bound
        with self.assertRaises(Exception) as exc:
            coordinate = Coordinate(1, -2, FACEDIRECTION.NORTH.value)
            robot.place(coordinate)

        self.assertTrue("Y Location is out of bounds" in str(exc.exception))

        # Invalid y max bound
        with self.assertRaises(Exception) as exc:
            coordinate = Coordinate(1, 6, FACEDIRECTION.NORTH)
            robot.place(coordinate)

        self.assertTrue("Y Location is out of bounds" in str(exc.exception))

    def test_move_robot(self):
        grid = Grid()
        robot = Robot(grid)
        coordinate = Coordinate(1, 1, FACEDIRECTION.NORTH.value)
        robot.place(coordinate)

        result = robot.move()

        # North Movement
        assert result.get_x_location() == 1
        assert result.get_y_location() == 2

        coordinate = Coordinate(1, 1, FACEDIRECTION.EAST.value)
        robot.place(coordinate)

        result = robot.move()

        # East Movement
        assert result.get_x_location() == 2
        assert result.get_y_location() == 1

        coordinate = Coordinate(1, 1, FACEDIRECTION.SOUTH.value)
        robot.place(coordinate)

        result = robot.move()

        # Sout Movement
        assert result.get_x_location() == 1
        assert result.get_y_location() == 0

        coordinate = Coordinate(1, 1, FACEDIRECTION.WEST.value)
        robot.place(coordinate)

        result = robot.move()

        # West  Movement
        assert result.get_x_location() == 0
        assert result.get_y_location() == 1

    def test_unplaced_robot_move(self):
        grid = Grid()
        robot = Robot(grid)

        with self.assertRaises(Exception) as exc:
            robot.move()

        self.assertTrue("Unplaced robot" in str(exc.exception))

    def test_rotate_right(self):
        grid = Grid()
        robot = Robot(grid)
        coordinate = Coordinate(1, 1, FACEDIRECTION.NORTH.value)
        robot.place(coordinate)

        result = robot.rotate_right()
        assert result.get_face_location() == FACEDIRECTION.EAST.value

        result = robot.rotate_right()
        assert result.get_face_location() == FACEDIRECTION.SOUTH.value

        result = robot.rotate_right()
        assert result.get_face_location() == FACEDIRECTION.WEST.value

        result = robot.rotate_right()
        assert result.get_face_location() == FACEDIRECTION.NORTH.value

    def test_unplaced_rotate_right(self):
        grid = Grid()
        robot = Robot(grid)

        with self.assertRaises(Exception) as exc:
            robot.rotate_right()

        self.assertTrue("Unplaced robot" in str(exc.exception))

    def test_rotate_left(self):
        grid = Grid()
        robot = Robot(grid)
        coordinate = Coordinate(1, 1, FACEDIRECTION.NORTH.value)
        robot.place(coordinate)

        result = robot.rotate_left()
        assert result.get_face_location() == FACEDIRECTION.WEST.value

        result = robot.rotate_left()
        assert result.get_face_location() == FACEDIRECTION.SOUTH.value

        result = robot.rotate_left()
        assert result.get_face_location() == FACEDIRECTION.EAST.value

        result = robot.rotate_left()
        assert result.get_face_location() == FACEDIRECTION.NORTH.value

    def test_unplaced_rotate_left(self):
        grid = Grid()
        robot = Robot(grid)

        with self.assertRaises(Exception) as exc:
            robot.rotate_left()

        self.assertTrue("Unplaced robot" in str(exc.exception))

    def test_report(self):
        grid = Grid()
        robot = Robot(grid)
        coordinate = Coordinate(2, 2, FACEDIRECTION.NORTH.value)
        robot.place(coordinate)

        robot.move()
        robot.rotate_right()
        robot.move()
        robot.move()
        robot.rotate_right()
        robot.move()
        robot.rotate_right()

        result = robot.get_present_location()

        assert result is not None
        assert result.get_x_location() == 4
        assert result.get_y_location() == 2
        assert result.get_face_location() == FACEDIRECTION.WEST.value

    def test_invalid_report(self):
        grid = Grid()
        robot = Robot(grid)

        result = robot.get_present_location()

        assert result is None
