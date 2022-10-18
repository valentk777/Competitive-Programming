# -----------------------------------------------------------
# URL    : https://open.kattis.com/problems/4thought
# Title  : 4 thought
# Notes  : tag-kattis, tag-2. medium
# -----------------------------------------------------------

# ---------------------------------------------------Shared part--------------------------------------------------------
import os
import time
from collections import defaultdict
from math import floor
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


# -------------------------------------------------------Solution-------------------------------------------------------

def solve():
    n = iinp()
    operators = ['*', '//', '+', '-']

    if abs(n) > 256:
        return "no solution"

    results = _dp(0)

    for i in operators:
        for j in operators:
            for k in operators:
                expression = f"4 {i} 4 {j} 4 {k} 4"
                result = floor(eval(expression))
                expression = expression.replace("//", "/")
                results[result] = f"{expression} = {result}"

    if n in results.keys():
        return results[n]
    else:
        return "no solution"


def run():
    t = iinp()

    for _ in range(t):
        print(solve())


if __name__ == "__main__":
    if os.environ.get("DEBUG_CODEFORCES"):
        stdin = open("../input.txt", "r")
        start_time = time.time()
        run()
        print("\n--- %s seconds ---\n" % (time.time() - start_time))
    else:
        run()
