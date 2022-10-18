# -----------------------------------------------------------
# URL    : https://open.kattis.com/problems/grille
# Title  : What's on the Grille?
# Notes  : tag-kattis, tag-medium
# -----------------------------------------------------------

# ---------------------------------------------------Shared part--------------------------------------------------------
import os
import time
from collections import defaultdict
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

def rotate_90_degree_clckwise(matrix):
    new_matrix = []
    for i in range(len(matrix[0])):
        li = list(map(lambda x: x[i], matrix))
        li.reverse()
        new_matrix.append(li)

    return new_matrix


def solve():
    n = iinp()
    grille = [list(inp()) for _ in range(n)]
    translated = [["*" for _ in range(n)] for _ in range(n)]
    message = inp()
    message_idx = 0

    if n == 1:
        return message

    for rotations in range(4):
        for row in range(n):
            for column in range(n):
                if grille[row][column] == ".":
                    if message_idx == len(message):
                        return "invalid grille"

                    translated[row][column] = message[message_idx]
                    message_idx += 1

        grille = rotate_90_degree_clckwise(grille)

    ans = ""

    for row in range(n):
        for column in range(n):
            if translated[row][column] == "*":
                return "invalid grille"

            ans += translated[row][column]

    return ans


def run():
    print(solve())


if __name__ == "__main__":
    if os.environ.get("DEBUG_CODEFORCES"):
        stdin = open("../input.txt", "r")
        start_time = time.time()
        run()
        print("\n--- %s seconds ---\n" % (time.time() - start_time))
    else:
        run()
