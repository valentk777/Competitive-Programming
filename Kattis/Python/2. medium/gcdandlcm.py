# -----------------------------------------------------------
# URL    : https://open.kattis.com/problems/gcdandlcm
# Title  : GCD and LCM
# Notes  : tag-kattis, tag-medium, tag-not-pass
# -----------------------------------------------------------

# ---------------------------------------------------Shared part--------------------------------------------------------
import math
import os
import time
from collections import defaultdict, Counter
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
fact = lambda number: math.factorial(number)
cnt = lambda _a: Counter(_a)


def lcm(a, b):
    return a * b // math.gcd(a, b)


def print_dp(_dict):
    for item in _dict.items():
        print(f"{item[0]} = {item[1]}")


MOD = 10 ** 9 + 7
INF = maxsize
A = 911382323
M = 9999999999879998


# -------------------------------------------------------Solution-------------------------------------------------------

def solve():
    x, y = intl()

    ans = set()
    _multi = x * y

    for i in range(x, (y >> 1) + 1):
        j = x

        while j <= y and i * j <= _multi:
            if i * j == _multi and math.gcd(i, j) == x:
                ans.add(i)
                ans.add(j)

            j += 1

    ans = sorted(ans)

    for e in ans:
        print(e, _multi // e)


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
