# -----------------------------------------------------------
# URL    : https://codeforces.com/contest/433/problem/A
# Title  : Kitahara Haruki's Gift
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
    n = inp()
    w = intl()

    count = {100: 0, 200: 0}
    _sum = 0

    for i in w:
        count[i] += 1
        _sum += i

    if count[200] & 1 == 0:
        if count[100] & 1 == 0:
            return "YES"
        else:
            return "NO"

    if count[100] < 1 or count[100] & 1 == 1:
        return "NO"

    return "YES"


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
