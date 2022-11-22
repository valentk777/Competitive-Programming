# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/381/problem/A
# Title  : A. Sereja and Dima
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
    n = iinp()
    a = intl()

    left = 0
    right = n - 1

    ans_s = 0
    ans_d = 0

    for i in range(n):
        if a[left] < a[right]:
            select = a[right]
            right -= 1
        else:
            select = a[left]
            left += 1

        if i & 1 == 0:
            ans_s += select
        else:
            ans_d += select

    return ans_s, ans_d


def run():
    print(*solve())


if __name__ == "__main__":
    if os.environ.get("DEBUG_CODEFORCES"):
        stdin = open("../../input.txt", "r")
        start_time = time.time()
        run()
        print("\n--- %s seconds ---\n" % (time.time() - start_time))
    else:
        run()
