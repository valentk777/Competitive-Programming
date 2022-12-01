# ---------------------------------------------------------------------------------------
# URL    : https://adventofcode.com/2020/day/3
# Title  : Toboggan Trajectory
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
def get_tree_count_for_slope(data, right: int, down: int) -> int:
    line_max = len(data)
    column_max = len(data[0])
    line = 0
    column = 0
    count_tree = 0
    while line < line_max:
        if data[line][column] == '#':
            count_tree += 1
        line += down
        column = (column + right) % column_max
    return count_tree


def solve_1(data):
    result = get_tree_count_for_slope(data, 3, 1)
    print(result)


def solve_2(data):
    result = (
            get_tree_count_for_slope(data, 1, 1)
            * get_tree_count_for_slope(data, 3, 1)
            * get_tree_count_for_slope(data, 5, 1)
            * get_tree_count_for_slope(data, 7, 1)
            * get_tree_count_for_slope(data, 1, 2)
    )
    print(result)


if __name__ == "__main__":
    input_data = read_lines()

    solve_1(input_data.copy())
    solve_2(input_data.copy())
