# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/1360/problem/C
# Title  : Similar Pairs
# Tags   : tag-codeforces, tag-problem-C, tag-div-3, tag-difficulty-1100
# Notes  : constructive algorithms, graph matchings, greedy, sortings
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
    n = iinp()
    a = intl()
    a = sorted(a)

    mod_a = list(map(lambda x: x % 2, a))

    _count = cnt(mod_a)

    if _count[0] % 2 == 0 and _count[1] % 2 == 0:
        return "YES"

    if (_count[0] % 2 == 1 and _count[1] % 2 == 0) or (_count[0] % 2 == 0 and _count[1] % 2 == 1):
        return "NO"

    for i in range(n - 1):
        if a[i + 1] - a[i] == 1:
            return "YES"

    return "NO"


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
