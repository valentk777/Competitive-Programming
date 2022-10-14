# -----------------------------------------------------------
# URL    : https://codeforces.com/contest/1343/problem/C
# Title  : Alternating Subsequence
# Notes  : tag-codeforces, tag-problem-C, tag-div-3
# -----------------------------------------------------------

# ---------------------------------------------------Shared part--------------------------------------------------------
import os
import time
from collections import defaultdict
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
    n = iinp()
    a = intl()

    _sum = a[0]
    current = a[0]
    is_positive = current > 0

    for i in range(1, n):
        if a[i] > 0:
            if is_positive:
                _sum -= current
                current = max(current, a[i])
            else:
                current = a[i]
                is_positive = True
        else:
            if is_positive:
                current = a[i]
                is_positive = False
            else:
                _sum -= current
                current = max(current, a[i])

        _sum += current

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
