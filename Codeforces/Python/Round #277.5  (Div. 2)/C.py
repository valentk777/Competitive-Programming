# -----------------------------------------------------------
# URL    : https://codeforces.com/contest/489/problem/C
# Title  : Given Length and Sum of Digits...
# Notes  : tag-codeforces, tag-problem-C, tag-div-2
# -----------------------------------------------------------

# ---------------------------------------------------Shared part--------------------------------------------------------
import os
import time
from sys import stdin, maxsize

inp = lambda: stdin.readline().strip()
iinp = lambda: int(inp())
intl = lambda: list(map(int, inp().split()))
strl = lambda: list(inp().split())
list_to_string = lambda _a: " ".join(map(str, _a))

MOD = 10 ** 9 + 7
INF = maxsize


# -------------------------------------------------------Solution-------------------------------------------------------


def solve():
    m, s = intl()  # len and sum of digits

    max_number = []
    min_number = []
    max_s = s
    min_s = s

    for i in range(m - 1):
        _max_possible = min(9, max_s)
        max_number.append(_max_possible)
        max_s -= _max_possible

        _max_possible = min(9, min_s - 1)
        min_number.append(_max_possible)
        min_s -= _max_possible

    max_number.append(min(9, max_s))
    min_number.append(min(9, min_s))

    if (s == 0 and m > 1) or sum(min_number) != sum(max_number) or len(max_number) != m or sum(max_number) != s:
        print(-1, -1)
    else:
        max_number = "".join(map(str, max_number))
        min_number = "".join(map(str, reversed(min_number)))
        print(min_number, max_number)


def run():
    solve()


if __name__ == "__main__":
    if os.environ.get("DEBUG_CODEFORCES"):
        stdin = open("../input.txt", "r")
        start_time = time.time()
        run()
        print("\n--- %s seconds ---\n" % (time.time() - start_time))
    else:
        run()
