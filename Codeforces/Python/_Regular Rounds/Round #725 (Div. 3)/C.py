# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/1538/problem/C
# Title  : C. Number of Pairs
# Tags   : tag-codeforces, tag-problem-C, tag-div-3
# ---------------------------------------------------------------------------------------

# ---------------------------------------------------Shared part--------------------------------------------------------
import os
import time
from bisect import bisect_left, bisect_right
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

# wrong answer
def solve_wrong():
    n, l, r = intl()
    a = intl()
    a = sorted(filter(lambda x: x <= r, a))
    n = len(a)

    i = 0
    j = n - 1

    while i < j:
        if a[i] + a[j] < l:
            i += 1
        elif a[i] + a[j] > r:
            j -= 1
        else:
            break

    if i == j:
        return 0

    a = a[i:j + 1]

    n = len(a)

    if n == 2:
        return 1

    ans = 0

    # binary search
    # find max range from every a[i] until end
    for i in range(n - 1):
        left = i
        right = n - 1
        min_l = 0

        while left <= right:
            min_l = (left + right) // 2

            if l <= a[i] + a[min_l]:
                right = min_l - 1
            else:
                left = min_l + 1

        if min_l == i:
            min_l += 1

        # full range okay, so we need to find a[i] -> a[?] where sum will be too small
        if a[i] + a[n - 1] <= r:
            ans += n - min_l
            continue

        left = min_l
        right = n - 1
        max_r = 0

        while left <= right:
            max_r = (left + right) // 2

            if a[i] + a[max_r] > r:
                right = max_r - 1
            else:
                left = max_r + 1

        ans += max_r - min_l

    return ans


# optional
def shorted_array(a, n, l, r):
    i = 0
    j = n - 1

    while i < j:
        if a[i] + a[j] < l:
            i += 1
        elif a[i] + a[j] > r:
            j -= 1
        else:
            break

    return a[i:j + 1]


def solve_with_array_shortening():
    n, l, r = intl()
    a = intl()

    a = sorted(a)

    # optional
    a = shorted_array(a, n, l, r)
    n = len(a)

    if n < 2:
        return 0

    if n == 2:
        return 1

    ans = 0

    # binary search
    for i in range(n):
        min_l = bisect_left(a, l - a[i])
        min_l = max(i + 1, min_l)
        max_r = bisect_right(a, r - a[i])

        if max_r > min_l:
            ans += (max_r - min_l)

    return ans


def solve():
    n, l, r = intl()
    a = intl()

    a = sorted(a)
    ans = 0

    for i in range(n):
        min_l = bisect_left(a, l - a[i])
        min_l = max(i + 1, min_l)
        max_r = bisect_right(a, r - a[i])

        if max_r > min_l:
            ans += (max_r - min_l)

    return ans


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
