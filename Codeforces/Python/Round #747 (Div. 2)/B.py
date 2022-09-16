# -----------------------------------------------------------
# URL    : https://codeforces.com/contest/1594/problem/B
# Title  : Special Numbers
# Notes  : tag-codeforces, tag-problem-B, tag-div-2
# -----------------------------------------------------------


MODULE_N = 10 ** 9 + 7


def solve():
    n, k = list(map(int, input().split()))

    # k-th element bit representation display witch bit should be power of n.
    k_bit = reversed(str(bin(k).replace("0b", "")))
    result = 0
    for i, e in enumerate(k_bit):
        if e == "1":
            result += (n ** i) % MODULE_N

    return result % MODULE_N


if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        print(solve())
