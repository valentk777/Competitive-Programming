# -----------------------------------------------------------
# URL    : https://codeforces.com/contest/545/problem/C
# Title  : Woodcutters
# Notes  : tag-codeforces, tag-problem-C, tag-div-2
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
list_to_string_List = lambda _a: " ".join(map(str, _a))
_dp = lambda default_value: defaultdict(lambda: default_value)

MOD = 10 ** 9 + 7
INF = maxsize


# -------------------------------------------------------Solution-------------------------------------------------------

def solve_greedy():
    n = iinp()

    trees = []
    for _ in range(n):
        x, h = intl()
        trees.append((x, h))

    current = -INF
    _count = 0

    for i in range(n):
        if current >= trees[i][0]:
            _count -= 1
            current -= trees[i - 1][1]

        if trees[i][0] - current > trees[i][1]:
            _count += 1
            current = trees[i][0]
        else:
            _count += 1
            current = trees[i][0] + trees[i][1]

    return _count


def solve_dp():
    n = iinp()

    trees = []
    for _ in range(n):
        x, h = intl()
        trees.append((x, h))

    dp = _dp(-1)
    dp[1, -1] = 1
    dp[1, 0] = 0
    dp[1, 1] = 1

    for i in range(2, n + 1):
        # crop left
        if trees[i - 2][0] + trees[i - 1][1] < trees[i - 1][0]:
            dp[i, -1] = max(dp[i, -1], dp[i - 1, -1] + 1)  # max if we cut left
            dp[i, -1] = max(dp[i, -1], dp[i - 1, 0] + 1)  # max if we leave before this one

        if trees[i - 2][0] + trees[i - 2][1] + trees[i - 1][1] < trees[i - 1][0]:
            dp[i, -1] = max(dp[i, -1], dp[i - 1, 1] + 1)

        # leave
        dp[i, 0] = max(dp[i - 1, -1], dp[i - 1, 0])

        if trees[i - 2][0] + trees[i - 2][1] < trees[i - 1][0]:
            dp[i, 0] = max(dp[i, 0], dp[i - 1, 1])

        # crop right
        dp[i, 1] = max(dp[i - 1, -1], dp[i - 1, 0]) + 1

        if trees[i - 2][0] + trees[i - 2][1] < trees[i - 1][0]:
            dp[i, 1] = max(dp[i, 1], dp[i - 1, 1] + 1)

    return max(dp[n, -1], dp[n, 0], dp[n, 1])


def run():
    print(solve_dp())


if __name__ == "__main__":
    if os.environ.get("DEBUG_CODEFORCES"):
        stdin = open("../input.txt", "r")
        start_time = time.time()
        run()
        print("\n--- %s seconds ---\n" % (time.time() - start_time))
    else:
        run()
