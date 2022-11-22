# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/1747/problem/C
# Title  : Swap Game
# Tags   : tag-codeforces, tag-problem-C, tag-div-2, tag-difficulty-1200, tag-not-pass
# Notes  : games
# ---------------------------------------------------------------------------------------

# ---------------------------------------------------Shared part--------------------------------------------------------
import os
import time
from collections import defaultdict, Counter
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

    _count = Counter(a)

    if a[0] == 1:
        return "Bob"

    if _count[1] > 0:
        return "Alice"

    _count[a[0]] -= 1
    _count[a[0] - 1] += 1

    print(_count)

    # for key, value in _count.items():

    if sum(a) & 1 == 0:
        return "Bob"
    else:
        return "Alice"


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
