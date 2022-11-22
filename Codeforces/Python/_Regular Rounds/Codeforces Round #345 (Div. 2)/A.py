# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/651/problem/A
# Title  : Joysticks
# Tags   : tag-codeforces, tag-problem-A, tag-div-2, tag-difficulty-1100
# Notes  : dp, greedy, implementation, math
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

def solve_dp():
    a, b = intl()

    if a == 1 and b == 1:
        return 0

    dp = _dp(0)
    dp[0] = 0

    while a > 0 and b > 0:
        if a - 2 > 0:
            dp[a - 2, b + 1] = dp[a, b] + 1
            a -= 2
            b += 1
        elif b - 2 > 0:
            dp[a + 1, b - 2] = dp[a, b] + 1
            a += 1
            b -= 2
        else:
            break

    return max(dp.values()) + 1


def solve_greedy():
    a, b = intl()

    if a == 1 and b == 1:
        return 0

    ans = 0

    while a > 0 and b > 0:
        if a < b:
            a, b = b, a

        a -= 2
        b += 1
        ans += 1

    return ans


def run():
    print(solve_dp())


if __name__ == "__main__":
    if os.environ.get("DEBUG_CODEFORCES"):
        stdin = open("../../input.txt", "r")
        start_time = time.time()
        run()
        print("\n--- %s seconds ---\n" % (time.time() - start_time))
    else:
        run()
