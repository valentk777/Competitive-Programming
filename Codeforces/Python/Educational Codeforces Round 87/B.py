# -----------------------------------------------------------
# URL    : https://codeforces.com/contest/1354/problem/B
# Title  : Ternary String
# Notes  : tag-codeforces, tag-problem-B, tag-div-2, tag-not-pass
# -----------------------------------------------------------

# ---------------------------------------------------Shared part--------------------------------------------------------
import os
import time
from sys import stdin, maxsize

inp = lambda: stdin.readline().strip()
iinp = lambda: int(inp())
intl = lambda: list(map(int, inp().split()))
strl = lambda: list(inp().split())

MOD = 10 ** 9 + 7
INF = maxsize


# -------------------------------------------------------Solution-------------------------------------------------------

# time limit exceeded
def solve():
    s = inp()
    n = len(s)

    if s.count("1") == 0 or s.count("2") == 0 or s.count("3") == 0:
        return 0

    _min = INF

    for i in range(n - 2):
        a = s[i]
        b = s[i + 1]

        if a != b:
            for j in range(i + 2, n):
                if s[j] != a and s[j] != b:
                    _min = min(_min, j - i + 1)

    if _min == INF:
        return 0
    else:
        return _min


# "abc" -> 111
def string_to_mask(x):
    if x == "1":
        return 1

    if x == "2":
        return 2

    if x == "3":
        return 4


# memory limit exceeded
def solve_dp():
    s = list(inp())
    n = len(s)

    _min = INF

    if s.count("1") == 0 or s.count("2") == 0 or s.count("3") == 0:
        return 0

    dp = [0 for _ in range(n + 1)]
    s = list(map(string_to_mask, s))

    for i in range(1, n + 1):
        dp[i - 1] = s[i - 1]

        # for j in range(i, n + 1):
        for j in range(i):
            dp[j] = dp[j - 1] | s[j - 1]

            if dp[j] == 7:
                _min = min(_min, j + 1 - i)
                break

    if _min == INF:
        return 0
    else:
        return _min


def run():
    t = iinp()

    for _ in range(t):
        print(solve())
        # print(solve_dp())


if __name__ == "__main__":
    if os.environ.get("DEBUG_CODEFORCES"):
        stdin = open("../input.txt", "r")
        start_time = time.time()
        run()
        print("\n--- %s seconds ---\n" % (time.time() - start_time))
    else:
        run()
