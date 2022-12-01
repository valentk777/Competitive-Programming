# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/1692/problem/G
# Title  : 2^Sort
# Tags   : tag-codeforces, tag-problem-G, tag-div-4, tag-difficulty-1400
# Notes  : data structures, dp, sortings, two pointers
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

# time limit
def solve_slow():
    n, k = intl()
    a = intl()
    ans = 0

    for i in range(n - k):
        before = a[i]
        power = 1
        found = True

        for j in range(1, k + 1):
            power *= 2
            candidate = a[i + j] * power

            if before < candidate:
                before = candidate
            else:
                found = False
                break

        if found:
            ans += 1

    return ans


# too complex
def solve_no():
    n, k = intl()
    a = intl()
    ans = 0

    left = n - 2
    right = n - 1

    power = 2 ** k
    a[n - 1] *= power

    while 0 <= left and 0 <= right:
        power //= 2
        a[left] *= power

        if a[left] < a[left + 1]:
            print("ok")
        else:

            print("not ok")

        if right - left == k:
            ans += 1

            print(a[left: right + 1])
            print("radom")

            right -= 1
            a[left] *= power

            left -= 1
        else:
            left -= 1


def solve():
    n, k = intl()
    a = intl()
    ans = 0

    dp = [True for _ in range(n - 1)]

    for i in range(1, n):
        dp[i - 1] = a[i - 1] * 2 < a[i] * 4

    left = 0
    right = 0

    while left < n - 1 and right < n - 1:
        if dp[right]:
            if right - left + 1 == k:
                ans += 1
                left += 1
                right += 1
            else:
                right += 1
        else:
            right += 1
            left = right

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
