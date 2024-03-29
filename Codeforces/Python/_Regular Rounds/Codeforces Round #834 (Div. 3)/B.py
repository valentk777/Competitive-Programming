# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/1759/problem/B
# Title  : Lost Permutation
# Tags   : tag-codeforces, tag-problem-B, tag-div-3, tag-difficulty-800
# Notes  : math
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
    m, s = intl()
    b = intl()
    _max = max(b)
    _sum = 0

    for i in range(1, _max):
        if i not in b:
            _sum += i

            if _sum > s:
                return "NO"

    if _sum == s:
        return "YES"

    for i in range(_max + 1, 100):
        _sum += i

        if _sum > s:
            return "NO"

        if _sum == s:
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
