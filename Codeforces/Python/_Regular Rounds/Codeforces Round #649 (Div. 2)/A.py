# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/1364/problem/A
# Title  : A. XXXXX
# Tags   : tag-codeforces, tag-problem-A, tag-div-2
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
    n, x = intl()
    a = intl()

    sum_a = sum(a)

    if sum_a % x != 0:
        return n

    first_idx = -1

    for i in range(n):
        if a[i] % x != 0:
            first_idx = i
            break

    if first_idx == -1:
        return -1

    last_index = -1

    for i in range(n - 1, -1, -1):
        if a[i] % x != 0:
            last_index = i
            break

    return max(n - (first_idx + 1), last_index)


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
