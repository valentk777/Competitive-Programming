# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/1097/problem/B
# Title  : B. Petr and a Combination Lock
# Tags   : tag-codeforces, tag-problem-B
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

def solve():
    n = iinp()
    rotations = []

    for i in range(n):
        rotations.append(iinp())

    candidates = {-rotations[0], rotations[0]}

    for i in range(1, n):
        _temp = set()

        for candidate in candidates:
            _temp.add((candidate + rotations[i]) % 360)
            _temp.add((candidate - rotations[i]) % 360)

        candidates = _temp

    if 0 in candidates:
        return "YES"
    else:
        return "NO"


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
