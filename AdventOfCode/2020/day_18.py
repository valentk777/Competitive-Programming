# ---------------------------------------------------------------------------------------
# URL    : https://adventofcode.com/2020/day/18
# Title  : Operation Order
# Tags   : tag-adventofcode
# ---------------------------------------------------------------------------------------

# region --------------------------------------------Shared part--------------------------------------------------------

import math
import sys
from collections import defaultdict, Counter
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

def evaluate_equal_expression(expression: str):
    if "*" not in expression:
        return str(eval(expression))

    if "+" not in expression:
        return str(eval(expression))

    number = ""
    first = True
    for i in range(len(expression)):
        if expression[i] in ["+", "-", "*", "/"]:
            if first:
                first = False
            else:
                number = str(eval(number))

        number += expression[i]

    return str(eval(number))


def evaluate_not_equal_expression(expression: str):
    if "*" not in expression:
        return str(eval(expression))

    if "+" not in expression:
        return str(eval(expression))

    number = 1
    for i in map(eval, expression.split("*")):
        number *= i

    return str(number)


def evaluate(evaluation_func):
    def step(expression):
        expression_without_brackets = ""
        for e in expression:
            if e == ")":
                idx = expression_without_brackets.rfind("(")
                result = evaluation_func(expression_without_brackets[idx + 1:])
                expression_without_brackets = expression_without_brackets[:idx] + result
            else:
                expression_without_brackets += e
        return int(evaluation_func(expression_without_brackets))

    return step


def get_sum_of_expressions(data: List[str], evaluation_func):
    return sum(map(evaluate(evaluation_func), data))


def solve_1(data: List[str]) -> None:
    print(get_sum_of_expressions(data, evaluate_equal_expression))


def solve_2(data: List[str]) -> None:
    print(get_sum_of_expressions(data, evaluate_not_equal_expression))


if __name__ == "__main__":
    input_data = read_lines()
    input_data = list(map(lambda x: x.replace(" ", ""), input_data))

    solve_1(input_data)
    solve_2(input_data)
