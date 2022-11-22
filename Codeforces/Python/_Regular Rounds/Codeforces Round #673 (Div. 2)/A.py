# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/1417/problem/A
# Title  : Copy-paste
# Tags   : tag-codeforces, tag-problem-A, tag-div-2
# ---------------------------------------------------------------------------------------


def solve():
    t = int(input())

    for _ in range(t):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))

        count = 0
        minx = min(a)
        a.remove(minx)

        for i in range(n - 1):
            count += (k - a[i]) // minx

        print(count)


if __name__ == "__main__":
    solve()
