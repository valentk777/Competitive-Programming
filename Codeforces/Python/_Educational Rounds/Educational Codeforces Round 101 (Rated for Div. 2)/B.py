# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/1469/problem/B
# Title  : Red and Blue
# Tags   : tag-codeforces, tag-problem-B, tag-div-2
# ---------------------------------------------------------------------------------------


def solve():
    n = int(input())
    r = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))

    # max value of function f
    dp = [[-10 ** 9 for _ in range(m + 1)] for _ in range(n + 1)]
    dp[0][0] = 0
    ans = 0

    for i in range(n + 1):
        for j in range(m + 1):
            if i < n:
                dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + r[i])

            if j < m:
                dp[i][j + 1] = max(dp[i][j + 1], dp[i][j] + b[j])

            ans = max(ans, dp[i][j])

    return ans


if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        print(solve())
