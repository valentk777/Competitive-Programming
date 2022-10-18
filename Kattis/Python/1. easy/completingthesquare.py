# -----------------------------------------------------------
# URL    : https://open.kattis.com/problems/completingthesquare
# Title  : Completing the Square
# Notes  : tag-kattis, tag-easy
# -----------------------------------------------------------

# ---------------------------------------------------Shared part--------------------------------------------------------
import os
import time
from collections import defaultdict
from math import dist
from sys import stdin, maxsize

inp = lambda: stdin.readline().strip("\n")
iinp = lambda: int(inp())
intl = lambda: list(map(int, inp().split()))
strl = lambda: list(inp().split())
list_to_string = lambda _a: "".join(map(str, _a))
list_to_string_list = lambda _a: " ".join(map(str, _a))
_dp = lambda default_value: defaultdict(lambda: default_value)
print_dp = lambda _dict: list(map(lambda item: print(f"{item[0]} = {item[1]}"), _dict.items()))
list_from_inp = lambda n: [inp() for _ in range(n)]

MOD = 10 ** 9 + 7
INF = maxsize
A = 911382323
M = 9999999999879998


# -------------------------------------------------------Solution-------------------------------------------------------

def solve():
    point1 = intl()
    point2 = intl()
    point3 = intl()

    dist_1_2 = dist(point1, point2)
    dist_1_3 = dist(point1, point3)

    if dist_1_2 == dist_1_3:
        point1, point3 = point3, point1
    elif dist_1_3 > dist_1_2:
        point2, point3 = point3, point2

    x = point1[0] + (point2[0] - point3[0])
    y = point1[1] + (point2[1] - point3[1])

    print(x, y)


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
