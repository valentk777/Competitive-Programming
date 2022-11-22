# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/580/problem/A
# Title  : Kefa and First Steps
# Tags   : tag-codeforces, tag-problem-A, tag-div-2
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
    a = intl()

    dp = [[0, -1] for _ in range(n + 1)]  # max value / value itself
    dp[0] = [0, 0]

    for i in range(1, n + 1):
        if dp[i - 1][1] <= a[i - 1]:
            dp[i] = [dp[i - 1][0] + 1, a[i - 1]]
        else:
            dp[i] = [1, a[i - 1]]

    return max([i[0] for i in dp])


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
