# ---------------------------------------------------------------------------------------
# URL    : https://adventofcode.com/2020/day/1
# Title  : Report Repair
# Tags   : tag-adventofcode
# ---------------------------------------------------------------------------------------

# region --------------------------------------------Shared part--------------------------------------------------------

import math
import sys
from collections import defaultdict, Counter

from utils import read_lines, to_int


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

def solve_1(data):
    n = len(data)

    for i in range(n):
        for j in range(i + 1, n):
            if data[i] + data[j] == 2020:
                print(data[i] * data[j])


def solve_2(data):
    n = len(data)

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if data[i] + data[j] + data[k] == 2020:
                    print(data[i] * data[j] * data[k])


if __name__ == "__main__":
    input_data = to_int(read_lines())

    solve_1(input_data.copy())
    solve_2(input_data.copy())
