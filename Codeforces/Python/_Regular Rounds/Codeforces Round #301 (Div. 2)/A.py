# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/540/problem/A
# Title  : Combination Lock
# Tags   : tag-codeforces, tag-problem-A, tag-div-2, tag-difficulty-800
# Notes  : implementation
# ---------------------------------------------------------------------------------------


def solve():
    k = int(input())
    a = list(map(int, list(input())))
    b = list(map(int, list(input())))
    m = 0

    for i in range(k):
        x = min(abs(a[i] - b[i]), 10 - abs(a[i] - b[i]))
        m += x

    print(m)


if __name__ == "__main__":
    solve()
