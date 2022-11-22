# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/1741/problem/B
# Title  : Funny Permutation
# Tags   : tag-codeforces, tag-problem-B, tag-div-3
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
print_dp = lambda _dict: list(map(lambda item: print(f"{item[0]} = {item[1]}"), _dict.items()))

MOD = 10 ** 9 + 7
INF = maxsize


# -------------------------------------------------------Solution-------------------------------------------------------

def solve():
    n = iinp()

    ans = []

    if n & 1 == 0:
        for i in range(n, 0, -1):
            ans.append(i)

        return list_to_string_list(ans)

    if n == 3:
        return -1

    mid = (n // 2) + 1

    for i in range(n, mid, -1):
        ans.append(i)

    for i in range(1, mid + 1):
        ans.append(i)

    return list_to_string_list(ans)


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
