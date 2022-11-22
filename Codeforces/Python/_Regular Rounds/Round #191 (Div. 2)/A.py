# -----------------------------------------------------------
# URL    : https://codeforces.com/contest/327/problem/A
# Title  : A. Flipping Game
# Notes  : tag-codeforces, tag-problem-A, tag-div-2
# -----------------------------------------------------------

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

# Largest Sum Contiguous Subarray (Kadane’s Algorithm)
def solve():
    n = iinp()
    a = intl()

    b = []

    for i in range(n):
        if a[i] == 1:
            b.append(-1)
        else:
            b.append(1)

    dp = _dp(0)

    for i in range(n):
        if a[i] == 0:
            dp[i] = dp[i - 1] + 1
        else:
            dp[i] = dp[i - 1] - 1

    max_so_far = -INF
    max_ending_here = 0
    start = 0
    end = 0
    s = 0

    for i in range(n):
        max_ending_here += b[i]

        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            start = s
            end = i

        if max_ending_here < 0:
            max_ending_here = 0
            s = i + 1

    if max_so_far > 0:
        return sum(a[:start]) + a[start:end + 1].count(0) + sum(a[end + 1:])
    else:
        return sum(a) - 1


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
