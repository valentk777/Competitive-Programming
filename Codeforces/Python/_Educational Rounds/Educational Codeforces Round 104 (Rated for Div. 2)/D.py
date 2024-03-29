# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/1487/problem/D
# Title  : Pythagorean Triples
# Tags   : tag-codeforces, tag-problem-D, tag-div-2, tag-difficulty-1500, tag-not-pass
# Notes  : binary search, brute force, math, number theory
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
yes = "YES"
no = "NO"

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

# time limit
def is_power_until_n(n):
    is_power = [False for _ in range(n + 1)]

    for i in range(2, n + 1):
        j = i ** 2

        while j < n:
            is_power[j] = True
            j *= i

    return is_power


def get_all_numbers(n):
    # c^2 = a^2 + b^2
    # c = a^2 + b. Rise second power of 2. => c^2 = a^4 - 2a^2b+ b^2. Join equations
    # a^2 == 0 (not an option) or a^2 - 2b - 1 = 0, after discriminant a = sqrt(2b + 1). It should be natural number.
    a_b_pairs = []

    for b in range(2, n + 1):
        if is_power_until_n(2 * b + 1):
            a_b_pairs.append((int(math.sqrt(2 * b + 1)), b))

    return a_b_pairs


# DATA = is_power_until_n(10 ** 9)


def solve():
    n = iinp()

    # c^2 = a^2 + b^2
    # c = a^2 + b. Rise second power of 2. => c^2 = a^4 - 2a^2b+ b^2. Join equations
    # a^2 == 0 (not an option) or a^2 - 2b - 1 = 0, after discriminant a = sqrt(2b + 1). It should be natural number.
    a_b_pairs = set()
    ans = 0

    for b in range(2, n + 1):
        _sqrt = math.sqrt(2 * b + 1)

        if _sqrt == int(_sqrt):
            # ans +=1
            a_b_pairs.add((int(_sqrt), b))

    return len(a_b_pairs)
    # return ans


def run():
    t = iinp()

    for _ in range(t):
        print(solve())


if __name__ == "__main__":
    if os.environ.get("DEBUG_CODEFORCES"):
        sys.stdin = open("../../input.txt", "r")
        start_time = time.time()
        run()
        print("\n--- %s seconds ---\n" % (time.time() - start_time))
    else:
        run()
