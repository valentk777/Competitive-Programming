# ---------------------------------------------------------------------------------------
# URL    : https://adventofcode.com/2021/day/5
# Title  : Hydrothermal Venture
# Tags   : tag-adventofcode
# ---------------------------------------------------------------------------------------

# region --------------------------------------------Shared part--------------------------------------------------------

import math
import sys
from collections import defaultdict, Counter

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

def get_points(data):
    points = []

    for line in data:
        a, b = line.split(" -> ")
        a = list(map(int, a.split(",")))
        b = list(map(int, b.split(",")))
        points.append([a, b])

    return points


def solve_1(data) -> None:
    matrix = _dp(0)

    for line in data:
        a, b = line

        if a[0] == b[0]:
            for i in range(min(a[1], b[1]), max(a[1], b[1]) + 1):
                matrix[a[0], i] += 1

        elif a[1] == b[1]:
            for i in range(min(a[0], b[0]), max(a[0], b[0]) + 1):
                matrix[i, a[1]] += 1

    ans = list(filter(lambda number: number > 1, matrix.values()))
    print(len(ans))


def solve_2(data) -> None:
    matrix = _dp(0)

    for line in data:
        a, b = line

        if a[0] == b[0]:
            for i in range(min(a[1], b[1]), max(a[1], b[1]) + 1):
                matrix[a[0], i] += 1

        elif a[1] == b[1]:
            for i in range(min(a[0], b[0]), max(a[0], b[0]) + 1):
                matrix[i, a[1]] += 1

        else:
            for i in range(abs(a[0] - b[0]) + 1):
                if a[0] < b[0]:
                    x = a[0] + i
                else:
                    x = a[0] - i

                if a[1] < b[1]:
                    y = a[1] + i
                else:
                    y = a[1] - i

                matrix[x, y] += 1

    ans = list(filter(lambda number: number > 1, matrix.values()))
    print(len(ans))


if __name__ == "__main__":
    input_data = read_lines()
    input_data = get_points(input_data)

    solve_1(input_data.copy())
    solve_2(input_data.copy())
