# -----------------------------------------------------------
# URL    : https://codeforces.com/contest/1740/problem/B
# Title  : B. Jumbo Extra Cheese 2
# Notes  : tag-codeforces, tag-problem-B, tag-div-1
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

def solve():
    n = iinp()

    x = []
    y = []

    for i in range(n):
        _x, _y = intl()

        if _x < _y:
            x.append(_x)
            y.append(_y)
        else:
            x.append(_y)
            y.append(_x)

    ans = 2 * sum(x)

    y = sorted(y)

    ans += y[0]

    for i in range(1, n):
        ans += (y[i] - y[i - 1])

    ans += y[-1]

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
