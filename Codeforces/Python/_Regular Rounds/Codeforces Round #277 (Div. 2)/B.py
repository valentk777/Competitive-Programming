# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/486/problem/B
# Title  : OR in Matrix
# Tags   : tag-codeforces, tag-problem-B, tag-div-2, tag-difficulty-1300
# Notes  : greedy, hashing, implementation
# ---------------------------------------------------------------------------------------

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

def solve():
    m, n = intl()
    matrix = []

    for i in range(m):
        s = intl()
        matrix.append(s)

    m_sums = [0 for _ in range(m)]
    n_sums = [0 for _ in range(n)]

    for i in range(m):
        _sum = sum(matrix[i])
        m_sums[i] = _sum

    for j in range(n):
        _sum = 0

        for i in range(m):
            _sum += matrix[i][j]

        n_sums[j] = _sum

    if n not in m_sums and sum(m_sums) != 0:
        print("NO")
        return

    if m not in n_sums and sum(n_sums) != 0:
        print("NO")
        return

    ans = []

    for i in range(m):
        ans.append([0 for _ in range(n)])

    for i in range(m):
        if m_sums[i] == n:
            ans[i] = [-1 for i in range(n)]

    for i in range(n):
        for j in range(m):
            if ans[j][i] == -1:
                if n_sums[i] == m:
                    ans[j][i] = 1
                else:
                    ans[j][i] = 0

    ats_m_sums = [0 for _ in range(m)]
    ats_n_sums = [0 for _ in range(n)]

    for i in range(m):
        _sum = 0
        for j in range(n):
            _sum |= ans[i][j]

        ats_m_sums[i] = _sum

    for j in range(n):
        _sum = 0

        for i in range(m):
            _sum |= ans[i][j]

        ats_n_sums[j] = _sum

    for i in range(m):
        for j in range(n):
            if (ats_n_sums[j] | ats_m_sums[i]) != matrix[i][j]:
                print("NO")
                return

    print("YES")

    for i in range(m):
        print(list_to_string_list(ans[i]))


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
