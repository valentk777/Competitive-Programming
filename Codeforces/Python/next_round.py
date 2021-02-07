# -----------------------------------------------------------
# URL    : https://codeforces.com/problemset/problem/158/A
# Title  : Next Round
# Notes  : tag-codeforces, tag-problem-A, tag-div-none
# -----------------------------------------------------------


def solve():
    n, k = map(int, input().split())
    participants = list(map(int, input().split()))
    score = participants[k - 1]
    print(len([x for x in participants if x >= score and x > 0]))


if __name__ == "__main__":
    solve()
