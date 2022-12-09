# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/1538/problem/D
# Title  : Another Problem About Dividing Numbers
# Tags   : tag-codeforces, tag-problem-D, tag-div-3, tag-difficulty-1700
# Notes  : constructive algorithms, math, number theory
# ---------------------------------------------------------------------------------------

# region --------------------------------------------Shared part--------------------------------------------------------
import math
import os
import sys
import time
from collections import defaultdict, Counter
from io import IOBase, BytesIO

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

# region -------------------------------------------Fast IO Region------------------------------------------------------
BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)


# endregion
# endregion

# -------------------------------------------------------Solution-------------------------------------------------------

def get_prime_range(n):
    history = [True] * n
    p = []

    for i in range(2, n):
        if history[i]:
            p.append(i)

            for j in range(i * i, n, i):
                history[j] = False
    return p


def get_number_of_prime_factors(_primes, n):
    number = 0

    for p in _primes:
        if p * p > n:
            break

        while n % p == 0:
            n //= p
            number += 1

    if n > 1:
        number += 1

    return number


def get_min(_a, _b):
    if _a == _b:
        return 0

    _gcd = math.gcd(_a, _b)
    if _gcd == _a or _gcd == _b:
        return 1

    return 2


def solve(_primes):
    a, b, k = intl()

    if a == 1 and b == 1:
        return "NO"

    _min = get_min(a, b)
    _max = get_number_of_prime_factors(_primes, a) + get_number_of_prime_factors(_primes, b)

    if _min <= k <= _max:
        if k != 1:
            return "YES"

        if _min == 1:
            return "YES"

    return "NO"


def run():
    prime_list = get_prime_range(int(10E5) + 1)
    t = iinp()

    for _ in range(t):
        print(solve(prime_list))


if __name__ == "__main__":
    if os.environ.get("DEBUG_CODEFORCES"):
        sys.stdin = open("../../input.txt", "r")
        start_time = time.time()
        run()
        print("\n--- %s seconds ---\n" % (time.time() - start_time))
    else:
        run()
