# -----------------------------------------------------------
# URL    : https://codeforces.com/contest/1744/problem/D
# Title  : D. Divisibility by 2^n
# Notes  : tag-codeforces, tag-problem-D, tag-div-3
# -----------------------------------------------------------

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
# fast
def count_number_of_2_divisors(x):
    ans = 0

    while x & 1 == 0:
        ans += 1
        x //= 2

    return ans


# # slower
# def count_number_of_2_divisors(x):
#     ans = 0
#     power = ceil(log(x) / log(2))
#     next_two = pow(2, power)
#
#     for p in range(power, 0, -1):
#
#         if x % next_two == 0:
#             ans += p
#             break
#
#         next_two >>= 1
#
#     return ans


# slow
def count_number_of_n_divisors(x, n):
    return 0 if x % n else count_number_of_n_divisors(x // n, n) + 1


def solve():
    n = iinp()
    a = intl()

    count_number_of_2 = 0

    for i in range(n):
        count_number_of_2 += count_number_of_2_divisors(a[i])

    if count_number_of_2 >= n:
        return 0

    powers = []

    for i in range(1, n + 1):
        powers.append(count_number_of_2_divisors(i))

    powers.sort(reverse=True)

    ans = 0

    for i in range(len(powers)):
        count_number_of_2 += powers[i]
        ans += 1

        if count_number_of_2 >= n:
            return ans

    if count_number_of_2 >= n:
        return ans

    return -1


def solve_with_log_2():
    n = iinp()
    a = intl()

    count_number_of_2 = sum(map(lambda x: count_number_of_n_divisors(x, 2), a))

    if count_number_of_2 >= n:
        return 0

    i = 0
    ans = 0
    addition = list(sorted(map(lambda x: count_number_of_n_divisors(x, 2), range(1, n + 1)), reverse=True))

    while count_number_of_2 < n and i < n:
        ans += 1
        count_number_of_2 += addition[i]
        i += 1

    if count_number_of_2 >= n:
        return ans

    return -1


def run():
    t = iinp()

    for _ in range(t):
        # print(solve())
        print(solve_with_log_2())


if __name__ == "__main__":
    if os.environ.get("DEBUG_CODEFORCES"):
        stdin = open("../../input.txt", "r")
        start_time = time.time()
        run()
        print("\n--- %s seconds ---\n" % (time.time() - start_time))
    else:
        run()
