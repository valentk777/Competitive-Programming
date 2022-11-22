# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/405/problem/C
# Title  : C. Unusual Product
# Tags   : tag-codeforces, tag-problem-C, tag-div-2
# ---------------------------------------------------------------------------------------

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

def action_1(_matrix, i):
    _matrix[i - 1] = [x ^ 1 for x in _matrix[i - 1]]
    return _matrix


def action_2(_matrix, i, n):
    for j in range(n):
        _matrix[j][i - 1] = _matrix[j][i - 1] ^ 1

    return _matrix


def action_3(_matrix, n):
    c = [[sum(a * b for a, b in zip(A_row, B_col)) for B_col in zip(*_matrix)] for A_row in _matrix]

    ans = 0

    for i in range(n):
        ans += c[i][i]

    return ans % 2


def solve_slow():
    n = iinp()

    matrix = []

    for i in range(n):
        matrix.append(intl())

    q = iinp()

    ans = []

    for i in range(q):
        action = intl()

        if action[0] == 1:
            matrix = action_1(matrix, action[1])
        elif action[0] == 2:
            matrix = action_2(matrix, action[1], n)
        else:
            ans.append(action_3(matrix, n))

    return list_to_string(ans)


def solve():
    n = iinp()

    matrix = []

    for i in range(n):
        matrix.append(intl())

    _sum = 0

    for i in range(n):
        _sum += matrix[i][i]

    _sum %= 2

    q = iinp()
    ans = []

    for i in range(q):
        action = intl()

        if action[0] == 3:
            ans.append(_sum)
        else:
            _sum ^= 1

    return list_to_string(ans)


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
