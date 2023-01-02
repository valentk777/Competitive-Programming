# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/26/problem/A
# Title  : Almost Prime
# Tags   : tag-codeforces, tag-problem-A, tag-difficulty-900
# Notes  : number theory
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


def memodict(f):
    """memoization decorator for a function taking a single argument"""

    class memodict(dict):
        def __missing__(self, key):
            ret = self[key] = f(key)
            return ret

    return memodict().__getitem__


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


@memodict
def get_prime_factors(n):
    """returns a Counter of the prime factorization of n"""

    def pollard_rho(_n):
        """pollard_rho - return a random factor of n; O(sqrt of lpf[n])"""
        if _n & 1 == 0:
            return 2

        if _n % 3 == 0:
            return 3

        s = ((_n - 1) & (1 - _n)).bit_length() - 1
        d = _n >> s

        for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
            p = pow(a, d, _n)
            if p == 1 or p == _n - 1 or a % _n == 0:
                continue

            for _ in range(s):
                prev = p
                p = (p * p) % _n

                if p == 1:
                    return math.gcd(prev - 1, _n)
                if p == _n - 1:
                    break
            else:
                for i in range(2, _n):
                    x, y = i, (i * i + 1) % _n
                    f = math.gcd(abs(x - y), _n)

                    while f == 1:
                        x, y = (x * x + 1) % _n, (y * y + 1) % _n
                        y = (y * y + 1) % _n
                        f = math.gcd(abs(x - y), _n)

                    if f != _n:
                        return f

        return _n

    if n <= 1:
        return Counter()

    function = pollard_rho(n)

    if function == n:
        return Counter([n])

    return get_prime_factors(function) + get_prime_factors(n // function)


def solve():
    n = iinp()
    ans = 0

    for i in range(1, n + 1):
        _count = get_prime_factors(i)

        if len(_count) == 2:
            ans += 1

    return ans


def run():
    print(solve())


if __name__ == "__main__":
    if os.environ.get("DEBUG_CODEFORCES"):
        sys.stdin = open("../../input.txt", "r")
        start_time = time.time()
        run()
        print("\n--- %s seconds ---\n" % (time.time() - start_time))
    else:
        run()
