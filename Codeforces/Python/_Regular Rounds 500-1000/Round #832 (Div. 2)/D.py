# -----------------------------------------------------------
# URL    : https://codeforces.com/contest/1747/problem/D
# Title  : D. Yet Another Problem
# Notes  : tag-codeforces, tag-problem-D, tag-div-2, tag-not-pass
# -----------------------------------------------------------

# ---------------------------------------------------Shared part--------------------------------------------------------
import os
import time
from collections import defaultdict
from functools import reduce
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

# time limit
def solve_slow():
    n, q = intl()
    a = intl()
    # prepare a list with max power of 2 for every element. then if our sublist contains
    # only one number with that power of two, it means it will always returns 1 in that range

    for i in range(q):
        l, r = intl()

        _range = a[l - 1:r]
        _sum = 0

        for e in _range:
            if _sum > 0:
                break

            _sum += e

        # if all zero
        if _sum == 0:
            print(0)
            continue

        # if we can take all range
        if (r - l + 1) % 2 != 0:
            result = reduce(lambda x, y: x ^ y, _range)

            if result == 0:
                print(1)
                continue
            else:
                # if range would be odd, second XOR for the same numbers would be 0
                # now it's impossible to get 0 if all elements is the same. ex 1 1 1 -> 0 1 -> 1
                print(-1)
                continue

        # if split range is only single number. We know that that single number not a 0
        if r - l == 1:
            print(-1)
            continue

        result = reduce(lambda x, y: x ^ y, _range)

        # if all range xor != 0 then no pair exist
        if result != 0:
            print(-1)
            continue

        # we can find a pair where result will be 0
        if _range[0] == 0 or _range[-1] == 0:
            print(1)
            continue

        _xor = _range[0]

        found = False

        for j in range(1, r - l, 2):
            _xor ^= _range[j]
            _xor ^= _range[j + 1]

            if _xor == 0:
                found = True
                break

        if found:
            print(2)
        else:
            print(-1)


# time limit
def solve():
    n, q = intl()
    a = intl()
    # prepare a list with max power of 2 for every element. then if our sublist contains
    # only one number with that power of two, it means it will always returns 1 in that range

    _xor_sums = [0]
    _sum = 0

    for i in range(n):
        _sum ^= a[i]
        _xor_sums.append(_sum)

    for i in range(q):
        l, r = intl()

        _range = a[l - 1:r]
        _sum = 0

        for e in _range:
            if _sum > 0:
                break

            _sum += e

        # if all zero
        if _sum == 0:
            print(0)
            continue

        # if we can take all range
        if (r - l + 1) % 2 != 0:
            result = _xor_sums[r] ^ _xor_sums[l - 1]

            # result = reduce(lambda x, y: x ^ y, _range)

            if result == 0:
                print(1)
                continue
            else:
                # if range would be odd, second XOR for the same numbers would be 0
                # now it's impossible to get 0 if all elements is the same. ex 1 1 1 -> 0 1 -> 1
                print(-1)
                continue

        # if split range is only single number. We know that that single number not a 0
        if r - l == 1:
            print(-1)
            continue

        result = _xor_sums[r] ^ _xor_sums[l - 1]
        # result = reduce(lambda x, y: x ^ y, _range)

        # if all range xor != 0 then no pair exist
        if result != 0:
            print(-1)
            continue

        # we can find a pair where result will be 0
        if _range[0] == 0 or _range[-1] == 0:
            print(1)
            continue

        _xor = _range[0]

        found = False

        for j in range(3, r - l, 2):
            _xor = _xor_sums[l - 1] ^ _xor_sums[j]

            if _xor == 0:
                found = True
                break

        if found:
            print(2)
        else:
            print(-1)


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
