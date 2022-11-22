# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/158/problem/B
# Title  : Taxi
# Tags   : tag-codeforces, tag-problem-B, tag-difficulty-1100
# Notes  : *special, greedy, implementation
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


# -------------------------------------------------------Solution-------------------------------------------------------

def solve():
    n = iinp()
    s = intl()

    childrens = _dp(0)

    for i in range(n):
        childrens[s[i]] += 1

    ans = childrens[4] + childrens[3] + (childrens[2] // 2)
    childrens[1] -= min(childrens[3], childrens[1])

    if childrens[2] & 1 == 1:
        if childrens[1] > 0:
            childrens[1] -= min(childrens[1], 2)

        ans += 1

    ans += ceil(childrens[1] / 4)

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
