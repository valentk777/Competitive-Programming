# -----------------------------------------------------------
# URL    : https://open.kattis.com/problems/highesthill
# Title  : Highest Hill
# Notes  : tag-kattis
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
list_from_inp = lambda n: [inp() for _ in range(n)]

MOD = 10 ** 9 + 7
INF = maxsize


# -------------------------------------------------------Solution-------------------------------------------------------

def solve():
    n = iinp()
    h = intl()

    start_index = 0

    while h[start_index] > h[start_index + 1]:
        start_index += 1

    h = h[start_index:]
    n -= start_index

    min_max = [h[0]]

    start_index = 1

    while start_index + 1 < n:
        while start_index + 1 < n and h[start_index] == h[start_index + 1]:
            start_index += 1

        if start_index + 1 == n:
            break

        while start_index + 1 < n and h[start_index] <= h[start_index + 1]:
            start_index += 1

        min_max.append(h[start_index])

        if start_index + 1 == n:
            break

        while start_index + 1 < n and h[start_index] >= h[start_index + 1]:
            start_index += 1

        min_max.append(h[start_index])
        start_index += 1

    n = len(min_max)

    if n < 3:
        return 0

    _max_mid = -INF

    for i in range(1, n - 1, 2):
        _max_mid = max(_max_mid, min(min_max[i] - min_max[i - 1], min_max[i] - min_max[i + 1]))

    return _max_mid


def run():
    print(solve())


if __name__ == "__main__":
    if os.environ.get("DEBUG_CODEFORCES"):
        stdin = open("input.txt", "r")
        start_time = time.time()
        run()
        print("\n--- %s seconds ---\n" % (time.time() - start_time))
    else:
        run()
