# -----------------------------------------------------------
# URL    : https://open.kattis.com/problems/nonprimefactors
# Title  : Non-Prime Factors
# Notes  : tag-kattis, tag-hard, tag-not-pass
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

_cache = _dp(0)


def get_factorization(x):
    count = 0
    v = []

    # Loop to find the divisors of the number 2
    while x % 2 == 0:
        count += 1
        x = x // 2

    if count != 0:
        v.append(count)

    # Loop to find the divisors of the given number up to SQRT(N)
    for i in range(3, int(sqrt(x)) + 12):
        count = 0

        while x % i == 0:
            count += 1
            x //= i

        if count != 0:
            v.append(count)

    # Condition to check if the rest number is also a prime number
    if x > 1:
        v.append(1)

    return v


# Function to find the non-prime divisors of the given number
def non_prime_divisors(number):
    v = get_factorization(number)
    ret = 1

    # Loop to count the number of the total divisors of given number
    for i in range(len(v)):
        ret = ret * (v[i] + 1)

    ret = ret - len(v)

    return ret


def solve():
    n = iinp()

    if _cache[n] == 0:
        _cache[n] = non_prime_divisors(n)

    return _cache[n]


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
