# Copyright Iress 2024

from models.constants import FACEDIRECTION


class Coordinate:
    """A class to represent a coordinate with a facing direction."""

    _x_location: int = None
    _y_location: int = None
    _face: str = None

    def __init__(self, x, y, face) -> None:
        """
        Initializes a new Coordinate instance.

        Args:
          x (int): The x-coordinate.
          y (int): The y-coordinate.
          face (Union[FACEDIRECTION, str, None]): The facing direction, which can be
            an instance of FACEDIRECTION enum, a string name of the enum, or None.

        Raises:
          Exception: If a string is provided for face and
          it is not a valid FACEDIRECTION name.
        """
        self._x_location = int(x)
        self._y_location = int(y)

        # Accept both enum, string, or None as face direction
        if face:
            if isinstance(face, str):
                if face not in [f.name for f in FACEDIRECTION]:
                    raise Exception("Invalid Face Value")
                face = FACEDIRECTION[face].name
            elif isinstance(face, FACEDIRECTION):
                face = face.name

        self._face = face

    def get_x_location(self):
        """
        Returns the x-coordinate of the Coordinate instance.

        Returns:
          int: The x-coordinate.
        """
        return self._x_location

    def get_y_location(self):
        """
        Returns the y-coordinate of the Coordinate instance.

        Returns:
          int: The y-coordinate.
        """
        return self._y_location

    def get_face_location(self):
        """
        Returns the facing direction of the Coordinate instance.

        Returns:
          str: The facing direction, or None if no facing direction is set.
        """
        return self._face

    def get_string_coordinate(self):
        """
        Returns a string representation of the Coordinate.

        Returns:
          str: The string representation in the format 'x,y,face'.
        """
        return f"{self._x_location},{self._y_location},{self._face}"
