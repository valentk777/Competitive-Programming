# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/762/problem/D
# Title  : D. Maximum path
# Tags   : tag-codeforces, tag-problem-D, tag-not-pass
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

def solve():
    n = iinp()

    matrix = []
    for i in range(3):
        matrix.append(intl())

    print(matrix)

    dp = _dp(0)

    for i in range(1, n + 1):
        dp[i, 1] = max(dp[i - 1, 1], dp[i, 2], dp[i + 1, 1]) + matrix[0][i - 1]
        dp[i, 2] = max(dp[i - 1, 2], dp[i, 1], dp[i, 3], dp[i + 1, 2]) + matrix[1][i - 1]
        dp[i, 3] = max(dp[i - 1, 3], dp[i, 2], dp[i + 1, 3]) + matrix[2][i - 1]

    print_dp(dp)


def run():
    print(solve())


if __name__ == "__main__":
    if os.environ.get("DEBUG_CODEFORCES"):
        stdin = open("../../input.txt", "r")
        start_time = time.time()
        run()
        print("\n--- %s seconds ---\n" % (time.time() - start_time))
    else:
        run()
