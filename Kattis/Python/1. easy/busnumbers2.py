# -----------------------------------------------------------
# URL    : https://open.kattis.com/problems/busnumbers2
# Title  : Bus Numbers
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

def solve():
    n = iinp()

    all_cubes = [i ** 3 for i in range(1, 75)]
    all_cubes = list(filter(lambda x: x < n, all_cubes))

    candidates = _dp(0)

    for i in range(len(all_cubes)):
        for j in range(i, len(all_cubes)):
            candidates[all_cubes[i] + all_cubes[j]] += 1

    candidates = dict(filter(lambda x: x[0] <= n and x[1] > 1, candidates.items()))

    if len(candidates.keys()) > 0:
        return max(candidates.keys())
    else:
        return "none"


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
