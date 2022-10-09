# -----------------------------------------------------------
# URL    : https://open.kattis.com/problems/datum
# Title  : Datum
# Notes  : tag-kattis
# -----------------------------------------------------------

# ---------------------------------------------------Shared part--------------------------------------------------------
import os
import time
from collections import defaultdict
from sys import stdin, maxsize

inp = lambda: stdin.readline().strip("\n")
iinp = lambda: int(inp())
intl = lambda: list(map(int, inp().split()))
strl = lambda: list(inp().split())
list_to_string = lambda _a: "".join(map(str, _a))
list_to_string_list = lambda _a: " ".join(map(str, _a))
_dp = lambda default_value: defaultdict(lambda: default_value)
print_dp = lambda _dict: list(map(lambda item: print(f"{item[0]} = {item[1]}"), _dict.items()))
list_from_inp = lambda n: [inp() for _ in range(n)]

MOD = 10 ** 9 + 7
INF = maxsize

# -------------------------------------------------------Solution-------------------------------------------------------

day_map = {
    0: "Thursday",
    1: "Friday",
    2: "Saturday",
    3: "Sunday",
    4: "Monday",
    5: "Tuesday",
    6: "Wednesday",
}


def solve():
    x = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    d, m = intl()

    day_in_year = 0

    for i in range(1, m):
        day_in_year += x[i - 1]

    day_in_year += d

    return day_map[(day_in_year - 1) % 7]


def run():
    print(solve())


if __name__ == "__main__":
    if os.environ.get("DEBUG_CODEFORCES"):
        stdin = open("input.txt", "r")
        start_time = time.time()
        run()
        print("\n--- %s seconds ---\n" % (time.time() - start_time))
    else:
        run()
