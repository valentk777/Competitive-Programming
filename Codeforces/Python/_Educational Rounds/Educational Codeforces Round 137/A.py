# -----------------------------------------------------------
# URL    : https://codeforces.com/contest/1743/problem/A
# Title  : Password
# Notes  : tag-codeforces, tag-problem-A, tag-div-2
# -----------------------------------------------------------

# ---------------------------------------------------Shared part--------------------------------------------------------
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


def print_dp(_dict):
    for item in _dict.items():
        print(f"{item[0]} = {item[1]}")


MOD = 10 ** 9 + 7
INF = maxsize
A = 911382323
M = 9999999999879998


# -------------------------------------------------------Solution-------------------------------------------------------

def solve():
    n = iinp()
    a = intl()

    possible_numbers = list(range(0, 10))

    for i in range(n):
        possible_numbers.remove(a[i])

    ans = 0

    for i in possible_numbers:
        for j in possible_numbers:
            for k in possible_numbers:
                for l in possible_numbers:
                    c = Counter([i, j, k, l])

                    if len(c.values()) == 2 and list(c.values())[0] == 2 and list(c.values())[1] == 2:
                        ans += 1

    return ans


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
