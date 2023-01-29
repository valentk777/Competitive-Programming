# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/1771/problem/B
# Title  : Hossam and Friends
# Tags   : tag-codeforces, tag-problem-B, tag-div-2, tag-difficulty-1400
# Notes  : binary search, constructive algorithms, dp, two pointers
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

def solve():
    n, m = intl()

    # we need to store only min b value for a single pair
    pairs = _dp(n)

    for i in range(m):
        a, b = intl()
        _min = min(a, b)
        _max = max(a, b)
        pairs[_min] = min(pairs[_min], _max - 1)

    # if we have a case where 1 -> 3 do not have any marker in this dictionary, but 2 -> 3 is not a fread, so 1 -> 3
    # have to be updated to min allowed value.
    for i in range(n, 0, -1):
        pairs[i] = min(pairs[i], pairs[i + 1])

    ans = 0

    # we can just iterate all starts and check number of pairs we can make from this point.
    for i in range(1, n + 1):
        ans += pairs[i] - i + 1

    return ans


# memory limit
def solve_memory_limit():
    n, m = intl()

    # we will use only half of matrix
    matrix = [[1 for _ in range(n)] for _ in range(n)]

    for i in range(m):
        a, b = intl()

        # if we found that from this point we are not able to make a pair,
        # then fill all values to 0 until end of the matrix

        for j in range(b - 1, n):
            matrix[a - 1][j] = 0

    ans = 0

    for i in range(n):
        for j in range(i, n):
            ans += matrix[i][j]

    return ans


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
