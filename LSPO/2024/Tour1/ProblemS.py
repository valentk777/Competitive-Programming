# ---------------------------------------------------------------------------------------
# URL    : https://programavimas.vgtu.lt/contests/55/problems/2109/
# Title  : Budėtojas
# Tags   : tag-LSPO, tag-vgtu, tag-problem-S
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
    _all = ["Jurgis", "Petras", "Monika", "Antanas", "Simona", "Arminas", "Donata"]
    a = list(inp().split())

    for e in a:
        _all.remove(e)

    return _all[0]


def run():
    print(solve())


if __name__ == "__main__":
    run()
