# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/1734/problem/C
# Title  : Removing Smallest Multiples
# Tags   : tag-codeforces, tag-problem-C, tag-div-2, tag-difficulty-1200
# Notes  : greedy, math
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
    t = list(inp())

    possible = {i + 1: False for i in range(n) if t[i] == "0"}

    _sum = 0
    for e in possible:
        if not possible[e]:
            _sum += e
            possible[e] = True

        for i in range(2, INF):
            if e * i in possible:
                if not possible[e * i]:
                    _sum += e
                    possible[e * i] = True
            else:
                break

    return _sum


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
