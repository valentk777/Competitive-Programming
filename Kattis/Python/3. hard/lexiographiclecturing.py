# -----------------------------------------------------------
# URL    : https://open.kattis.com/problems/lexiographiclecturing
# Title  : Lexicographical Lecturing
# Notes  : tag-kattis, tag-3. hard, tag-not-pass
# -----------------------------------------------------------

# ---------------------------------------------------Shared part--------------------------------------------------------

import os
import time
from sys import stdin, maxsize

inp = lambda: stdin.readline().strip()
iinp = lambda: int(inp())
intl = lambda: list(map(int, inp().split()))
strl = lambda: list(inp().split())
list_from_inp = lambda n: [inp() for _ in range(n)]

MOD = 10 ** 9 + 7
INF = maxsize


# -------------------------------------------------------Solution-------------------------------------------------------

def solve_slow():
    n, l = intl()
    ids = list_from_inp(n)
    ids = list(map(list, ids))
    ids = sorted(ids)

    index = []

    for i in range(n):
        index.append((i, ids[i]))

    _min = INF
    _min_i = -INF
    _min_j = INF

    shuffle_index = index.copy()
    shuffle_index = sorted(shuffle_index, key=lambda x: x[1], reverse=True)

    for i in range(l):
        for j in range(i + 1, l + 1):
            nex_idx = [(idx[0], idx[1][i:j]) for idx in shuffle_index]
            nex_idx = sorted(nex_idx, key=lambda x: x[1])

            is_sorted = True

            for z in range(n):
                if nex_idx[z][0] != z:
                    is_sorted = False
                    break

            if is_sorted:
                if j - i + 1 < _min_j - _min_i + 1:
                    _min_j = j
                    _min_i = i

                break

    return f"{_min_i + 1} {_min_j}"


def solve():
    n, l = intl()
    ids = list_from_inp(n)
    ids = list(map(list, ids))
    ids = sorted(ids)

    index = []

    for i in range(n):
        index.append((i, ids[i]))

    # dp = [False for _ in range(2 * l + 1)]
    _min = INF
    _min_i = -INF
    _min_j = INF

    shuffle_index = index.copy()
    shuffle_index = sorted(shuffle_index, key=lambda x: x[1], reverse=True)

    number_of_letters = 1

    while number_of_letters <= l:

        for i in range(l - number_of_letters + 1):
            nex_idx = [(idx[0], idx[1][i:i + number_of_letters]) for idx in shuffle_index]
            nex_idx = sorted(nex_idx, key=lambda x: x[1])

            is_sorted = True

            for z in range(n):
                if nex_idx[z][0] != z:
                    is_sorted = False
                    break

            if is_sorted:
                _min_j = i + number_of_letters
                _min_i = i
                return f"{_min_i + 1} {_min_j}"

        number_of_letters += 1


def run():
    try:
        while True:
            print(solve())
    except:
        pass


if __name__ == "__main__":
    if os.environ.get("DEBUG_CODEFORCES"):
        stdin = open("../input.txt", "r")
        start_time = time.time()
        run()
        print("\n--- %s seconds ---\n" % (time.time() - start_time))
    else:
        run()
