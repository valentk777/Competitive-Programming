# -----------------------------------------------------------
# URL    : https://codeforces.com/contest/1419/problem/B
# Title  : B. Stairs
# Notes  : tag-codeforces, tag-problem-B, tag-div-2
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

def arithmetic_progression_sum(a1, an, n):
    return (a1 + an) * n // 2


def solve():
    x = iinp()

    _nice_stairs = []
    _correct = 1

    while _correct < x + 1:
        _nice_stairs.append(_correct)
        _correct = (_correct * 2) + 1

    _sum = 0
    ans = 0

    for stair in _nice_stairs:
        _sum += arithmetic_progression_sum(1, stair, stair)
        ans += 1

        if _sum > x:
            ans -= 1
            break

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
