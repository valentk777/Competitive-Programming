# ---------------------------------------------------------------------------------------
# URL    : https://adventofcode.com/2022/day/6
# Title  : Tuning Trouble
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

def solve_1(data) -> None:
    n = len(data)

    for i in range(n - 3):
        _letters = data[i:i + 4]

        if len(set(_letters)) == 4:
            print(i + 4)
            break


def solve_2(data) -> None:
    n = len(data)

    for i in range(n - 13):
        _letters = data[i:i + 14]

        if len(set(_letters)) == 14:
            print(i + 14)
            break


if __name__ == "__main__":
    input_data = read_lines()[0]
    print(input_data)

    solve_1(input_data)
    solve_2(input_data)
