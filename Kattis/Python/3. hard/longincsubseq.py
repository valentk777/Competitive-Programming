# -----------------------------------------------------------
# URL    : https://open.kattis.com/problems/longincsubseq
# Title  : Longest Increasing Subsequence
# Notes  : tag-kattis, tag-hard
# -----------------------------------------------------------

# ---------------------------------------------------Shared part--------------------------------------------------------
import os
import time
from bisect import bisect_left
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


# LIS (the longest increasing subsequence) + sequence itself
def find_lis_with_sequence_slow(a, n):
    # if we want sequence itself, we can store array as well
    dp = defaultdict(list)

    for i in range(n):
        n_dp_i = len(dp[i])

        for j in range(i):
            if a[j] < a[i] and (n_dp_i < len(dp[j]) + 1):
                dp[i] = dp[j].copy()
            pass

        dp[i].append(i)

    _max = []

    for lis in dp.values():
        if len(lis) > len(_max):
            _max = lis

    return len(_max), _max


def find_lis_with_sequence_fast(a, n):
    _idx = []  # index of last element for each length of LIS
    _values = []  # value of last element for each length of LIS
    _predecessor = [-1] * n  # index of predecessor for LIS ending here

    for i, e in enumerate(a):
        j = bisect_left(_values, e)

        if j == len(_values):
            _values.append(e)
            _idx.append(i)
        else:
            _values[j] = e
            _idx[j] = i
        if j > 0:
            _predecessor[i] = _idx[j - 1]

    i = _idx[-1]

    for j in range(len(_values) - 1, -1, -1):
        _values[j] = i
        i = _predecessor[i]

    return _values


def solve():
    n = iinp()
    a = intl()

    _lis = find_lis_with_sequence_fast(a, n)

    print(len(_lis))
    print(*_lis)


def run():
    while True:
        try:
            solve()
        except:
            break


if __name__ == "__main__":
    if os.environ.get("DEBUG_CODEFORCES"):
        stdin = open("../input.txt", "r")
        start_time = time.time()
        run()
        print("\n--- %s seconds ---\n" % (time.time() - start_time))
    else:
        run()
