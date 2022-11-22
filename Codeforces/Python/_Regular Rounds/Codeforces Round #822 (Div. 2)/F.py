# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/1734/problem/F
# Title  : Zeros and Ones
# Tags   : tag-codeforces, tag-problem-F, tag-div-2, tag-difficulty-2500, tag-not-pass
# Notes  : bitmasks, divide and conquer, dp, math
# ---------------------------------------------------------------------------------------

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


_s = ["01"]
_s_len = 1
_max_number = 2


def invert_bits(number):
    return "".join(["1" if i == "0" else "0" for i in number])


def hamming_distance(a, b, n):
    _sum = 0

    for i in range(n):
        if a[i] != b[i]:
            _sum += 1

    return _sum
    # return (a ^ b).bit_count()


def precompute(until=10 ** 18):
    global _s, _s_len, _max_number

    while _max_number < until:
        _s.append(_s[-1] + invert_bits(_s[-1]))
        _s_len += 1
        _max_number <<= 1


def solve():
    x = 10
    print(bin(10))

    n, m = intl()

    precompute(n + m)

    dist = hamming_distance(_s[-1][:m], _s[-1][n:n + m], m)
    return dist


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
