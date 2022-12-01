# ---------------------------------------------------------------------------------------
# URL    : https://adventofcode.com/2021/day/3
# Title  : Binary Diagnostic
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

def get_max_bit(data, position):
    _count = cnt(list(map(lambda x: x[position], data)))

    if _count["0"] > _count["1"]:
        return "0"

    return "1"


def get_min_bit(data, position):
    _count = cnt(list(map(lambda x: x[position], data)))

    if _count["0"] <= _count["1"]:
        return "0"

    return "1"


def solve_1(data: List[str]) -> None:
    n = len(data[0])
    gamma = ""
    epsilon = ""

    for i in range(n):
        gamma += get_max_bit(data, i)
        epsilon += get_min_bit(data, i)

    print(int(gamma, 2) * int(epsilon, 2))


def solve_2(data: List[str]) -> None:
    n = len(data[0])
    oxygen = data.copy()
    co2 = data.copy()

    for i in range(n):
        _max = get_max_bit(oxygen, i)
        _min = get_min_bit(co2, i)

        if len(oxygen) != 1:
            oxygen = list(filter(lambda x: x[i] == _max, oxygen))

        if len(co2) != 1:
            co2 = list(filter(lambda x: x[i] == _min, co2))

    print(int(oxygen[0], 2) * int(co2[0], 2))


if __name__ == "__main__":
    input_data = read_lines()

    solve_1(input_data.copy())
    solve_2(input_data.copy())
