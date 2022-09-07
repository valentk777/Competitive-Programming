# -----------------------------------------------------------
# Notes  : tag-adventOfCode
# -----------------------------------------------------------


from typing import List

from utils import read_lines

input_data = read_lines()
y_len = len(input_data)
x_len = len(input_data[0])


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

    while True:
        for y in range(y_len):
            for x in range(x_len):
                new_map[y][x] = get_status_rules_2(data, x, y)

        if ["".join(line) for line in new_map] == data:
            print(sum([sum(map(lambda s: s == "#", line)) for line in new_map]))
            break

        data = ["".join(line) for line in new_map]


solve_1(input_data)
solve_2(input_data)
