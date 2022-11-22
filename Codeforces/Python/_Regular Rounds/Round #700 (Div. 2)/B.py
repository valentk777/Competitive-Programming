# -----------------------------------------------------------
# URL    : https://codeforces.com/contest/1480/problem/B
# Title  : The Great Hero
# Notes  : tag-codeforces, tag-problem-B, tag-div-2
# -----------------------------------------------------------

# ---------------------------------------------------Shared part--------------------------------------------------------
import os
import time
from math import ceil
from sys import stdin, maxsize

inp = lambda: stdin.readline().strip()
iinp = lambda: int(inp())
intl = lambda: list(map(int, inp().split()))
strl = lambda: list(inp().split())

MOD = 10 ** 9 + 7
INF = maxsize


# -------------------------------------------------------Solution-------------------------------------------------------

def solve():
    a, b, n = intl()
    a_i = intl()
    b_i = intl()

    all_damage = sum(a_i[i] * ceil(b_i[i] / a) for i in range(n))

    b -= all_damage

    if b > 0:
        return "YES"

    # if hero alive after all damage except any of monster damage, then hero can select that monster as a last one
    # and dead alter the last monster hit
    for i in range(n):
        if b + a_i[i] > 0:
            return "YES"

    return "NO"


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
