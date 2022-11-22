# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/1359/problem/B
# Title  : B. New Theatre Square
# Tags   : tag-codeforces, tag-problem-B, tag-div-2
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
    n, m, x, y = intl()
    ans = 0

    for _ in range(n):
        dp = _dp(0)
        line = ["*"] + list(inp())

        for j in range(1, m + 1):
            if line[j] == "*":
                dp[j] = dp[j - 1]
                dp[j] = dp[j - 1]
            else:
                if line[j - 1] == "*":
                    dp[j] = dp[j - 1] + x
                else:
                    dp[j] = dp[j - 2] + min(2 * x, y)
                    line[j] = "*"

        ans += dp[m]

    return ans


def solve_greedy():
    n, m, x, y = intl()
    _count_one = 0
    _count_two = 0

    for _ in range(n):
        s = inp()
        _count_two += s.count("..")
        s = s.replace("..", "")
        _count_one += s.count(".")

    # better buy all 1x1
    if 2 * x <= y:
        return (_count_two * 2 + _count_one) * x
    else:
        return _count_two * y + _count_one * x


def run():
    t = iinp()

    for _ in range(t):
        print(solve_dp())


if __name__ == "__main__":
    if os.environ.get("DEBUG_CODEFORCES"):
        stdin = open("../../input.txt", "r")
        start_time = time.time()
        run()
        print("\n--- %s seconds ---\n" % (time.time() - start_time))
    else:
        run()
