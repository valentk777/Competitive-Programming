# -----------------------------------------------------------
# URL    : https://open.kattis.com/problems/bijele
# Title  : Bijele
# Notes  : tag-kattis, tag-easy
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

def solve():
    _set = intl()
    ats = []

    for i in range(0, 2):
        ats.append(1 - _set[i])

    for i in range(2, 5):
        ats.append(2 - _set[i])

    for i in range(5, 6):
        ats.append(8 - _set[i])

    return list_to_string_list(ats)


def run():
    print(solve())


if __name__ == "__main__":
    if os.environ.get("DEBUG_CODEFORCES"):
        stdin = open("../input.txt", "r")
        start_time = time.time()
        run()
        print("\n--- %s seconds ---\n" % (time.time() - start_time))
    else:
        run()
