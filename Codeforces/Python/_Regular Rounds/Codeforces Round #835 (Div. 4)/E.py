# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/1760/problem/E
# Title  : Binary Inversions
# Tags   : tag-codeforces, tag-problem-E, tag-div-4, tag-difficulty-0
# Notes  : data structures, greedy, math
# ---------------------------------------------------------------------------------------

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


def lcm(a, b):
    return a * b // math.gcd(a, b)


def print_dp(_dict):
    for item in _dict.items():
        print(f"{item[0]} = {item[1]}")


MOD = 10 ** 9 + 7
INF = maxsize
A = 911382323
M = 9999999999879998


# -------------------------------------------------------Solution-------------------------------------------------------

def get_count(_a, _n):
    ans = 0
    worth = 0

    for i in range(_n):
        if _a[i] == 1:
            worth += 1
        else:
            ans += worth

    return ans


def solve():
    n = iinp()
    a = intl()

    number_of_0 = a.count(0)
    number_of_1 = a.count(1)

    a_1 = a.copy()
    a_2 = a.copy()

    for i in range(n):
        if a_1[i] == 0:
            a_1[i] = 1
            number_of_0 -= 1
            number_of_1 += 1
            break

    for i in range(n - 1, -1, -1):
        if a_2[i] == 1:
            a_2[i] = 0
            number_of_0 += 1
            number_of_1 -= 1
            break

    return max(get_count(a, n), get_count(a_1, n), get_count(a_2, n))


def run():
    t = iinp()

    for _ in range(t):
        print(solve())


if __name__ == "__main__":
    if os.environ.get("DEBUG_CODEFORCES"):
        stdin = open("../../input.txt", "r")
        start_time = time.time()
        run()
        print("\n--- %s seconds ---\n" % (time.time() - start_time))
    else:
        run()
