# ---------------------------------------------------------------------------------------
# URL    : https://adventofcode.com/2022/day/14
# Title  : PROBLEM_TITLE
# Tags   : tag-adventofcode, tag-not-pass
# ---------------------------------------------------------------------------------------

# region --------------------------------------------Shared part--------------------------------------------------------

import math
import sys
from collections import defaultdict, Counter
from time import sleep

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

# def get_map(data):
#     # n = 12
#     n = 180
#     __map = [["." for _ in range(n)] for _ in range(n)]
#     __map[0][n // 2] = "+"
#
#     for line in data:
#         parts = line.split(" -> ")
#
#         for i in range(len(parts) - 1):
#             x_1, y_1 = list(map(int, parts[i].split(",")))
#             x_2, y_2 = list(map(int, parts[i + 1].split(",")))
#
#             x_1 -= (1000 - n) // 2
#             x_2 -= (1000 - n) // 2
#
#             # to right
#             if x_2 > x_1:
#                 for x in range(x_1, x_2 + 1):
#                     __map[y_1][x] = "#"
#             # to left
#             elif x_2 < x_1:
#                 for x in range(x_2, x_1 + 1):
#                     __map[y_1][x] = "#"
#             # to top
#             elif y_2 > y_1:
#                 for y in range(y_1, y_2 + 1):
#                     __map[y][x_1] = "#"
#             # to down
#             elif y_2 < y_1:
#                 for y in range(y_2, y_1 + 1):
#                     __map[y][x_1] = "#"
#
#     return __map

def get_rocks(data):
    rocks = set()

    for line in data:
        parts = line.split(" -> ")

        for i in range(len(parts) - 1):
            x_1, y_1 = list(map(int, parts[i].split(",")))
            x_2, y_2 = list(map(int, parts[i + 1].split(",")))

            # to right
            if x_2 > x_1:
                for x in range(x_1, x_2 + 1):
                    rocks.add((x, y_1))
            # to left
            elif x_2 < x_1:
                for x in range(x_2, x_1 + 1):
                    rocks.add((x, y_1))
            # to top
            elif y_2 > y_1:
                for y in range(y_1, y_2 + 1):
                    rocks.add((x_1, y))
            # to down
            elif y_2 < y_1:
                for y in range(y_2, y_1 + 1):
                    rocks.add((x_1, y))

    return rocks


def print_map(data):
    sleep(1)
    print()
    for line in data:
        print(line)

    print()


# def solve_1(data):
#     n = len(data)
#     start_x = data[0].index("+")
#     ans = 0
#     stop = False
#
#     while not stop:
#         for i in range(1, n):
#             if data[i][start_x] == ".":
#                 continue
#
#             if data[i][start_x] == "#":
#                 data[i - 1][start_x] = "o"
#                 ans += 1
#                 print_map(data)
#                 break
#
#             if data[i][start_x] == "o":
#                 # to left
#                 if data[i][start_x - 1] == ".":
#
#                     _left_x = start_x - 1
#                     _left_y = i + 1
#
#                     while _left_y < n and _left_x > -1:
#                         if data[_left_y][_left_x] == ".":
#                             _left_y += 1
#                             continue
#
#                         if data[_left_y][_left_x - 1] != ".":
#                             _left_y -= 1
#                             break
#
#                         _left_x -= 1
#                         #
#                         # while _left_y > n and _left_x > -1 and data[_left_y][_left_x] == ".":
#                         #     _left_y += 1
#                         #
#                         #
#                         #     _left_x -= 1
#                         #     _left_y += 1
#                         #
#                         # if _left_y == n or _left_x == -1:
#                         #     stop = False
#                         #     break
#
#                     if _left_y == n or _left_x == -1:
#                         stop = False
#                         break
#
#                     data[_left_y][_left_x] = "o"
#                     ans += 1
#
#                 # to right
#                 elif data[i][start_x + 1] == ".":
#                     # todo: handle what if here is not safe place as well
#                     data[i][start_x + 1] = "o"
#                     ans += 1
#                 else:
#                     data[i - 1][start_x] = "o"
#                     ans += 1
#
#                 print_map(data)
#
#                 break

def solve_1(data) -> None:
    left = min(r[0] for r in data)
    right = max(r[0] for r in data)
    bottom = max(r[1] for r in data)
    sand = set()

    while True:
        x, y = 500, 0
        stop = False

        while not stop:
            stop = True

            while left <= x <= right and y < bottom:
                if (x, y + 1) not in data and (x, y + 1) not in sand:
                    y += 1
                    stop = False
                    continue

                if (x - 1, y + 1) not in data and (x - 1, y + 1) not in sand:
                    y += 1
                    x -= 1
                    stop = False
                    continue

                if (x + 1, y + 1) not in data and (x + 1, y + 1) not in sand:
                    y += 1
                    x += 1
                    stop = False
                    continue

                break

        if x < left or x > right or y >= bottom:
            break

        if (x, y) in sand:
            break

        sand.add((x, y))

    print(len(sand))


def solve_2(data) -> None:
    bottom = max(r[1] for r in data)
    sand = set()

    while True:
        x, y = 500, 0
        stop = False

        while not stop:
            stop = True

            while y < bottom + 1:
                if (x, y + 1) not in data and (x, y + 1) not in sand:
                    y += 1
                    stop = False
                    continue

                if (x - 1, y + 1) not in data and (x - 1, y + 1) not in sand:
                    y += 1
                    x -= 1
                    stop = False
                    continue

                if (x + 1, y + 1) not in data and (x + 1, y + 1) not in sand:
                    y += 1
                    x += 1
                    stop = False
                    continue

                break

        if (x, y) in sand:
            break

        sand.add((x, y))

    print(len(sand))


if __name__ == "__main__":
    input_data = read_lines()

    print(get_rocks(input_data))

    solve_1(get_rocks(input_data))
    solve_2(get_rocks(input_data))
