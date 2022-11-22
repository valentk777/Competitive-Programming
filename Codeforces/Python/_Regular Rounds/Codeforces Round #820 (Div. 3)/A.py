# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/1729/problem/A
# Title  : Two Elevators
# Tags   : tag-codeforces, tag-problem-A, tag-div-3, tag-difficulty-800
# Notes  : math
# ---------------------------------------------------------------------------------------


def solve():
    a, b, c = list(map(int, input().split()))

    if a == (abs(c - b) + c):
        return 3

    if a > (abs(c - b) + c):
        return 2

    if a < (abs(c - b) + c):
        return 1


if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        print(solve())
