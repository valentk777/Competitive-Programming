# -----------------------------------------------------------
# URL    : https://codeforces.com/contest/1447/problem/C
# Title  : Knapsack
# Notes  : tag-codeforces, tag-problem-C, tag-div-2
# -----------------------------------------------------------

# ---------------------------------------------------Shared part--------------------------------------------------------
import os
import time
from collections import defaultdict
from math import ceil
from sys import stdin, maxsize

inp = lambda: stdin.readline().strip()
iinp = lambda: int(inp())
intl = lambda: list(map(int, inp().split()))
strl = lambda: list(inp().split())
list_to_string = lambda _a: "".join(map(str, _a))
list_to_string_list = lambda _a: " ".join(map(str, _a))
_dp = lambda default_value: defaultdict(lambda: default_value)

MOD = 10 ** 9 + 7
INF = maxsize


# -------------------------------------------------------Solution-------------------------------------------------------

def solve():
    n, w = intl()
    a = intl()
    half_w = ceil(w / 2)

    aa = [(e, i + 1) for i, e in enumerate(a)]
    aa = filter(lambda x: x[0] <= w, aa)
    aa = sorted(aa, key=lambda x: x[0], reverse=True)

    if len(aa) == 0:
        print(-1)
        return

    if aa[-1][0] > w:
        print(-1)
        return

    if aa[0][0] >= half_w:
        print(1)
        print(aa[0][1])
        return

    items_to_pack = []
    total_sum = 0

    for i in range(len(aa)):
        items_to_pack.append(aa[i][1])
        total_sum += aa[i][0]

        if total_sum >= half_w:
            print(len(items_to_pack))
            print(list_to_string_list(items_to_pack))
            return

    print(-1)


def run():
    t = iinp()

    for _ in range(t):
        solve()


if __name__ == "__main__":
    if os.environ.get("DEBUG_CODEFORCES"):
        stdin = open("../input.txt", "r")
        start_time = time.time()
        run()
        print("\n--- %s seconds ---\n" % (time.time() - start_time))
    else:
        run()
