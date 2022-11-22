# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/1739/problem/B
# Title  : Array Recovery
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
list_to_string = lambda _a: " ".join(map(str, _a))

MOD = 10 ** 9 + 7
INF = maxsize


# -------------------------------------------------------Solution-------------------------------------------------------

def solve():
    n = iinp()
    d = intl()

    a = [d[0]]

    for i in range(1, n):
        if a[i - 1] - d[i] >= 0 and a[i - 1] - d[i] != d[i] + a[i - 1]:
            return -1

        a.append(d[i] + a[i - 1])

    return list_to_string(a)


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
