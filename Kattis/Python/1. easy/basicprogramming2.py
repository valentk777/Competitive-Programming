# -----------------------------------------------------------
# URL    : https://open.kattis.com/problems/basicprogramming2
# Title  : Basic Programming 2
# Notes  : tag-kattis, tag-easy
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

def solve():
    n, t = intl()
    a = intl()
    a = sorted(a)

    if t == 1:
        left = 0
        right = n - 1

        while left < right:
            if a[left] + a[right] == 7777:
                return "Yes"

            if a[left] + a[right] < 7777:
                left += 1
                continue

            if a[left] + a[right] > 7777:
                right -= 1
                continue

        return "No"

    if t == 2:
        if len(a) == len(set(a)):
            return "Unique"

        return "Contains duplicate"

    if t == 3:
        _cnt = cnt(a)
        _times = n // 2

        for key, value in _cnt.items():
            if value > _times:
                return key

        return -1

    if t == 4:
        mid = n // 2

        if n & 1 == 0:
            return list_to_string_list([a[mid - 1], a[mid]])

        return a[mid]

    if t == 5:
        a = list(filter(lambda x: 100 <= x <= 999, a))
        return list_to_string_list(a)


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
