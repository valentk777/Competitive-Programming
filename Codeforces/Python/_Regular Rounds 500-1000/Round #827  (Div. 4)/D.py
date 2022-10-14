# -----------------------------------------------------------
# URL    : https://codeforces.com/contest/1742/problem/D
# Title  : Coprime
# Notes  : tag-codeforces, tag-problem-D, tag-div-4
# -----------------------------------------------------------

# ---------------------------------------------------Shared part--------------------------------------------------------
import os
import time
from collections import defaultdict
from math import gcd
from sys import stdin, maxsize

inp = lambda: stdin.readline().strip()
iinp = lambda: int(inp())
intl = lambda: list(map(int, inp().split()))
strl = lambda: list(inp().split())
list_to_string = lambda _a: "".join(map(str, _a))
list_to_string_list = lambda _a: " ".join(map(str, _a))
_dp = lambda default_value: defaultdict(lambda: default_value)
print_dp = lambda _dict: list(map(lambda item: print(f"{item[0]} = {item[1]}"), _dict.items()))

MOD = 10 ** 9 + 7
INF = maxsize


# -------------------------------------------------------Solution-------------------------------------------------------

def solve():
    n = iinp()
    a = intl()

    _numbers = _dp(-1)

    for i in range(n):
        _numbers[a[i]] = max(_numbers[a[i]], i + 1)

    _max = -1

    keys = list(_numbers.keys())
    n_keys = len(keys)

    for i in range(n_keys):
        for j in range(i, n_keys):
            if _max < _numbers[keys[i]] + _numbers[keys[j]]:
                if gcd(keys[i], keys[j]) == 1:
                    _max = _numbers[keys[i]] + _numbers[keys[j]]

    return _max


def run():
    t = iinp()

    for _ in range(t):
        print(solve())


if __name__ == "__main__":
    if os.environ.get("DEBUG_CODEFORCES"):
        stdin = open("../input.txt", "r")
        start_time = time.time()
        run()
        print("\n--- %s seconds ---\n" % (time.time() - start_time))
    else:
        run()
