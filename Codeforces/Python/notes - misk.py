from bisect import bisect_left, bisect_right
from collections import defaultdict


# region - LIS (the longest increasing subsequence)

# LIS (the longest increasing subsequence)
def find_lis(a, n):
    # max value where elements are smaller than current value
    dp = defaultdict(int)

    for i in range(n):
        dp[i] = 1

        for j in range(i):
            if a[j] < a[i] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1


# LIS (the longest increasing subsequence) + sequence itself
def find_lis_with_sequence(a, n):
    # if we want sequence itself, we can store array as well
    dp = defaultdict(list)

    for i in range(n):
        for j in range(i):
            if a[j] < a[i] and (len(dp[i]) < len(dp[j]) + 1):
                dp[i] = dp[j].copy()

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


# endregion

# region - SEARCH (Binary)

# for binary search
a = [1, 5, 5, 9]
print(bisect_left(a, 4))
print(bisect_right(a, 4))


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return -1


# endregion

# region - GRAPHS

def dfs(v, graph, used, k):
    ans = k
    used.add(v)

    for u in graph[v]:
        if u not in used:
            ans = max(ans, dfs(u, graph, used | {u}, k + 1))

    return ans

# endregion
