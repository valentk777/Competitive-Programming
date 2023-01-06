# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/1759/problem/E
# Title  : The Humanoid
# Tags   : tag-codeforces, tag-problem-E, tag-div-3, tag-difficulty-1500
# Notes  : brute force, dp, sortings
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

def try_1(a, h, n):
    green = 2
    blue = 1
    i = 0

    while i < n:
        if h > a[i]:
            h += math.floor(a[i] / 2)
            i += 1
            continue

        if h * 2 > a[i] and green > 0:
            green -= 1
            h *= 2
            h += math.floor(a[i] / 2)
            i += 1
            continue

        if h * 3 > a[i] and blue > 0:
            blue -= 1
            h *= 3
            h += math.floor(a[i] / 2)
            i += 1
            continue

        if h * 4 > a[i] and green > 1:
            green -= 2
            h *= 4
            h += math.floor(a[i] / 2)
            i += 1
            continue

        if h * 6 > a[i] and green > 0 and blue > 0:
            green -= 1
            blue -= 1
            h *= 6
            h += math.floor(a[i] / 2)
            i += 1
            continue

        if h * 12 > a[i] and green > 1 and blue > 0:
            green -= 2
            blue -= 1
            h *= 12
            h += math.floor(a[i] / 2)
            i += 1
            continue

        break

    return i


def try_2(a, h, n):
    green = 2
    blue = 1
    i = 0

    while i < n:
        if h > a[i]:
            h += math.floor(a[i] / 2)
            i += 1
            continue

        if h * 3 > a[i] and blue > 0:
            blue -= 1
            h *= 3
            h += math.floor(a[i] / 2)
            i += 1
            continue

        if h * 2 > a[i] and green > 0:
            green -= 1
            h *= 2
            h += math.floor(a[i] / 2)
            i += 1
            continue

        if h * 4 > a[i] and green > 1:
            green -= 2
            h *= 4
            h += math.floor(a[i] / 2)
            i += 1
            continue

        if h * 6 > a[i] and green > 0 and blue > 0:
            green -= 1
            blue -= 1
            h *= 6
            h += math.floor(a[i] / 2)
            i += 1
            continue

        if h * 12 > a[i] and green > 1 and blue > 0:
            green -= 2
            blue -= 1
            h *= 12
            h += math.floor(a[i] / 2)
            i += 1
            continue

        break

    return i


def try_3(a, h, n):
    green = 2
    blue = 1
    i = 0

    while i < n:
        if h > a[i]:
            h += math.floor(a[i] / 2)
            i += 1
            continue

        if h * 2 > a[i] and green > 0:
            green -= 1
            h *= 2
            h += math.floor(a[i] / 2)
            i += 1
            continue

        if h * 3 > a[i] and blue > 0:
            blue -= 1
            h *= 3
            h += math.floor(a[i] / 2)
            i += 1
            continue

        if h * 6 > a[i] and green > 0 and blue > 0:
            green -= 1
            blue -= 1
            h *= 6
            h += math.floor(a[i] / 2)
            i += 1
            continue

        if h * 4 > a[i] and green > 1:
            green -= 2
            h *= 4
            h += math.floor(a[i] / 2)
            i += 1
            continue

        if h * 12 > a[i] and green > 1 and blue > 0:
            green -= 2
            blue -= 1
            h *= 12
            h += math.floor(a[i] / 2)
            i += 1
            continue

        break

    return i


def try_4(a, h, n):
    green = 2
    blue = 1
    i = 0

    while i < n:
        if h > a[i]:
            h += math.floor(a[i] / 2)
            i += 1
            continue

        if h * 3 > a[i] and blue > 0:
            blue -= 1
            h *= 3
            h += math.floor(a[i] / 2)
            i += 1
            continue

        if h * 2 > a[i] and green > 0:
            green -= 1
            h *= 2
            h += math.floor(a[i] / 2)
            i += 1
            continue

        if h * 6 > a[i] and green > 0 and blue > 0:
            green -= 1
            blue -= 1
            h *= 6
            h += math.floor(a[i] / 2)
            i += 1
            continue

        if h * 4 > a[i] and green > 1:
            green -= 2
            h *= 4
            h += math.floor(a[i] / 2)
            i += 1
            continue

        if h * 12 > a[i] and green > 1 and blue > 0:
            green -= 2
            blue -= 1
            h *= 12
            h += math.floor(a[i] / 2)
            i += 1
            continue

        break

    return i


def try_5(a, h, n):
    green = 2
    blue = 1
    i = 0

    while i < n:
        if h > a[i]:
            h += math.floor(a[i] / 2)
            i += 1
            continue

        if h * 4 > a[i] and green > 1:
            green -= 2
            h *= 4
            h += math.floor(a[i] / 2)
            i += 1
            continue

        if h * 3 > a[i] and blue > 0:
            blue -= 1
            h *= 3
            h += math.floor(a[i] / 2)
            i += 1
            continue

        if h * 6 > a[i] and green > 0 and blue > 0:
            green -= 1
            blue -= 1
            h *= 6
            h += math.floor(a[i] / 2)
            i += 1
            continue

        if h * 12 > a[i] and green > 1 and blue > 0:
            green -= 2
            blue -= 1
            h *= 12
            h += math.floor(a[i] / 2)
            i += 1
            continue

        break

    return i


def try_6(a, h, n):
    green = 2
    blue = 1
    i = 0

    while i < n:
        if h > a[i]:
            h += math.floor(a[i] / 2)
            i += 1
            continue

        if h * 6 > a[i] and green > 0 and blue > 0:
            green -= 1
            blue -= 1
            h *= 6
            h += math.floor(a[i] / 2)
            i += 1
            continue

        if h * 2 > a[i] and green > 0:
            green -= 1
            h *= 2
            h += math.floor(a[i] / 2)
            i += 1
            continue

        if h * 4 > a[i] and green > 1:
            green -= 2
            h *= 4
            h += math.floor(a[i] / 2)
            i += 1
            continue

        if h * 12 > a[i] and green > 1 and blue > 0:
            green -= 2
            blue -= 1
            h *= 12
            h += math.floor(a[i] / 2)
            i += 1
            continue

        break

    return i


# greedy not working. try all possible greedy options
def solve():
    n, h = intl()
    a = intl()
    a = sorted(a)
    i_1 = try_1(a, h, n)

    if i_1 == n:
        return n

    i_2 = try_2(a, h, n)

    if i_2 == n:
        return n

    i_3 = try_3(a, h, n)

    if i_3 == n:
        return n

    i_4 = try_4(a, h, n)

    if i_4 == n:
        return n

    i_5 = try_5(a, h, n)

    if i_5 == n:
        return n

    i_6 = try_6(a, h, n)

    if i_6 == n:
        return n

    return max(i_1, i_2, i_3, i_4, i_5, i_6)


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
