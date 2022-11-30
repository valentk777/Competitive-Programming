# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/2/problem/A
# Title  : Winner
# Tags   : tag-codeforces, tag-problem-A, tag-difficulty-1500
# Notes  : hashing, implementation
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

# Wrong answer (when winner lost score, he still winner)
def solve_wrong():
    n = iinp()

    _scores = _dp(0)
    _winner = ""
    _best_score = -INF

    for i in range(n):
        name, score = inp().split()
        _scores[name] += int(score)

        if _scores[name] > _best_score:
            _winner = name
            _best_score = _scores[name]

    return _winner


def solve():
    n = iinp()

    _scores = _dp(0)
    _winner = _dp([])
    history = []

    for i in range(n):
        name, score = inp().split()
        history.append([name, score])

        score = int(score)

        old_score = _scores[name]
        new_score = _scores[name] + score
        _scores[name] += score

        if old_score in _winner.keys() and name in _winner[old_score]:
            _winner[old_score].remove(name)

            if _winner[old_score] == []:
                del _winner[old_score]

        if new_score not in _winner.keys():
            _winner[new_score] = [name]
        else:
            _winner[new_score].append(name)

    _max = max(_winner.keys())
    candidates = _winner[_max]

    _scores = _dp(0)

    for name, score in history:
        if name not in candidates:
            continue

        _scores[name] += int(score)

        if _scores[name] >= _max:
            return name


def run():
    print(solve())


if __name__ == "__main__":
    if os.environ.get("DEBUG_CODEFORCES"):
        stdin = open("../../input.txt", "r")
        start_time = time.time()
        run()
        print("\n--- %s seconds ---\n" % (time.time() - start_time))
    else:
        run()
