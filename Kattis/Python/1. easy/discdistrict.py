# -----------------------------------------------------------
# URL    : https://open.kattis.com/problems/discdistrict
# Title  : Disc District
# Notes  : tag-kattis, tag-easy
# -----------------------------------------------------------

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
list_from_inp = lambda n: [inp() for _ in range(n)]

MOD = 10 ** 9 + 7
INF = maxsize


# -------------------------------------------------------Solution-------------------------------------------------------

def solve():
    r = iinp()
    print(1, r)


def solve_2():
    r = iinp()
    r2 = r ** 2
    x, y = 0, 0
    _min = INF

    for _x in range(r + 1):
        for _y in range(r + 1):
            s = _x ** 2 + _y ** 2

            if s - r2 > 0:
                if s < _min:
                    _min = s
                    x = _x
                    y = _y

    print(x, y)


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
