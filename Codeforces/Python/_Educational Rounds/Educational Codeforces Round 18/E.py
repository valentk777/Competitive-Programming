# -----------------------------------------------------------
# URL    : https://codeforces.com/contest/792/problem/E
# Title  : E. Colored Balls
# Notes  : tag-codeforces, tag-problem-E, tag-not-pass
# -----------------------------------------------------------

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

def get_min(a, b, k):
    ans = 0

    while k % b != 0 and k > 0:
        k -= a
        ans += 1

    if k >= 0:
        ans += k // b
        return ans
    else:
        return INF


def solve():
    n = iinp()
    a = intl()
    a = sorted(a)

    _min = a[0]

    ans_1 = 0

    for i in range(n):
        ans_1 += get_min(_min - 1, _min, a[i])

    ans_2 = 0

    for i in range(n):
        ans_2 += get_min(_min, _min + 1, a[i])

    return min(ans_1, ans_2)


def run():
    print(solve())


if __name__ == "__main__":
    if os.environ.get("DEBUG_CODEFORCES"):
        stdin = open("../../input.txt", "r")
        start_time = time.time()
        run()
        print("\n--- %s seconds ---\n" % (time.time() - start_time))
    else:
        run()
