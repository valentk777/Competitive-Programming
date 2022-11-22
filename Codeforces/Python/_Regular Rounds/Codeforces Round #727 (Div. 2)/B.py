# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/1539/problem/B
# Title  : Love Song
# Tags   : tag-codeforces, tag-problem-B, tag-div-2
# ---------------------------------------------------------------------------------------


MODULE_N = 10 ** 9 + 7


def solve():
    n, q = list(map(int, input().split()))
    s = input()

    sums = [0 for _ in range(n + 1)]
    sums[0] = 0

    for i in range(1, n + 1):
        sums[i] = sums[i - 1] + ord(s[i - 1]) - ord("a") + 1

    for _ in range(q):
        l, r = list(map(int, input().split()))
        print(sums[r] - sums[l - 1])


if __name__ == "__main__":
    solve()
