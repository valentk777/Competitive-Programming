# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/1566/problem/C
# Title  : MAX-MEX Cut
# Tags   : tag-codeforces, tag-problem-C, tag-difficulty-1000
# Notes  : bitmasks, constructive algorithms, dp, greedy
# ---------------------------------------------------------------------------------------
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
    a = list(inp())
    b = list(inp())
    c = []

    for i in range(n):
        if a[i] + b[i] == "01" or a[i] + b[i] == "10":
            c.append(2)
        elif a[i] + b[i] == "00":
            c.append(1)
        else:
            c.append(0)

    dp = _dp(0)
    dp[0] = c[0]

    for i in range(1, n):
        dp[i] = dp[i - 1] + c[i]

        if c[i - 1] + c[i] == 1:
            dp[i] += 1
            c[i] = 2

    return dp[n - 1]


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
