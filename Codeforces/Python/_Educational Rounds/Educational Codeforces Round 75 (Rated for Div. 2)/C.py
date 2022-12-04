# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/1251/problem/C
# Title  : Minimize The Integer
# Tags   : tag-codeforces, tag-problem-C, tag-div-2, tag-difficulty-1600
# Notes  : greedy, two pointers
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
    a = inp()
    odd = []
    even = []

    for i in a:
        if int(i) & 1:
            odd.append(i)
        else:
            even.append(i)

    ans = []
    i = 0
    j = 0

    while i < len(even) or j < len(odd):
        if i == len(even):
            ans.append(str(odd[j]))
            j += 1
        elif j == len(odd):
            ans.append(str(even[i]))
            i += 1
        elif even[i] < odd[j]:
            ans.append(str(even[i]))
            i += 1
        else:
            ans.append(str(odd[j]))
            j += 1

    return list_to_string(ans)
    # return list_to_string(merge(odd, even))


# two pointers
def solve_2():
    a = list(map(int, list(inp())))
    n = len(a)
    left = 0
    right = 1
    ans = []

    while left < n and right < n:
        if a[right] == -1:
            right += 1

        if a[left] % 2 != a[right] % 2:
            while left <= right and a[left] < a[right]:
                if a[left] != -1:
                    ans.append(a[left])

                left += 1

            if a[left] > a[right]:
                ans.append(a[right])
                a[right] = -1
                right += 1

        else:
            right += 1

    while left < n:
        if a[left] != -1:
            ans.append(a[left])

        left += 1

    return list_to_string(ans)


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
