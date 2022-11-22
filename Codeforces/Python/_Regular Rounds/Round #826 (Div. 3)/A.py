# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/1741/problem/A
# Title  : Compare T-Shirt Sizes
# Tags   : tag-codeforces, tag-problem-A, tag-div-3
# ---------------------------------------------------------------------------------------

# ---------------------------------------------------Shared part--------------------------------------------------------
import os
import time
from collections import defaultdict
from sys import stdin, maxsize

inp = lambda: stdin.readline().strip()
iinp = lambda: int(inp())
intl = lambda: list(map(int, inp().split()))
strl = lambda: list(inp().split())
list_to_string = lambda _a: "".join(map(str, _a))
list_to_string_list = lambda _a: " ".join(map(str, _a))
_dp = lambda default_value: defaultdict(lambda: default_value)
print_dp = lambda _dict: list(map(lambda item: print(f"{item[0]} = {item[1]}"), _dict.items()))

MOD = 10 ** 9 + 7
INF = maxsize


# -------------------------------------------------------Solution-------------------------------------------------------

def solve():
    a, b = strl()

    if a == b:
        return "="

    len_a = len(a)
    len_b = len(b)

    if a[-1] == "S":
        if b[-1] == "M" or b[-1] == "L":
            return "<"
        else:
            if len_a > len_b:
                return "<"
            else:
                return ">"

    if a[-1] == "M":
        if b[-1] == "L":
            return "<"
        else:
            return ">"

    if a[-1] == "L":
        if b[-1] == "M" or b[-1] == "S":
            return ">"
        else:
            if len_a < len_b:
                return "<"
            else:
                return ">"


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
