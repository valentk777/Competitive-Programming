# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/1195/problem/C
# Title  : Sport Mafia
# Tags   : tag-codeforces, tag-problem-B, tag-div-2, tag-difficulty-1000
# Notes  : binary search, brute force, math
# ---------------------------------------------------------------------------------------


def solve():
    n = int(input())
    h_1 = list(map(int, input().split()))
    h_2 = list(map(int, input().split()))

    dp_1, dp_2, dp_3 = 0, 0, 0

    for i in range(n):
        t_dp_1, t_dp_2, t_dp_3 = max(dp_2 + h_1[i], dp_3 + h_1[i]), max(dp_1 + h_2[i], dp_3 + h_2[i]), max(dp_1, dp_2)
        dp_1, dp_2, dp_3 = t_dp_1, t_dp_2, t_dp_3

    print(max(dp_1, dp_2, dp_3))


if __name__ == "__main__":
    solve()
