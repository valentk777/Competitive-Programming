# -----------------------------------------------------------
# URL    : https://open.kattis.com/problems/janitortroubles
# Title  : Janitor Troubles
# Notes  : tag-kattis
# -----------------------------------------------------------

# ---------------------------------------------------Shared part--------------------------------------------------------
import os
import time
from collections import defaultdict
from math import sqrt
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

def solve():
    a, b, c, d = intl()

    semi_perimeter = (a + b + c + d) / 2
    return sqrt((semi_perimeter - a) * (semi_perimeter - b) * (semi_perimeter - c) * (semi_perimeter - d))


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
