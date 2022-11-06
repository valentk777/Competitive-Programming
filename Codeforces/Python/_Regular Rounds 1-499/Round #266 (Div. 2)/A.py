# -----------------------------------------------------------
# URL    : https://codeforces.com/contest/466/problem/A
# Title  : A. Cheap Travel
# Notes  : tag-codeforces, tag-problem-A, tag-div-2
# -----------------------------------------------------------

# ---------------------------------------------------Shared part--------------------------------------------------------
import os
import time
from collections import defaultdict
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

def solve():
    n, m, a, b = intl()

    combined_price_for_single_trip = b / m

    if combined_price_for_single_trip > a:
        # better buy single tickets
        return n * a

    ans = 0

    # buy as many tickets with combined as possible
    if n > m:
        _count = n // m
        ans += _count * b
        n %= m

    # if no rides left
    if n == 0:
        return ans

    # now we know that n < m. We need to check if buy one combined or multiple single better
    price_for_multiple_single = n * a

    if price_for_multiple_single < b:
        ans += price_for_multiple_single
    else:
        ans += b

    return ans


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
