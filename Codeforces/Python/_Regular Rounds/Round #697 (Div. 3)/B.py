# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/1475/problem/B
# Title  : New Year's Number
# Tags   : tag-codeforces, tag-problem-B, tag-div-3
# ---------------------------------------------------------------------------------------

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
    t = iinp()

    dp = _dp(0)
    dp[2020] = 1
    dp[2021] = 1

    for i in range(2022, 1000001):
        dp[i] = dp[i - 2020] | dp[i - 2021]

    for _ in range(t):
        n = iinp()

        if dp[n] == 1:
            print("YES")
        else:
            print("NO")


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
