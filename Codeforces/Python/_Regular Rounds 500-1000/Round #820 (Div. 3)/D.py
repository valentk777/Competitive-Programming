# -----------------------------------------------------------
# URL    : https://codeforces.com/contest/1729/problem/D
# Title  : Friends and the Restaurant
# Notes  : tag-codeforces, tag-problem-D, tag-div-3
# -----------------------------------------------------------


def solve():
    n = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    diff = [y[i] - x[i] for i in range(n)]
    diff = sorted(diff)

    start = 0
    end = n - 1

    group = 0

    wrong = []

    while start < end:
        if diff[start] + diff[end] >= 0:
            group += 1
            start += 1
            end -= 1
        else:
            wrong.append(diff[start])
            start += 1

    return group


if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        print(solve())
