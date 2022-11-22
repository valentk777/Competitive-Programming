# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/162/problem/C
# Title  : Prime factorization
# Tags   : tag-codeforces, tag-problem-C, tag-difficulty-1800
# Notes  : *special
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

def get_prime_factors(n):
    factors = []

    c = 2

    while n > 1:

        if n % c == 0:
            factors.append(c)
            n = n / c
        else:
            c = c + 1

    return factors


def solve():
    n = iinp()
    prime_factors = get_prime_factors(n)
    return "*".join(map(str, prime_factors))


def run():
    print(solve())


if __name__ == "__main__":
    if os.environ.get("DEBUG_CODEFORCES"):
        stdin = open("../../input.txt", "r")
        start_time = time.time()
        run()
        print("\n--- %s seconds ---\n" % (time.time() - start_time))
    else:
        run()
