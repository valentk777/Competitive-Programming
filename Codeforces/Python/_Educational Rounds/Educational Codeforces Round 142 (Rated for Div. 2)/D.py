# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/1792/problem/D
# Title  : D. Fixed Prefix Permutations
# Tags   : tag-codeforces, tag-problem-D, tag-div-2, tag-difficulty-0, tag-not-pass
# Notes  : binary search, data structures, math, sortings, strings
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

# tree using matrix (faster, less memory)
class TrieArray:
    def __init__(self, m):
        self.root = [None] * m
        self.size = m

    def insert(self, _list):
        current_root = self.root

        for element in _list:
            if current_root[element] is None:
                current_root[element] = [None] * self.size

            current_root = current_root[element]

    def query(self, word):
        current_root = self.root
        prefix = []

        for element in word:
            if current_root[element] is None:
                return prefix

            current_root = current_root[element]
            prefix.append(element)

        return prefix


# tree using dictionary
class TrieDict:
    def __init__(self):
        self.root = {}

    def insert(self, _list):
        current_root = self.root

        for element in _list:
            if element not in current_root:
                current_root[element] = {}

            current_root = current_root[element]

    def query(self, word):
        current_root = self.root
        prefix = []

        for element in word:
            if element not in current_root:
                return prefix

            current_root = current_root[element]
            prefix.append(element)

        return prefix


def solve_array():
    n, m = intl()

    permutations = [intl() for _ in range(n)]
    trie = TrieArray(m + 1)

    for i in range(n):
        trie.insert(get_perfect_permutation(permutations[i]))

    ans = []

    for perm in permutations:
        ans.append(len(trie.query(perm)))

    return list_to_string_list(ans)


def solve_dict():
    n, m = intl()

    permutations = [intl() for _ in range(n)]
    trie = TrieDict()

    for i in range(n):
        trie.insert(get_perfect_permutation(permutations[i]))

    ans = []

    for perm in permutations:
        ans.append(len(trie.query(perm)))

    return list_to_string_list(ans)


def get_perfect_permutation(p):
    ideal = list(enumerate(p, 1))
    ideal.sort(key=lambda x: x[1])
    ideal = [i[0] for i in ideal]
    return ideal


def solve_works():
    n, m = intl()

    permutations = []
    for i in range(n):
        permutations.append(intl())

    ideals = []
    for i in range(n):
        ideals.append(get_perfect_permutation(permutations[i]))

    trie = {}
    for ideal in ideals:
        root = trie
        for i in ideal:
            root = root.setdefault(i, {})

    ans = []

    for perm in permutations:
        root = trie
        mx = 0
        for i in perm:
            if i not in root:
                break
            mx += 1
            root = root[i]

        ans.append(mx)

    return list_to_string_list(ans)


def max_after_multiply(n, p1, p2):
    for i, e in enumerate(p1):
        if p2[e - 1] != i + 1:
            return i

    return n


# time limit
def solve_slow():
    n, m = intl()
    permutations = []

    for i in range(n):
        permutations.append(intl())

    ans = [0] * n

    for i in range(n):
        p1 = permutations[i]

        if ans[i] == m:
            continue

        for j in range(n):
            p2 = permutations[j]

            # check if possible to be bigger
            if p2[p1[ans[i]] - 1] != ans[i] + 1:
                continue

            candidate = max_after_multiply(m, p1, p2)

            if candidate > ans[i]:
                ans[i] = candidate

                if ans[i] == m:
                    break

    return list_to_string_list(ans)


def run():
    t = iinp()

    for _ in range(t):
        print(solve_array())


if __name__ == "__main__":
    if os.environ.get("DEBUG_CODEFORCES"):
        sys.stdin = open("../../input.txt", "r")
        start_time = time.time()
        run()
        print("\n--- %s seconds ---\n" % (time.time() - start_time))
    else:
        run()
