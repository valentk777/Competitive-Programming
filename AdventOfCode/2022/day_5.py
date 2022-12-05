# ---------------------------------------------------------------------------------------
# URL    : https://adventofcode.com/2022/day/5
# Title  : Supply Stacks
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

def get_stacks(data):
    _stacks = list(filter(lambda x: "move" not in x, data))
    number_of_stacks = int(_stacks[-1].strip()[-1])
    _stacks = _stacks[:-1]

    new_stacks = [[] for _ in range(number_of_stacks)]

    for line in _stacks[::-1]:
        n = len(line)
        current_stack = 0

        for i in range(1, min(n, number_of_stacks * 4) + 1, 4):
            if line[i] != " ":
                new_stacks[current_stack].append(line[i])
            current_stack += 1

    return new_stacks


def get_commands(data):
    _commands = filter(lambda x: "move" in x, data)
    _commands = map(lambda x: list(map(int, [x.split()[1], x.split()[3], x.split()[5]])), _commands)
    _commands = list(_commands)
    return _commands


def get_ans_from_stacks(_stacks):
    return list_to_string(map(lambda x: x[-1], _stacks))


def solve_1(_stacks, _commands) -> None:
    for a, b, c in _commands:
        for i in range(a):
            last = _stacks[b - 1].pop()
            _stacks[c - 1].append(last)

    ans = get_ans_from_stacks(_stacks)
    print(ans)


def solve_2(_stacks, _commands) -> None:
    for a, b, c in _commands:
        move = _stacks[b - 1][-a:]
        _stacks[c - 1].extend(move)
        _stacks[b - 1] = _stacks[b - 1][:-a]

    ans = get_ans_from_stacks(_stacks)
    print(ans)


if __name__ == "__main__":
    input_data = read_lines()

    stacks = get_stacks(input_data)
    commands = get_commands(input_data)
    solve_1(stacks, commands)

    stacks = get_stacks(input_data)
    commands = get_commands(input_data)
    solve_2(stacks, commands)
