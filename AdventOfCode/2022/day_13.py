# ---------------------------------------------------------------------------------------
# URL    : https://adventofcode.com/2022/day/13
# Title  : Distress Signal
# Tags   : tag-adventofcode
# ---------------------------------------------------------------------------------------

# region --------------------------------------------Shared part--------------------------------------------------------
import ast
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

def parse_input(data):
    updated = []

    for line in data:
        updated.append(ast.literal_eval(line))

    return updated


def compare_lists(list1, list2):
    # If both values are integers, compare the integers directly
    if isinstance(list1, int) and isinstance(list2, int):
        if list1 == list2:
            return -1
        else:
            return list1 < list2

    # If both values are lists, compare each element in the lists
    elif isinstance(list1, list) and isinstance(list2, list):
        if list1 == list2:
            return -1

        for i in range(min(len(list1), len(list2))):
            # If a comparison makes a decision about the order, return the result
            result = compare_lists(list1[i], list2[i])

            if result != -1:
                return result

        if len(list1) == len(list2):
            return -1

        else:
            return len(list1) < len(list2)

    # If exactly one value is an integer, convert the integer to a list and retry the comparison
    else:
        if isinstance(list1, int):
            list1 = [list1]
        else:
            list2 = [list2]

        return compare_lists(list1, list2)


def solve_1(data: List[str]) -> None:
    ans = 0
    pair = 1

    for i in range(1, len(data), 2):
        if compare_lists(data[i - 1], data[i]):
            ans += pair

        pair += 1

    print(ans)


def solve_2(data: List[str]) -> None:
    stop = False

    while not stop:
        stop = True

        for i in range(1, len(data)):
            if not compare_lists(data[i - 1], data[i]):
                data[i - 1], data[i] = data[i], data[i - 1]
                stop = False

    ans = 1

    for i in range(len(data)):
        if data[i] == [[2]] or data[i] == [[6]]:
            ans *= (1 + i)

    print(ans)


if __name__ == "__main__":
    input_data = read_lines()

    solve_1(parse_input(input_data))

    input_data.append("[[2]]")
    input_data.append("[[6]]")
    solve_2(parse_input(input_data))
