# -----------------------------------------------------------
# URL    : https://codeforces.com/contest/546/problem/A
# Title  : Soldier and Bananas
# Notes  : tag-codeforces, tag-problem-A, tag-div-2
# -----------------------------------------------------------


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
