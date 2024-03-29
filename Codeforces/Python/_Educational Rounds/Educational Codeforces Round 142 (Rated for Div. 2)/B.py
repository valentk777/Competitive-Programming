# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/1792/problem/B
# Title  : B. Stand-up Comedian
# Tags   : tag-codeforces, tag-problem-B, tag-div-2, tag-difficulty-0
# Notes  : greedy, math
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
    jokes = intl()

    if jokes[0] == 0:
        return 1

    # say all positive jokes
    ans = jokes[0]

    # say double minimum amount of jokes that only one likes. After this, jokes_1 or jokes_2 should be 0
    ans += 2 * min(jokes[1], jokes[2])

    # after this, our listeners have same or more mood than initially. So min mood is jokes[0].
    min_mood = jokes[0]
    jokes_left_after_2and_3 = max(jokes[1], jokes[2]) - min(jokes[1], jokes[2])
    bad_jokes_left = jokes_left_after_2and_3 + jokes[3]

    # we have more bad jokes than mood, so we consume whole mood to become 0 and then + 1
    if bad_jokes_left > min_mood:
        ans += min_mood + 1
    else:
        ans += bad_jokes_left

    return ans


# ugly
def solve_ugly():
    jokes = intl()

    if jokes[0] == 0:
        return 1

    # say all jokes for all
    ans = jokes[0]
    _a = jokes[0]
    _b = jokes[0]
    jokes[0] = 0

    _max = max(jokes[1], jokes[2])

    # say as many jokes as you can to make someone boosted and another one == 0
    if jokes[1] > jokes[2]:
        if _b - jokes[1] >= 0:
            _a += jokes[1]
            _b -= jokes[1]
            ans += jokes[1]
            jokes[1] = 0
        else:
            _a += _b
            ans += _b
            jokes[1] -= _b
            _b = 0
    else:
        if _a - jokes[2] >= 0:
            _b += jokes[2]
            _a -= jokes[2]
            ans += jokes[2]
            jokes[2] = 0
        else:
            _b += _a
            ans += _a
            jokes[2] -= _a
            _a = 0

    # both not 0
    if min(jokes[1], jokes[2]) != 0:
        if _a == 0:
            x = max((jokes[1] // _b) - 1, 0)
            y = max((jokes[2] // _b) - 1, 0)
            z = min(x, y)

            ans += z * _b * 2
            jokes[1] -= z * _b
            jokes[2] -= z * _b
        else:
            x = max((jokes[1] // _a) - 1, 0)
            y = max((jokes[2] // _a) - 1, 0)
            z = min(x, y)

            ans += z * _a * 2
            jokes[1] -= z * _a
            jokes[2] -= z * _a

    while True:
        if _a == 0 or _b == 0:
            pass

        _max = max(jokes[1], jokes[2])

        if _max == 0:
            break

        if _max == jokes[1] and _b > 0:
            joke = jokes[1]

            if _b - joke >= 0:
                _a += joke
                _b -= joke
                ans += joke
                jokes[1] = 0
            else:
                _a += _b
                ans += _b
                jokes[1] -= _b
                _b = 0

        elif _max == jokes[2] and _a > 0:
            joke = jokes[2]

            if _a - joke >= 0:
                _b += joke
                _a -= joke
                ans += joke
                jokes[2] = 0
            else:
                _b += _a
                ans += _a
                jokes[2] -= _a
                _a = 0

        elif jokes[1] > 0 and _b > 0:
            joke = jokes[1]

            if _b - joke >= 0:
                _a += joke
                _b -= joke
                ans += joke
                jokes[1] = 0
            else:
                _a += _b
                ans += _b
                jokes[1] -= _b
                _b = 0

        elif jokes[2] > 0 and _a > 0:
            joke = jokes[2]

            if _a - joke >= 0:
                _b += joke
                _a -= joke
                ans += joke
                jokes[2] = 0
            else:
                _b += _a
                ans += _a
                jokes[2] -= _a
                _a = 0


        else:
            break

    if _a > 0 and _b > 0:
        _min = min(_a, _b, jokes[3])
        ans += _min
        jokes[3] -= _min

    if jokes[1] > 0 or jokes[2] > 0 or jokes[3] > 0:
        ans += 1

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
