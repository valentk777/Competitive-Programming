# -----------------------------------------------------------
# URL    : https://codeforces.com/contest/1325/problem/B
# Title  : CopyCopyCopyCopyCopy
# Notes  : tag-codeforces, tag-problem-B, tag-div-2
# -----------------------------------------------------------

# ---------------------------------------------------Shared part--------------------------------------------------------
import os
import time
from bisect import bisect_left
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

def normalise(array):
    set_array = list(set(array))

    for i in range(len(array)):
        array[i] = set_array.index(array[i])

    return array


# O(N**2)
def solve_dp_slow():
    n = iinp()
    a = normalise(intl()) * n

    # length of increasing until a_i
    dp = _dp(-INF)

    for i in range(len(a)):
        _max = 0

        for j in range(i + 1):

            if a[j] < a[i]:
                _max = max(_max, dp[j])

        dp[i] = _max + 1

    return max(dp.values())


# O(N*Log(N)
# Binary search (note boundaries in the caller) A[] is ceilIndex in the caller
def find_element_binary_search(_array, element_count, find_element):
    left = -1
    right = element_count

    while right - left > 1:
        m = left + (right - left) // 2
        if _array[m] >= find_element:
            right = m
        else:
            left = m
    return right


def solve_nlogn_v1():
    n = iinp()
    a = normalise(intl()) * n
    n = len(a)

    # 1-st element in l always be the smallest; last element in l always be the biggest; position = count in sequence
    tail = [0 for _ in range(n + 1)]
    tail[0] = a[0]
    idx = 1

    for i in range(1, n):
        # A[i] wants to extend the largest subsequence
        if a[i] > tail[idx - 1]:
            tail[idx] = a[i]
            idx += 1

        # new smallest value
        elif a[i] < tail[0]:
            tail[0] = a[i]

        # A[i] wants to be current end candidate of an existing subsequence. It will replace ceil value in tail_table
        else:
            tail[find_element_binary_search(tail, idx - 1, a[i])] = a[i]

    return idx


def solve_nlogn_v2():
    n = iinp()
    a = normalise(intl()) * n
    n = len(a)

    tail = [0 for _ in range(n + 1)]
    tail[0] = a[0]
    idx = 1

    for i in range(1, n):
        if a[i] > tail[idx - 1]:
            tail[idx] = a[i]
            idx += 1
        else:
            tail[bisect_left(tail, a[i], 0, idx - 1)] = a[i]

    return idx


def solve_nlogn_v3():
    n = iinp()
    a = normalise(intl()) * n
    n = len(a)

    tail = [INF for _ in range(n + 1)]

    for i in range(n):
        tail[bisect_left(tail, a[i], 0, n)] = a[i]

    for i in range(n + 1):
        if tail[i] == INF:
            return i


def solve():
    _ = iinp()
    a = intl()

    return len(set(a))


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
