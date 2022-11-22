# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/1721/problem/D
# Title  : Maximum AND
# Tags   : tag-codeforces, tag-problem-D, tag-div-2, tag-difficulty-1800
# Notes  : bitmasks, dfs and similar, divide and conquer, greedy, sortings
# ---------------------------------------------------------------------------------------

# ---------------------------------------------------Shared part--------------------------------------------------------
import os
import time
from collections import defaultdict
from sys import stdin, maxsize, stdout

inp = lambda: stdin.readline().strip()
iinp = lambda: int(inp())
intl = lambda: list(map(int, inp().split()))
strl = lambda: list(inp().split())
list_to_string = lambda _a: "".join(map(str, _a))
list_to_string_list = lambda _a: " ".join(map(str, _a))
_dp = lambda default_value: defaultdict(lambda: default_value)
flush = lambda: stdout.flush()
print_flush = lambda _text: (print(_text), flush())


def print_dp(_dict):
    for item in _dict.items():
        print(f"{item[0]} = {item[1]}")


MOD = 10 ** 9 + 7
INF = maxsize
A = 911382323
M = 9999999999879998


# -------------------------------------------------------Solution-------------------------------------------------------
def get_kth_bit(n, k):
    return (n & (1 << (k - 1))) >> (k - 1)


def is_possible_to_get_max(pre, a, b, n):
    _counts = _dp(0)

    for i in range(n):
        _counts[a[i] & pre] += 1
        _counts[(b[i] & pre) ^ pre] -= 1

    for value in _counts.values():
        if value != 0:
            return False

    return True


def solve():
    n = iinp()
    a = intl()
    b = intl()

    ans = 0
    for bit in range(30, -1, -1):
        if is_possible_to_get_max(ans | (1 << bit), a, b, n):
            ans |= 1 << bit

    return ans


def run():
    t = iinp()

    for _ in range(t):
        print(solve())


if __name__ == "__main__":
    if os.environ.get("DEBUG_CODEFORCES"):
        stdin = open("../../input.txt", "r")
        start_time = time.time()
        run()
        print("\n--- %s seconds ---\n" % (time.time() - start_time))
    else:
        run()
