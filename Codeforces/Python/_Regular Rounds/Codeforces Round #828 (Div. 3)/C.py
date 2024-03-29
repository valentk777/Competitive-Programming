# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/1744/problem/C
# Title  : Traffic Light
# Tags   : tag-codeforces, tag-problem-C, tag-div-3, tag-difficulty-1000
# Notes  : binary search, implementation, two pointers
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
    n, c = strl()
    n = int(n)
    s = inp()

    if c == "g":
        return 0

    n_2 = n * 2
    s += s
    _max = -INF
    i = 0
    _count = 1

    while i < n_2:
        _count = 1

        if s[i] == c:
            for j in range(i + 1, n_2):
                if i > n:
                    i = n_2 + 1
                    break

                if s[j] == "g":
                    _max = max(_max, _count)
                    i = j
                    break

                _count += 1

        i += 1

    return _max


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
