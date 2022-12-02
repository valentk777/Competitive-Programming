# ---------------------------------------------------------------------------------------
# URL    : https://adventofcode.com/2021/day/4
# Title  : Giant Squid
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

def validate_matrix(matrix):
    _matrix = matrix.copy()

    for i in range(5):
        winner = True

        for j in range(5):
            if not _matrix[i][j][1]:
                winner = False
                break

        if winner:
            return True

    for i in range(5):
        winner = True

        for j in range(5):
            if not _matrix[j][i][1]:
                winner = False
                break

        if winner:
            return True

    return False


def update_matrix(matrix, number):
    _matrix = matrix.copy()

    for i in range(5):
        for j in range(5):
            if _matrix[i][j][0] == number:
                _matrix[i][j][1] = True

    return _matrix


def get_score(matrix, current_number):
    ans = 0

    for i in range(5):
        for j in range(5):
            if not matrix[i][j][1]:
                ans += matrix[i][j][0]

    return ans * current_number


def get_matrixs(data):
    _matrixs = []
    _matrix = []

    for idx, line in enumerate(data):
        if idx != 0 and idx % 5 == 0:
            _matrixs.append(_matrix)
            _matrix = []

        _matrix.append([[number, False] for number in to_int(line.split())])

    _matrixs.append(_matrix)

    return _matrixs


def solve_1(_numbers, _matrixs) -> None:
    for number in _numbers:
        for matrix in _matrixs:
            matrix = update_matrix(matrix, number)
            if validate_matrix(matrix):
                print(get_score(matrix, number))
                return


def solve_2(_numbers, _matrixs) -> None:
    _last_winner_and_number = ()

    for number in _numbers:
        new_matrixs = []

        for matrix in _matrixs:
            matrix = update_matrix(matrix, number)

            if validate_matrix(matrix):
                _last_winner_and_number = (matrix, number)
            else:
                new_matrixs.append(matrix)

        _matrixs = new_matrixs

    print(get_score(_last_winner_and_number[0], _last_winner_and_number[1]))
    return


if __name__ == "__main__":
    input_data = read_lines()
    numbers = to_int(input_data[0].split(","))
    matrixs = get_matrixs(input_data[1:])

    solve_1(numbers, matrixs.copy())

    matrixs = get_matrixs(input_data[1:])
    solve_2(numbers, matrixs.copy())
