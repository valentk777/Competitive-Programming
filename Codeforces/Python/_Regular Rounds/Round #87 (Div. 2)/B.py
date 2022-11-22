# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/116/problem/B
# Title  : B. Little Pigs and Wolves
# Tags   : tag-codeforces, tag-problem-B, tag-div-2
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

def check_wolves(matrix, i, j, n, m):
    wolves = []

    if i - 1 >= 0 and matrix[i - 1][j] == "W":
        wolves.append((i - 1, j))

    if j - 1 >= 0 and matrix[i][j - 1] == "W":
        wolves.append((i, j - 1))

    if i + 1 < n and matrix[i + 1][j] == "W":
        wolves.append((i + 1, j))

    if j + 1 < m and matrix[i][j + 1] == "W":
        wolves.append((i, j + 1))

    return wolves


def is_pig_exist(matrix, n, m):
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == "P":
                return True

    return False


def solve():
    n, m = intl()

    _matrix = []
    ans = 0

    for i in range(n):
        _matrix.append(list(inp()))

    while True:
        if not is_pig_exist(_matrix, n, m):
            break

        for i in range(n):
            for j in range(m):
                if _matrix[i][j] == "P":
                    wolves = check_wolves(_matrix, i, j, n, m)

                    if len(wolves) == 0:
                        _matrix[i][j] = "."

                    if len(wolves) == 1:
                        ans += 1
                        _matrix[i][j] = "."
                        _matrix[wolves[0][0]][wolves[0][1]] = "."

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
