# -----------------------------------------------------------
# URL    : https://codeforces.com/contest/1519/problem/B
# Title  : The Cake Is a Lie
# Notes  : tag-codeforces, tag-problem-B, tag-div-2
# -----------------------------------------------------------


def solve():
    n, m, k = list(map(int, input().split()))

    dp = [[1 for _ in range(m + 1)] for _ in range(n + 2)]
    dp[0][0] = 0

    for _n in range(n + 1):
        dp[_n + 1][0] += dp[_n][0]

        for _m in range(m):
            dp[_n][_m + 1] += dp[_n][_m] + _n

    if dp[n - 1][m - 1] == k:
        return "YES"
    else:
        return "NO"


if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        print(solve())
