# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/230/problem/A
# Title  : A. Dragons
# Tags   : tag-codeforces, tag-problem-A, tag-div-2
# ---------------------------------------------------------------------------------------

# ---------------------------------------------------Shared part--------------------------------------------------------
import math
import os
import time
from collections import defaultdict, Counter
from sys import stdin, maxsize, stdout

inp = lambda: stdin.readline().strip()
iinp = lambda: int(inp())
intl = lambda: list(map(int, inp().split()))
strl = lambda: list(inp().split())
list_to_string = lambda _a: "".join(map(str, _a))
list_to_string_list = lambda _a: " ".join(map(str, _a))
_dp = lambda default_value: defaultdict(lambda: default_value)
flush = lambda: stdout.flush()
print_flush = lambda _text: (print(_text), flush())
fact = lambda number: math.factorial(number)
cnt = lambda _a: Counter(_a)


def lcm(a, b):
    return a * b // math.gcd(a, b)


def print_dp(_dict):
    for item in _dict.items():
        print(f"{item[0]} = {item[1]}")


MOD = 10 ** 9 + 7
INF = maxsize
A = 911382323
M = 9999999999879998


# -------------------------------------------------------Solution-------------------------------------------------------

def solve_1():
    s, n = intl()

    levels = []

    for i in range(n):
        levels.append(intl())

    levels = sorted(levels, key=lambda x: (x[1]), reverse=True)

    stop = False

    while not stop:
        stop = True
        new_levels = []

        for i in range(n):
            strength, bonus = levels[i]

            if s > strength:
                s += bonus
                stop = False
            else:
                new_levels.append(levels[i])

        levels = new_levels
        n = len(levels)

    if n == 0:
        return "YES"

    return "NO"


def solve_2():
    s, n = intl()

    levels = []

    for i in range(n):
        levels.append(intl())

    levels = sorted(levels)

    for i in range(n):
        if s <= levels[i][0]:
            return "NO"

        s += levels[i][1]

    return "YES"


def run():
    print(solve_2())


if __name__ == "__main__":
    if os.environ.get("DEBUG_CODEFORCES"):
        stdin = open("../../input.txt", "r")
        start_time = time.time()
        run()
        print("\n--- %s seconds ---\n" % (time.time() - start_time))
    else:
        run()
