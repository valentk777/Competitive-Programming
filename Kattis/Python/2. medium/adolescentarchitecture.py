# -----------------------------------------------------------
# URL    : https://open.kattis.com/problems/adolescentarchitecture
# Title  : Adolescent Architecture
# Notes  : tag-kattis, tag-medium
# -----------------------------------------------------------

# ---------------------------------------------------Shared part--------------------------------------------------------
import os
import time
from math import sqrt
from sys import stdin, maxsize

inp = lambda: stdin.readline().strip()
iinp = lambda: int(inp())
intl = lambda: list(map(int, inp().split()))
strl = lambda: list(inp().split())

MOD = 10 ** 9 + 7
INF = maxsize


# -------------------------------------------------------Solution-------------------------------------------------------

def solve():
    n = iinp()

    # shape, shape_index(1 - cylinder, 2 - cube), ranking_length, length
    shapes = []

    for _ in range(n):
        shape, length = strl()

        if shape == "cube":
            shapes.append((shape, 2, int(length), int(length)))
        else:
            shapes.append((shape, 1, 2 * int(length), int(length)))

    shapes = sorted(shapes, key=lambda x: (x[2], x[1]))

    is_impossible = False

    for i in range(n - 1, 0, -1):
        # cube on cylinder
        if shapes[i][1] < shapes[i - 1][1]:
            if shapes[i][2] < shapes[i - 1][2] * sqrt(2):
                is_impossible = True
                break

    if is_impossible:
        print("impossible")
        return

    for shape in shapes:
        print(f"{shape[0]} {shape[3]}")


def run():
    solve()


if __name__ == "__main__":
    if os.environ.get("DEBUG_CODEFORCES"):
        stdin = open("../input.txt", "r")
        start_time = time.time()
        run()
        print("\n--- %s seconds ---\n" % (time.time() - start_time))
    else:
        run()
