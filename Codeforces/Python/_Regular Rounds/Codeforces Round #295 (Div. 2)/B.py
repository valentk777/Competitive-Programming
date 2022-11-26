# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/520/problem/B
# Title  : Two Buttons
# Tags   : tag-codeforces, tag-problem-B, tag-div-2, tag-difficulty-1400
# Notes  : dfs and similar, graphs, greedy, implementation, math, shortest paths
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
    n, m = intl()
    ans = 0

    while m != n:
        if m < n:
            m += 1
        elif m % 2 == 0:
            m //= 2
        else:
            m += 1

        ans += 1

    return ans


def solve_2():
    n, m = intl()

    if n >= m:
        return n - m

    ats = 0

    while m > n:
        if m % 2 == 1:
            m += 1
            ats += 1
            continue

        new_m = m // 2

        if new_m > n:
            ats += 1
            m = new_m
        else:
            if n - new_m < 2 * n - m:
                ats += n - new_m + 1
            else:
                ats += 2 * n - m + 1

            m = n
            break

    ats += abs(n - m)

    return ats


def run():
    print(solve())


if __name__ == "__main__":
    if os.environ.get("DEBUG_CODEFORCES"):
        stdin = open("../../input.txt", "r")
        start_time = time.time()
        run()
        print("\n--- %s seconds ---\n" % (time.time() - start_time))
    else:
        run()
