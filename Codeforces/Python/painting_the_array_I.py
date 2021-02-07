# -----------------------------------------------------------
# URL    : https://codeforces.com/contest/1480/problem/D1
# Title  : Painting the Array I
# Notes  : tag-codeforces, tag-problem-D, tag-div-2
# -----------------------------------------------------------


def solve():
    n = int(input())
    a = list(map(int, input().split()))

    total = 1
    a_1 = a[0]
    a_2 = None

    for x in a[1:]:
        if x == a_1:
            if a_2 is None or x != a_2:
                a_2 = x
                total += 1

        else:
            a_1 = x
            total += 1

    print(total)


if __name__ == "__main__":
    solve()
