# -----------------------------------------------------------
# URL    : https://codeforces.com/contest/791/problem/A
# Title  : Bear and Big Brother
# Notes  : tag-codeforces, tag-problem-A, tag-div-2
# -----------------------------------------------------------

def solve():
    a, b = map(int, input().split())
    i = 0
    while a <= b:
        a = a * 3
        b = b * 2
        i += 1

    print(1) if i == 0 else print(i)


if __name__ == "__main__":
    solve()
