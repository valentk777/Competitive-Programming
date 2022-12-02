# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/792/problem/C
# Title  : Divide by Three
# Tags   : tag-codeforces, tag-problem-C, tag-difficulty-2000
# Notes  : dp, greedy, math, number theory
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
    n = inp()
    len_n = len(n)
    _count = defaultdict(int)
    _zeros = []
    _sum = 0

    for i in range(len_n):
        _count[int(n[i]) % 3] += 1
        _sum += int(n[i])
        _sum %= 3

        if n[i] == "0":
            _zeros.append(i)

    if _sum == 0:
        return n

    ans = []

    if len_n - 1 != 0:
        for candidate in range(_sum, 10, 3):
            if _count[candidate % 3] >= 1:
                index = n.rfind(str(candidate))

                if index == -1:
                    continue

                x = n[:index] + n[index + 1:]
                ans.append(int(x))

    if len(ans) != 0:
        ans = sorted(ans, reverse=True)

        if len(str(ans[0])) == len_n - 1:
            return ans[0]

    if len_n - 2 != 0:
        for i in range(1, 9):
            for j in range(1, 9):
                if (i + j) % 3 != _sum or i % 3 == 0 or j % 3 == 0:
                    continue

                if (i == j and _count[i % 3] >= 2) or (i != j and _count[i % 3] >= 1 and _count[j % 3] >= 1):
                    index = n.rfind(str(i))

                    if index == -1:
                        continue

                    x = n[:index] + n[index + 1:]
                    index = x.rfind(str(j))

                    if index == -1:
                        continue

                    x = x[:index] + x[index + 1:]
                    ans.append(int(x))

    if len(ans) == 0:
        return -1

    return max(ans)


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
