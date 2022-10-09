# -----------------------------------------------------------
# URL    : https://open.kattis.com/problems/acearbiter
# Title  : Ace Arbiter
# Notes  : tag-kattis
# -----------------------------------------------------------

# ---------------------------------------------------Shared part--------------------------------------------------------
import os
import time
from collections import defaultdict
from math import floor
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
    n = iinp()
    a, b = list(map(int, inp().split("-")))
    _a = a
    _b = b
    is_end = a == 11 or b == 11

    if a == 11 and b == 11:
        return f"error {1}"

    for i in range(1, n):
        a, b = list(map(int, inp().split("-")))

        if a == _a and b == _b:
            continue

        if floor((_a + _b + 1) / 2.0) % 2 != floor((a + b + 1) / 2.0) % 2:
            _a, _b = _b, _a

        if a < _a or b < _b:
            return f"error {i + 1}"

        if is_end:
            return f"error {i + 1}"
        else:
            is_end = a == 11 or b == 11

        _a = a
        _b = b

    return "ok"


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
