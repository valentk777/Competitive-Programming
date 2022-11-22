# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/1251/problem/A
# Title  : Broken Keyboard
# Tags   : tag-codeforces, tag-problem-A, tag-div-2, tag-difficulty-1000
# Notes  : brute force, strings, two pointers
# ---------------------------------------------------------------------------------------

# ---------------------------------------------------Shared part--------------------------------------------------------
import os
import string
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
    s = inp()
    n = len(s)

    _counter = Counter(string.ascii_lowercase)

    i = 0

    while i < n:
        if i + 1 < n and s[i] == s[i + 1]:
            i += 2
        else:
            _counter[s[i]] -= 1
            i += 1

    ans = []

    for key, value in _counter.items():
        if value != 1:
            ans.append(key)

    return list_to_string(ans)


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
