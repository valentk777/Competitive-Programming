# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/1754/problem/B
# Title  : Kevin and Permutation
# Tags   : tag-codeforces, tag-problem-B, tag-div-2, tag-difficulty-800
# Notes  : constructive algorithms, greedy, math
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

def generate_list_with_step_n(n, step):
    a = list(range(1, n + 1))
    ans = [-1 for _ in range(n)]

    ans[0] = a[step]
    a[step] = -1

    ans_i = 1
    i = 0
    left = n - 1

    while left > 0:
        if a[i] != -1:
            ans[ans_i] = a[i]
            a[i] = -1
            ans_i += 1
            left -= 1
        else:
            i += 1
            continue

        i = (i + step) % n

    return ans


def solve():
    n = iinp()

    mid = int(ceil((n + 1) / 2) - 1)
    a = generate_list_with_step_n(n, mid)
    return list_to_string_list(a)


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
