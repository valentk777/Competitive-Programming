# -----------------------------------------------------------
# URL    : https://open.kattis.com/problems/marko
# Title  : Marko
# Notes  : tag-kattis, tag-1. easy
# -----------------------------------------------------------

# ---------------------------------------------------Shared part--------------------------------------------------------
import os
import re
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

# -------------------------------------------------------Solution-------------------------------------------------------


keyboard = {
    '2': '[abc]{1}',
    '3': '[def]{1}',
    '4': '[ghi]{1}',
    '5': '[jkl]{1}',
    '6': '[mno]{1}',
    '7': '[pqrs]{1}',
    '8': '[tuv]{1}',
    '9': '[wxyz]{1}'
}


def solve():
    n = iinp()
    words = list_from_inp(n)
    s = inp()

    expression = '^'

    for letter in s:
        expression += keyboard[letter]

    possible = 0

    for word in words:
        if re.match(expression, word) is not None:
            possible += 1

    return possible


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
