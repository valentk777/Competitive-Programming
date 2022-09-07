# -----------------------------------------------------------
# Notes  : tag-adventOfCode
# -----------------------------------------------------------


from typing import List

from utils import read_lines

input_data = read_lines()


def solve_1(data: List[int]):
    three_count = 0
    one_count = 0
    for i in range(1, len(data)):
        if data[i] - data[i - 1] == 3:
            three_count += 1
        elif data[i] - data[i - 1] == 1:
            one_count += 1

    print(three_count * one_count)


def solve_2(data: List[int]):
    step_count = [1] + [0 for _ in range(data[-1])]

    if 1 in data:
        step_count[1] = 1

    if 2 in data:
        step_count[2] = step_count[1] + step_count[0]

    for i in data[3:]:
        step_count[i] = step_count[i - 1] + step_count[i - 2] + step_count[i - 3]

    print(step_count[-1])


input_data_int = list(map(int, input_data))
input_data_int.sort()
input_data_int = [0] + input_data_int + [input_data_int[-1] + 3]

solve_1(input_data_int)
solve_2(input_data_int)
