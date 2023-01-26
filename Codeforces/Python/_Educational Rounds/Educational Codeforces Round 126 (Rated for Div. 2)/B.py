# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/1661/problem/B
# Title  : Getting Zero
# Tags   : tag-codeforces, tag-problem-B, tag-div-2, tag-difficulty-1300
# Notes  : bitmasks, brute force, dfs and similar, dp, graphs, greedy, shortest paths
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


def solve():
    n = iinp()
    a = intl()
    ans = []
    # bin -> 1000000000000000
    mod = 32768

    # if we multiply by 2, it will shift current bitwise representation to left.
    # if we reach mod area, that 1 will be removed. so in worse case scenario,
    # when we get 1, we can multiply this number by 2 until it react 16'th position and after mod become 0
    # so the answer never exceed 16.
    # but just multiply it is not enough. sometimes add 1 will be fewer steps than remove all ones by shifting.
    # 11111111111 will be only one step +1, but a lot of steps removing by multiplication.
    # also there is mixed cases, such as 101111111111.
    # Fastest way to add 1 and then multiply until all ones will be removed.

    # if we multiply firs, then it is never worth adding ones. and we can try adding ones only until 16,
    # because this is the worse case scenario by multiplication.

    for i in range(n):
        if a[i] % mod == 0:
            ans.append(0)
            continue

        # so we can try all additions and then multiplications.
        # key number, value min steps needed
        candidates = _dp(INF)

        for j in range(17):
            c = a[i] + j
            candidates[c % mod] = j

            if c == mod:
                # all next addition will be worse than we have now
                break

        result = candidates.copy()

        for key, value in candidates.items():
            for j in range(1, 17):
                c = key * (1 << j) % mod
                result[c] = min(result[c], value + j)

        ans.append(result[0])

    return ans


# time limit
def solve_slow():
    n = iinp()
    a = intl()
    ans = []
    mod = 32768

    for i in range(n):
        _min = mod - a[i]

        if a[i] % mod == 0:
            ans.append(0)
            continue

        data = [INF for i in range(mod + 1)]
        data[a[i]] = 0

        history = {a[i]}
        temp = set()

        while data[0] == INF:
            for e in history:
                c1 = (e + 1) % mod
                c2 = (e * 2) % mod
                # print(bin(c1))
                # print(bin(c2))

                data[c1] = min(data[c1], data[e] + 1)
                data[c2] = min(data[c2], data[e] + 1)

                temp.add(c1)
                temp.add(c2)

            history = temp
            temp = set()

        ans.append(data[0])

    return ans


def run():
    print(*solve())


if __name__ == "__main__":
    if os.environ.get("DEBUG_CODEFORCES"):
        sys.stdin = open("../../input.txt", "r")
        start_time = time.time()
        run()
        print("\n--- %s seconds ---\n" % (time.time() - start_time))
    else:
        run()
