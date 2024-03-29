# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/1474/problem/B
# Title  : Different Divisors
# Tags   : tag-codeforces, tag-problem-B, tag-div-2, tag-difficulty-1000
# Notes  : binary search, constructive algorithms, greedy, math, number theory
# ---------------------------------------------------------------------------------------

# ---------------------------------------------------Shared part--------------------------------------------------------
import os
import time
from collections import defaultdict
from math import sqrt
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


def print_dp(_dict):
    for item in _dict.items():
        print(f"{item[0]} = {item[1]}")


MOD = 10 ** 9 + 7
INF = maxsize
A = 911382323
M = 9999999999879998


# -------------------------------------------------------Solution-------------------------------------------------------
def is_prime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if (n % i) == 0:
            return False
    return True


def solve():
    d = iinp()

    a = 1

    candidate = d + 1

    while not is_prime(candidate):
        candidate += 1

    a *= candidate

    candidate += d

    while not is_prime(candidate):
        candidate += 1

    a *= candidate

    return a


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
