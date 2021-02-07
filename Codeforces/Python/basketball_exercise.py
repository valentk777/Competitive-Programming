# -----------------------------------------------------------
# URL    : https://codeforces.com/problemset/problem/1195/C
# Title  : Basketball Exercise
# Notes  : tag-codeforces, tag-problem-C, tag-div-2
# -----------------------------------------------------------


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
