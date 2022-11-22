# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/1759/problem/C
# Title  : C. Thermostat
# Tags   : tag-codeforces, tag-problem-C, tag-div-3
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

def solve():
    l, r, x = intl()
    a, b = intl()

    if a == b:
        return 0

    l_a = abs(a - l)
    r_a = abs(a - r)
    l_b = abs(b - l)
    r_b = abs(b - r)

    if l_a < x and r_a < x:
        return -1

    if l_b < x and r_b < x:
        return -1

    if abs(a - b) >= x:
        return 1

    if l_a >= x and l_b >= x:
        return 2

    if r_a >= x and r_b >= x:
        return 2

    if l_a >= x and r_b >= x:
        return 3

    if l_a >= x and r_b >= x:
        return 3

    if l_b >= x and r_a >= x:
        return 3

    return -1


def run():
    t = iinp()

    for _ in range(t):
        print(solve())


if __name__ == "__main__":
    if os.environ.get("DEBUG_CODEFORCES"):
        stdin = open("../../input.txt", "r")
        start_time = time.time()
        run()
        print("\n--- %s seconds ---\n" % (time.time() - start_time))
    else:
        run()
