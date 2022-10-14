# -----------------------------------------------------------
# URL    : https://codeforces.com/contest/1728/problem/B
# Title  : Best Permutation
# Notes  : tag-codeforces, tag-problem-B, tag-div-2
# -----------------------------------------------------------


def solve():
    n = int(input())

    a = []

    if n % 2 == 0:
        for i in range(1, n - 1, 2):
            a.extend([i + 1, i])
    else:
        a.extend([1, 2, 3])

        for i in range(4, n - 1, 2):
            a.extend([i + 1, i])

    a.extend([n - 1, n])

    print(" ".join(map(str, a)))


if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        solve()
