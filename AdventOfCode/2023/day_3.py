# ---------------------------------------------------------------------------------------
# URL    : https://adventofcode.com/2023/day/3
# Title  : Gear Ratios
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

class EnginePart:
    def __init__(self):
        self.number = ""
        self.parts = set()

    def get_number(self):
        return int(self.number)

    def is_empty(self):
        return self.number == ""

    def is_part_of_engine(self):
        return len(self.parts) != 0

    def get_gears(self):
        return list(filter(lambda x: x[0] == "*", self.parts))

    def has_gear(self):
        return len(self.get_gears()) != 0


def get_engine_parts_from_data(data: List[str]) -> List[EnginePart]:
    matrix = _dp(0)
    len_i = len(data)
    len_j = len(data[0])

    for i in range(len_i):
        for j in range(len_j):
            matrix[i, j] = data[i][j]

    engine_parts = []

    for i in range(len_i):
        engine = EnginePart()

        for j in range(len_j):
            if matrix[i, j].isdigit():
                engine.number += matrix[i, j]

                if (i + 1 < len_i
                        and j + 1 < len_j
                        and not matrix[i + 1, j + 1].isdigit()
                        and matrix[i + 1, j + 1] != "."):
                    engine.parts.add((matrix[i + 1, j + 1], i + 1, j + 1))

                if (i + 1 < len_i
                        and not matrix[i + 1, j].isdigit()
                        and matrix[i + 1, j] != "."):
                    engine.parts.add((matrix[i + 1, j], i + 1, j))

                if (i + 1 < len_i
                        and j - 1 > -1
                        and not matrix[i + 1, j - 1].isdigit()
                        and matrix[i + 1, j - 1] != "."):
                    engine.parts.add((matrix[i + 1, j - 1], i + 1, j - 1))

                if (j + 1 < len_j
                        and not matrix[i, j + 1].isdigit()
                        and matrix[i, j + 1] != "."):
                    engine.parts.add((matrix[i, j + 1], i, j + 1))

                if (j - 1 > -1
                        and not matrix[i, j - 1].isdigit()
                        and matrix[i, j - 1] != "."):
                    engine.parts.add((matrix[i, j - 1], i, j - 1))

                if (i - 1 > -1
                        and j - 1 > -1
                        and not matrix[i - 1, j - 1].isdigit()
                        and matrix[i - 1, j - 1] != "."):
                    engine.parts.add((matrix[i - 1, j - 1], i - 1, j - 1))

                if (i - 1 > -1
                        and not matrix[i - 1, j].isdigit()
                        and matrix[i - 1, j] != "."):
                    engine.parts.add((matrix[i - 1, j], i - 1, j))

                if (i - 1 > -1
                        and j + 1 < len_j
                        and not matrix[i - 1, j + 1].isdigit()
                        and matrix[i - 1, j + 1] != "."):
                    engine.parts.add((matrix[i - 1, j + 1], i - 1, j + 1))

            else:
                if not engine.is_empty() and engine.is_part_of_engine():
                    engine_parts.append(engine)

                engine = EnginePart()

        if not engine.is_empty() and engine.is_part_of_engine():
            engine_parts.append(engine)

    return engine_parts


def solve_1(data: List[str]) -> None:
    engine_parts = get_engine_parts_from_data(data)
    result = sum(map(lambda x: x.get_number(), engine_parts))

    print(result)


def solve_2(data: List[str]) -> None:
    engine_parts = get_engine_parts_from_data(data)
    engine_parts = list(filter(lambda x: x.has_gear(), engine_parts))
    gears_count = _dp(0)
    gears_results = _dp(1)
    result = 0

    for i in range(len(engine_parts)):
        for gear in engine_parts[i].get_gears():
            gears_count[gear] += 1
            gears_results[gear] *= engine_parts[i].get_number()

    for gear, count in gears_count.items():
        if count == 2:
            result += gears_results[gear]

    print(result)


if __name__ == "__main__":
    input_data = read_lines()

    solve_1(input_data.copy())
    solve_2(input_data.copy())
