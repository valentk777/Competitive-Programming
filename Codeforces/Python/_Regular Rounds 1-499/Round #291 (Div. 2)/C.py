# -----------------------------------------------------------
# URL    : https://codeforces.com/contest/514/problem/C
# Title  : Watto and Mechanism
# Notes  : tag-codeforces, tag-problem-C, tag-div-2
# -----------------------------------------------------------

# ---------------------------------------------------Shared part--------------------------------------------------------
import os
import time
from collections import defaultdict
from sys import stdin, maxsize

inp = lambda: stdin.readline().strip()
iinp = lambda: int(inp())
intl = lambda: list(map(int, inp().split()))
strl = lambda: list(inp().split())
list_to_string = lambda _a: "".join(map(str, _a))
list_to_string_list = lambda _a: " ".join(map(str, _a))
_dp = lambda default_value: defaultdict(lambda: default_value)
print_dp = lambda _dict: list(map(lambda item: print(f"{item[0]} = {item[1]}"), _dict.items()))

MOD = 10 ** 9 + 7
INF = maxsize


# -------------------------------------------------------Solution-------------------------------------------------------

def can_we_make_it(value, s, n):
    left = 0
    right = n
    mismatch = 0

    while left < right:
        mid = (left + right) // 2

        if value[left: mid] != s[left: mid] and value[mid: right] != s[mid: right]:
            return False

        if right - left == 1:
            return True

        if value[left: mid] == s[left: mid]:
            left = mid
        elif value[mid: right] == s[mid: right]:
            right = mid

    return mismatch < 2


def solve_not_pass():
    n, m = intl()

    if n == 0:
        return "NO"

    memory = _dp([])

    for i in range(n):
        s = inp()

        if len(s) in memory.keys():
            memory[len(s)].append(s)
        else:
            memory[len(s)] = []
            memory[len(s)].append(s)

    for i in range(m):
        s = inp()
        s_n = len(s)

        if not memory[s_n]:
            print("NO")
            continue

        stop = False

        for value in memory[s_n]:
            if can_we_make_it(value, s, s_n):
                stop = True
                break

        if stop:
            print("YES")
        else:
            print("NO")


M = 9999999999879998
random_number = 203


def str_hash(s):
    _hash = 0
    _pow = 1

    for c in s:
        _hash = (_hash + ord(c) * _pow) % M
        _pow = (_pow * random_number) % M

    return _hash


def solve():
    n, m = intl()
    memory = set()

    for i in range(n):
        s = inp()
        h = str_hash(s)
        p = 1

        # add all hashes with changed only single character
        for j in range(len(s)):
            for k in range(ord("a"), ord("c") + 1):
                # if we can make a new word
                if ord(s[j]) != k:
                    memory.add((h + p * (k - ord(s[j]))) % M)

            p = (p * random_number) % M

    for i in range(m):
        s = inp()
        b = str_hash(s)

        if b in memory:
            print('YES')
        else:
            print('NO')


def run():
    solve()


if __name__ == "__main__":
    if os.environ.get("DEBUG_CODEFORCES"):
        stdin = open("../../input.txt", "r")
        start_time = time.time()
        run()
        print("\n--- %s seconds ---\n" % (time.time() - start_time))
    else:
        run()
