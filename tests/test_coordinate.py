# Copyright Iress 2024

from unittest import TestCase

from controller.coordinate import Coordinate
from models.constants import FACEDIRECTION


class CoordinateTest(TestCase):
    def test_create_coordinate(self):
        x = 1
        y = 2
        face = FACEDIRECTION.NORTH

        coordinate = Coordinate(x, y, face)

        assert coordinate.get_x_location() == x
        assert coordinate.get_y_location() == y
        assert coordinate.get_face_location() == face.value
        assert coordinate.get_string_coordinate() == "1,2,NORTH"

    def test_invalid_coordinate(self):
        with self.assertRaises(Exception) as exc:
            Coordinate(1, 2, "NOTH")

        self.assertTrue("Invalid Face Value" in str(exc.exception))
