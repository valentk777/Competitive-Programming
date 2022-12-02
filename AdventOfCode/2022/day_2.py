# ---------------------------------------------------------------------------------------
# URL    : https://adventofcode.com/2022/day/2
# Title  : Rock Paper Scissors
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

def get_game_score(data):
    ans = 0

    for line in data:
        you, me = line.split()

        if me == "X":
            ans += 1

            if you == "C":
                ans += 6

            if you == "A":
                ans += 3

        elif me == "Y":
            ans += 2

            if you == "A":
                ans += 6

            if you == "B":
                ans += 3
        else:
            ans += 3

            if you == "B":
                ans += 6

            if you == "C":
                ans += 3

    return ans


def solve_1(data: List[str]) -> None:
    ans = get_game_score(data)
    print(ans)


def solve_2(data: List[str]) -> None:
    for i in range(len(data)):
        you, end = data[i].split()

        if end == "X":
            if you == "A":
                data[i] = f"{you} Z"
            elif you == "B":
                data[i] = f"{you} X"
            else:
                data[i] = f"{you} Y"
        elif end == "Y":
            if you == "A":
                data[i] = f"{you} X"
            elif you == "B":
                data[i] = f"{you} Y"
            else:
                data[i] = f"{you} Z"
        else:
            if you == "A":
                data[i] = f"{you} Y"
            elif you == "B":
                data[i] = f"{you} Z"
            else:
                data[i] = f"{you} X"

    ans = get_game_score(data)
    print(ans)


if __name__ == "__main__":
    input_data = read_lines()

    solve_1(input_data.copy())
    solve_2(input_data.copy())
