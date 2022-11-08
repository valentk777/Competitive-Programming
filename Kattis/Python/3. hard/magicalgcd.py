# -----------------------------------------------------------
# URL    : https://open.kattis.com/problems/magicalgcd
# Title  : Magical GCD
# Notes  : tag-kattis, tag-hard, tag-not-pass
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


def print_dp(_dict):
    for item in _dict.items():
        print(f"{item[0]} = {item[1]}")


MOD = 10 ** 9 + 7
INF = maxsize
A = 911382323
M = 9999999999879998


# -------------------------------------------------------Solution-------------------------------------------------------

def solve():
    n = iinp()
    a = intl()

    if n == 1:
        return a[0]

    # gcd, value
    dp = [[0, 0] for _ in range(n + 1)]

    for i in range(1, n + 1):
        new_gcd =  math.gcd(dp[i - 1][0], a[i-1])

        if new_gcd > dp[i - 1][0]


        dp[i][0] = max(a[i-1], dp[i - 1][0])
        dp[i][1] = max()

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
