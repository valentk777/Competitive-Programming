# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/1782/problem/D
# Title  : D. Many Perfect Squares
# Tags   : tag-codeforces, tag-problem-D, tag-div-1, tag-div-2, tag-difficulty-1800, tag-not-pass
# Notes  : brute force, dp, math, number theory
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

def get_perfect_squares(_from, _to):
    result = []

    _from = max(0, int(math.sqrt(_from)) - 1)

    for i in range(_from, _to + 1):
        number = i ** 2

        result.append(number)

    return result


# DATA = get_perfect_squares(0, 1000)
def get_next_perfect_square(n):
    _from = int(math.sqrt(n))
    candidate = _from ** 2

    if candidate < n:
        return (_from + 1) ** 2

    return candidate


def solve():
    # print(DATA)
    # print([b - a for a, b in zip(DATA[:], DATA[1:])])
    # print([b - a for a, b in zip(DATA[:], DATA[2:])])
    # print([b - a for a, b in zip(DATA[:], DATA[3:])])
    # print([b - a for a, b in zip(DATA[:], DATA[4:])])
    # print([b - a for a, b in zip(DATA[:], DATA[6:])])
    # print([b - a for a, b in zip(DATA[:], DATA[8:])])
    n = iinp()
    a = intl()

    odd_count = 1  # initialize odd_count to 1 as the smallest perfect square is 1
    for i in range(1, n):
        if (a[i] - a[i - 1]) % 2 != 0:  # check if the difference is odd
            odd_count += 1  # increment odd_count if difference is odd

    return odd_count

    if n == 1:
        return 1

    # the diff between perfect square numbers is all odd numbers. [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25...] if they are close numbers
    # or 4 multipliers [4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80] if not close.
    # it is index * 2 + 1
    # no matter what we add to numbers, diff will keep the same.
    # so we can check diffs between numbers and use these diffs to check if two numbers can make a perfect square.

    for i in range(n):
        for j in range(i + 1, n):
            print(a[i], a[j])
            x = get_next_perfect_square(a[i])
            y = get_next_perfect_square(x + 1)
            diff = a[j] - a[i]

            # it is impossible to get two perfect squares from this pair.
            if y - x <= diff:
                print("possible")
            else:
                pass

            # idx = (diff - 1) // 2
            # print(idx)
            print(diff)
        print("*" * 50)

    # print(DATA)
    # print([b - a for a, b in zip(DATA[:], DATA[1:])])
    #
    #
    #
    #
    #
    #
    # ans = -INF
    # perfect_squares = get_perfect_squares(a[0], a[-1])
    # print(perfect_squares)
    #
    # for x in range(100):
    #     _count = 0
    #
    #     for i in range(n):
    #         if a[i] + x in perfect_squares:
    #             _count += 1
    #
    #     if _count >= ans:
    #         print(np.array(a) + x)
    #
    #     if _count == n:
    #         ans = _count
    #         break
    #
    #     if _count > ans:
    #         ans = _count
    #
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
