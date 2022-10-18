# -----------------------------------------------------------
# URL    : https://open.kattis.com/problems/genetics2
# Title  : Genetics
# Notes  : tag-kattis, tag-hard, not-pass
# -----------------------------------------------------------

# ---------------------------------------------------Shared part--------------------------------------------------------
import os
import time
from collections import defaultdict
from random import randint
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

def compare(str1, str2, n, drop_count):
    _count = 0

    for i in range(n):
        if str1[i] != str2[i]:
            _count += 1

        if _count > drop_count + 1:
            return -1

    return _count


def solve_slow():
    n, m, k = intl()
    s = list_from_inp(n)

    i = 0

    candidates = [1 for _ in range(n)]

    while i < n - 1:
        _score = -INF

        # if candidates[i] == 0:
        #     i += 1
        #     continue

        for j in range(i + 1, n):
            if candidates[j] == 0:
                continue

            score = compare(s[i], s[j], m, k)

            if score != k:
                candidates[i] = 0
                candidates[j] = 0

            # print(score)
            # if score != k:
            #     _score = -INF
            #     break
            #
            # if _score == -INF:
            #     _score = score
            # else:
            #     if _score != score:
            #         _score = -INF
            #         break
            #
            # print(score)

        # if _score != -INF:
        i += 1
    # print(s)
    # print(candidates)

    return candidates.index(1) + 1


def solve():
    n, m, k = intl()
    _strings = _dp(0)

    for i in range(n):
        s = inp()

        for j in range(m):
            _strings[i, j] = (ord(s[j]) >> 1) & 3

    ncand = n
    is_candidate = [True for _ in range(n)]

    while ncand > 1:
        weights = _dp(0)
        tot_weight = 0

        for i in range(n):
            weights[i] = randint(1, INF)
            tot_weight += weights[i]

        _count = _dp(0)
        _count[0] = [0 for _ in range(m)]
        _count[1] = [0 for _ in range(m)]
        _count[2] = [0 for _ in range(m)]
        _count[3] = [0 for _ in range(m)]

        for i in range(n):
            for j in range(m):
                _count[_strings[i, j]][j] += weights[i]

        for i in range(n):
            if not is_candidate[i]:
                continue

            sum_dif = 0

            for j in range(m):
                sum_dif += tot_weight - _count[_strings[i, j]][j]

            expected_sum_dif = (tot_weight - weights[i]) * k
            if sum_dif != expected_sum_dif:
                is_candidate[i] = False
                ncand -= 1
    ans = -1

    for i in range(n):
        if is_candidate[i]:
            ans = i

    return ans + 1


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
