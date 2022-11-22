# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/1742/problem/C
# Title  : Stripes
# Tags   : tag-codeforces, tag-problem-C, tag-div-4, tag-difficulty-900
# Notes  : implementation
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
    inp()
    matrix = [list(inp()) for _ in range(8)]

    for row in range(8):
        s = list(set(matrix[row]))

        if len(s) == 1 and (s[0] == "R"):
            return s[0]

    for column in range(8):
        s = set()

        for row in range(8):
            s.add(matrix[row][column])

        s = list(s)

        if len(s) == 1 and s[0] == "B":
            return s[0]


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
