# -----------------------------------------------------------
# URL    : https://open.kattis.com/problems/division
# Title  : Division
# Notes  : tag-kattis, tag-not-pass
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
def get_number(t, a, b):
    if a == b:
        return 1

    if a > b:
        tb = t ** b
        ta = tb * (t ** (a - b))
    else:
        ta = t ** a
        tb = ta * (t ** (b - a))

    diffta = ta - 1
    diffba = tb - 1

    if diffba != 0:
        return -1

    result = diffta // diffba

    if len(str(result)) > 100:
        return -1

    return result


def solve():
    t, a, b = intl()

    ats = get_number(t, a, b)

    if ats != -1:
        return f"({t}^{a}-1)/({t}^{b}-1) {ats}"
    else:
        return f"({t}^{a}-1)/({t}^{b}-1) is not an integer with less than 100 digits."


def run():
    try:
        while True:
            print(solve())
    except:
        pass

if __name__ == "__main__":
    if os.environ.get("DEBUG_CODEFORCES"):
        stdin = open("input.txt", "r")
        start_time = time.time()
        run()
        print("\n--- %s seconds ---\n" % (time.time() - start_time))
    else:
        run()
