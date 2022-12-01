# ---------------------------------------------------------------------------------------
# URL    : https://adventofcode.com/2020/day/9
# Title  : Encoding Error
# Tags   : tag-adventofcode
# ---------------------------------------------------------------------------------------

# region --------------------------------------------Shared part--------------------------------------------------------

import math
import sys
from collections import defaultdict, Counter
from itertools import combinations
from typing import List

from utils import read_lines, to_int

inp = lambda: sys.stdin.readline().strip().rstrip("\r\n")
iinp = lambda: int(inp())
intl = lambda: list(map(int, inp().split()))
strl = lambda: list(inp().split())
list_to_string = lambda _a: "".join(map(str, _a))
list_to_string_list = lambda _a: " ".join(map(str, _a))
_dp = lambda default_value: defaultdict(lambda: default_value)
flush = lambda: sys.stdout.flush()
print_flush = lambda _text: (print(_text), flush())
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


def make_sums(data: List[int]):
    return map(sum, combinations(data, 2))


def solve_1(data: List[int]):
    n = 25
    for i in range(len(data) - n):
        sums = make_sums(data[i:i + n])
        if data[i + n] not in sums:
            print(data[i + n])
            return data[i + n]


def solve_2(data: List[int], search_number):
    for i in range(len(data) - 3):
        for j in range(i + 3, len(data)):
            if search_number == sum(data[i:j]):
                print(max(data[i:j]) + min(data[i:j]))
                break


if __name__ == "__main__":
    input_data = to_int(read_lines())

    invalid_number = solve_1(input_data.copy())
    solve_2(input_data.copy(), invalid_number)
