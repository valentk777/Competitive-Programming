# -----------------------------------------------------------
# URL    : https://codeforces.com/contest/1447/problem/C
# Title  : Knapsack
# Notes  : tag-codeforces, tag-problem-C, tag-div-2, tag-not-pass
# -----------------------------------------------------------


import math


def solve():
    n, w = list(map(int, input().split()))
    a = list(map(int, input().split()))
    half_w = math.floor(w // 2)

    if min(a) > w:
        print(-1)
    else:
        items_to_pack = []
        total_sum = 0

        for i in range(n):
            if a[i] > w:
                a[i] = 0

        while half_w > total_sum:
            maxx = max(a)

            if maxx == 0:
                break

            summ = total_sum + maxx
            idx = a.index(maxx)

            if summ <= w:
                total_sum = summ
                items_to_pack.append(idx + 1)

            a[idx] = 0

        if half_w <= total_sum:
            print(len(items_to_pack))
            print(" ".join(map(str, items_to_pack)))
        else:
            print(-1)


if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        solve()
