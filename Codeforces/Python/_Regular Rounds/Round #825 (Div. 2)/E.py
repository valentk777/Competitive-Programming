# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/1736/problem/E
# Title  : Swap and Take
# Tags   : tag-codeforces, tag-problem-E, tag-div-2, tag-not-pass
# ---------------------------------------------------------------------------------------

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

def solve():
    n = iinp()
    a = intl()

    dp = _dp(-INF)
    dp[0, n, 0] = 0

    for i in range(n):
        for j in range((2 * n) + 1):
            for k in range(n + 1):
                nj = j - (i - k) + 1

                if n <= nj <= 2 * n:
                    dp[1, nj, k + 1] = max(dp[1, nj, k + 1], dp[0, j, k] + a[i])

        for j in range((2 * n) + 1):
            for k in range(n + 1):
                if dp[1, j, k] > 0:
                    dp[1, j, k + 1] = max(dp[1, j, k + 1], dp[1, j, k] + a[i])

    for j in range((2 * n) + 1):
        for k in range(n + 1):
            dp[0, j, k] = max(dp[0, j, k], dp[1, j, k])

    ans = -INF

    for i in range(n, (2 * n) + 1):
        ans = max(ans, dp[0, i, n])

    return ans


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
