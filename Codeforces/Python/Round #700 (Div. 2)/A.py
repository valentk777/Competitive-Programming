# -----------------------------------------------------------
# URL    : https://codeforces.com/contest/1480/problem/A
# Title  : Yet Another String Game
# Notes  : tag-codeforces, tag-problem-A, tag-div-2
# -----------------------------------------------------------


def solve():
    s = list(input())

    for i in range(len(s)):
        if i % 2 == 0:
            s[i] = 'b' if s[i] == 'a' else 'a'
        else:
            s[i] = 'y' if s[i] == 'z' else 'z'

    print("".join(s))


if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        solve()
