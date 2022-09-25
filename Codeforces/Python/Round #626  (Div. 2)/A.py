# -----------------------------------------------------------
# URL    : https://codeforces.com/contest/1323/problem/A
# Title  : Even Subset Sum Problem
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
    n = iinp()
    a = intl()

    if n == 1 and a[0] & 1 != 0:
        print(-1)
        return

    for i in range(n):
        if a[i] & 1 == 0:
            print(1)
            print(i + 1)
            return

        if i > 0:
            print(2)
            print(1, 2)
            return

    print()


def run():
    t = iinp()

    for _ in range(t):
        solve()


if __name__ == "__main__":
    if os.environ.get("DEBUG_CODEFORCES"):
        stdin = open("../input.txt", "r")
        start_time = time.time()
        run()
        print("\n--- %s seconds ---\n" % (time.time() - start_time))
    else:
        run()
