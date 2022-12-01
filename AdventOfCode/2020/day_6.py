# ---------------------------------------------------------------------------------------
# URL    : https://adventofcode.com/2020/day/6
# Title  : Custom Customs
# Tags   : tag-adventofcode
# ---------------------------------------------------------------------------------------

# region --------------------------------------------Shared part--------------------------------------------------------

import math
import sys
from collections import defaultdict, Counter
from functools import reduce
from typing import Iterator

from utils import read_with_empty_lines


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

def remove_duplicates(data: Iterator[str]) -> str:
    return "".join(set("".join(data)))


def string_intersect(data: Iterator[str]) -> str:
    return "".join(reduce(lambda x, y: set(x) & set(y), data))


def convert_to_length(data: Iterator[str]):
    return map(lambda x: len(x), data)


def solve_1(data):
    one_group_selections = map(remove_duplicates, data)
    print(reduce(lambda x, y: x + len(y), one_group_selections, 0))


def solve_2(data):
    one_group_selections = map(string_intersect, data)
    print(reduce(lambda x, y: x + len(y), one_group_selections, 0))


if __name__ == "__main__":
    input_data = read_with_empty_lines()

    solve_1(input_data.copy())
    solve_2(input_data.copy())
