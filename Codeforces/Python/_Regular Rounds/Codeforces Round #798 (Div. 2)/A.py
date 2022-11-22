# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/1689/problem/A
# Title  : Lex String
# Tags   : tag-codeforces, tag-problem-A, tag-div-2, tag-difficulty-800
# Notes  : brute force, greedy, implementation, sortings, two pointers
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

def solve():
    n, m, k = intl()
    a = inp()
    a = sorted(a)

    b = inp()
    b = sorted(b)

    c = []

    left_a = 0
    left_b = 0
    k_a = 0
    k_b = 0

    while left_a < n and left_b < m:
        if a[left_a] <= b[left_b] and k_a < k:
            c.append(a[left_a])
            k_a += 1
            k_b = 0
            left_a += 1
        elif a[left_a] >= b[left_b] and k_b < k:
            c.append(b[left_b])
            k_b += 1
            k_a = 0
            left_b += 1
        elif k_a < k:
            c.append(a[left_a])
            k_a += 1
            k_b = 0
            left_a += 1
        elif k_b < k:
            c.append(b[left_b])
            k_b += 1
            k_a = 0
            left_b += 1

    return list_to_string(c)


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
