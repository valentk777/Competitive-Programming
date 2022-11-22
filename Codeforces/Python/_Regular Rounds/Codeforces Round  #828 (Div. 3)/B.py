# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/1744/problem/B
# Title  : B. Even-Odd Increments
# Tags   : tag-codeforces, tag-problem-B, tag-div-3
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
    n, q = intl()
    a = intl()

    _even = 0
    _odd = 0
    _sum = 0

    for i in range(n):
        _sum += a[i]

        if a[i] & 1 == 0:
            _even += 1
        else:
            _odd += 1

    for k in range(q):
        t, x = intl()

        if t == 0:
            _sum += _even * x

            if x & 1 == 1:
                _odd += _even
                _even = 0
        else:
            _sum += _odd * x

            if x & 1 == 1:
                _even += _odd
                _odd = 0

        print(_sum)


def run():
    t = iinp()

    for _ in range(t):
        solve()


if __name__ == "__main__":
    if os.environ.get("DEBUG_CODEFORCES"):
        stdin = open("../../input.txt", "r")
        start_time = time.time()
        run()
        print("\n--- %s seconds ---\n" % (time.time() - start_time))
    else:
        run()
