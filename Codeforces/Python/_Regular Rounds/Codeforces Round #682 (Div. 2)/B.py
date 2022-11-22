# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/1438/problem/B
# Title  : Valerii Against Everyone
# Tags   : tag-codeforces, tag-problem-B, tag-div-2
# ---------------------------------------------------------------------------------------


def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()

    prev = a[0]
    found = False
    for element in a[1:]:
        if element == prev:
            found = True
            break
        else:
            prev = element

    if found:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        solve()
