# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/996/problem/A
# Title  : Hit the Lottery
# Tags   : tag-codeforces, tag-problem-A, tag-div-2
# ---------------------------------------------------------------------------------------


def count_and_n(n, count, denomination):
    count += n // denomination
    return count, n % denomination


def solve():
    n = int(input())
    count = 0
    for denomination in [100, 20, 10, 5, 1]:
        count, n = count_and_n(n, count, denomination)

    print(count)


if __name__ == "__main__":
    solve()
