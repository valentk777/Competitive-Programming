# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/1753/problem/A1
# Title  : Make Nonzero Sum (easy version)
# Tags   : tag-codeforces, tag-problem-A, tag-div-1, tag-difficulty-1300
# Notes  : constructive algorithms, dp, greedy
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

def solve_c2():
    n = iinp()
    a = intl()

    if (n - a.count(0)) % 2 != 0:
        print(-1)
        return

    ans = []
    i = 0

    temp_number = 0
    temp_idx = -1

    while i < n:
        # if 0, we can add all zeros except between two ones
        if a[i] == 0:
            if temp_number == 0:
                ans.append((i + 1, i + 1))

            i += 1

        # if we here, it means a[i] != 0.
        # If we have a single one somewhere, we need to add another one and close section
        elif temp_number != 0:
            if temp_number == a[i]:
                ans.append((temp_idx + 1, i - 1))
                ans.append((i, i + 1))
            else:
                ans.append((temp_idx + 1, i))
                ans.append((i + 1, i + 1))

            temp_number = 0
            temp_idx = -1
            i += 1
            continue

        # equal (1, 1) or (-1, -1) -> 0
        elif a[i] == a[i + 1]:
            ans.append((i + 1, i + 2))
            i += 2

        # (-1, 1) or (1, -1) -> 0
        elif a[i] + a[i + 1] == 0:
            ans.append((i + 1, i + 1))
            ans.append((i + 2, i + 2))
            i += 2

        # (1, 0), (-1, 0)
        else:
            temp_number = a[i]
            temp_idx = i
            i += 2

    print(len(ans))

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
