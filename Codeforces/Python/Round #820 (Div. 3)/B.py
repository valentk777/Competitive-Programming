# -----------------------------------------------------------
# URL    : https://codeforces.com/contest/1729/problem/B
# Title  : Decode String
# Notes  : tag-codeforces, tag-problem-B, tag-div-3
# -----------------------------------------------------------


def solve():
    n = int(input())
    s = input()
    s = s[::-1]

    result = ""

    base = 96
    i = 0

    while i < n:
        if s[i] == '0':
            result += chr(int(s[i + 2] + s[i + 1]) + base)
            i += 3
        else:
            result += chr(int(s[i]) + base)
            i += 1

    return result[::-1]


if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        print(solve())
