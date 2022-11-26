# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/910/problem/A
# Title  : The Way to Home
# Tags   : tag-codeforces, tag-problem-A, tag-difficulty-800
# Notes  : dfs and similar, dp, greedy, implementation
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

def solve_greedy():
    n, d = intl()
    s = list(inp())

    i = 0
    ans = 0

    while i < n - 1:
        _max = i

        for j in range(i + 1, min(n, i + d + 1)):
            if s[j] == "1":
                _max = j

        if _max == i:
            break

        i = _max
        ans += 1

    if i == n - 1:
        return ans
    else:
        return -1


def solve_dp():
    n, d = intl()
    s = list(inp())
    dp = _dp(INF)
    dp[0] = 0

    for i in range(1, n):
        for j in range(1, d + 1):
            if s[i] == '1':
                dp[i] = min(dp[i], dp[i - j] + 1)

    if dp[n - 1] == INF:
        return -1
    else:
        return dp[n - 1]


def solve_dp_2():
    n, d = intl()
    s = list(inp())

    dp = _dp(-1)
    dp[0] = 0

    for i in range(n):
        if s[i] == "0":
            found = False

            for j in range(i + 1, min(n, i + d + 1)):
                if dp[j] != -1:
                    found = True
                    break

            if found:
                continue
            else:
                return -1

        for j in range(i + 1, min(n, i + d + 1)):
            if s[j] == "1":
                if dp[j] == -1:
                    dp[j] = dp[i] + 1
                else:
                    dp[j] = min(dp[j], dp[i] + 1)

    return dp[n - 1]


def run():
    # print(solve_greedy())
    print(solve_dp())


if __name__ == "__main__":
    if os.environ.get("DEBUG_CODEFORCES"):
        stdin = open("../../input.txt", "r")
        start_time = time.time()
        run()
        print("\n--- %s seconds ---\n" % (time.time() - start_time))
    else:
        run()
