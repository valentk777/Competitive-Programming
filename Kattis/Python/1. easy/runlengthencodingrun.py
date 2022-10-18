# -----------------------------------------------------------
# URL    : https://open.kattis.com/problems/runlengthencodingrun
# Title  : Run-Length Encoding, Run!
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
    s = strl()

    command = s[0]
    message = s[1]
    ats = []

    if command == "E":
        prev = message[0]
        _count = 0

        for i in range(len(message)):
            if message[i] == prev:
                _count += 1
            else:
                ats.append(prev + str(_count))
                _count = 1
                prev = message[i]

        ats.append(prev + str(_count))
    else:
        _count = 0

        for i in range(1, len(message), 2):
            ats.append(message[i - 1] * int(message[i]))

    return list_to_string(ats)


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
