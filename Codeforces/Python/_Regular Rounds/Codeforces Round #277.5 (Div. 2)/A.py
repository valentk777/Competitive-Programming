# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/489/problem/A
# Title  : SwapSort
# Tags   : tag-codeforces, tag-problem-A, tag-div-2, tag-difficulty-1200
# Notes  : greedy, implementation, sortings
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
    n = iinp()
    a = intl()

    sorted_a = sorted(a)

    ans = 0
    swaps = []

    for i in range(n):
        if a[i] != sorted_a[i]:
            for j in range(i + 1, n):
                if a[j] == sorted_a[i]:
                    ans += 1
                    swaps.append((i, j))
                    a[j] = a[i]
                    break

    print(ans)
    for swap in swaps:
        print(*swap)


def run():
    solve()


if __name__ == "__main__":
    if os.environ.get("DEBUG_CODEFORCES"):
        stdin = open("../../input.txt", "r")
        start_time = time.time()
        run()
        print("\n--- %s seconds ---\n" % (time.time() - start_time))
    else:
        run()
