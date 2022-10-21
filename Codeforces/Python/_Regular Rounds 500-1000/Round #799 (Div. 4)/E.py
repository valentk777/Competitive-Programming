# -----------------------------------------------------------
# URL    : https://codeforces.com/contest/1692/problem/E
# Title  : E. Binary Deque
# Notes  : tag-codeforces, tag-problem-E, tag-div-4
# -----------------------------------------------------------

# ---------------------------------------------------Shared part--------------------------------------------------------
import os
import time
from collections import defaultdict
from sys import stdin, maxsize, stdout

inp = lambda: stdin.readline().strip()
iinp = lambda: int(inp())
intl = lambda: list(map(int, inp().split()))
strl = lambda: list(inp().split())
list_to_string = lambda _a: "".join(map(str, _a))
list_to_string_list = lambda _a: " ".join(map(str, _a))
_dp = lambda default_value: defaultdict(lambda: default_value)
flush = lambda: stdout.flush()
print_flush = lambda _text: (print(_text), flush())


def print_dp(_dict):
    for item in _dict.items():
        print(f"{item[0]} = {item[1]}")


MOD = 10 ** 9 + 7
INF = maxsize
A = 911382323
M = 9999999999879998


# -------------------------------------------------------Solution-------------------------------------------------------

# Time limit exceeded
# two pointers
def solve_slow():
    n, s = intl()
    a = intl()
    sum_a = sum(a)

    if sum_a < s:
        return -1

    if sum_a == s:
        return 0

    i = 0
    j = 1

    _min = INF

    while i < n:
        while j <= n:
            _sum = sum(a[i: j])
            if _sum == s:
                _min = min(_min, n - (j - i))
            if _sum > s:
                break

            j += 1
        i += 1

    return _min


# same two pointers but with optimised sum calculation. PASS!!
def solve():
    n, s = intl()
    a = intl()
    sum_a = sum(a)

    if sum_a < s:
        return -1

    if sum_a == s:
        return 0

    i = 0
    j = 1

    _min = INF

    _sum = sum(a[i: j])

    while i < n:
        while j <= n:

            if _sum == s:
                _min = min(_min, n - (j - i))
            if _sum > s:
                break

            j += 1

            if j <= n:
                _sum += a[j - 1]

        _sum -= a[i]
        i += 1

    return _min


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
