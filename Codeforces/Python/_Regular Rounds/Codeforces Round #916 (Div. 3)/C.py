# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/1914/problem/C
# Title  : Quests
# Tags   : tag-codeforces, tag-problem-C, tag-div-3, tag-difficulty-0
# Notes  : brute force, greedy, math
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
_cnt = lambda _a: Counter(_a)


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

def solve_slow():
    n, k = intl()
    a = intl()
    b = intl()

    # n, k
    dp = _dp(0)
    end = min(n, k) + 1

    # Case 1: complete the quest for the first time
    for i in range(1, end):
        dp[i, i] = dp[i - 1, i - 1] + a[i - 1]

    # Case 2: complete the quest again
    for i in range(1, end):
        for j in range(i + 1, k + 1):
            dp[i, j] = max(dp[i - 1, j - 1] + a[i - 1], dp[i, j - 1] + b[i - 1])

    print(dp)

    return max(dp.values())


def solve_memory():
    n, k = intl()
    a = intl()
    b = intl()

    # n, k
    dp = _dp(0)
    max_b = _dp(0)
    end = min(n, k) + 1

    # Case 1: complete the quest for the first time
    for i in range(1, end):
        max_b[i] = max(max_b[i - 1], b[i - 1])
        dp[i, i] = dp[i - 1, i - 1] + a[i - 1]

    for i in range(1, end):
        for j in range(i + 1, end):
            dp[i, j] = max(dp[i - 1, j - 1] + a[i - 1], dp[i, j - 1] + max_b[i])

    if k > n:
        for i in range(1, end):
            dp[i, end] = dp[i, end - 1] + max_b[i] * (k - n)

    return max(dp.values())


def solve():
    n, k = intl()
    a = intl()
    b = intl()

    # n, k
    sum_a = _dp(0)
    max_b = _dp(0)

    end = min(n, k) + 1

    for i in range(1, end):
        sum_a[i] = sum_a[i - 1] + a[i - 1]
        max_b[i] = max(max_b[i - 1], b[i - 1])

    candidates = [*sum_a.values()]

    for i in range(1, end):
        candidates.append(sum_a[i] + max_b[i] * (k - i))

    return max(candidates)


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
