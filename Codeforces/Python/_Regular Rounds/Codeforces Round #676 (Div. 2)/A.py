# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/1421/problem/A
# Title  : XORwice
# Tags   : tag-codeforces, tag-problem-A, tag-div-2, tag-difficulty-800
# Notes  : bitmasks, greedy, math
# ---------------------------------------------------------------------------------------


def solve():
    a, b = map(int, input().split())
    x = a & b
    return (a ^ x) + (x ^ b)


if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        print(solve())
