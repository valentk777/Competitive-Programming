# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/1462/problem/A
# Title  : Favorite Sequence
# Tags   : tag-codeforces, tag-problem-A, tag-div-3, tag-difficulty-800
# Notes  : implementation, two pointers
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
    n = iinp()
    b = intl()
    a = []

    left = 0
    right = n - 1

    while left <= right:
        a.append(b[left])
        left += 1

        if left < right:
            a.append(b[right])
            right -= 1

    return a


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
