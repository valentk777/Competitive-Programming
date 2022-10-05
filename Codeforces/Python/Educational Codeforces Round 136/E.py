# -----------------------------------------------------------
# URL    : https://codeforces.com/contest/1739/problem/E
# Title  : Cleaning Robot
# Notes  : tag-codeforces, tag-problem-E, tag-div-2
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
list_to_string = lambda _a: " ".join(map(str, _a))
_dp = lambda default_value: defaultdict(lambda: default_value)

MOD = 10 ** 9 + 7
INF = maxsize


# -------------------------------------------------------Solution-------------------------------------------------------

def solve():
    n = iinp()

    line_1 = list(map(int, list(inp())))
    line_2 = list(map(int, list(inp())))

    s = [line_1, line_2]

    # the largest number of dirty cells that we can leave to the robot if
    # i - row, j - column, is_dirty - is true if the cell in the opposite row of the i-th column is dirty.
    dp = _dp(-INF)
    dp[0, 0, 0] = 0
    dp[0, 0, int(line_2[0] == 1)] = int(line_2[0] == 1)

    # push dp
    for i in range(n - 1):
        for j in range(2):
            # next need to clean
            next_j_1 = int(s[j][i + 1] == 1)
            next_j_2 = int(s[j ^ 1][i + 1] == 1)

            dp[i + 1, j ^ 1, 0] = max(dp[i + 1, j ^ 1, 0], dp[i, j, 1] + next_j_2)
            dp[i + 1, j, next_j_2] = max(dp[i + 1, j, next_j_2], dp[i, j, 0] + next_j_2 + next_j_1)
            dp[i + 1, j, 0] = max(dp[i + 1, j, 0], dp[i, j, 0] + next_j_1)

    return max(dp[n - 1, 0, 0], dp[n - 1, 0, 1], dp[n - 1, 1, 0], dp[n - 1, 1, 1])


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
