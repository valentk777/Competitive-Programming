# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/546/problem/A
# Title  : Soldier and Bananas
# Tags   : tag-codeforces, tag-problem-A, tag-div-2, tag-difficulty-800
# Notes  : brute force, implementation, math
# ---------------------------------------------------------------------------------------


def solve():
    k, n, w = list(map(int, input().split()))

    t_sum = 0

    for i in range(w + 1):
        t_sum += k * i

    pin = n - t_sum

    if pin >= 0:
        return 0
    else:
        return -pin


if __name__ == "__main__":
    print(solve())
