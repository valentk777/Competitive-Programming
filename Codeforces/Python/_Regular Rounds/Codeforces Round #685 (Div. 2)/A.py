# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/1451/problem/A
# Title  : Subtract or Divide
# Tags   : tag-codeforces, tag-problem-A, tag-div-2, tag-difficulty-800
# Notes  : greedy, math
# ---------------------------------------------------------------------------------------


def solve():
    n = int(input())

    moves = 0

    while n > 1:
        if n & 1 == 1 or n == 2:
            n -= 1
        else:
            n = 2

        moves += 1

    return moves


if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        print(solve())
