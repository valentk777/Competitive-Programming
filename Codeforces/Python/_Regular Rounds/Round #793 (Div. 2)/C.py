# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/1682/problem/C
# Title  : C. LIS or Reverse LIS?
# Tags   : tag-codeforces, tag-problem-C, tag-div-2
# ---------------------------------------------------------------------------------------

# ---------------------------------------------------Shared part--------------------------------------------------------
import os
import time
from collections import defaultdict
from math import ceil
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

def solve():
    n = iinp()
    a = intl()
    a = sorted(a)

    increasing_n = 1
    duplicate_n = 0
    skip = 0
    current = a[0]
    last_duplicate = None

    for i in range(1, n):
        if a[i] == current:
            if last_duplicate is None:
                duplicate_n += 1
                last_duplicate = a[i]
            else:
                skip += 1
        else:
            increasing_n += 1
            current = a[i]
            last_duplicate = None

    if abs(increasing_n - duplicate_n) < 2:
        return max(increasing_n, duplicate_n)
    else:
        return ceil((increasing_n + duplicate_n) / 2)


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
