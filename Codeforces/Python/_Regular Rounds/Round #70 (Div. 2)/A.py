# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/78/problem/A
# Title  : A. Haiku
# Tags   : tag-codeforces, tag-problem-A, tag-div-2
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

def solve():
    text = []

    for i in range(100):
        try:
            s = inp()
            text.append(s)
        except:
            break

    text = list(filter(lambda x: x != "", text))

    if len(text) != 3:
        return "NO"

    if text[0].count("a") + text[0].count("e") + text[0].count("i") + text[0].count("o") + text[0].count("u") != 5:
        return "NO"

    if text[1].count("a") + text[1].count("e") + text[1].count("i") + text[1].count("o") + text[1].count("u") != 7:
        return "NO"

    if text[2].count("a") + text[2].count("e") + text[2].count("i") + text[2].count("o") + text[2].count("u") != 5:
        return "NO"

    return "YES"


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
