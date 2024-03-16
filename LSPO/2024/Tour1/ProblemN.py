# ---------------------------------------------------------------------------------------
# URL    : https://programavimas.vgtu.lt/contests/55/problems/2047/
# Title  : Ir dalinas, ir sumuojas
# Tags   : tag-LSPO, tag-vgtu, tag-problem-N
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

def sum_of_digits(number):
    _sum = 0

    while number > 0:
        _sum += number % 10
        number //= 10

    return _sum

def solve():
    n, k = intl()

    start = int('1' + '0' * (n-1))

    for i in range(30):
        if (start + i) %  k == 0:
            start += i
            break

    for candidate in range(start, int('9' * 1000) + 1, k):
        if sum_of_digits(candidate) == k:
            return candidate

    return start


def run():
    print(solve())


if __name__ == "__main__":
    run()
