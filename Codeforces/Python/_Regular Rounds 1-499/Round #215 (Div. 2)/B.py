# -----------------------------------------------------------
# URL    : https://codeforces.com/contest/368/problem/B
# Title  : Sereja and Suffixes
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
    n, m = intl()
    a = intl()

    dp = _dp(0)
    find = _dp(0)
    dp[n] = 0

    for i in range(n - 1, -1, -1):
        if find[a[i]] == 0:
            dp[i] = dp[i + 1] + 1
            find[a[i]] += 1
        else:
            dp[i] = dp[i + 1]

    for i in range(m):
        l = iinp()
        print(dp[l - 1])


def run():
    solve()


if __name__ == "__main__":
    if os.environ.get("DEBUG_CODEFORCES"):
        stdin = open("../../input.txt", "r")
        start_time = time.time()
        run()
        print("\n--- %s seconds ---\n" % (time.time() - start_time))
    else:
        run()
