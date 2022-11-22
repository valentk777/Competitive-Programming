# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/1759/problem/D
# Title  : D. Make It Round
# Tags   : tag-codeforces, tag-problem-D, tag-div-3
# ---------------------------------------------------------------------------------------

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


def get_2_and_5_count(n):
    _counts = defaultdict(int)

    while n % 2 == 0:
        _counts[2] += 1
        n //= 2

    while n % 5 == 0:
        _counts[5] += 1
        n //= 5

    return _counts


def solve():
    n, m = intl()

    _counts = get_2_and_5_count(n)
    ans = 1

    if _counts[2] > _counts[5]:
        while _counts[2] > _counts[5]:
            if ans * 5 > m:
                break

            ans *= 5
            _counts[5] += 1

    elif _counts[2] < _counts[5]:
        while _counts[2] < _counts[5]:
            if ans * 2 > m:
                break

            ans *= 2
            _counts[2] += 1

    while ans * 10 <= m:
        ans *= 10

    return (m // ans) * n * ans


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
