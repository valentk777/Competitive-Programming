# -----------------------------------------------------------
# URL    : https://codeforces.com/contest/489/problem/B
# Title  : BerSU Ball
# Notes  : tag-codeforces, tag-problem-B, tag-div-2
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
    a = sorted(a)

    m = iinp()
    b = intl()
    b = sorted(b)

    a_i = 0
    b_i = 0
    _count = 0

    while a_i < n and b_i < m:
        diff = abs(a[a_i] - b[b_i])

        if diff < 2:
            _count += 1
            a_i += 1
            b_i += 1
            continue

        if a[a_i] < b[b_i]:
            a_i += 1
            continue
        else:
            b_i += 1
            continue

    return _count


def run():
    print(solve())


if __name__ == "__main__":
    if os.environ.get("DEBUG_CODEFORCES"):
        stdin = open("../input.txt", "r")
        start_time = time.time()
        run()
        print("\n--- %s seconds ---\n" % (time.time() - start_time))
    else:
        run()
