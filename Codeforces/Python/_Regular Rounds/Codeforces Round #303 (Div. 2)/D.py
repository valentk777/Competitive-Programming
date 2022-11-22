# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/545/problem/D
# Title  : Queue
# Tags   : tag-codeforces, tag-problem-D, tag-div-2, tag-difficulty-1300
# Notes  : greedy, implementation, sortings
# ---------------------------------------------------------------------------------------

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
list_to_string_List = lambda _a: " ".join(map(str, _a))
_dp = lambda default_value: defaultdict(lambda: default_value)

MOD = 10 ** 9 + 7
INF = maxsize


# -------------------------------------------------------Solution-------------------------------------------------------

def solve():
    n = iinp()
    a = intl()
    a = sorted(a)

    _count = 0
    _sum = 0
    for i in range(n):
        if a[i] >= _sum:
            _count += 1
            _sum += a[i]

    return _count


def run():
    print(solve())


if __name__ == "__main__":
    if os.environ.get("DEBUG_CODEFORCES"):
        stdin = open("../../input.txt", "r")
        start_time = time.time()
        run()
        print("\n--- %s seconds ---\n" % (time.time() - start_time))
    else:
        run()
