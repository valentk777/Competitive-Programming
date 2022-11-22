# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/1760/problem/F
# Title  : Quests
# Tags   : tag-codeforces, tag-problem-F, tag-div-4, tag-difficulty-0
# Notes  : binary search, greedy, sortings
# ---------------------------------------------------------------------------------------

# ---------------------------------------------------Shared part--------------------------------------------------------
import math
import os
import time
from collections import defaultdict, Counter
from sys import stdin, maxsize, stdout

inp = lambda: stdin.readline().strip()
iinp = lambda: int(inp())
intl = lambda: list(map(int, inp().split()))
strl = lambda: list(inp().split())
list_to_string = lambda _a: "".join(map(str, _a))
list_to_string_list = lambda _a: " ".join(map(str, _a))
_dp = lambda default_value: defaultdict(lambda: default_value)
flush = lambda: stdout.flush()
print_flush = lambda _text: (print(_text), flush())
fact = lambda number: math.factorial(number)
cnt = lambda _a: Counter(_a)


def lcm(a, b):
    return a * b // math.gcd(a, b)


def print_dp(_dict):
    for item in _dict.items():
        print(f"{item[0]} = {item[1]}")


MOD = 10 ** 9 + 7
INF = maxsize
A = 911382323
M = 9999999999879998


# -------------------------------------------------------Solution-------------------------------------------------------

def calculate(d, a, c, take):
    _sum = 0
    _max_days = 0

    for i in range(math.ceil(d // take)):
        for j in range(take):
            _sum += a[j]

            if _sum >= c:
                return (d // (i + 1)) - take + 1

    return 0


def solve():
    n, c, d = intl()
    a = intl()
    a = sorted(a, reverse=True)

    if sum(a[:d]) >= c:
        return "Infinity"

    if d * a[0] < c:
        return "Impossible"

    _sums = [0]

    for i in range(n):
        _sums.append(_sums[-1] + a[i])

    ans = 0

    for k in range(1, d + 1):
        single_part_size = d // k

        # fill full sums
        _sum = _sums[min(k, n)] * single_part_size

        # add partial sum (last needed)
        _sum += _sums[min(d % k, n)]

        if _sum >= c:
            # we save new max k
            ans = k - 1

    return ans


def solve_wrong():
    n, c, d = intl()
    a = intl()
    a = sorted(a, reverse=True)

    if sum(a[:d]) >= c:
        return "Infinity"

    _max = d * a[0]

    if _max < c:
        return "Impossible"

    ans = [calculate(d, a, c, 1)]

    for i in range(2, min(d, n) + 1):
        ans.append(calculate(d, a, c, i))

        if ans[-1] < ans[-2]:
            break

    print(ans)

    return max(ans)


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
