# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/1382/problem/B
# Title  : Sequential Nim
# Tags   : tag-codeforces, tag-problem-B, tag-div-2, tag-difficulty-1100
# Notes  : dp, games
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

def strategy_one(a, i, number_of_ones):
    # strategy one
    if a[i] > 1:
        a[i] = 1
        number_of_ones += 1
    elif a[i] == 1:
        number_of_ones -= 1
        a[i] = 0
        i += 1
    return i, number_of_ones


# wrong answer
def solve_wrong():
    n = iinp()
    a = intl()

    # if we have one pile - take all and winner first
    # if first pile contains k stones, so this player always win,
    # because he can remove all of them or k -1 based on the most optimal situation
    # so the first player which gets pile != 1 - wins

    number_of_ones = a[:-1].count(1)
    move = 0
    i = 0

    while i < n:
        if i + 1 == n:
            # last move
            a[i] = 0
            i += 1

        elif number_of_ones & 1 == 0:
            i, number_of_ones = strategy_one(a, i, number_of_ones)
        else:
            # strategy two. use strategy 1 if next 1 in current player position.
            use_strategy_one = False
            for j in range(i + 2, n - 1, 2):
                if a[j] == 1:
                    use_strategy_one = True
                    break

            if use_strategy_one:
                i, number_of_ones = strategy_one(a, i, number_of_ones)
            else:
                if a[i] == 1:
                    number_of_ones -= 1

                a[i] = 0
                i += 1

        move ^= 1

    if move == 0:
        return "Second"

    return "First"


def solve():
    n = iinp()
    a = intl()

    # if we have one pile - take all and winner first
    # if first pile contains k stones, so this player always win,
    # because he can remove all of them or k -1 based on the most optimal situation
    # so the first player which gets pile != 1 - wins
    move = 0

    for i in range(n):
        move ^= 1

        if a[i] != 1:
            break

    if move == 0:
        return "Second"

    return "First"


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
