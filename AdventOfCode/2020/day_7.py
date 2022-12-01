# ---------------------------------------------------------------------------------------
# URL    : https://adventofcode.com/2020/day/7
# Title  : Handy Haversacks
# Tags   : tag-adventofcode
# ---------------------------------------------------------------------------------------

# region --------------------------------------------Shared part--------------------------------------------------------

import math
import sys
from collections import defaultdict, Counter
from dataclasses import dataclass
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
class DataBag:
    name: str
    number_of_gold_bags: int
    contains: List[str]


def to_data_bag(data: str) -> DataBag:
    name, contains = data.split(" bags contain ")
    contains = contains[:-1]
    contains = [] if "no other bags" in contains else contains.split(', ')
    return DataBag(name.strip(), 0, contains)


def get_next_idx(n, i):
    if n != 0:
        i = (i + 1) % n
    return i


def get_total(data, dict_map):
    total = 0
    for contain in data.contains:
        name = contain[2:-4].strip()
        if name in dict_map.keys():
            total += dict_map[name] * int(contain[:2].strip())
            data.contains.remove(contain)
    return total


def update_bags(bags, dict_map, data, add_if_last=1):
    data.number_of_gold_bags += get_total(data, dict_map)
    if not data.contains:
        dict_map[data.name] = data.number_of_gold_bags + add_if_last
        bags.remove(data)


def solve_1(data: List[DataBag]) -> None:
    dict_map = {}

    for bag in data:
        if bag.name == "shiny gold":
            dict_map[bag.name] = 1

            additional_dictionary = {contain[2:-4].strip(): 0 for contain in bag.contains}
            dict_map = {**dict_map, **additional_dictionary}
            data.remove(bag)

        elif not bag.contains:
            dict_map[bag.name] = 0
            data.remove(bag)

    i = 0
    while data:
        update_bags(data, dict_map, data[i], 0)
        i = get_next_idx(len(data), i)

    result = sum([1 for v in dict_map.values() if v != 0])
    print(result - 1)


def solve_2(data: List[DataBag]) -> None:
    dict_map = {}

    for bag in data:
        if not bag.contains:
            dict_map[bag.name] = 1
            data.remove(bag)

    i = 0

    while data:
        update_bags(data, dict_map, data[i], 1)
        i = get_next_idx(len(data), i)

    print(dict_map["shiny gold"] - 1)


if __name__ == "__main__":
    input_data = read_lines()
    input_data = list(map(to_data_bag, input_data))

    solve_1(input_data.copy())
    solve_2(input_data.copy())
