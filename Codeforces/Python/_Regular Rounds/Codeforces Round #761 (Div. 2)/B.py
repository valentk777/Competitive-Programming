# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/1617/problem/B
# Title  : GCD Problem
# Tags   : tag-codeforces, tag-problem-B, tag-div-2, tag-difficulty-900
# Notes  : brute force, constructive algorithms, math, number theory
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


def print_dp(_dict):
    for item in _dict.items():
        print(f"{item[0]} = {item[1]}")


MOD = 10 ** 9 + 7
INF = maxsize
A = 911382323
M = 9999999999879998


# -------------------------------------------------------Solution-------------------------------------------------------

def solve():
    n = iinp()
    c = 1
    n -= c

    if n & 1 == 1:
        a = n // 2
        b = (n // 2) + 1

        return a, b, c

    mid = n // 2

    if mid & 1 == 0:
        return mid - 1, mid + 1, 1

    return mid - 2, mid + 2, 1


def run():
    t = iinp()

    for _ in range(t):
        print(*solve())


if __name__ == "__main__":
    if os.environ.get("DEBUG_CODEFORCES"):
        stdin = open("../../input.txt", "r")
        start_time = time.time()
        run()
        print("\n--- %s seconds ---\n" % (time.time() - start_time))
    else:
        run()
