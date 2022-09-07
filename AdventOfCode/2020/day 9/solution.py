# -----------------------------------------------------------
# Notes  : tag-adventOfCode
# -----------------------------------------------------------


from itertools import combinations
from typing import List

from utils import read_lines

input_data = read_lines()
input_data = list(map(int, input_data))


def make_sums(data: List[int]):
    return map(sum, combinations(data, 2))


def solve_1(data: List[int]):
    n = 25
    for i in range(len(data) - n):
        sums = make_sums(data[i:i + n])
        if data[i + n] not in sums:
            print(data[i + n])
            return data[i + n]


def solve_2(data: List[int], search_number):
    for i in range(len(data) - 3):
        for j in range(i + 3, len(data)):
            if search_number == sum(data[i:j]):
                print(max(data[i:j]) + min(data[i:j]))
                break


invalid_number = solve_1(input_data)
solve_2(input_data, invalid_number)
