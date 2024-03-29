# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/1479/problem/B1
# Title  : Painting the Array I
# Tags   : tag-codeforces, tag-problem-D, tag-div-2, tag-difficulty-1900, tag-not-pass
# Notes  : constructive algorithms, data structures, dp, greedy, implementation
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
    a = intl()

    # dp = _dp(0)

    _count = 1
    last_1 = a[0]
    last_2 = INF

    for i in range(1, n + 1):
        if a[i] != last_1:
            last_1 = a[i]
            _count += 1
        elif a[i] != last_2:
            last_2 = a[i]
            _count += 1

    return _count


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
