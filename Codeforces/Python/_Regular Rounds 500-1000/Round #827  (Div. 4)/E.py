# -----------------------------------------------------------
# URL    : https://codeforces.com/contest/1742/problem/E
# Title  : Scuza
# Notes  : tag-codeforces, tag-problem-E, tag-div-4
# -----------------------------------------------------------

# ---------------------------------------------------Shared part--------------------------------------------------------
import os
import time
from bisect import bisect_right
from collections import defaultdict
from sys import stdin, maxsize

inp = lambda: stdin.readline().strip()
iinp = lambda: int(inp())
intl = lambda: list(map(int, inp().split()))
strl = lambda: list(inp().split())
list_to_string = lambda _a: "".join(map(str, _a))
list_to_string_list = lambda _a: " ".join(map(str, _a))
_dp = lambda default_value: defaultdict(lambda: default_value)
print_dp = lambda _dict: list(map(lambda item: print(f"{item[0]} = {item[1]}"), _dict.items()))
MOD = 10 ** 9 + 7
INF = maxsize


# -------------------------------------------------------Solution-------------------------------------------------------


# the idea: we can calculate all maximums at position i and find first index where max > step
def find_max_index_with_binary_search(_a, n, step):
    x = 0
    y = n - 1

    while y >= x:
        mid = (x + y) // 2

        if _a[mid] <= step:
            x = mid + 1
        else:
            y = mid - 1

    return x - 1


# only for testing
def solve_slow():
    n, q = intl()
    a = intl()
    k = intl()

    _sums = [0]
    _sum = 0

    for i in range(n):
        _sum += a[i]
        _sums.append(_sum)

    ans = []

    for i in range(q):
        if k[i] == 0:
            ans.append(0)
            continue

        stop = False

        for j in range(n):
            if a[j] > k[i]:
                ans.append(_sums[j])
                stop = True
                break

        if not stop:
            ans.append(_sums[n])

    return list_to_string_list(ans)


def solve():
    n, q = intl()
    a = intl()
    k = intl()

    _sums = []
    _sum = 0

    for i in range(n):
        _sum += a[i]
        _sums.append(_sum)

    _maxs = []
    _max = 0

    for i in range(n):
        if a[i] > _max:
            _max = a[i]

        _maxs.append(_max)

    ans = []

    for i in range(q):
        if k[i] == 0:
            ans.append(0)
            continue

        idx = find_max_index_with_binary_search(_maxs, n, k[i])

        if idx == -1:
            ans.append(0)
        else:
            ans.append(_sums[idx])

    return list_to_string_list(ans)


def solve_using_bisect_right():
    n, q = intl()
    a = intl()
    k = intl()

    _sums = [0]
    _sum = 0

    for i in range(n):
        _sum += a[i]
        _sums.append(_sum)

    _maxs = []
    _max = 0

    for i in range(n):
        if a[i] > _max:
            _max = a[i]

        _maxs.append(_max)

    ans = []

    for i in range(q):
        # this function 'bisect_right' return index where to insert provided number  (most right one) for sorted list
        # this function 'bisect_left' return index where to insert provided number (most left one) for sorted list
        ans.append(_sums[bisect_right(_maxs, k[i])])

    return ans


def run():
    t = iinp()

    for _ in range(t):
        # print(solve())
        print(*solve_using_bisect_right())


if __name__ == "__main__":
    if os.environ.get("DEBUG_CODEFORCES"):
        stdin = open("../input.txt", "r")
        start_time = time.time()
        run()
        print("\n--- %s seconds ---\n" % (time.time() - start_time))
    else:
        run()
