# ---------------------------------------------------------------------------------------
# URL    : https://adventofcode.com/2022/day/9
# Title  : Rope Bridge
# Tags   : tag-adventofcode, tag-not-pass
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

start_coordinates = 10


class Point:
    def __init__(self):
        self.x = start_coordinates
        self.y = start_coordinates


def get_grid(n):
    starting_grid = [[[] for _ in range(n)] for _ in range(n)]
    return starting_grid


def get_new_tail_after_head(grid, head, tail, target_number):
    around_tail = get_objects_around(grid, tail)

    if target_number in around_tail:
        return tail

    if head.x == tail.x:
        if head.y - tail.y == 2:
            tail.y += 1
        else:
            tail.y -= 1
    elif head.y == tail.y:
        if head.x - tail.x == 2:
            tail.x += 1
        else:
            tail.x -= 1
    else:
        if head.x - tail.x == 2:
            tail.x += 1
            tail.y = head.y
        elif head.x - tail.x == -2:
            tail.x -= 1
            tail.y = head.y
        elif head.y - tail.y == 2:
            tail.y += 1
            tail.x = head.x
        else:
            tail.y -= 1
            tail.x = head.x

    return tail


def get_objects_around(grid, point):
    around_point = []
    n = len(grid)

    for i in range(-1, 2):
        for j in range(-1, 2):
            if point.x + i < 0 or point.y + j < 0 or point.x + i > n - 1 or point.y + j > n - 1:
                continue

            around_point.extend(grid[point.x + i][point.y + j])

    return around_point


def update_head(direction, head, grid):
    old_head_x, old_head_y = head.x, head.y

    if direction == "R":
        head.x += 1
    elif direction == "L":
        head.x -= 1
    elif direction == "U":
        head.y += 1
    elif direction == "D":
        head.y -= 1

    grid[old_head_x][old_head_y].remove(0)
    grid[head.x][head.y].append(0)

    return grid


def solve_1(data: List[str]) -> None:
    # none = [], head = 0, tail = 1
    n = start_coordinates * 2
    main_grid = get_grid(n)
    main_grid[start_coordinates][start_coordinates] = list(range(2))

    # not visited = 0, visited = 1,
    visited_grid = [[0] * n for _ in range(n)]
    visited_grid[start_coordinates][start_coordinates] = 1

    # x, y
    head = Point()
    tail = Point()

    for line in data:
        direction, steps = line.split()
        steps = int(steps)

        for i in range(steps):
            main_grid = update_head(direction, head, main_grid)

            old_tail_x, old_tail_y = tail.x, tail.y

            tail = get_new_tail_after_head(main_grid, head, tail, 0)

            visited_grid[tail.x][tail.y] = 1

            main_grid[old_tail_x][old_tail_y].remove(1)
            main_grid[tail.x][tail.y].append(1)

            # print(main_grid)
            # print(visited_grid)

    print(sum(list(map(lambda x: sum(x), visited_grid))))


def solve_2(data: List[str]) -> None:
    # none = [], head = 0, tail = 1
    n = start_coordinates * 2
    main_grid = get_grid(n)
    main_grid[start_coordinates][start_coordinates] = list(range(10))

    # not visited = 0, visited = 1,
    visited_grid = [[0] * n for _ in range(n)]
    visited_grid[start_coordinates][start_coordinates] = 1

    # x, y
    head = Point()
    tails = [Point() for _ in range(1, 10)]

    for line in data:
        direction, steps = line.split()
        steps = int(steps)

        for i in range(steps):
            main_grid = update_head(direction, head, main_grid)

            for tail_number in range(1, 10):
                tail = tails[tail_number - 1]
                old_tail_x, old_tail_y = tail.x, tail.y

                if tail_number == 1:
                    tail = get_new_tail_after_head(main_grid, head, tail, tail_number - 1)
                else:
                    # TODO: write leading tail logic
                    pass

                # print(tail.x, tail.y)
                visited_grid[tail.x][tail.y] = 1

                main_grid[old_tail_x][old_tail_y].remove(tail_number)
                main_grid[tail.x][tail.y].append(tail_number)

            # print(main_grid)
    print(visited_grid)

    print(sum(list(map(lambda x: sum(x), visited_grid))))


if __name__ == "__main__":
    input_data = read_lines()

    solve_1(input_data.copy())
    solve_2(input_data.copy())
