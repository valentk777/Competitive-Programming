# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/158/problem/A
# Title  : Next Round
# Tags   : tag-codeforces, tag-problem-A, tag-difficulty-800
# Notes  : *special, implementation
# ---------------------------------------------------------------------------------------


def solve():
    n, k = map(int, input().split())
    participants = list(map(int, input().split()))
    score = participants[k - 1]
    print(len([x for x in participants if x >= score and x > 0]))


if __name__ == "__main__":
    solve()
