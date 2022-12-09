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

class Point:
    def __init__(self):
        self.x = 1000
        self.y = 1000


def get_grid(n):
    starting_grid = [[0] * n for _ in range(n)]
    starting_grid[1000][1000] = 1

    return starting_grid


def update_tail_coordinated(grid, head, tail):
    around_tail = get_objects_around(grid, tail)

    if 1 in around_tail:
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

    # print(around_tail)
    return tail


def get_objects_around(grid, point):
    around_point = []
    n = len(grid)

    for i in range(-1, 2):
        for j in range(-1, 2):
            if point.x + i < 0 or point.y + j < 0 or point.x + i > n - 1 or point.y + j > n - 1:
                continue

            around_point.append(grid[point.x + i][point.y + j])

    return around_point


def is_head_covers_tail(grid, head):
    around_tail = get_objects_around(grid, head)
    return 2 not in around_tail


def solve_1(data: List[str]) -> None:
    # none = 0, head = 1, tail = 2
    # not visited = 0, visited = 1,
    n = 2000
    main_grid = get_grid(n)
    visited_grid = get_grid(n)
    # x, y
    head = Point()
    tail = Point()

    for line in data:
        direction, steps = line.split()
        steps = int(steps)

        for i in range(steps):
            is_cover = is_head_covers_tail(main_grid, head)
            old_head_x, old_head_y = head.x, head.y
            old_tail_x, old_tail_y = tail.x, tail.y

            if direction == "R":
                head.x += 1
            elif direction == "L":
                head.x -= 1
            elif direction == "U":
                head.y += 1
            elif direction == "D":
                head.y -= 1

            if is_cover:
                main_grid[old_head_x][old_head_y] = 2
            else:
                main_grid[old_head_x][old_head_y] = 0

            main_grid[head.x][head.y] = 1

            tail = update_tail_coordinated(main_grid, head, tail)

            visited_grid[tail.x][tail.y] = 1

            main_grid[old_tail_x][old_tail_y] = 0
            main_grid[tail.x][tail.y] = 2

            # print(main_grid)
            # print(visited_grid)

    print(sum(list(map(lambda x: sum(x), visited_grid))))


def solve_2(data: List[str]) -> None:
    # none = 0, head = 1, tail = 2
    # not visited = 0, visited = 1,
    n = 2000
    main_grid = get_grid(n)
    visited_grid = get_grid(n)


if __name__ == "__main__":
    input_data = read_lines()

    solve_1(input_data.copy())
    solve_2(input_data.copy())
