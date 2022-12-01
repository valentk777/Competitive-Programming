# ---------------------------------------------------------------------------------------
# URL    : https://adventofcode.com/2020/day/8
# Title  : Handheld Halting
# Tags   : tag-adventofcode
# ---------------------------------------------------------------------------------------

# region --------------------------------------------Shared part--------------------------------------------------------

import math
import sys
from collections import defaultdict, Counter
from dataclasses import dataclass, field
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


@dataclass
class Operation:
    operation: str
    move: int
    visited: bool = field(default=False)


def to_operation(data: str):
    return Operation(data[:3], int(data[4:]))


def make_a_move(data: Operation, position, accumulator_value):
    if data.operation == "jmp":
        position += data.move
    elif data.operation == "acc":
        accumulator_value += data.move
        position += 1
    else:
        position += 1

    return position, accumulator_value


def iterate(data: List[Operation]):
    accumulator_value = 0
    position = 0
    while position != len(data) and not data[position].visited:
        data[position].visited = True
        position, accumulator_value = make_a_move(data[position], position, accumulator_value)

    return accumulator_value, position == len(data)


def replace_operation(data: Operation):
    if data.operation == "jmp":
        data.operation = "nop"
    elif data.operation == "nop":
        data.operation = "jmp"


def remove_visited(data: List[Operation]):
    for d in data:
        d.visited = False


def solve_1(data: List[Operation]):
    accumulator_value, _ = iterate(data.copy())
    remove_visited(data)
    print(accumulator_value)


def solve_2(data: List[Operation]):
    for d in data:
        replace_operation(d)
        if d.operation == "acc":
            continue

        accumulator_value, is_finite = iterate(data)
        if is_finite:
            print(accumulator_value)
            break

        replace_operation(d)
        remove_visited(data)


if __name__ == "__main__":
    input_data = read_lines()
    input_data = list(map(to_operation, input_data))

    solve_1(input_data.copy())
    solve_2(input_data.copy())
