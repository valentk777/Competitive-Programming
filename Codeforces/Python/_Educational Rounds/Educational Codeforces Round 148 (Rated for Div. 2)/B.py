# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/1832/problem/B
# Title  : Maximum Sum
# Tags   : tag-codeforces, tag-problem-B, tag-div-2, tag-difficulty-0
# Notes  : brute force, greedy
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

# the solution really simple. we need to calculate all possible options.
# firstly we make a list with possible loss choosing removing two smallest items
# secondly we make a list with possible loss choosing removing one largest items
# then we calculate all possible combinations.
# ex: choosing k times option1 and 0 option2, then k - 1 times option1 and 1 time option2, etc.
def solve():
    n, k = intl()
    a = intl()
    a = sorted(a)
    total = sum(a)

    sums_1 = [0]

    for i in range(0, 2 * k, 2):
        sums_1.append(sums_1[-1] + a[i] + a[i + 1])

    sums_2 = [0]
    for i in range(k):
        sums_2.append(sums_2[-1] + a[n - 1 - i])

    ans = -1

    for i in range(k + 1):
        candidate = total - sums_1[i] - sums_2[k - i]

        if candidate > ans:
            ans = candidate

    return ans


# Memory limit exceeded on test 4
def solve_memory():
    n, k = intl()
    a = intl()
    a = sorted(a)

    dp_matrix = _dp(0)
    # option1 - left times
    # option2 - right times
    dp_matrix[0, 0] = [0, n - 1, sum(a)]

    for option1 in range(1, k + 1):
        left = dp_matrix[option1 - 1, 0][0]
        right = dp_matrix[option1 - 1, 0][1]
        total = dp_matrix[option1 - 1, 0][2]
        dp_matrix[option1, 0] = [left + 2, right, total - a[left] - a[left + 1]]

    for option2 in range(1, k + 1):
        left = dp_matrix[0, option2 - 1][0]
        right = dp_matrix[0, option2 - 1][1]
        total = dp_matrix[0, option2 - 1][2]
        dp_matrix[0, option2] = [left, right - 1, total - a[right]]

    for option1 in range(1, k):
        for option2 in range(1, k):
            left = dp_matrix[option1 - 1, option2 - 1][0]
            right = dp_matrix[option1 - 1, option2 - 1][1]
            total = dp_matrix[option1 - 1, option2 - 1][2]

            dp_matrix[option1, option2] = [left + 2, right - 1, total - a[left] - a[left + 1] - a[right]]

    # print_dp(dp_matrix)

    ans = -1

    for i in range(k + 1):
        if ans < dp_matrix[i, k - i][2]:
            ans = dp_matrix[i, k - i][2]

    return ans


# Wrong answer on test 3
def solve_wrong():
    n, k = intl()
    a = intl()
    a = sorted(a)

    while k > 0:
        # if this is a last run - pick the smallest
        if k == 1:
            if a[0] + a[1] < a[-1]:
                a = a[2:]
            else:
                a = a[:-1]
        # else, pick smallest out of two.
        else:
            if a[0] + a[1] <= a[-1] and a[0] + a[1] + a[2] + a[3] <= a[-1] + a[-2]:
                a = a[2:]
            else:
                a = a[:-1]

        k -= 1

    return sum(a)


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
