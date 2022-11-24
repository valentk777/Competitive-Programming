# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/1511/problem/C
# Title  : Yet Another Card Deck
# Tags   : tag-codeforces, tag-problem-C, tag-div-2, tag-difficulty-1100
# Notes  : brute force, data structures, implementation, trees
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

def solve():
    n, q = intl()
    a = intl()
    queries = intl()

    # we can store only max index of a single color
    highest_card_by_color = [-1 for _ in range(52)]

    for i in range(n):
        if highest_card_by_color[a[i]] == -1:
            highest_card_by_color[a[i]] = i + 1

    ans = []

    for q in queries:
        old_idx = highest_card_by_color[q]

        ans.append(old_idx)

        for i in range(52):
            if highest_card_by_color[i] != -1 and highest_card_by_color[i] < old_idx:
                highest_card_by_color[i] += 1

        highest_card_by_color[q] = 1

    return list_to_string_list(ans)


def run():
    print(solve())


if __name__ == "__main__":
    if os.environ.get("DEBUG_CODEFORCES"):
        stdin = open("../../input.txt", "r")
        start_time = time.time()
        run()
        print("\n--- %s seconds ---\n" % (time.time() - start_time))
    else:
        run()
