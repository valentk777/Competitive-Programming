from typing import List

from utils import read_lines

input_data = read_lines()
input_data = list(map(lambda x: x.replace(" ", ""), input_data))


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


solve_1(input_data)
solve_2(input_data)
