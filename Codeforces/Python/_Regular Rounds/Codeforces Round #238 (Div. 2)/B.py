# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/405/problem/B
# Title  : Domino Effect
# Tags   : tag-codeforces, tag-problem-B, tag-div-2, tag-difficulty-1100
# Notes  : 
# ---------------------------------------------------------------------------------------

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

def solve():
    n = iinp()
    s = inp()

    ans = 0
    _count = 0
    found_lr = False

    for i in range(n):
        if s[i] == 'R':
            ans += _count
            found_lr = True
            _count = 1

        elif s[i] == 'L' and found_lr:
            found_lr = False
            _count += 1

            if _count % 2 == 1:
                ans += 1
            _count = 0

        elif s[i] == 'L' and not found_lr:
            _count = 0

        else:
            _count += 1

    if not found_lr:
        ans += _count

    return ans


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
