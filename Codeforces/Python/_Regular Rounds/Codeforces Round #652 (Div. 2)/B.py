# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/1369/problem/B
# Title  : AccurateLee
# Tags   : tag-codeforces, tag-problem-B, tag-div-2, tag-difficulty-1200
# Notes  : greedy, implementation, strings
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
    n = iinp()
    s = list(map(int, inp()))

    is_increasing = True
    start = True
    end = False

    zeros = 0
    ones = 0

    if s[0] == 0:
        zeros += 1
    else:
        start = False
        end = True

    for i in range(1, n):
        if is_increasing and s[i - 1] > s[i]:
            is_increasing = False

        if start:
            if s[i] == 0:
                zeros += 1
                continue
            else:
                start = False
                end = True
                ones += 1
                continue

        if end:
            if s[i] == 0:
                ones = 0
            else:
                ones += 1

    if is_increasing:
        return list_to_string(s)

    return "0" * (zeros + 1) + "1" * ones


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
