# -----------------------------------------------------------
# URL    : https://codeforces.com/contest/546/problem/B
# Title  : Soldier and Badges
# Notes  : tag-codeforces, tag-problem-B, tag-div-2
# -----------------------------------------------------------


def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()

    coins = 0

    for i in range(1, n):
        while a[i - 1] >= a[i]:
            a[i] += 1
            coins += 1

    return coins


if __name__ == "__main__":
    print(solve())
