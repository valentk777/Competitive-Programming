# -----------------------------------------------------------
# URL    : https://codeforces.com/contest/1754/problem/C1
# Title  : C1. Make Nonzero Sum (easy version)
# Notes  : tag-codeforces, tag-problem-C, tag-div-2
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

# not working
def solve_c2():
    n = iinp()
    a = intl()

    ans = []
    i = 0

    while i < n:
        # equal (0, 0) or (1, 1) or (-1, -1) -> 0
        if a[i - 1] == a[i]:
            ans.append((i, i + 1))

        # (-1, 1) or (1, -1) -> 0
        elif a[i - 1] + a[i] == 0:
            ans.append((i, i))
            ans.append((i + 1, i + 1))

        # (1, 0), (0, 1) (-1, 0), (0, -1)
        else:
            print("xxxx")
            print(i, i + 1)

        i += 2

    print(len(ans))

    # if n & 1 == 1:
    #     print(-1)
    #     return

    for pair in ans:
        print(*pair)


def solve_c1():
    n = iinp()
    a = intl()

    ans = []

    if n & 1 == 1:
        print(-1)
        return
    for i in range(1, n, 2):
        # equal (1, 1) or (-1, -1) -> 0
        if a[i - 1] == a[i]:
            ans.append((i, i + 1))

        # (-1, 1) or (1, -1) -> 0
        else:
            ans.append((i, i))
            ans.append((i + 1, i + 1))

    print(len(ans))

    for pair in ans:
        print(*pair)


def run():
    t = iinp()

    for _ in range(t):
        solve_c2()


if __name__ == "__main__":
    if os.environ.get("DEBUG_CODEFORCES"):
        stdin = open("../../input.txt", "r")
        start_time = time.time()
        run()
        print("\n--- %s seconds ---\n" % (time.time() - start_time))
    else:
        run()
