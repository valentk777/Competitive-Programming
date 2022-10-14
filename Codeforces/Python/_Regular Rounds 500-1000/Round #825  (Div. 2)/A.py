# -----------------------------------------------------------
# URL    : https://codeforces.com/contest/1736/problem/A
# Title  : Make A Equal to B
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

def solve():
    n = iinp()
    a = intl()
    b = intl()

    if a == b:
        return 0

    sum_a = sum(a)
    sum_b = sum(b)

    if sum_a == sum_b:
        return 1

    ans = 0

    if sum_a > sum_b:
        for i in range(n):
            if a[i] == b[i]:
                continue
            elif a[i] > b[i]:
                ans += 1
                sum_a -= 1
                a[i] = 0
            else:
                continue

            if sum_a == sum_b:
                if a == b:
                    return ans
                else:
                    return ans + 1
    else:
        for i in range(n):
            if a[i] == b[i]:
                continue
            elif a[i] > b[i]:
                continue
            else:
                ans += 1
                sum_a += 1
                a[i] = 1

            if sum_a == sum_b:
                if a == b:
                    return ans
                else:
                    return ans + 1


def run():
    t = iinp()

    for _ in range(t):
        print(solve())


if __name__ == "__main__":
    if os.environ.get("DEBUG_CODEFORCES"):
        stdin = open("../input.txt", "r")
        start_time = time.time()
        run()
        print("\n--- %s seconds ---\n" % (time.time() - start_time))
    else:
        run()
