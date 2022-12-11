# ---------------------------------------------------------------------------------------
# URL    : https://adventofcode.com/2022/day/11
# Title  : Monkey in the Middle
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

class Monkey:
    def __init__(self, number):
        self.number = number
        self.items = []
        self.operation = ""
        self.operation_by_number = INF
        self.test_number = INF
        self.throw_true = INF
        self.throw_false = INF

    def apply_operation(self, item):
        return eval(f"{item}{self.operation}{self.operation_by_number}")

    def add_item(self, item):
        self.items.append(item)

    def test(self, item):
        return item % self.test_number == 0

    def throw_to(self, item):
        if self.test(item):
            return self.throw_true

        return self.throw_false

    def __str__(self):
        return f"number = {self.number}; items = {self.items}"


def get_monkeys(data):
    _monkeys = []

    for line in data:
        if "Monkey" in line:
            info = line.replace("Monkey ", "").replace(":", "")
            _monkeys.append(Monkey(int(info)))
            continue

        if "Starting items:" in line:
            items = line.replace("Starting items: ", "").split(", ")
            items = list(map(int, items))
            _monkeys[-1].items = items
            continue

        if "Operation:" in line:
            info = line.replace("Operation: new = old", "").strip().split(" ")
            _monkeys[-1].operation = info[0]

            if info[1] == "old":
                _monkeys[-1].operation = "**"
                _monkeys[-1].operation_by_number = 2
            else:
                _monkeys[-1].operation_by_number = int(info[1])
            continue

        if "Test:" in line:
            info = line.replace("Test: divisible by ", "")
            _monkeys[-1].test_number = int(info)
            continue

        if "If true:" in line:
            info = line.replace("If true: throw to monkey ", "")
            _monkeys[-1].throw_true = int(info)
            continue

        if "If false:" in line:
            info = line.replace("If false: throw to monkey ", "")
            _monkeys[-1].throw_false = int(info)
            continue

    return _monkeys


def get_divisible_by(data):
    divisible_by = 1

    for monkey in data:
        divisible_by *= monkey.test_number

    return divisible_by


def solve_1(data) -> None:
    number_of_iterations = 20
    ans = [0 for _ in range(len(data))]

    for r in range(1, number_of_iterations + 1):
        for monkey in data:
            ans[monkey.number] += len(monkey.items)

            while len(monkey.items) != 0:
                item = monkey.items[0]
                # only this line different
                new_value = monkey.apply_operation(item) // 3
                throw_to = monkey.throw_to(new_value)
                monkey.items.remove(item)
                data[throw_to].items.append(new_value)

    ans = sorted(ans, reverse=True)
    print(ans[0] * ans[1])


def solve_2(data) -> None:
    number_of_iterations = 10000
    ans = [0 for _ in range(len(data))]
    divisible_by = get_divisible_by(data)

    for r in range(1, number_of_iterations + 1):
        for monkey in data:
            ans[monkey.number] += len(monkey.items)

            while len(monkey.items) != 0:
                item = monkey.items[0]
                # only this line different
                new_value = monkey.apply_operation(item) % divisible_by
                throw_to = monkey.throw_to(new_value)
                monkey.items.remove(item)
                data[throw_to].add_item(new_value)

    ans = sorted(ans, reverse=True)
    print(ans[0] * ans[1])


if __name__ == "__main__":
    input_data = read_lines()

    monkeys = get_monkeys(input_data)
    solve_1(monkeys)

    monkeys = get_monkeys(input_data)
    solve_2(monkeys)
