# -----------------------------------------------------------
# URL    : https://open.kattis.com/problems/reverserot
# Title  : Reverse Rot
# Notes  : tag-kattis, tag-easy
# -----------------------------------------------------------

# ---------------------------------------------------Shared part--------------------------------------------------------
import os
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
A = 911382323
M = 9999999999879998

# -------------------------------------------------------Solution-------------------------------------------------------

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."


def encrypt_letter(c, n):
    _ord = 0

    if c == ".":
        _ord = 27
    elif c == "_":
        _ord = 26
    else:
        _ord = ord(c) - ord("A")

    return alphabet[(_ord + n) % 28]


def solve():
    n, s = strl()
    n = int(n)

    ans = [encrypt_letter(s[i], n) for i in range(len(s))]
    ans = ans[::-1]

    return list_to_string(ans)


def run():
    try:
        while True:
            print(solve())
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
