# -----------------------------------------------------------
# URL    : https://codeforces.com/contest/2/problem/A
# Title  : Winner
# Notes  : tag-codeforces, tag-problem-A, tag-div-2, tag-not-pass
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
def solve():
    n = iinp()

    _scores = _dp(0)
    _winner = ""
    _best_score = -INF

    for i in range(n):
        name, score = inp().split()
        _scores[name] += int(score)

        if _scores[name] > _best_score:
            _winner = name
            _best_score = _scores[name]

    return _winner


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
