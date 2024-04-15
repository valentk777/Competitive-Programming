# ---------------------------------------------------------------------------------------
# URL    : https://programavimas.vgtu.lt/contests/55/problems/1975/
# Title  : Sumos dalumas
# Tags   : tag-LSPO, tag-vgtu, tag-problem-G
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

def get_prime_factors(n):
    factors = []

    while n % 2 == 0:
        factors.append(2)
        n = n // 2

    # n became odd
    _sqrt = int(math.sqrt(n))
    for i in range(3, _sqrt + 1, 2):

        while n % i == 0:
            factors.append(i)
            n = n // i

    if n > 2:
        factors.append(n)

    return factors


def solve():
    n = iinp()

    primes = get_prime_factors(n)
    candidates = [n - 1, 2*n - 1]

    if len(primes) > 1:
        for p in primes:
            if p % 2 == 0:
                candidates.append((n // 2) - 1)
                break

    d = 1 + 8 * n

    _sqrt = math.sqrt(d)
    if _sqrt == int(_sqrt):
        candidates.append((-1 + int(_sqrt)) // 2)

    candidates = sorted(candidates)

    for i in candidates:
        if (i*(i + 1) // 2) % n == 0:

            print("cia")
            print(i)
            break

    for i in range(1, 10**15):
        if i*(i + 1) // 2 % n == 0:
            return i



def run():
    print(solve())


if __name__ == "__main__":
    run()
