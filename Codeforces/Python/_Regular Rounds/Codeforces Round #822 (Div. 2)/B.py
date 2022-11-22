# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/1734/problem/B
# Title  : Bright, Nice, Brilliant
# Tags   : tag-codeforces, tag-problem-B, tag-div-2
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

    print(1)
    for i in range(1, n):
        for x in ["1"] + ["0"] * (i - 1) + ["1"]:
            print(x, end=" ")
        print()


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
