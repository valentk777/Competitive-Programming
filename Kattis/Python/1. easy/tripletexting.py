# -----------------------------------------------------------
# URL    : https://open.kattis.com/problems/tripletexting
# Title  : Triple Texting
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
    s = inp()
    n = len(s)
    len_word = n // 3

    correct = ["" for _ in range(len_word)]
    for i in range(len_word):
        if s[i] == s[i + len_word] or s[i] == s[i + 2 * len_word]:
            correct[i] = s[i]
        elif s[i + len_word] == s[i + 2 * len_word]:
            correct[i] = s[i + len_word]
        else:
            print("klaida")

    return list_to_string(correct)


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
