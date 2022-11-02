# -----------------------------------------------------------
# URL    : https://codeforces.com/contest/702/problem/A
# Title  : Maximum Increase
# Notes  : tag-codeforces, tag-problem-A
# -----------------------------------------------------------


def solve():
    n = int(input())
    a = list(map(int, input().split()))
    dp = [1 for _ in range(n)]

    for i in range(1, n):
        if a[i - 1] < a[i]:
            dp[i] += dp[i - 1]

    print(max(dp))


if __name__ == "__main__":
    solve()
