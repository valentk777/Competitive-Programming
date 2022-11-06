# -----------------------------------------------------------
# URL    : https://codeforces.com/contest/230/problem/B
# Title  : B. T-primes
# Notes  : tag-codeforces, tag-problem-B, tag-div-2
# -----------------------------------------------------------

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
print_std = lambda x: stdout.write(x)
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


def count_divisors(n):
    i = 1
    count = 0
    _sqrt = sqrt(n)

    while i <= _sqrt:
        if n % i == 0:
            if n / i != i:
                count += 1

            count += 1

            if count > 3:
                break

        i = i + 1

    return count == 3


def solve_slow():
    n = iinp()
    x = intl()

    ans = ["" for i in range(n)]

    for i in range(n):
        if count_divisors(x[i]):
            ans[i] = "YES"
        else:
            ans[i] = "NO"

    print("\n".join(map(str, ans)))


def is_square_of_prime(k):
    if k == 1:
        return False

    n = int(sqrt(k))

    if n * n != k:
        return False

    i = 2

    while i * i <= n:
        if n / i == n // i:
            return False

        i += 1

    return True


def solve_faster_still_slow():
    n = iinp()
    x = intl()

    for i in range(n):
        if is_square_of_prime(x[i]):
            print("YES")
        else:
            print("NO")


def get_all_prime_squares(max_value):
    a = [1] * max_value
    s = set()

    for i in range(2, max_value):
        if a[i]:
            s.add(i * i)

            for j in range(i * i, max_value, i):
                a[j] = 0

    return s


def solve():
    max_value = 1000000
    all_numbers = get_all_prime_squares(max_value)

    n = iinp()
    x = intl()

    for i in range(n):
        if x[i] in all_numbers:
            print("YES")
        else:
            print("NO")


def run():
    solve()


if __name__ == "__main__":
    if os.environ.get("DEBUG_CODEFORCES"):
        stdin = open("../../input.txt", "r")
        start_time = time.time()
        run()
        print("\n--- %s seconds ---\n" % (time.time() - start_time))
    else:
        run()
