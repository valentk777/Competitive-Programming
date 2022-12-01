# ---------------------------------------------------------------------------------------
# URL    : https://adventofcode.com/2020/day/14
# Title  : Docking Data
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
class Command:
    mask: str
    registry: int
    value: str

    def merged_bits(self) -> int:
        new = []

        for i in range(1, len(self.mask) + 1):
            if self.mask[-i] == "X":
                new.append("0" if len(self.value) < i else self.value[-i])
            else:
                new.append(self.mask[-i])

        new.reverse()
        return int("".join(new), 2)

    def generate_registry(self) -> List[str]:
        masks = [list(self.__modify_mask())]
        while True:
            new = []
            for mask in masks:
                if "X" not in mask:
                    continue

                idx = mask.index("X")
                mask[idx] = "0"
                new.append(mask.copy())
                mask[idx] = "1"
                new.append(mask.copy())

            if not new:
                break
            else:
                masks = new

        return list(map("".join, masks))

    def __modify_mask(self) -> str:
        new = []
        value = f"{self.registry:b}"
        for i in range(1, len(self.mask) + 1):
            if self.mask[-i] == "0":
                new.append(self.mask[-i] if len(value) < i else value[-i])
            else:
                new.append(self.mask[-i])

        new.reverse()
        return "".join(new)


def to_commands(data: List[str]) -> List[Command]:
    current_mask = ""
    commands = []
    for line in data:
        if line.startswith("mask"):
            current_mask = line.split(" = ")[1]
        else:
            commands.append(to_command(current_mask)(line))
    return commands


def to_command(_mask: str):
    def step(data: str):
        data = data.split(" = ")
        registry = data[0][4:-1]
        return Command(_mask, int(registry), f"{int(data[1]):b}")

    return step


def solve_1(data: List[Command]) -> None:
    memory = {}
    for d in data:
        memory[d.registry] = d.merged_bits()
    print(sum(memory.values()))


def solve_2(data: List[Command]) -> None:
    memory = {}
    for d in data:
        for mask in d.generate_registry():
            memory[mask] = int(d.value, 2)

    print(sum(memory.values()))


if __name__ == "__main__":
    input_data = read_lines()
    input_data = to_commands(input_data)

    solve_1(input_data.copy())
    solve_2(input_data.copy())
