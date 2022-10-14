# -----------------------------------------------------------
# URL    : https://codeforces.com/gym/100781
# Title  : Disastrous Downtime
# Notes  : tag-codeforces, tag-problem-D
# -----------------------------------------------------------

# ---------------------------------------------------Shared part--------------------------------------------------------
import os
import time
from collections import defaultdict
from math import ceil
from sys import stdin, maxsize

inp = lambda: stdin.readline().strip()
iinp = lambda: int(inp())
intl = lambda: list(map(int, inp().split()))
strl = lambda: list(inp().split())
list_to_string = lambda _a: " ".join(map(str, _a))
_dp = lambda default_value: defaultdict(lambda: default_value)

MOD = 10 ** 9 + 7
INF = maxsize


# -------------------------------------------------------Solution-------------------------------------------------------

def solve():
    n, k = intl()

    _handling = [0 for _ in range(100000 + 1000)]

    for _ in range(n):
        t = iinp()

        for i in range(t, t + 1000):
            _handling[i] += 1

    return ceil(max(_handling) / k)


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
