# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/1451/problem/B
# Title  : Non-Substring Subsequence
# Tags   : tag-codeforces, tag-problem-B, tag-div-2, tag-difficulty-900
# Notes  : dp, greedy, implementation, strings
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
    n, q = intl()
    s = list(inp())

    for i in range(q):
        l, r = intl()
        left_s = s[:l - 1]
        right_s = s[r:]

        if s[l - 1] in left_s:
            print("YES")
            continue

        if s[r - 1] in right_s:
            print("YES")
            continue

        print("NO")


def run():
    t = iinp()

    for _ in range(t):
        solve()


if __name__ == "__main__":
    if os.environ.get("DEBUG_CODEFORCES"):
        stdin = open("../../input.txt", "r")
        start_time = time.time()
        run()
        print("\n--- %s seconds ---\n" % (time.time() - start_time))
    else:
        run()
