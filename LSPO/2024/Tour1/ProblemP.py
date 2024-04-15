# ---------------------------------------------------------------------------------------
# URL    : https://programavimas.vgtu.lt/contests/55/problems/2067/
# Title  : Sritys
# Tags   : tag-LSPO, tag-vgtu, tag-problem-P
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

    # if n + m < 100 we can use 1x(m+n) table






    n, m, k, l = intl()

    for aukstas in range(n):
        eilute = ""

        if aukstas % 2 == 0:
            simbolis = "."
        else:
            simbolis = "#"

        for blokas in range(k):
            if blokas % 2 == 0:
                eilute += simbolis * l
            else:
                if simbolis == ".":
                    eilute += "#" * l
                else:
                    eilute += "." * l

        for metras in range(m):
            print(eilute)


def run():
    solve()


if __name__ == "__main__":
    run()
