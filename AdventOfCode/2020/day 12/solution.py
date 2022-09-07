# -----------------------------------------------------------
# Notes  : tag-adventOfCode
# -----------------------------------------------------------


from dataclasses import dataclass, field
from enum import Enum
from typing import List

from utils import read_lines


@dataclass
class Command:
    direction: str
    units: int


@dataclass
class MapLocation:
    north: int = field(default=0)
    south: int = field(default=0)
    east: int = field(default=0)
    west: int = field(default=0)


class Map(Enum):
    N = 0
    E = 1
    S = 2
    W = 3


input_data = read_lines()


def to_command(data: str):
    return Command(data[0], int(data[1:]))


def make_move(data: Command, location: MapLocation):
    if data.direction == "N":
        location.north += data.units
    elif data.direction == "S":
        location.south += data.units
    elif data.direction == "E":
        location.east += data.units
    elif data.direction == "W":
        location.west += data.units
    return location


def make_rotation(data: Command, current_position: int):
    if data.direction == "R":
        current_position += data.units // 90
    else:
        current_position -= data.units // 90
    return current_position % 4


def make_waypoint_move(data: Command, current_waypoint_location: MapLocation, current_location: MapLocation):
    current_location.north += current_waypoint_location.north * data.units
    current_location.south += current_waypoint_location.south * data.units
    current_location.east += current_waypoint_location.east * data.units
    current_location.west += current_waypoint_location.west * data.units
    return current_location


def make_waypoint_rotation(data: Command, current_position: MapLocation):
    def rotate_r():
        current_position.east, current_position.south, current_position.west, current_position.north = \
            current_position.north, current_position.east, current_position.south, current_position.west

    def rotate_l():
        current_position.west, current_position.north, current_position.east, current_position.south = \
            current_position.north, current_position.east, current_position.south, current_position.west

    if data.direction == "R":
        for i in range(data.units // 90):
            rotate_r()
    else:
        for i in range(data.units // 90):
            rotate_l()
    return current_position


def solve_1(data: List[Command]):
    current_position = 1
    current_location = MapLocation()

    for d in data:
        if d.direction in ["N", "S", "E", "W"]:
            current_location = make_move(d, current_location)
        elif d.direction in ["L", "R"]:
            current_position = make_rotation(d, current_position)
        else:
            current_location = make_move(Command(Map(current_position).name, d.units), current_location)

    print(abs(current_location.north - current_location.south) + abs(current_location.west - current_location.east))


def solve_2(data: List[Command]):
    current_location = MapLocation()
    current_waypoint_location = MapLocation(east=10, north=1)

    for d in data:
        if d.direction in ["N", "S", "E", "W"]:
            current_waypoint_location = make_move(d, current_waypoint_location)
        elif d.direction in ["L", "R"]:
            current_waypoint_location = make_waypoint_rotation(d, current_waypoint_location)
        else:
            current_location = make_waypoint_move(d, current_waypoint_location, current_location)

    print(abs(current_location.north - current_location.south) + abs(current_location.west - current_location.east))


input_data = list(map(to_command, input_data))
solve_1(input_data)
solve_2(input_data)
