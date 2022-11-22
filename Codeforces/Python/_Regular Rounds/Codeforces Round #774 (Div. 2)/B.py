# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/1646/problem/B
# Title  : Quality vs Quantity
# Tags   : tag-codeforces, tag-problem-B, tag-div-2, tag-difficulty-800
# Notes  : brute force, constructive algorithms, greedy, sortings, two pointers
# ---------------------------------------------------------------------------------------

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

def solve_2():
    n = iinp()
    a = intl()
    a = sorted(a)

    count_r = n // 2
    count_b = n - count_r

    if count_r == count_b:
        count_r -= 1

    if sum(a[:count_b]) < sum(a[-count_r:]):
        return "YES"
    else:
        return "NO"


def solve():
    n = iinp()
    a = intl()
    a = sorted(a)

    count_r = n // 2
    count_b = n - count_r

    if count_r == count_b:
        count_r -= 1

    left = 0
    right = n - 1

    sum_r = 0
    sum_b = 0
    stop = False

    while left <= right and not stop:
        if left < count_b:
            sum_b += a[left]
            left += 1
            stop = False
        else:
            stop = True

        if n - right - 1 < count_r:
            sum_r += a[right]
            right -= 1
            stop = False
        else:
            stop = stop and True

    if sum_r > sum_b:
        return "YES"
    else:
        return "NO"


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
