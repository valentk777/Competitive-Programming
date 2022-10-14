# -----------------------------------------------------------
# URL    : https://codeforces.com/contest/189/problem/A
# Title  : Cut Ribbon
# Notes  : tag-codeforces, tag-problem-A, tag-div-2
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
    n, a, b, c = intl()

    # f(i) max cuts for ribbon of length i
    dp = [-INF for _ in range(n + 1)]
    dp[0] = 0

    options = set()

    for o in [a, b, c]:
        if o <= n:
            options.add(o)
            dp[o] = 1

    for i in range(n + 1):
        for o in options:
            if i >= o:
                dp[i] = max(dp[i], dp[i - o] + 1)

    return dp[n]


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
