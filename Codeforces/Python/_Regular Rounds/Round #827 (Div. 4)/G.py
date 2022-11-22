# -----------------------------------------------------------
# URL    : https://codeforces.com/contest/1742/problem/G
# Title  : G. Orray
# Notes  : tag-codeforces, tag-problem-G, tag-div-4
# -----------------------------------------------------------

# ---------------------------------------------------Shared part--------------------------------------------------------
import os
import time
from collections import defaultdict
from sys import stdin, maxsize, stdout

inp = lambda: stdin.readline().strip()
iinp = lambda: int(inp())
intl = lambda: list(map(int, inp().split()))
strl = lambda: list(inp().split())
list_to_string = lambda _a: "".join(map(str, _a))
list_to_string_list = lambda _a: " ".join(map(str, _a))
_dp = lambda default_value: defaultdict(lambda: default_value)
flush = lambda: stdout.flush()
print_flush = lambda _text: (print(_text), flush())


def print_dp(_dict):
    for item in _dict.items():
        print(f"{item[0]} = {item[1]}")


MOD = 10 ** 9 + 7
INF = maxsize
A = 911382323
M = 9999999999879998


# -------------------------------------------------------Solution-------------------------------------------------------

def solve():
    n = iinp()
    a = intl()
    a = sorted(a, reverse=True)
    b = [a[0]]
    ans = [a[0]]

    a.remove(a[0])

    for _ in range(n - 1):
        e = b[-1]

        _max = -INF
        _remove = 0

        for j in range(len(a)):
            if a[j] | e > _max:
                _max = a[j] | e
                _remove = a[j]

        b.append(_max)
        ans.append(_remove)
        a.remove(_remove)

        if _max == e:
            ans.extend(a)
            break

    return list_to_string_list(ans)


def run():
    t = iinp()

    for _ in range(t):
        print(solve())


if __name__ == "__main__":
    if os.environ.get("DEBUG_CODEFORCES"):
        stdin = open("../../input.txt", "r")
        start_time = time.time()
        run()
        print("\n--- %s seconds ---\n" % (time.time() - start_time))
    else:
        run()
