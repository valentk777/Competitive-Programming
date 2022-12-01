# ---------------------------------------------------------------------------------------
# URL    : https://adventofcode.com/2020/day/15
# Title  : Rambunctious Recitation
# Tags   : tag-adventofcode
# ---------------------------------------------------------------------------------------

# region --------------------------------------------Shared part--------------------------------------------------------

import math
import sys
from collections import defaultdict, Counter
from typing import List

from utils import read_lines

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

def find_solution(data: List[int], number_of_iterations: int) -> int:
    n = len(data)
    d = {data[number - 1]: number for number in range(1, n)}

    current = data[-1]
    count = n
    while count != number_of_iterations:
        if current not in d.keys():
            d[current] = count
            current = 0
        else:
            new_current = count - d[current]
            d[current] = count
            current = new_current
        count += 1
    return current


def solve_1(data: List[int]):
    result = find_solution(data, 2020)
    print(result)


def solve_2(data: List[int]):
    result = find_solution(data, 30000000)
    print(result)


if __name__ == "__main__":
    input_data = read_lines()
    input_data = list(map(int, input_data[0].split(',')))

    solve_1(input_data.copy())
    solve_2(input_data.copy())
