# -----------------------------------------------------------
# URL    : https://codeforces.com/contest/1354/problem/B
# Title  : Ternary String
# Notes  : tag-codeforces, tag-problem-B, tag-div-2
# -----------------------------------------------------------

# ---------------------------------------------------Shared part--------------------------------------------------------
import os
import time
from collections import defaultdict
from sys import stdin, maxsize

inp = lambda: stdin.readline().strip()
iinp = lambda: int(inp())
intl = lambda: list(map(int, inp().split()))
strl = lambda: list(inp().split())
list_to_string = lambda _a: "".join(map(str, _a))
list_to_string_list = lambda _a: " ".join(map(str, _a))
_dp = lambda default_value: defaultdict(lambda: default_value)
print_dp = lambda _dict: list(map(lambda item: print(f"{item[0]} = {item[1]}"), _dict.items()))

MOD = 10 ** 9 + 7
INF = maxsize


# -------------------------------------------------------Solution-------------------------------------------------------

# Time limit exceeded
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


# Time limit exceeded
def solve_dp_slow():
    _min = INF

    s = list(inp())

    if s.count("1") == 0 or s.count("2") == 0 or s.count("3") == 0:
        return 0

    s = list(map(string_to_mask, s))
    n = len(s)

    dp = [0 for _ in range(n + 1)]
    _min = INF

    for i in range(1, n + 1):
        dp[i - 1] = s[i - 1]

        for j in range(i, n):
            dp[j] = dp[j - 1] | s[j]

            if dp[j] == 7:
                _min = min(_min, j + 1 - i)
                break

    if _min == INF:
        return 0
    else:
        return _min


def is_full_number_exist(dp, _from, _to, _string):
    return (dp[_from, 1] - dp[_to, 1] + (_string[_to] == 1) >= 1
            and dp[_from, 2] - dp[_to, 2] + (_string[_to] == 2) >= 1
            and dp[_from, 3] - dp[_to, 3] + (_string[_to] == 3) >= 1)


def solve_dp():
    s = list(map(int, list(inp())))
    n = len(s)

    # count of numbers in [position, number_we_count]
    dp = _dp(0)
    dp[0, s[0]] = 1

    for i in range(1, n):
        for j in range(1, 4):
            if j == s[i]:
                dp[i, j] = dp[i - 1, j] + 1
            else:
                dp[i, j] = dp[i - 1, j]

    _max = INF

    for c in range(2, n):
        i = 0
        j = c

        while j - i > 1:
            _mid = (i + j) // 2

            if is_full_number_exist(dp, c, _mid, s):
                i = _mid
            else:
                j = _mid

        if is_full_number_exist(dp, c, j, s):
            _max = min(_max, c - j + 1)
        elif is_full_number_exist(dp, c, i, s):
            _max = min(_max, c - i + 1)

        if _max == 3:
            return _max

    if _max == INF:
        return 0
    else:
        return _max


def run():
    t = iinp()

    for _ in range(t):
        print(solve_dp())


if __name__ == "__main__":
    if os.environ.get("DEBUG_CODEFORCES"):
        stdin = open("../input.txt", "r")
        start_time = time.time()
        run()
        print("\n--- %s seconds ---\n" % (time.time() - start_time))
    else:
        run()
