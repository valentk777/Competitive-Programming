# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/1479/problem/A
# Title  : Searching Local Minimum
# Tags   : tag-codeforces, tag-problem-A, tag-div-1, tag-difficulty-1700
# Notes  : binary search, interactive, ternary search
# ---------------------------------------------------------------------------------------

# ---------------------------------------------------Shared part--------------------------------------------------------
from sys import maxsize, stdout

MOD = 10 ** 9 + 7
INF = maxsize


# -------------------------------------------------------Solution-------------------------------------------------------

def print_ats(ans: int):
    print(f"! {ans}")
    stdout.flush()


def query(x):
    print(f"? {x}")
    return int(input())


def solve_slow():
    n = int(input())

    mid = -INF
    right = -INF

    for i in range(1, n + 1):
        left = mid
        mid = right
        right = query(i)

        if left > mid < right:
            print_ats(i - 1)
            return


def solve():
    n = int(input())

    a = [INF for _ in range(n + 1)]

    left = 1
    right = n

    while left < right:
        midd = (left + right) // 2

        a[midd] = query(midd)
        a[midd + 1] = query(midd + 1)

        if a[midd] < a[midd + 1]:
            right = midd
        else:
            left = midd + 1

    print_ats(left)


if __name__ == "__main__":
    solve()
