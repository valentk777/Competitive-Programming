# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/1538/problem/A
# Title  : Stone Game
# Tags   : tag-codeforces, tag-problem-A, tag-div-3, tag-difficulty-800
# Notes  : brute force, dp, greedy
# ---------------------------------------------------------------------------------------


def solve():
    n = int(input())
    a = list(map(int, input().split()))

    _min = 10 ** 5
    _min_pos = -1
    _max = -10 ** 5
    _max_pos = -1

    for i in range(n):
        if a[i] < _min:
            _min = a[i]
            _min_pos = i

        if a[i] > _max:
            _max = a[i]
            _max_pos = i

    x = min(_min_pos, _max_pos)
    y = max(_min_pos, _max_pos)

    # min (min(<from beginning till max position> , <all minus few from beginning>), <from beginning + from right>)
    return min(min(y + 1, n - x), x + n - y + 1)


if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        print(solve())
