# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/1780/problem/D
# Title  : D. Bit Guessing Game
# Tags   : tag-codeforces, tag-problem-D, tag-div-2, tag-difficulty-0
# Notes  : binary search, bitmasks, interactive
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


# sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
#

# endregion
# endregion

# -------------------------------------------------------Solution-------------------------------------------------------


def solve_v1():
    n = iinp()
    res = 0
    prev = n
    more = 0

    while True:
        # guess will always be power of two
        guess = 1 + more
        print_flush(f"- {guess}")
        now = iinp()
        res += 1

        if now == 0:
            print_flush(f"! {res}")
            return

        if now == prev - 1:
            prev = now
        else:
            diff = now - prev

            # get number from possible and current. Like if we had 11110 - 1 => 11101. so it is same amount of 1'ns.
            # so we know that it will be as at least diff power of two.
            # if we had 10 = 3 and 10 - 1 = 1, so we have at least 3 - 1 = 2 more.
            # We can add this to result and to future guesses.
            more = (1 << diff + 1) - 1
            prev = prev - 1
            res += more

            if not prev:
                print_flush(f"! {res}")
                return


def solve_v2():
    n = iinp()
    prev = n
    idx = 0
    guess = 1
    res = 0

    while n != 0:
        print_flush(f"- {guess}")
        res += guess
        n = iinp()
        idx += 1

        if n < prev:
            # if we get smaller amount of 1's, we can remove only power of two (only 1 one). all ones one by one
            guess = (1 << idx)
        elif n > prev:
            # if we get more 1's than before, so we need to remove new power of two same as in n < prev case,
            # but in addition remove old ones as well (the ones was added).
            guess |= (1 << idx)
        else:
            # if n == prev, we know that, we just guess same old value
            pass

        prev = n

    print_flush(f"! {res}")


# time limit
def solve_slow():
    history = []
    res = 0

    while True:
        number_of_one = iinp()
        history.append(number_of_one)

        if number_of_one == 0:
            break

        guess = int("1" * number_of_one, 2)

        if len(history) == 1:
            res += guess
            print_flush(f"- {guess}")
            continue

        historical = int("1" * history[-2], 2)

        for i in range(guess, INF):
            if bin(i).count("1") == number_of_one and bin(i + historical).count("1") == history[-2]:
                guess = i
                break

        res += guess

        print_flush(f"- {guess}")

    print_flush(f"! {res}")


def run():
    t = iinp()

    for _ in range(t):
        solve_v2()


if __name__ == "__main__":
    if os.environ.get("DEBUG_CODEFORCES"):
        sys.stdin = open("../../input.txt", "r")
        start_time = time.time()
        run()
        print("\n--- %s seconds ---\n" % (time.time() - start_time))
    else:
        run()
