# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/455/problem/A
# Title  : Boredom
# Tags   : tag-codeforces, tag-problem-A, tag-div-1
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

    _max = max(a)

    _count = [0 for _ in range(_max + 1)]

    for i in range(n):
        _count[a[i]] += 1

    # max value until i-th
    dp = [-1 for i in range(_max + 1)]
    dp[0] = 0
    dp[1] = _count[1]

    for i in range(2, _max + 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + (i * _count[i]))

    return dp[_max]


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
