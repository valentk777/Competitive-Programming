# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/112/problem/C
# Title  : C. Petya and Inequiations
# Tags   : tag-codeforces, tag-problem-C, tag-div-2
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


# -------------------------------------------------------Solution-------------------------------------------------------

def solve():
    n, x, y = intl()

    if n > y:
        print(-1)
        return

    ans = [(y - n + 1)] + [1] * (n - 1)
    _sums = sum(ans)
    _sums_power = ans[0] ** 2 + sum(ans[1:])

    if _sums_power < x:
        print(-1)
        return

    for i in range(n):
        print(ans[i])


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
