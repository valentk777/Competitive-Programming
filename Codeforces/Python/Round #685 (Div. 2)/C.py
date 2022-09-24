# -----------------------------------------------------------
# URL    : https://codeforces.com/contest/1451/problem/C
# Title  : String Equality
# Notes  : tag-codeforces, tag-problem-C, tag-div-2
# -----------------------------------------------------------

# ---------------------------------------------------Shared part--------------------------------------------------------
import os
import time
from sys import stdin, maxsize

inp = lambda: stdin.readline().strip()
iinp = lambda: int(inp())
intl = lambda: list(map(int, inp().split()))
strl = lambda: list(inp().split())

MOD = 10 ** 9 + 7
INF = maxsize


# -------------------------------------------------------Solution-------------------------------------------------------

# initial solution rejected because it was too slow. It runs out, that reading input was too slow
# changing to stdin.readline() speed up both solutions and now both of them accepted.
def solve():
    n, k = intl()
    a = list(map(lambda x: ord(x) - ord("a") + 1, list(inp())))
    b = list(map(lambda x: ord(x) - ord("a") + 1, list(inp())))

    sum_a = sum(a)
    sum_b = sum(b)

    if sum_a > sum_b:
        return "No"

    if sum_a == sum_b:
        if sorted(a) == sorted(b):
            return "Yes"
        else:
            return "No"

    if (sum_b - sum_a) % k != 0:
        return "No"

    new_a = []

    for i in range(n):
        if a[i] in b:
            b.remove(a[i])
        else:
            new_a.append(a[i])

    a = new_a
    n_a = len(a)

    if n_a < k:
        return "No"

    if n_a % k != 0:
        return "No"

    a = sorted(a)
    b = sorted(b)

    for i in range(0, n_a, k):
        if a[i:i + k].count(a[i:i + k][0]) != len(a[i:i + k]):
            return "No"

        if b[i:i + k].count(b[i:i + k][0]) != len(b[i:i + k]):
            return "No"

    return "Yes"


def solve_fast():
    n, k = intl()

    a = inp()
    b = inp()

    # aa = {chr(i): 0 for i in range(ord("a"), ord("z") + 2)}
    # bb = {chr(i): 0 for i in range(ord("a"), ord("z") + 2)}

    # letters = list(string.ascii_lowercase)
    # aa = {i: 0 for i in letters + ["{"]}
    # bb = {i: 0 for i in letters + ["{"]}

    aa = [0 for _ in range(27)]
    bb = [0 for _ in range(27)]

    for i in range(n):
        aa[ord(a[i]) - ord("a")] += 1
        bb[ord(b[i]) - ord("a")] += 1

    for i in range(25):
        if aa[i] < bb[i]:
            return "No"

        aa[i] -= bb[i]

        if aa[i] % k != 0:
            return "No"

        aa[i + 1] += aa[i]

    if aa[26] != bb[26]:
        return "No"

    return "Yes"


def run():
    t = iinp()

    for _ in range(t):
        print(solve_fast())


if __name__ == "__main__":
    if os.environ.get("DEBUG_CODEFORCES"):
        stdin = open("../input.txt", "r")
        start_time = time.time()
        run()
        print("\n--- %s seconds ---\n" % (time.time() - start_time))
    else:
        run()
