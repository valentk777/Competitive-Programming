# -----------------------------------------------------------
# URL    : https://open.kattis.com/problems/coffeecupcombo
# Title  : Coffee Cup Combo
# Notes  : tag-kattis, tag-easy
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
list_from_inp = lambda n: [inp() for _ in range(n)]

MOD = 10 ** 9 + 7
INF = maxsize


# -------------------------------------------------------Solution-------------------------------------------------------

def solve():
    n = iinp()
    s = list(map(int, inp()))

    dp = _dp(0)
    full = 0

    for i in range(1, n + 1):
        if s[i - 1] == 1:
            dp[i] = dp[i - 1] + 1
            full = 2
        elif full > 0:
            full -= 1
            dp[i] = dp[i - 1] + 1
        else:
            dp[i] = dp[i - 1]

    return dp[n]


def run():
    print(solve())


if __name__ == "__main__":
    if os.environ.get("DEBUG_CODEFORCES"):
        stdin = open("../input.txt", "r")
        start_time = time.time()
        run()
        print("\n--- %s seconds ---\n" % (time.time() - start_time))
    else:
        run()
