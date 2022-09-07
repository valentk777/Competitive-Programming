# -----------------------------------------------------------
# Notes  : tag-adventOfCode
# -----------------------------------------------------------


from dataclasses import dataclass
from typing import List

from utils import read_lines

input_data = read_lines()


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


def solve_1(bags: List[DataBag]) -> None:
    dict_map = {}

    for data in bags:
        if data.name == "shiny gold":
            dict_map[data.name] = 1

            additional_dictionary = {contain[2:-4].strip(): 0 for contain in data.contains}
            dict_map = {**dict_map, **additional_dictionary}
            bags.remove(data)

        elif not data.contains:
            dict_map[data.name] = 0
            bags.remove(data)

    i = 0
    while bags:
        update_bags(bags, dict_map, bags[i], 0)
        i = get_next_idx(len(bags), i)

    result = sum([1 for v in dict_map.values() if v != 0])
    print(result - 1)


def solve_2(bags: List[DataBag]) -> None:
    dict_map = {}

    for data in bags:
        if not data.contains:
            dict_map[data.name] = 1
            bags.remove(data)

    i = 0
    while bags:
        update_bags(bags, dict_map, bags[i], 1)
        i = get_next_idx(len(bags), i)

    print(dict_map["shiny gold"] - 1)


bags_data = list(map(to_data_bag, input_data))

solve_1(bags_data)
# solve_2(bags_data)
