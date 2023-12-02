# ---------------------------------------------------------------------------------------
# URL    : https://adventofcode.com/2023/day/1
# Title  : Trebuchet?!
# Tags   : tag-adventofcode
# ---------------------------------------------------------------------------------------

# region --------------------------------------------Shared part--------------------------------------------------------

import math
import sys
from collections import defaultdict, Counter

from utils import *

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

def get_only_digits(_text: str):
    return ''.join(i for i in _text if i.isdigit())


def replace_spelled_with_digits(_text: str):
    new_text = ""

    for i in range(len(_text)):
        if _text[i].isdigit():
            new_text += _text[i]
        elif _text[i:i + 3] == "one":
            new_text += "1"
        elif _text[i:i + 3] == "two":
            new_text += "2"
        elif _text[i:i + 5] == "three":
            new_text += "3"
        elif _text[i:i + 4] == "four":
            new_text += "4"
        elif _text[i:i + 4] == "five":
            new_text += "5"
        elif _text[i:i + 3] == "six":
            new_text += "6"
        elif _text[i:i + 5] == "seven":
            new_text += "7"
        elif _text[i:i + 5] == "eight":
            new_text += "8"
        elif _text[i:i + 4] == "nine":
            new_text += "9"
        elif _text[i:i + 4] == "zero":
            new_text += "0"

    return new_text


def solve_1(data):
    all_digits = map(get_only_digits, data)
    only_first_and_last = list(map(lambda x: int(x[0] + x[-1]), all_digits))

    print(sum(only_first_and_last))


def solve_2(data):
    all_digits = map(replace_spelled_with_digits, data)
    only_first_and_last = list(map(lambda x: int(x[0] + x[-1]), all_digits))

    print(sum(only_first_and_last))


if __name__ == "__main__":
    input_data = read_lines()

    solve_1(input_data.copy())
    solve_2(input_data.copy())
