# -----------------------------------------------------------
# URL    : https://codeforces.com/contest/1138/problem/A
# Title  : Sushi for Two
# Notes  : tag-codeforces, tag-problem-A, tag-div-2
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

# count number of two consecutive elements
def solve():
    n = iinp()
    t = intl()
    _count_before = 0
    _count_now = 0
    result = 0

    for i in range(1, n):
        if t[i - 1] == t[i]:
            _count_now += 1
        else:
            result = max(result, min(_count_before, _count_now + 1))
            _count_before = _count_now + 1
            _count_now = 0

    return max(result, min(_count_before, _count_now + 1)) * 2


def solve_2():
    n = iinp()
    t = intl()

    count_1 = 0
    count_2 = 0
    before = t[0]
    scores = []

    if before == 1:
        count_1 += 1
    else:
        count_2 += 1

    for i in range(1, n):
        if t[i] == before:
            if t[i] == 1:
                count_1 += 1
            else:
                count_2 += 1
        else:
            if t[i] == 1:
                scores.append(count_2)
                count_2 = 0
                count_1 += 1
                before = 1
            else:
                scores.append(count_1)
                count_1 = 0
                count_2 += 1
                before = 2

    if before == 1:
        scores.append(count_1)
    else:
        scores.append(count_2)

    _sums = []

    for i in range(1, len(scores)):
        _sums.append(min(scores[i - 1], scores[i]))

    return max(_sums) * 2


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
