# -----------------------------------------------------------
# URL    : https://open.kattis.com/problems/flipflow
# Title  : Flip Flow
# Notes  : tag-kattis, tag-easy
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
    t, s, n = intl()
    a = intl()

    flip_time = a[0]
    half_top = s
    half_bottom = 0

    for i in range(1, n):
        duration = a[i] - flip_time
        half_top, half_bottom = min(s, half_bottom + duration), max(0, half_top - duration)
        flip_time = a[i]

    duration = t - flip_time
    print(max(0, half_top - duration))


def run():
    solve()


if __name__ == "__main__":
    if os.environ.get("DEBUG_CODEFORCES"):
        stdin = open("../input.txt", "r")
        start_time = time.time()
        run()
        print("\n--- %s seconds ---\n" % (time.time() - start_time))
    else:
        run()
