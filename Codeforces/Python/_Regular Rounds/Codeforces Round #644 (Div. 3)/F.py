# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/1360/problem/F
# Title  : F. Spy-string
# Tags   : tag-codeforces, tag-problem-F, tag-div-3
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
ddict = defaultdict
_dp = lambda default_value: ddict(lambda: default_value)
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

def get_all_possible_string_combinations(s, m):
    _strings = set()

    for j in range(26):
        for i in range(m):
            _strings.add(s[:i] + chr(97 + j) + s[i + 1:])

    return _strings


def solve():
    n, m = intl()
    s = inp()

    st = get_all_possible_string_combinations(s, m)

    for i in range(n - 1):
        st = st & get_all_possible_string_combinations(inp(), m)

    if st:
        return list(st)[0]
    else:
        return -1


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
