# -----------------------------------------------------------
# URL    : https://codeforces.com/contest/706/problem/B
# Title  : Interesting drink
# Notes  : tag-codeforces, tag-problem-B, tag-div-2
# -----------------------------------------------------------

# ---------------------------------------------------Shared part--------------------------------------------------------
import os
import time
from sys import stdin, maxsize

inp = lambda: stdin.readline().strip()
iinp = lambda: int(inp())
intl = lambda: list(map(int, inp().split()))
strl = lambda: list(inp().split())
list_to_string = lambda _a: " ".join(map(str, _a))

MOD = 10 ** 9 + 7
INF = maxsize


# -------------------------------------------------------Solution-------------------------------------------------------

def solve_slow():
    n = iinp()
    x = intl()
    x = sorted(x)

    q = iinp()

    for i in range(q):
        m = iinp()
        _count = 0

        for j in range(n - 1, -1, -1):
            if m >= x[j]:
                _count = j + 1
                break

        print(_count)


def solve_slow_dp():
    n = iinp()
    x = intl()
    q = iinp()

    _max = max(x)

    dp = [0 for _ in range(_max + 1)]

    for i in range(1, _max + 1):
        dp[i] = dp[i - 1] + x.count(i)

    for i in range(q):
        m = iinp()

        if m > _max:
            print(n)
        else:
            print(dp[m])


def solve_slow_dp_2():
    n = iinp()

    dp = [0 for _ in range(100000 + 1)]

    x = intl()
    q = iinp()

    for i in range(n):
        dp[x[i]] += 1

    for _ in range(q):
        m = iinp()

        if m >= 100000:
            print(n)
        else:
            _sum = 0

            for i in range(m + 1):
                _sum += dp[i]

            print(_sum)


def solve():
    n = iinp()
    x = intl()
    q = iinp()
    dp = [0 for _ in range(100000 + 1)]

    for i in range(n):
        dp[x[i]] += 1

    for i in range(1, 100000 + 1):
        dp[i] += dp[i - 1]

    for _ in range(q):
        m = iinp()

        if m >= 100000:
            print(n)
        else:
            print(dp[m])


def run():
    solve()


if __name__ == "__main__":
    if os.environ.get("DEBUG_CODEFORCES"):
        stdin = open("../../input.txt", "r")
        start_time = time.time()
        run()
        print("\n--- %s seconds ---\n" % (time.time() - start_time))
    else:
        run()
