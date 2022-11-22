# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/492/problem/B
# Title  : Vanya and Lanterns
# Tags   : tag-codeforces, tag-problem-B, tag-div-2, tag-difficulty-1200
# Notes  : binary search, implementation, math, sortings
# ---------------------------------------------------------------------------------------

# ---------------------------------------------------Shared part--------------------------------------------------------
import os
import time
from collections import defaultdict
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
    n, l = intl()
    a = intl()
    a = sorted(a)

    diffs = []

    for i in range(1, n):
        diffs.append(a[i] - a[i - 1])

    ans = max(a[0], l - a[-1])

    if diffs:
        return max(ans, max(diffs) / 2)
    else:
        return ans


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
