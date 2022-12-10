# ---------------------------------------------------------------------------------------
# URL    : https://adventofcode.com/2022/day/10
# Title  : Cathode-Ray Tube
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

def solve_1(data: List[str]) -> None:
    cycle = 1
    x = 1
    ans = 0

    for line in data:
        cycle += 1

        if cycle in list(range(20, 220 + 1, 40)):
            ans += x * cycle

        if line != "noop":
            cycle += 1
            x += int(line.replace("addx ", ""))

            if cycle in list(range(20, 220 + 1, 40)):
                ans += x * cycle

    print(ans)


def solve_2(data: List[str]) -> None:
    pixel_position = 0
    sprite_position = 1
    ans = [list("." * 40) for _ in range(6)]

    for line in data:
        if sprite_position - 1 <= pixel_position % 40 <= sprite_position + 1:
            ans[pixel_position // 40][pixel_position % 40] = "#"

        pixel_position += 1

        if line != "noop":
            if sprite_position - 1 <= pixel_position % 40 <= sprite_position + 1:
                ans[pixel_position // 40][pixel_position % 40] = "#"

            sprite_position += int(line.replace("addx ", ""))
            pixel_position += 1

    for line in ans:
        print(list_to_string(line))


if __name__ == "__main__":
    input_data = read_lines()

    solve_1(input_data.copy())
    solve_2(input_data.copy())
