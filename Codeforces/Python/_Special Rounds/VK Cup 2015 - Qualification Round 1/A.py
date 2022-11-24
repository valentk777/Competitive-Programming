# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/522/problem/A
# Title  : Reposts
# Tags   : tag-codeforces, tag-problem-A, tag-difficulty-1200
# Notes  : *special, dfs and similar, dp, graphs, trees
# ---------------------------------------------------------------------------------------

# ---------------------------------------------------Shared part--------------------------------------------------------
import math
import os
import time
from collections import defaultdict, Counter
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
fact = lambda number: math.factorial(number)
cnt = lambda _a: Counter(_a)


def lcm(a, b):
    return a * b // math.gcd(a, b)


def print_dp(_dict):
    for item in _dict.items():
        print(f"{item[0]} = {item[1]}")


MOD = 10 ** 9 + 7
INF = maxsize
A = 911382323
M = 9999999999879998


# -------------------------------------------------------Solution-------------------------------------------------------

def find_depht(trees, names):
    if len(names) == 0:
        return 0

    _max = 0

    for name in names:
        candidate = find_depht(trees, trees[name]) + 1

        if _max < candidate:
            _max = candidate

    return _max


def dfs(v, graph, used, k):
    ans = k
    used.add(v)

    for u in graph[v]:
        if u not in used:
            ans = max(ans, dfs(u, graph, used | {u}, k + 1))

    return ans


def solve_dp():
    n = iinp()

    dp = _dp(0)
    dp['polycarp'] = 1

    for i in range(n):
        _new, _, _old = strl()
        dp[_new.lower()] = dp[_old.lower()] + 1

    return max(dp.values())


def solve():
    n = iinp()

    graph = defaultdict(set)

    for i in range(n):
        _new, _, _old = strl()
        graph[_old.lower()].add(_new.lower())

    find_depht(graph, graph["polycarp"]) + 1
    ans = dfs('polycarp', graph, set(), 1)
    return ans


def solve_dfs():
    n = iinp()

    graph = defaultdict(set)

    for i in range(n):
        _new, _, _old = strl()
        graph[_old.lower()].add(_new.lower())

    return dfs('polycarp', graph, set(), 1)


def run():
    print(solve_dp())


if __name__ == "__main__":
    if os.environ.get("DEBUG_CODEFORCES"):
        stdin = open("../../input.txt", "r")
        start_time = time.time()
        run()
        print("\n--- %s seconds ---\n" % (time.time() - start_time))
    else:
        run()
