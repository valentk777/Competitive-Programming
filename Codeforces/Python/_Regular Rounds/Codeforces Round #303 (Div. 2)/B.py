# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/545/problem/B
# Title  : Equidistant String
# Tags   : tag-codeforces, tag-problem-B, tag-div-2, tag-difficulty-1100
# Notes  : greedy
# ---------------------------------------------------------------------------------------

# ---------------------------------------------------Shared part--------------------------------------------------------
import os
import time
from collections import defaultdict
from sys import stdin, maxsize

inp = lambda: stdin.readline().strip()
iinp = lambda: int(inp())
intl = lambda: list(map(int, inp().split()))
strl = lambda: list(inp().split())
list_to_string = lambda _a: "".join(map(str, _a))
list_to_string_list = lambda _a: " ".join(map(str, _a))
_dp = lambda default_value: defaultdict(lambda: default_value)

MOD = 10 ** 9 + 7
INF = maxsize


# -------------------------------------------------------Solution-------------------------------------------------------

def solve():
    s = inp()
    t = inp()
    n = len(s)

    if s == t:
        return s

    bin_s = int(s, 2)
    bin_t = int(t, 2)
    _diff = bin_s ^ bin_t
    _diff = bin(_diff).count("1")

    if _diff & 1 == 1:
        return "impossible"

    # faster then append
    result = ["0" for _ in range(n)]
    missing_s = _diff // 2

    for i in range(n):
        if s[i] != t[i]:
            if missing_s > 0:
                result[i] = s[i]
                missing_s -= 1
            else:
                result[i] = t[i]

    return list_to_string(result)


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
