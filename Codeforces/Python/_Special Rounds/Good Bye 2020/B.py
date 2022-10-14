# -----------------------------------------------------------
# URL    : https://codeforces.com/contest/1466/problem/B
# Title  : Last minute enhancements
# Notes  : tag-codeforces, tag-problem-B, tag-div-2
# -----------------------------------------------------------

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
    x = intl()

    # maybe it's already sorted?
    x = sorted(x)

    # number of diff elements
    dp = [0 for _ in range(n + 1)]
    dp[0] = 0
    dp[1] = 1

    for i in range(1, n):
        if x[i - 1] < x[i]:
            dp[i + 1] = dp[i] + 1
        elif x[i - 1] == x[i]:
            x[i] += 1
            dp[i + 1] = dp[i] + 1
        else:
            x[i] += 1
            dp[i + 1] = dp[i]

    return dp[n]


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
