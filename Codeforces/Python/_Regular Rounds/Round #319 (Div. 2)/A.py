# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/577/problem/A
# Title  : A. Multiplication Table
# Tags   : tag-codeforces, tag-problem-A, tag-div-2
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
    n, x = intl()

    if x > n ** 2:
        return 0

    divisors = get_divisors(x)

    if x <= n:
        return len(divisors)

    ans = 0
    len_div = len(divisors)

    if len_div & 1 == 0:
        for i in range(0, len_div, 2):
            if divisors[i] <= n:
                ans += 2
    else:
        for i in range(0, len_div - 1, 2):
            if divisors[i] <= n:
                ans += 2

        if divisors[-1] <= n:
            ans += 1

    return ans


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
