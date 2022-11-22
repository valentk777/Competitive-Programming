# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/1692/problem/D
# Title  : The Clock
# Tags   : tag-codeforces, tag-problem-D, tag-div-4, tag-difficulty-1100
# Notes  : brute force, implementation
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
    s, x = inp().split()
    x = int(x)

    candidates = [s]

    h, m = list(map(int, s.split(":")))
    start = s

    for step in range(x, INF, x):
        hours = (((m + step) // 60) + h) % 24
        minutes = (m + step) % 60

        new_time = f"{hours:02d}:{minutes:02d}"

        if new_time != start:
            candidates.append(new_time)
        else:
            break

    ans = 0

    for c in candidates:
        if c[0] == c[-1] and c[1] == c[-2]:
            ans += 1

    return ans


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
