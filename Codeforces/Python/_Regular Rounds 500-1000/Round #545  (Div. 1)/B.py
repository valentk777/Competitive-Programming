# -----------------------------------------------------------
# URL    : https://codeforces.com/contest/1137/problem/B
# Title  : Sushi for Two
# Notes  : tag-codeforces, tag-problem-B, tag-div-1, tag-not-pass
# -----------------------------------------------------------

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
print_dp = lambda _dict: list(map(lambda item: print(f"{item[0]} = {item[1]}"), _dict.items()))

MOD = 10 ** 9 + 7
INF = maxsize


# -------------------------------------------------------Solution-------------------------------------------------------

# Wrong answer
# count number of two consecutive elements
def solve():
    s = inp()
    t = inp()

    n_s = len(s)
    n_t = len(t)

    if n_s < n_t:
        return s

    count_s = _dp(0)
    count_t = _dp(0)

    for i in range(n_s):
        count_s[s[i]] += 1

    for i in range(n_t):
        count_t[t[i]] += 1

    ans = ""

    while count_s["0"] - count_t["0"] >= 0 and count_s["1"] - count_t["1"] >= 0:
        count_s["0"] -= count_t["0"]
        count_s["1"] -= count_t["1"]

        ans += t

    ans += count_s["0"] * "0" + count_s["1"] * "1"
    return ans


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
