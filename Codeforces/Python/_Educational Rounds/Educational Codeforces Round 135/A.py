# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/1728/problem/A
# Title  : Colored Balls: Revisited
# Tags   : tag-codeforces, tag-problem-A, tag-div-2
# ---------------------------------------------------------------------------------------


def solve():
    n = int(input())
    a = list(map(int, input().split()))

    sum_a = sum(a)

    if n == 1:
        print(1)
        return

    if n == 2:
        if a[0] > a[1]:
            print(1)
        else:
            print(2)
        return

    max_e = max(a)

    if max_e > sum_a - max_e:
        print(a.index(max_e) + 1)
    else:
        print(len(a))


if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        solve()
