# Copyright Iress 2024

from enum import Enum


class COMMANDS(Enum):
    PLACE = "PLACE"
    MOVE = "MOVE"
    RIGHT = "RIGHT"
    LEFT = "LEFT"
    REPORT = "REPORT"
    PRINT = "PRINT"


class FACEDIRECTION(Enum):
    NORTH = "NORTH"
    SOUTH = "SOUTH"
    EAST = "EAST"
    WEST = "WEST"


class FACEICON(Enum):
    NORTH = "▲"
    SOUTH = "▼"
    EAST = "▶"
    WEST = "◀"


FACEICONMAPPING = {
    FACEDIRECTION.NORTH.value: FACEICON.NORTH.value,
    FACEDIRECTION.SOUTH.value: FACEICON.SOUTH.value,
    FACEDIRECTION.WEST.value: FACEICON.WEST.value,
    FACEDIRECTION.EAST.value: FACEICON.EAST.value,
}


class EXECUTIONTYPE(Enum):
    CONSOLE = "CONSOLE"
    COMMANDLIST = "COMMANDLIST"


GRID_SIZE = 5
MOVESPEED = 1
