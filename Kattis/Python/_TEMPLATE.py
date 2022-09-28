# -----------------------------------------------------------
# URL    : https://open.kattis.com/problems/xxxxx
# Title  : TEXT
# Notes  : tag-kattis
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
    pass


def run():
    solve()


def run():
    t = iinp()

    for _ in range(t):
        solve()


def run():
    try:
        while True:
            print(solve())
    except:
        pass


if __name__ == "__main__":
    if os.environ.get("DEBUG_CODEFORCES"):
        stdin = open("input.txt", "r")
        start_time = time.time()
        run()
        print("\n--- %s seconds ---\n" % (time.time() - start_time))
    else:
        run()
