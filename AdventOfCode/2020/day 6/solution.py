# -----------------------------------------------------------
# Notes  : tag-adventOfCode
# -----------------------------------------------------------


from functools import reduce
from typing import Iterator

from utils import read_with_empty_lines

input_data = read_with_empty_lines()


def remove_duplicates(data: Iterator[str]) -> str:
    return "".join(set("".join(data)))


def string_intersect(data: Iterator[str]) -> str:
    return "".join(reduce(lambda x, y: set(x) & set(y), data))


def convert_to_length(data: Iterator[str]):
    return map(lambda x: len(x), data)


def solve_1():
    one_group_selections = map(remove_duplicates, input_data)
    print(reduce(lambda x, y: x + len(y), one_group_selections, 0))


def solve_2():
    one_group_selections = map(string_intersect, input_data)
    print(reduce(lambda x, y: x + len(y), one_group_selections, 0))


solve_1()
solve_2()
