# -----------------------------------------------------------
# URL    : https://codeforces.com/contest/1438/problem/C
# Title  : Engineer Artem
# Notes  : tag-codeforces, tag-problem-C, tag-div-2
# -----------------------------------------------------------


def solve():
    n, m = list(map(int, input().split()))
    for i in range(n):
        a = list(map(int, input().split()))
        for j in range(m):
            if (i + j) % 2 == 0:
                if a[j] % 2 == 0:
                    print(a[j], end=" ")
                else:
                    print(a[j] + 1, end=" ")
            else:
                if a[j] % 2 == 0:
                    print(a[j] + 1, end=" ")
                else:
                    print(a[j], end=" ")
        print()


if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        solve()
