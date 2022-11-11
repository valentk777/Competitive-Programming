# -----------------------------------------------------------
# URL    : https://codeforces.com/contest/115/problem/A
# Title  : A. Party
# Notes  : tag-codeforces, tag-problem-A, tag-div-1
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

# find depht of element in graph
def deep(edges, x):
    temp = x
    level = 0

    while temp != 0:
        level += 1
        temp = edges[temp]

    return level


def solve():
    n = iinp()
    nodes = []

    for i in range(n):
        p = iinp()
        nodes.append(p)

    edges = defaultdict(int)

    for i in range(n):
        if nodes[i] != -1:
            edges[i + 1] = nodes[i]
        else:
            edges[i + 1] = 0

    ans = 0

    for e in list(edges.keys()):
        ans = max(ans, deep(edges, e))

    return ans


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
