# -----------------------------------------------------------
# URL    : https://codeforces.com/contest/1743/problem/C
# Title  : C. Save the Magazines
# Notes  : tag-codeforces, tag-problem-C, tag-div-2
# -----------------------------------------------------------

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

def solve():
    n = iinp()
    s = list(map(int, inp()))
    a = intl()

    ans = 0

    # store last not added box (with index 0)
    prev = 0

    for i in range(n):
        # if we found new box without cover, then this box our new last box without cover
        if s[i] == 0:
            prev = a[i]
        else:
            # if last box without cover better thant current, add previous by removing index from a[i].
            # now a[i] new previous - box without cover
            if prev > a[i]:
                ans += prev
                prev = a[i]

            # if previous worse than this one. Add current but do not update previous.
            # In case we found new a[i] with smaller previous, we will add previous. in case of 0, 1, 1, 1.
            else:
                ans += a[i]

    return ans


# wrong answer
def solve_wrong():
    n = iinp()
    s = list(map(int, list(inp()))) + [0, 0]
    a = intl() + [-INF, -INF]

    _count_zero = s.count(0) - 2
    _count_one = n - _count_zero

    if _count_zero == n:
        return 0

    if _count_zero == n:
        return sum(a)

    dp = _dp(0)

    i = 0
    while i < n:
        if s[i] == 1:
            dp[i] = dp[i - 1] + a[i]
            i += 1
        else:
            if s[i + 1] == 0:
                dp[i] = dp[i - 1]
                i += 1
            else:
                if s[i + 2] == 0:
                    if a[i] > a[i + 1]:
                        dp[i] = dp[i - 1] + a[i]
                        dp[i + 1] = dp[i]
                    else:
                        dp[i] = dp[i - 1]
                        dp[i + 1] = dp[i] + a[i + 1]
                    i += 2
                else:
                    if a[i] > min(a[i + 1], a[i + 2]):
                        dp[i] = dp[i - 1] + a[i]
                        s[i + 1] = 0

                        i += 1
                    else:
                        dp[i] = dp[i - 1]
                        dp[i + 1] = dp[i] + a[i + 1]
                        dp[i + 2] = dp[i + 1] + a[i + 2]

                        i += 2

    return dp[n - 1]


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
