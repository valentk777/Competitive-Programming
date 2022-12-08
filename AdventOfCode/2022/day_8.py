# ---------------------------------------------------------------------------------------
# URL    : https://adventofcode.com/2022/day/8
# Title  : Treetop Tree House
# Tags   : tag-adventofcode
# ---------------------------------------------------------------------------------------

# region --------------------------------------------Shared part--------------------------------------------------------

import math
import sys
from collections import defaultdict, Counter

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

def solve_1(data) -> None:
    row = len(data)
    col = len(data[0])
    is_visible_matrix = [[False for _ in range(col)] for _ in range(row)]

    for i in range(row):
        for j in range(col):
            if i == 0 or i == row - 1 or j == 0 or j == col - 1:
                is_visible_matrix[i][j] = True

    # from left
    for i in range(1, row - 1):
        _max = data[i][0]

        for j in range(1, col - 1):
            if _max < data[i][j]:
                is_visible_matrix[i][j] = True

            _max = max(_max, data[i][j])

    # from right
    for i in range(1, row - 1):
        _max = data[i][-1]

        for j in range(col - 2, 0, -1):
            if _max < data[i][j]:
                is_visible_matrix[i][j] = True

            _max = max(_max, data[i][j])

    # from top
    for j in range(1, col - 1):
        _max = data[0][j]

        for i in range(1, row - 1):
            if _max < data[i][j]:
                is_visible_matrix[i][j] = True

            _max = max(_max, data[i][j])

    # from bottom
    for j in range(1, col - 1):
        _max = data[-1][j]

        for i in range(row - 2, 0, -1):
            if _max < data[i][j]:
                is_visible_matrix[i][j] = True

            _max = max(_max, data[i][j])

    ans = sum(map(lambda x: sum(x), is_visible_matrix))
    print(ans)


def solve_2(data) -> None:
    row = len(data)
    col = len(data[0])
    visible_distance_matrix = [[1 for _ in range(col)] for _ in range(row)]

    # from left
    for i in range(1, row - 1):
        _max = data[i][0]
        latest_view = [0 for _ in range(10)]

        for j in range(1, col - 1):
            if _max < data[i][j]:
                visible_distance_matrix[i][j] *= j
            else:
                candidate = j

                for k in range(data[i][j], 10):
                    if latest_view[k] != 0:
                        candidate = min(candidate, j - latest_view[k])

                visible_distance_matrix[i][j] *= candidate

            _max = max(_max, data[i][j])
            latest_view[data[i][j]] = j

    # from right
    for i in range(1, row - 1):
        _max = data[i][-1]
        latest_view = [col for _ in range(10)]

        for j in range(col - 2, 0, -1):
            if _max < data[i][j]:
                visible_distance_matrix[i][j] *= (col - j - 1)
            else:
                candidate = col - j - 1

                for k in range(data[i][j], 10):
                    if latest_view[k] != col:
                        candidate = min(candidate, latest_view[k] - j)

                visible_distance_matrix[i][j] *= candidate

            _max = max(_max, data[i][j])
            latest_view[data[i][j]] = j

    # from top
    for j in range(1, col - 1):
        _max = data[0][j]
        latest_view = [0 for _ in range(10)]

        for i in range(1, row - 1):
            if _max < data[i][j]:
                visible_distance_matrix[i][j] *= i
            else:
                candidate = i

                for k in range(data[i][j], 10):
                    if latest_view[k] != 0:
                        candidate = min(candidate, i - latest_view[k])

                visible_distance_matrix[i][j] *= candidate

            _max = max(_max, data[i][j])
            latest_view[data[i][j]] = i

    # from bottom
    for j in range(1, col - 1):
        _max = data[-1][j]
        latest_view = [row for _ in range(10)]

        for i in range(row - 2, 0, -1):
            if _max < data[i][j]:
                visible_distance_matrix[i][j] *= (row - i - 1)
            else:
                candidate = row - i - 1

                for k in range(data[i][j], 10):
                    if latest_view[k] != row:
                        candidate = min(candidate, latest_view[k] - i)

                visible_distance_matrix[i][j] *= candidate

            _max = max(_max, data[i][j])
            latest_view[data[i][j]] = i

    print(max(map(lambda x: max(x), visible_distance_matrix)))


if __name__ == "__main__":
    input_data = read_lines()
    input_data = list(map(lambda x: list(map(int, x)), input_data))

    solve_1(input_data)
    solve_2(input_data)
