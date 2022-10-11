# -----------------------------------------------------------
# URL    : https://codeforces.com/contest/1736/problem/C
# Title  : Good Subarrays (Easy Version)
# Notes  : tag-codeforces, tag-problem-C, tag-div-2
# -----------------------------------------------------------

# ---------------------------------------------------Shared part--------------------------------------------------------
import os
import time
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

def solve_1():
    n = iinp()
    a = intl()

    ans = 0
    r = 0

    for j in range(n):
        while (r < n) and (a[r] >= r - j + 1):
            r += 1
        ans += r - j

    return ans


def solve_2():
    n = iinp()
    a = intl()

    tag = [n for _ in range(n + 1)]

    for j in range(1, n + 1):
        if j >= a[j - 1]:
            tag[j - a[j - 1]] = min(tag[j - a[j - 1]], j - 1)

    ans = 0
    _min = n

    for j in range(n, 0, -1):
        _min = min(_min, tag[j])
        ans += _min - j + 1

    return ans


def solve_two_pointers():
    n = iinp()
    a = intl()

    left = 0
    right = 0
    fixed_idx = 1
    ans = 0

    while right < n:
        while left < n and fixed_idx > a[right]:
            left += 1
            fixed_idx -= 1

        ans += (right - left + 1)
        right += 1
        fixed_idx += 1

    return ans


def run():
    t = iinp()

    for _ in range(t):
        print(solve_two_pointers())


if __name__ == "__main__":
    # for i in range(100):
    #     print(randint(1, 200000), end= " ")
    # print()

    if os.environ.get("DEBUG_CODEFORCES"):
        stdin = open("../input.txt", "r")
        start_time = time.time()
        run()
        print("\n--- %s seconds ---\n" % (time.time() - start_time))
    else:
        run()

#
#
# # -----------------------------------------------------------
# # URL    : https://codeforces.com/contest/XXXXX/problem/C
# # Title  : TEXT
# # Notes  : tag-codeforces, tag-problem-C, tag-div-2
# # -----------------------------------------------------------
#
# # ---------------------------------------------------Shared part--------------------------------------------------------
# import os
# import time
# from collections import defaultdict
# from sys import stdin, maxsize
#
# inp = lambda: stdin.readline().strip()
# iinp = lambda: int(inp())
# intl = lambda: list(map(int, inp().split()))
# strl = lambda: list(inp().split())
# list_to_string = lambda _a: "".join(map(str, _a))
# list_to_string_list = lambda _a: " ".join(map(str, _a))
# _dp = lambda default_value: defaultdict(lambda: default_value)
# print_dp = lambda _dict: list(map(lambda item: print(f"{item[0]} = {item[1]}"), _dict.items()))
#
# MOD = 10 ** 9 + 7
# INF = maxsize
#
#
# # -------------------------------------------------------Solution-------------------------------------------------------
#
# def solve():
#     n = iinp()
#     a = [0] + intl()
#
#     ans = [0 for _ in range(n + 2)]
#
#     for i in range(n + 1):
#         if i + 1 <= a[i]:
#             ans[i + 1] = min(i + 1, a[i - 1] + 1)
#         else:
#             ans[i + 1] = a[i]
#
#     return sum(ans)
#
#     # a = intl()
#     #
#     # _count = 0
#     # for i in range(n):
#     #     for j in range(i, n):
#     #         qq = a[i:j + 1]
#     #         stop = False
#     #
#     #         for z in range(len(qq)):
#     #             if z >= qq[z]:
#     #                 stop = True
#     #                 break
#     #
#     #         if not stop:
#     #             _count += 1
#     #
#     # print(_count)
#
#
#     _sums = 0
#     for i in range(1, n + 1):
#
#         _sums += ans[i] - ans[i - 1]
#
#     if ans[i] <= i:
#
#     if ans[i] - ans[i - 1] > 1:
#
#     else:
#         _sums += ans[i]
#
#     return _sums
#
#
# def run():
#     t = iinp()
#
#     for _ in range(t):
#         print(solve())
#
#
# if __name__ == "__main__":
#     if os.environ.get("DEBUG_CODEFORCES"):
#         stdin = open("../input.txt", "r")
#         start_time = time.time()
#         run()
#         print("\n--- %s seconds ---\n" % (time.time() - start_time))
#     else:
#         run()
