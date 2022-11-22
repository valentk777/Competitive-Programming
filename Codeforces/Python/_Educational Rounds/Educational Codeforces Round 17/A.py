# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/762/problem/A
# Title  : A. k-th divisor
# Tags   : tag-codeforces, tag-problem-A
# ---------------------------------------------------------------------------------------

# ---------------------------------------------------Shared part--------------------------------------------------------
import os
import time
from collections import defaultdict
from math import sqrt
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

def get_divisors(n):
    i = 1
    divisors = []

    while i <= sqrt(n):
        if n % i == 0:
            if n / i != i:
                divisors.append(n // i)

            divisors.append(i)

        i = i + 1

    return divisors


def solve():
    n, k = intl()

    divisors = get_divisors(n)
    divisors = sorted(divisors)

    if len(divisors) < k:
        return -1
    else:
        return divisors[k - 1]


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
