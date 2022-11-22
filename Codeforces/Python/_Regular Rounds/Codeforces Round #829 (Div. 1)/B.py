# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/1753/problem/B
# Title  : Factorial Divisibility
# Tags   : tag-codeforces, tag-problem-B, tag-div-1, tag-difficulty-1600, tag-not-pass
# Notes  : math, number theory
# ---------------------------------------------------------------------------------------

# ---------------------------------------------------Shared part--------------------------------------------------------
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


def print_dp(_dict):
    for item in _dict.items():
        print(f"{item[0]} = {item[1]}")


MOD = 10 ** 9 + 7
INF = maxsize
A = 911382323
M = 9999999999879998


# -------------------------------------------------------Solution-------------------------------------------------------

def factorial(n, end):
    ans = 1

    for i in range(end, n + 1):
        ans *= i

    return ans




# time limit
def solve():
    n, x = intl()
    a = intl()
    end_factorial = min(a)

    if x <= end_factorial:
        return "Yes"

    x_value = factorial(end_factorial + 1, x)
    a_counter = Counter(a)
    a_value = 0

    for k, v in a_counter.items():
        a_value += v * factorial(k, end_factorial + 1)

    if a_value % x_value == 0:
        return "Yes"
    else:
        return "No"


def solve():
    n, x = intl()
    a = intl()
    #TODO: finish

def run():
    print(solve())


if __name__ == "__main__":
    if os.environ.get("DEBUG_CODEFORCES"):
        stdin = open("../../input.txt", "r")
        start_time = time.time()
        run()
        print("\n--- %s seconds ---\n" % (time.time() - start_time))
    else:
        run()
