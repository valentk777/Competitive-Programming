# -----------------------------------------------------------
# URL    : https://open.kattis.com/problems/phonelist
# Title  : Phone List
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


# -------------------------------------------------------Solution-------------------------------------------------------


def create_prefixes(phone_list):
    prefixes = _dp([])

    for phone in phone_list:
        for i in range(1, len(phone)):
            prefix = phone[0:i]
            prefixes[prefix].append(phone)

    return prefixes


def create_prefixes_bool(phone_list):
    prefixes = _dp(False)

    for phone in phone_list:
        for i in range(1, len(phone)):
            prefix = phone[0:i]
            prefixes[prefix] = True

    return prefixes


def solve():
    n = iinp()

    numbers = list_from_inp(n)
    prefixes = create_prefixes_bool(numbers)
    # prefixes = create_prefixes(numbers)

    for number in numbers:
        if prefixes.get(number):
            return "NO"
    return "YES"


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
