# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/1779/problem/C
# Title  : C. Least Prefix Sum
# Tags   : tag-codeforces, tag-problem-C, tag-difficulty-1600, tag-not-pass
# Notes  : data structures, greedy
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

def solve():
    n, m = intl()
    a = intl()

    sums = [a[0]]

    for i in range(1, n):
        sums.append(sums[-1] + a[i])

    target_min = sums[m - 1]

    is_changes_needed = False

    for i in range(n):
        if sums[i] < target_min:
            is_changes_needed = True
            break

    if not is_changes_needed:
        return 0

    ans = 0

    # if our min not the smallest value until m, then we need to minimise it
    if target_min > min(sums[:m]):
        while True:
            is_found_smaller = False
            found_idx = -1

            for i in range(m):
                if sums[i] < target_min:
                    found_idx = i
                    is_found_smaller = True
                    break

            if is_found_smaller:
                _max = max(a[found_idx:m])
                _max_idx = a[found_idx:m].index(_max)

                old_value = a[found_idx + _max_idx]
                new_value = -1 * old_value

                a[found_idx + _max_idx] = new_value

                for i in range(found_idx + _max_idx, n):
                    sums[i] -= old_value
                    sums[i] += new_value

                target_min = sums[m - 1]
                ans += 1
            else:
                break

    # if we found some values after m, then we need to maximize minimum after that
    if len(sums[m:]) > 0 and target_min > min(sums[m:]):
        while True:
            is_found_smaller = False
            found_idx = -1

            for i in range(m, n):
                if sums[i] < target_min:
                    is_found_smaller = True
                    found_idx = i
                    break

            if is_found_smaller:
                _min = min(a[m:found_idx + 1])
                _min_idx = a[m:].index(_min)

                old_value = a[m + _min_idx]
                new_value = -1 * old_value

                a[m + _min_idx] = new_value

                for i in range(m + _min_idx, n):
                    sums[i] -= old_value
                    sums[i] += new_value

                ans += 1
            else:
                break

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
