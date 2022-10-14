# -----------------------------------------------------------
# URL    : https://codeforces.com/contest/1730/problem/E
# Title  : Maximums and Minimums
# Notes  : tag-codeforces, tag-problem-E, tag-div-2, tag-not-pass
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

def solve_slow():
    n = iinp()
    a = list(intl())
    count = 0

    for i in range(n):
        _min = a[i]
        _max = a[i]

        for j in range(i, n):
            if _min > a[j]:
                _min = a[j]

            if _max < a[j]:
                _max = a[j]

            if _max % _min == 0:
                count += 1

    return count


def solve():
    pass


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
