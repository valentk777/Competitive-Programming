# ---------------------------------------------------------------------------------------
# URL    : https://programavimas.vgtu.lt/contests/55/problems/2105/
# Title  : 3x3 maksas
# Tags   : tag-LSPO, tag-vgtu, tag-problem-R
# Notes  :
# ---------------------------------------------------------------------------------------

# region --------------------------------------------Shared part--------------------------------------------------------
import math
import sys
from collections import defaultdict, Counter

inp = lambda: sys.stdin.readline().strip().rstrip("\r\n")
iinp = lambda: int(inp())
intl = lambda: list(map(int, inp().split()))
strl = lambda: list(inp().split())
list_to_string = lambda _a: "".join(map(str, _a))
list_to_string_list = lambda _a: " ".join(map(str, _a))
_dp = lambda default_value: defaultdict(lambda: default_value)
flush = lambda: sys.stdout.flush()
print_flush = lambda _text: (print(_text), flush())
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


def solve():
    candidates = []
    matrix = []

    for i in range(3):
        matrix.append(intl())

    candidates.append(
        [
            matrix[0][0],
            matrix[0][1],
            matrix[0][2],
            matrix[1][2],
            matrix[1][1],
            matrix[1][0],
            matrix[2][0],
            matrix[2][1],
            matrix[2][2],
        ])

    candidates.append(
        [
            matrix[0][0],
            matrix[0][1],
            matrix[0][2],
            matrix[1][2],
            matrix[2][2],
            matrix[2][1],
            matrix[2][0],
            matrix[1][0],
            matrix[1][1],
        ])

    candidates.append(
        [
            matrix[0][0],
            matrix[0][1],
            matrix[0][2],
            matrix[1][2],
            matrix[2][2],
            matrix[2][1],
            matrix[1][1],
            matrix[1][0],
            matrix[2][0],
        ])

    candidates.append(
        [
            matrix[0][0],
            matrix[0][1],
            matrix[1][1],
            matrix[1][0],
            matrix[2][0],
            matrix[2][1],
            matrix[2][2],
            matrix[1][2],
            matrix[0][2],
        ])

    candidates.append(
        [
            matrix[0][0],
            matrix[1][0],
            matrix[1][1],
            matrix[0][1],
            matrix[0][2],
            matrix[1][2],
            matrix[2][2],
            matrix[2][1],
            matrix[2][0],
        ])

    candidates.append(
        [
            matrix[0][0],
            matrix[1][0],
            matrix[2][0],
            matrix[2][1],
            matrix[1][1],
            matrix[0][1],
            matrix[0][2],
            matrix[1][2],
            matrix[2][2],
        ])

    candidates.append(
        [
            matrix[0][0],
            matrix[1][0],
            matrix[2][0],
            matrix[2][1],
            matrix[2][2],
            matrix[1][2],
            matrix[1][1],
            matrix[0][1],
            matrix[0][2],
        ])
    candidates.append(
        [
            matrix[0][0],
            matrix[1][0],
            matrix[2][0],
            matrix[2][1],
            matrix[2][2],
            matrix[1][2],
            matrix[0][2],
            matrix[0][1],
            matrix[1][1],
        ])

    candidates = list(map(lambda x: int("".join(list(map(lambda y: str(y), x)))), candidates))

    return max(candidates)

def run():
    print(solve())


if __name__ == "__main__":
    run()
