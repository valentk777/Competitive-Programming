# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/1741/problem/C
# Title  : Minimize the Thickness
# Tags   : tag-codeforces, tag-problem-C, tag-div-3
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

def solve_dp():
    n = iinp()
    a = intl()

    _sum = 0
    _sums = []

    for i in range(n):
        _sum += a[i]
        _sums.append(_sum)

    dp = _dp(0)

    for i in range(n):
        dp[i] = [[_sums[i], i + 1]]

    for i in range(n):
        for j in range(i):
            for k in dp[j]:
                if _sums[i] - _sums[j] == k[0]:
                    dp[i].append([k[0], max(k[1], i - j)])

    _min = n

    for i in dp[n - 1]:
        _min = min(_min, i[1])

    return _min


# wrong answer
def solve():
    n = iinp()
    a = intl()

    if n < 3:
        return len(set(a))

    x = 1
    ans = n

    while x < n:
        global_max = x
        target_sum = sum(a[:x])
        local_sum = 0
        local_length = 0

        for i in range(x, n):
            local_sum += a[i]
            local_length += 1

            if local_sum == target_sum:
                local_sum = 0
                global_max = max(x, global_max, local_length)
                local_length = 0
                continue

            if local_sum > target_sum:
                break

        if local_sum == 0:
            if global_max <= x:
                return global_max
            else:
                ans = min(ans, global_max)

        x += 1

    return ans


def run():
    t = iinp()

    for _ in range(t):
        # print(solve())
        print(solve_dp())


if __name__ == "__main__":
    if os.environ.get("DEBUG_CODEFORCES"):
        stdin = open("../../input.txt", "r")
        start_time = time.time()
        run()
        print("\n--- %s seconds ---\n" % (time.time() - start_time))
    else:
        run()
