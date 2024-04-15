# ---------------------------------------------------------------------------------------
# URL    : https://programavimas.vgtu.lt/contests/55/problems/1944/
# Title  : Nuolaidos kuponai
# Tags   : tag-LSPO, tag-vgtu, tag-problem-D
# Notes  :
# ---------------------------------------------------------------------------------------

# region --------------------------------------------Shared part--------------------------------------------------------
import math
import sys
from collections import defaultdict, Counter

inp = lambda: sys.stdin.readline().strip().rstrip("\r\n")
iinp = lambda: int(inp())
intl = lambda: list(map(int, inp().split()))
strl = lambda: list(inp().split())
list_to_string = lambda _a: "".join(map(str, _a))
list_to_string_list = lambda _a: " ".join(map(str, _a))
_dp = lambda default_value: defaultdict(lambda: default_value)
flush = lambda: sys.stdout.flush()
print_flush = lambda _text: (print(_text), flush())
fact = lambda number: math.factorial(number)
cnt = lambda _a: Counter(_a)


def lcm(a, b):
    return a * b // math.gcd(a, b)


def print_dp(_dict):
    for item in _dict.items():
        print(f"{item[0]} = {item[1]}")


MOD = 10 ** 9 + 7
INF = sys.maxsize
A = 911382323
M = 9999999999879998


# endregion
# -------------------------------------------------------Solution-------------------------------------------------------

def solve():
    n, m = intl()
    a = intl()

    _count = cnt(a)
    _count = dict(sorted(_count.items(), key=lambda x: (x[0])))

    print(_count)





    a = sorted(a, reverse=True)
    position = 0

    for i in range(m):
        a[position] = a[position] // 2
        _max = max(a)

        if _max == a[position]:
            continue

        if position + 1 < n and _max == a[position + 1]:
            position += 1
            continue

        a = sorted(a, reverse=True)
        position = 0

    return sum(a)


def run():
    print(solve())


if __name__ == "__main__":
    run()
