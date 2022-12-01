# ---------------------------------------------------------------------------------------
# URL    : https://adventofcode.com/2020/day/11
# Title  : Seating System
# Tags   : tag-adventofcode
# ---------------------------------------------------------------------------------------

# region --------------------------------------------Shared part--------------------------------------------------------

import math
import sys
from collections import defaultdict, Counter
from typing import List

from utils import read_lines

inp = lambda: sys.stdin.readline().strip().rstrip("\r\n")
iinp = lambda: int(inp())
intl = lambda: list(map(int, inp().split()))
strl = lambda: list(inp().split())
list_to_string = lambda _a: "".join(map(str, _a))
list_to_string_list = lambda _a: " ".join(map(str, _a))
_dp = lambda default_value: defaultdict(lambda: default_value)
flush = lambda: sys.stdout.flush()
print_flush = lambda _text: (print(_text), flush())
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


def get_status_rules_1(data: List[str], x: int, y: int) -> str:
    if data[y][x] == "L":
        if all(map(lambda d: d != "#", __get_all_places_around(data, x, y))):
            return "#"

    elif data[y][x] == "#":
        if sum(map(lambda d: d == "#", __get_all_places_around(data, x, y))) >= 4:
            return "L"

    return data[y][x]


def get_status_rules_2(data: List[str], x: int, y: int) -> str:
    if data[y][x] == "L":
        if all(map(lambda d: d != "#", __get_all_places_you_can_see(data, x, y))):
            return "#"

    elif data[y][x] == "#":
        if sum(map(lambda d: d == "#", __get_all_places_you_can_see(data, x, y))) >= 5:
            return "L"

    return data[y][x]


def __get_all_places_around(data, x, y):
    y_len = len(input_data)
    x_len = len(input_data[0])

    if x - 1 >= 0:
        yield data[y][x - 1]

        if y - 1 >= 0:
            yield data[y - 1][x - 1]

        if y + 1 < y_len:
            yield data[y + 1][x - 1]

    if x + 1 < x_len:
        yield data[y][x + 1]

        if y - 1 >= 0:
            yield data[y - 1][x + 1]

        if y + 1 < y_len:
            yield data[y + 1][x + 1]

    if y - 1 >= 0:
        yield data[y - 1][x]

    if y + 1 < y_len:
        yield data[y + 1][x]


def __generate_places_you_can_see(data, x, y, x_move, y_move):
    y_len = len(input_data)
    x_len = len(input_data[0])

    temp_x = x + x_move
    temp_y = y + y_move
    while 0 <= temp_x < x_len and 0 <= temp_y < y_len:
        if data[temp_y][temp_x] == ".":
            temp_x += x_move
            temp_y += y_move
        else:
            yield data[temp_y][temp_x]
            break


def __get_all_places_you_can_see(data, x, y):
    for x_move, y_move in [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]:
        for place in __generate_places_you_can_see(data, x, y, x_move, y_move):
            yield place


def solve_1(data: List[str]):
    new_map = [list(line) for line in data]
    y_len = len(input_data)
    x_len = len(input_data[0])

    while True:
        for y in range(y_len):
            for x in range(x_len):
                new_map[y][x] = get_status_rules_1(data, x, y)

        if ["".join(line) for line in new_map] == data:
            print(sum([sum(map(lambda s: s == "#", line)) for line in new_map]))
            break

        data = ["".join(line) for line in new_map]


def solve_2(data: List[str]):
    new_map = [list(line) for line in data]
    y_len = len(input_data)
    x_len = len(input_data[0])

    while True:
        for y in range(y_len):
            for x in range(x_len):
                new_map[y][x] = get_status_rules_2(data, x, y)

        if ["".join(line) for line in new_map] == data:
            print(sum([sum(map(lambda s: s == "#", line)) for line in new_map]))
            break

        data = ["".join(line) for line in new_map]


if __name__ == "__main__":
    input_data = read_lines()

    solve_1(input_data.copy())
    solve_2(input_data.copy())
