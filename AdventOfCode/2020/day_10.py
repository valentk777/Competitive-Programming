# ---------------------------------------------------------------------------------------
# URL    : https://adventofcode.com/2020/day/10
# Title  : Adapter Array
# Tags   : tag-adventofcode
# ---------------------------------------------------------------------------------------

# region --------------------------------------------Shared part--------------------------------------------------------

import math
import sys
from collections import defaultdict, Counter
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

def solve_1(data: List[int]):
    three_count = 0
    one_count = 0
    for i in range(1, len(data)):
        if data[i] - data[i - 1] == 3:
            three_count += 1
        elif data[i] - data[i - 1] == 1:
            one_count += 1

    print(three_count * one_count)


def solve_2(data: List[int]):
    step_count = [1] + [0 for _ in range(data[-1])]

    if 1 in data:
        step_count[1] = 1

    if 2 in data:
        step_count[2] = step_count[1] + step_count[0]

    for i in data[3:]:
        step_count[i] = step_count[i - 1] + step_count[i - 2] + step_count[i - 3]

    print(step_count[-1])


if __name__ == "__main__":
    input_data = to_int(read_lines())
    input_data.sort()
    input_data = [0] + input_data + [input_data[-1] + 3]

    solve_1(input_data.copy())
    solve_2(input_data.copy())
