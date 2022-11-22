# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/1133/problem/D
# Title  : D. Zero Quantity Maximization
# Tags   : tag-codeforces, tag-problem-D, tag-div-3
# ---------------------------------------------------------------------------------------

# ---------------------------------------------------Shared part--------------------------------------------------------
import os
import time
from collections import defaultdict
from fractions import Fraction
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
    b = intl()

    ans = 0
    d = _dp(0)

    for i in range(n):
        # count zeros
        if a[i] == b[i] == 0:
            ans += 1
        elif a[i] != 0:
            d[Fraction(b[i], a[i])] += 1

    if len(d.values()) == 0:
        return ans
    else:
        return ans + max(d.values())


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
