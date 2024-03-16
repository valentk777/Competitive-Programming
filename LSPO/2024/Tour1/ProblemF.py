# ---------------------------------------------------------------------------------------
# URL    : https://programavimas.vgtu.lt/contests/55/problems/1974/
# Title  : Apmokėjimas
# Tags   : tag-LSPO, tag-vgtu, tag-problem-F
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
    n, k = intl()
    d = intl()
    liked = [str(i) for i in range(10) if i not in d]
    n_in_parts = list(str(n))

    print(liked)
    print(n_in_parts)

    ans = ""
    for e in n_in_parts:
        if e in liked:
            ans += e
        else:
            for i in range(int(e) + 1, 10):
                if str(i) in liked:
                    ans += e
                    break



def run():
    print(solve())


if __name__ == "__main__":
    run()
