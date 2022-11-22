# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/1692/problem/F
# Title  : 3SUM
# Tags   : tag-codeforces, tag-problem-F, tag-div-4, tag-difficulty-1300
# Notes  : brute force, math
# ---------------------------------------------------------------------------------------

# ---------------------------------------------------Shared part--------------------------------------------------------
import math
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
fact = lambda number: math.factorial(number)
cnt = lambda _a: Counter(_a)


def lcm(a, b):
    return a * b // math.gcd(a, b)


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
    a = strl()
    a = list(map(lambda ix: int(ix[-1]), a))

    _count = cnt(a)

    xxx = []
    for x in range(10):
        for y in range(10):
            for z in range(10):
                if str(x + y + z)[-1] == "3":
                    new_count = _count.copy()

                    if new_count[x] == 0:
                        continue
                    else:
                        new_count[x] -= 1

                    if new_count[y] == 0:
                        continue
                    else:
                        new_count[y] -= 1

                    if new_count[z] == 0:
                        continue
                    else:
                        new_count[z] -= 1

                    return "YES"

    return "NO"


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
