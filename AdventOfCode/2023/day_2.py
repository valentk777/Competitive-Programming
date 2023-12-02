# ---------------------------------------------------------------------------------------
# URL    : https://adventofcode.com/2023/day/2
# Title  : Cube Conundrum
# Tags   : tag-adventofcode
# ---------------------------------------------------------------------------------------

# region --------------------------------------------Shared part--------------------------------------------------------

import math
import sys
from collections import defaultdict, Counter
from typing import List

from utils import read_lines

list_to_string = lambda _a: "".join(map(str, _a))
list_to_string_list = lambda _a: " ".join(map(str, _a))
_dp = lambda default_value: defaultdict(lambda: default_value)
fact = lambda number: math.factorial(number)
cnt = lambda _a: Counter(_a)


def lcm(a, b):
    return a * b // math.gcd(a, b)


def print_dp(_dict):
    for item in _dict.items():
        print(f"{item[0]} = {item[1]}")


MOD = 10 ** 9 + 7
INF = sys.maxsize
A = 911382323
M = 9999999999879998


# endregion

# -------------------------------------------------------Solution-------------------------------------------------------

class Set:
    def __init__(self, blue, red, green):
        self.blue = blue
        self.red = red
        self.green = green

    @staticmethod
    def create(data: str):
        colors = list(map(lambda x: x.strip(), data.split(",")))
        blue = 0
        red = 0
        green = 0

        for color in colors:
            if "blue" in color:
                blue = int(color.split(" ")[0])
            elif "red" in color:
                red = int(color.split(" ")[0])
            elif "green" in color:
                green = int(color.split(" ")[0])

        return Set(blue, red, green)

    def is_valid(self, max_blue, max_red, max_green):
        return self.blue <= max_blue and self.red <= max_red and self.green <= max_green


class Game:
    def __init__(self, game_id, sets):
        self.game_id = game_id
        self.sets: List[Set] = sets

    @staticmethod
    def create(data: str):
        game_id, sets = data.split(":")
        sets = sets.split(";")

        return Game(int(game_id.split(" ")[1].strip()), list(map(Set.create, sets)))

    def is_game_valid(self, max_blue, max_red, max_green):
        return all(map(lambda x: x.is_valid(max_blue, max_red, max_green), self.sets))

    def get_max_game_colors_values(self):
        blue = max(map(lambda x: x.blue, self.sets))
        red = max(map(lambda x: x.red, self.sets))
        green = max(map(lambda x: x.green, self.sets))

        return blue * red * green


def solve_1(data: List[str]) -> None:
    games = list(map(Game.create, data))
    result = sum(map(lambda game: game.game_id, filter(lambda game: game.is_game_valid(14, 12, 13), games)))

    print(result)


def solve_2(data: List[str]) -> None:
    games = list(map(Game.create, data))
    result = sum(map(lambda game: game.get_max_game_colors_values(), games))

    print(result)


if __name__ == "__main__":
    input_data = read_lines()

    solve_1(input_data.copy())
    solve_2(input_data.copy())
