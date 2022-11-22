# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/gym/101021/problem/1
# Title  : Guess the Number
# Tags   : tag-codeforces
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
print_dp = lambda _dict: list(map(lambda item: print(f"{item[0]} = {item[1]}"), _dict.items()))
flush = lambda: stdout.flush()
print_flush = lambda _text: (print(_text), flush())

MOD = 10 ** 9 + 7
INF = maxsize


# -------------------------------------------------------Solution-------------------------------------------------------

def solve():
    left = 0
    right = 10 ** 6

    while left < right:
        mid = (left + right + 1) // 2

        print_flush(mid)

        ans = inp()

        if ans == "<":
            right = mid - 1
        else:
            left = mid

    return f"! {left}"


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
