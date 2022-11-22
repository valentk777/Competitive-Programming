# -----------------------------------------------------------
# URL    : https://codeforces.com/contest/1485/problem/B
# Title  : B. Replace and Keep Sorted
# Notes  : tag-codeforces, tag-problem-B, tag-div-2
# -----------------------------------------------------------

# ---------------------------------------------------Shared part--------------------------------------------------------
import math
import os
import time
from collections import defaultdict, Counter
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
fact = lambda number: math.factorial(number)
cnt = lambda _a: Counter(_a)


def lcm(a, b):
    return a * b // math.gcd(a, b)


def print_dp(_dict):
    for item in _dict.items():
        print(f"{item[0]} = {item[1]}")


MOD = 10 ** 9 + 7
INF = maxsize
A = 911382323
M = 9999999999879998


# -------------------------------------------------------Solution-------------------------------------------------------

# counts for position except itself
def get_counts(a, k, n):
    _counts = [0 for _ in range(n + 1)]

    for i in range(1, n + 1):
        _counts[i] = a[i + 1] - a[i - 1] - 2

    return _counts


def get_sums(_counts, n):
    _sums = [0 for _ in range(n + 1)]
    _sum = 0

    for i in range(n + 1):
        _sum += _counts[i]
        _sums[i] = _sum

    return _sums


def solve():
    n, q, k = intl()
    a = [0] + intl() + [k + 1]
    _counts = get_counts(a, k, n)
    _sums = get_sums(_counts, n)

    for i in range(q):
        l, r = intl()

        range_sum = _sums[r] - _sums[l - 1]
        edges_count = _counts[l] + _counts[r]
        left_count = a[l + 1] - 2
        right_count = k - a[r - 1] - 1

        print(range_sum - edges_count + left_count + right_count)


def run():
    solve()


if __name__ == "__main__":
    if os.environ.get("DEBUG_CODEFORCES"):
        stdin = open("../../input.txt", "r")
        start_time = time.time()
        run()
        print("\n--- %s seconds ---\n" % (time.time() - start_time))
    else:
        run()
