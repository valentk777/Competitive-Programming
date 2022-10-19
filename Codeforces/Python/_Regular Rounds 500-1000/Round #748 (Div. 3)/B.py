# -----------------------------------------------------------
# URL    : https://codeforces.com/contest/1593/problem/B
# Title  : Make it Divisible by 25
# Notes  : tag-codeforces, tag-problem-B, tag-div-3, tag-not-pass
# -----------------------------------------------------------

# ---------------------------------------------------Shared part--------------------------------------------------------
import os
import time
from collections import defaultdict
from sys import stdin, maxsize

inp = lambda: stdin.readline().strip()
iinp = lambda: int(inp())
intl = lambda: list(map(int, inp().split()))
strl = lambda: list(inp().split())
list_to_string = lambda _a: "".join(map(str, _a))
list_to_string_list = lambda _a: " ".join(map(str, _a))
_dp = lambda default_value: defaultdict(lambda: default_value)
print_dp = lambda _dict: list(map(lambda item: print(f"{item[0]} = {item[1]}"), _dict.items()))

MOD = 10 ** 9 + 7
INF = maxsize


# -------------------------------------------------------Solution-------------------------------------------------------

# wrong answer
def solve():
    number = inp()
    number = number[::-1]

    ans = []
    removed = 0

    while len(number) > 0:
        if number[0] not in ["0", "5"]:
            removed += 1
            number = number[1:]
            continue

        if number[:2] in ["00", "52", "05", "57"]:
            return removed

        candidate = removed

        if number[0] == "0":
            for i in range(1, len(number)):
                if number[i] != "0" and number[i] != "5":
                    candidate += 1
                else:
                    ans.append(candidate)
                    break

            number = number[1:]
            removed += 1

        if number[0] == "5":
            for i in range(1, len(number)):
                if number[i] != "2" and number[i] != "7":
                    candidate += 1
                else:
                    ans.append(candidate)
                    break

            number = number[1:]
            removed += 1

    return min(ans)


# Greedy
def solve_2():
    number = inp()
    a = list(number)
    b = list(number)
    ans_1 = 0
    ans_2 = 0

    # try 00 or 50
    while len(a) > 0 and a[-1] != "0":
        a.pop(-1)
        ans_1 += 1

    while len(a) > 1 and a[-2] != "0" and a[-2] != "5":
        a.pop(-2)
        ans_1 += 1

    # try 25 or 75
    while len(b) > 0 and b[-1] != "5":
        b.pop(-1)
        ans_2 += 1

    while len(b) > 1 and b[-2] != "2" and b[-2] != "7":
        b.pop(-2)
        ans_2 += 1

    return min(ans_1, ans_2)


def run():
    t = iinp()

    for _ in range(t):
        # print(solve())
        print(solve_2())


if __name__ == "__main__":
    if os.environ.get("DEBUG_CODEFORCES"):
        stdin = open("../../input.txt", "r")
        start_time = time.time()
        run()
        print("\n--- %s seconds ---\n" % (time.time() - start_time))
    else:
        run()
