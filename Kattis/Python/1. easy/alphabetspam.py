# -----------------------------------------------------------
# URL    : https://open.kattis.com/problems/alphabetspam
# Title  : Alphabet Spam
# Notes  : tag-kattis, tag-easy
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


# -------------------------------------------------------Solution-------------------------------------------------------

def solve():
    s = list(inp())
    n = len(s)

    count_whitespace = 0
    count_lowercase = 0
    count_uppercase = 0
    count_symbols = 0

    for i in range(n):
        if s[i] == "_":
            count_whitespace += 1
        elif ord("a") <= ord(s[i]) <= ord("z"):
            count_lowercase += 1
        elif ord("A") <= ord(s[i]) <= ord("Z"):
            count_uppercase += 1
        else:
            count_symbols += 1

    print(count_whitespace / n)
    print(count_lowercase / n)
    print(count_uppercase / n)
    print(count_symbols / n)


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
