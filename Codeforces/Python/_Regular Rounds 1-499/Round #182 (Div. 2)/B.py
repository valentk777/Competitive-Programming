# -----------------------------------------------------------
# URL    : https://codeforces.com/contest/302/problem/B
# Title  : B. Eugeny and Play List
# Notes  : tag-codeforces, tag-problem-B, tag-div-2
# -----------------------------------------------------------

# ---------------------------------------------------Shared part--------------------------------------------------------
import os
import time
from bisect import bisect_left
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

# time limit / memory limit
def solve_slow():
    n, m = intl()

    songs_numbers = [0]
    songs_end_time = [0]

    for i in range(1, n + 1):
        c, t = intl()
        songs_numbers.append(songs_numbers[-1] + c)

        for j in range(c):
            songs_end_time.append(songs_end_time[-1] + t)

    v_list = intl()

    for v in v_list:
        value = bisect_left(songs_end_time, v)
        number = bisect_left(songs_numbers, value)
        print(number)


def solve():
    n, m = intl()

    songs_end_time = [0]

    for i in range(1, n + 1):
        c, t = intl()
        songs_end_time.append(songs_end_time[-1] + (t * c))

    v_list = intl()

    for v in v_list:
        value = bisect_left(songs_end_time, v)
        print(value)


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
