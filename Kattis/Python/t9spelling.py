# -----------------------------------------------------------
# URL    : https://open.kattis.com/problems/t9spelling
# Title  : T9 Spelling
# Notes  : tag-kattis
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

letters = {
    "a": "2",
    "b": "2" * 2,
    "c": "2" * 3,

    "d": "3",
    "e": "3" * 2,
    "f": "3" * 3,

    "g": "4",
    "h": "4" * 2,
    "i": "4" * 3,

    "j": "5",
    "k": "5" * 2,
    "l": "5" * 3,

    "m": "6",
    "n": "6" * 2,
    "o": "6" * 3,

    "p": "7",
    "q": "7" * 2,
    "r": "7" * 3,
    "s": "7" * 4,

    "t": "8",
    "u": "8" * 2,
    "v": "8" * 3,

    "w": "9",
    "x": "9" * 2,
    "y": "9" * 3,
    "z": "9" * 4,

    " ": "0" * 1
}


def solve():
    t = iinp()

    for case in range(1, t + 1):
        result = [f"Case #{case}: "]
        s = inp()

        prev = "-1"

        for c in s:
            current = letters[c]

            if prev[0] == current[0]:
                prev = current
                current = " " + current
            else:
                prev = current

            result.append(current)

        print(list_to_string(result))


def run():
    solve()


if __name__ == "__main__":
    if os.environ.get("DEBUG_CODEFORCES"):
        stdin = open("input.txt", "r")
        start_time = time.time()
        run()
        print("\n--- %s seconds ---\n" % (time.time() - start_time))
    else:
        run()
