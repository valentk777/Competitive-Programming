# -----------------------------------------------------------
# URL    : https://open.kattis.com/problems/almostperfect
# Title  : Almost Perfect
# Notes  : tag-kattis, tag-medium
# -----------------------------------------------------------

# ---------------------------------------------------Shared part--------------------------------------------------------
import os
import time
from collections import defaultdict
from math import sqrt
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
    n = iinp()

    divisors = get_divisors(n)
    divisors_sum = sum(divisors) - n

    is_perfect = divisors_sum == n
    is_almost_perfect = n - 2 <= divisors_sum <= n + 2

    if is_perfect:
        print(n, "perfect")
    elif is_almost_perfect:
        print(n, "almost perfect")
    else:
        print(n, "not perfect")


def run():
    try:
        while True:
            solve()
    except:
        pass


if __name__ == "__main__":
    if os.environ.get("DEBUG_CODEFORCES"):
        stdin = open("../input.txt", "r")
        start_time = time.time()
        run()
        print("\n--- %s seconds ---\n" % (time.time() - start_time))
    else:
        run()
