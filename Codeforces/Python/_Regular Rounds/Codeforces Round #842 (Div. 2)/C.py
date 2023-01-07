# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/1768/problem/C
# Title  : Elemental Decompress
# Tags   : tag-codeforces, tag-problem-C, tag-div-2, tag-difficulty-0
# Notes  : constructive algorithms, greedy, implementation, sortings
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

def solve():
    n = iinp()
    a = intl()
    a = [(k, i) for i, k in enumerate(a)]
    a = sorted(a, key=lambda x: x[0], reverse=True)

    ans_1 = [1 for _ in range(n)]
    ans_2 = [1 for _ in range(n)]

    free_idx_1 = []
    free_idx_2 = []

    count_numbers_of_same_element = 0
    max_element = n
    iteration_index = 0

    # iterate all numbers
    while max_element > 0:
        if iteration_index < n and a[iteration_index][0] == max_element:
            element, index = a[iteration_index]
            # we found this element first time
            if count_numbers_of_same_element == 0:
                ans_1[index] = element
                free_idx_2.append(index)

            # second (or more) time we see this element
            else:
                ans_2[index] = element
                free_idx_1.append(index)

            count_numbers_of_same_element += 1
            iteration_index += 1

        # if we have a gap like in [3, 3, 1] case where ans would be [3, 2, 1] and [2, 3, 1]
        # or we are missing second number
        else:
            if len(free_idx_2) == 0:
                print("NO")
                return

            # we have a gap
            if count_numbers_of_same_element == 0:
                if len(free_idx_1) == 0:
                    print("NO")
                    return

                index_1 = free_idx_1.pop()
                ans_1[index_1] = max_element
                index_2 = free_idx_2.pop()
                ans_2[index_2] = max_element

                count_numbers_of_same_element = 2
            # we are missing a second number
            else:
                index_2 = free_idx_2.pop()
                element, index = a[iteration_index - 1]
                ans_2[index_2] = element
                count_numbers_of_same_element += 1

        if count_numbers_of_same_element == 2:
            count_numbers_of_same_element = 0
            max_element -= 1

    print("YES")
    print(*ans_1)
    print(*ans_2)
    return


def run():
    t = iinp()

    for _ in range(t):
        solve()


if __name__ == "__main__":
    if os.environ.get("DEBUG_CODEFORCES"):
        sys.stdin = open("../../input.txt", "r")
        start_time = time.time()
        run()
        print("\n--- %s seconds ---\n" % (time.time() - start_time))
    else:
        run()
