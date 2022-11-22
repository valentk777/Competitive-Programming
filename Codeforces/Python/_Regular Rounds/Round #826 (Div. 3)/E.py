# -----------------------------------------------------------
# URL    : https://codeforces.com/contest/1741/problem/E
# Title  : Sending a Sequence Over the Network
# Notes  : tag-codeforces, tag-problem-E, tag-div-3, tag-not-pass
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

# check if provided array could be treated as correct: have element count at the start or at the end
def validate(_a, n, x, y):
    return _a[x] == n - 1 or _a[y] == n - 1


# slower than first one
# def validate(_a, n):
#     return _a[0] == n - 1 or _a[-1] == n - 1


# time limit exceeded
def solve_slow():
    n = iinp()
    a = intl()

    if len(set(a)) == 1:
        if n % (a[0] + 1) == 0:
            return "YES"
        else:
            return "NO"

    dp = _dp(False)
    dp[0] = True

    oki = {0}

    for i in range(1, n + 1):
        for j in oki:
            if dp[j] and validate(a, i - j, j, i - 1):
                dp[i] = True
                oki.add(i)
                break

    if dp[n]:
        return "YES"
    else:
        return "NO"


def solve():
    n = iinp()
    a = intl()

    dp = _dp(False)
    dp[0] = True

    for i in range(n):
        if i - a[i] >= 0:
            # take as last
            dp[i + 1] |= dp[i - a[i]]
        if i + a[i] < n:
            # take as first
            dp[i + 1 + a[i]] |= dp[i]

    print_dp(dp)

    if dp[n]:
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
