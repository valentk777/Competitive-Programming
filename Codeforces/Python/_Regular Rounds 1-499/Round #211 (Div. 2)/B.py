# -----------------------------------------------------------
# URL    : https://codeforces.com/contest/363/problem/B
# Title  : Fence
# Notes  : tag-codeforces, tag-problem-B, tag-div-2
# -----------------------------------------------------------

# ---------------------------------------------------Shared part--------------------------------------------------------
import os
import time
from collections import defaultdict
from sys import stdin, maxsize

inp = lambda: stdin.readline().strip()
iinp = lambda: int(inp())
intl = lambda: list(map(int, inp().split()))
strl = lambda: list(inp().split())
list_to_string = lambda _a: " ".join(map(str, _a))
_dp = lambda default_value: defaultdict(lambda: default_value)

MOD = 10 ** 9 + 7
INF = maxsize


# -------------------------------------------------------Solution-------------------------------------------------------

def solve():
    n, k = intl()
    h = intl()

    sums = _dp(-INF)
    sums[0] = 0

    for i in range(1, n + 1):
        sums[i] = sums[i - 1] + h[i - 1]

    dp = _dp(INF)

    _min = INF
    _min_idx = -1

    for i in range(k, n + 1):
        dp[i] = sums[i] - sums[i - k]

    return list(dp.values()).index(min(dp.values())) + 1


def run():
    print(solve())


if __name__ == "__main__":
    if os.environ.get("DEBUG_CODEFORCES"):
        stdin = open("../input.txt", "r")
        start_time = time.time()
        run()
        print("\n--- %s seconds ---\n" % (time.time() - start_time))
    else:
        run()
