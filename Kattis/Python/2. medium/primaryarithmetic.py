# -----------------------------------------------------------
# URL    : https://open.kattis.com/problems/primaryarithmetic
# Title  : Primary Arithmetic
# Notes  : tag-kattis, tag-medium
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


# -------------------------------------------------------Solution-------------------------------------------------------

def solve():
    a, b = strl()

    if a == b == "0":
        return

    n = max(len(a), len(b))
    a = a.zfill(n)[::-1]
    b = b.zfill(n)[::-1]
    carry = 0
    _count = 0

    for i in range(n):
        if int(a[i]) + int(b[i]) + carry > 9:
            carry = 1
            _count += 1
        else:
            carry = 0

    if _count > 1:
        print(f"{_count} carry operations.")
    elif _count == 1:
        print(f"{_count} carry operation.")
    else:
        print("No carry operation.")


def run():
    try:
        while True:
            solve()
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
