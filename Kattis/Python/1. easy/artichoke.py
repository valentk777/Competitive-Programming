# -----------------------------------------------------------
# URL    : https://open.kattis.com/problems/artichoke
# Title  : Amalgamated Artichokes
# Notes  : tag-kattis, tag-easy
# -----------------------------------------------------------

# ---------------------------------------------------Shared part--------------------------------------------------------
import os
import time
from collections import defaultdict
from math import sin, cos
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
A = 911382323
M = 9999999999879998


# -------------------------------------------------------Solution-------------------------------------------------------


def solve():
    p, a, b, c, d, n = intl()

    def price(k):
        return p * (sin(a * k + b) + cos(c * k + d) + 2)

    prices = []

    for i in range(1, n + 1):
        prices.append(price(i))

    max_price = 0
    max_decline = 0

    for i in range(n):
        diff = max_price - prices[i]

        if diff > max_decline:
            max_decline = diff

        if diff < 0:
            max_price = prices[i]

    return max_decline


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
