# -----------------------------------------------------------
# URL    : https://codeforces.com/contest/279/problem/B
# Title  : B. Books
# Notes  : tag-codeforces, tag-problem-B, tag-div-2
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

def solve():
    n, t = intl()
    a = intl()

    if n == 1:
        if t >= a[0]:
            return 1
        else:
            return 0

    left = 0
    right = 0
    _sum = 0
    _max = 0

    while left < n and right < n:
        _current = right - left + 1
        _sum += a[right]

        if _sum <= t:
            _max = max(_max, _current)
            right += 1
        else:
            _sum -= a[left]
            left += 1
            right += 1

    return _max


def solve_2():
    n, t = intl()
    a = intl()

    left = 0
    _sum = 0
    _max = 0

    for i in range(n):
        _sum += a[i]

        while _sum > t:
            _sum -= a[left]
            left += 1

        _max = max(_max, i - left + 1)

    return _max


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
