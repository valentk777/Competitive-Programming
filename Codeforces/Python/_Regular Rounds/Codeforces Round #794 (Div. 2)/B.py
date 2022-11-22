# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/1686/problem/B
# Title  : Odd Subarrays
# Tags   : tag-codeforces, tag-problem-B, tag-div-2, tag-difficulty-800
# Notes  : dp, greedy
# ---------------------------------------------------------------------------------------

# ---------------------------------------------------Shared part--------------------------------------------------------
import os
import time
from sys import stdin, maxsize

inp = lambda: stdin.readline().strip()
iinp = lambda: int(inp())
intl = lambda: list(map(int, inp().split()))
strl = lambda: list(inp().split())

MOD = 10 ** 9 + 7
INF = maxsize


# -------------------------------------------------------Solution-------------------------------------------------------

def solve():
    n = iinp()
    p = intl()

    # max number of splits
    dp = [-1 for _ in range(n + 1)]
    dp[0] = 0

    i = 1

    while i < n:
        if p[i - 1] > p[i]:
            dp[i] = dp[i - 1] + 1
            i += 1

        dp[i] = dp[i - 1]
        i += 1

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
