# -----------------------------------------------------------
# URL    : https://codeforces.com/contest/1447/problem/B
# Title  : Numbers Box
# Notes  : tag-codeforces, tag-problem-B, tag-div-2
# -----------------------------------------------------------


def solve():
    n, m = list(map(int, input().split()))

    a = []
    for _ in range(n):
        a.extend(list(map(int, input().split())))

    neg_numbers = []
    sum_a = 0
    is_zero = False
    for i in range(n * m):
        if a[i] < 0:
            neg_numbers.append(a[i])
            a[i] = abs(a[i])
        elif a[i] == 0:
            is_zero = True
        sum_a += a[i]

    if is_zero or len(neg_numbers) % 2 == 0:
        print(sum_a)
    else:
        print(sum_a - 2 * min(a))


if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        solve()
