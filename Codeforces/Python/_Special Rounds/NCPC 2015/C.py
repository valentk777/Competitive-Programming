# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/gym/100781
# Title  : Cryptographer’s Conundrum
# Tags   : tag-codeforces, tag-problem-C
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
list_to_string = lambda _a: " ".join(map(str, _a))
_dp = lambda default_value: defaultdict(lambda: default_value)

MOD = 10 ** 9 + 7
INF = maxsize


# -------------------------------------------------------Solution-------------------------------------------------------

def solve():
    s = inp()
    _count = 0

    for i in range(0, len(s), 3):
        if s[i] != 'P':
            _count += 1

    for i in range(1, len(s), 3):
        if s[i] != 'E':
            _count += 1

    for i in range(2, len(s), 3):
        if s[i] != 'R':
            _count += 1

    return _count


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
