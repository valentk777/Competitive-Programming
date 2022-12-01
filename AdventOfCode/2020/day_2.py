# ---------------------------------------------------------------------------------------
# URL    : https://adventofcode.com/2020/day/2
# Title  : Password Philosophy
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

class PassObject:
    def __init__(self, data):
        numbers, letter, password = data.split()
        number1, number2 = numbers.split('-')
        self.first_number: int = int(number1)
        self.second_number: int = int(number2)
        self.letter: str = letter[0]
        self.password: str = password


def compare_letters(letter: str):
    def step(data):
        return data == letter

    return step


def validate_password_1(data: PassObject) -> bool:
    return data.first_number <= len(list(filter(compare_letters(data.letter), data.password))) <= data.second_number


def validate_password_2(data: PassObject) -> bool:
    return (data.password[data.first_number - 1] == data.letter
            and data.password[data.second_number - 1] != data.letter
            or data.password[data.first_number - 1] != data.letter
            and data.password[data.second_number - 1] == data.letter)


def solve_1(data):
    print(sum(map(validate_password_1, data)))


def solve_2(data):
    print(sum(map(validate_password_2, data)))


if __name__ == "__main__":
    input_data = read_lines()
    pass_data = list(map(PassObject, input_data))

    solve_1(input_data.copy())
    solve_2(input_data.copy())
