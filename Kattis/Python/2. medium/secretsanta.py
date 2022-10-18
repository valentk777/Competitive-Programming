# -----------------------------------------------------------
# URL    : https://open.kattis.com/problems/secretsanta
# Title  : Secret Santa
# Notes  : tag-kattis, tag-medium
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
A = 911382323
M = 9999999999879998


# -------------------------------------------------------Solution-------------------------------------------------------

def factorial(n):
    if n > 10:
        return 1000000
    if n == 1 or n == 2:
        return n
    else:
        return n * factorial(n - 1)


def solve():
    n = iinp()

    if n > 10:
        n = 10

    prob = 0.0

    for i in range(1, n + 1):
        prob += (-1) ** (i + 1) * 1 / factorial(i)

    return prob


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
