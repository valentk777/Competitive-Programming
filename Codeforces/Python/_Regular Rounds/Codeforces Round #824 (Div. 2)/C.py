# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/1735/problem/C
# Title  : Phase Shift
# Tags   : tag-codeforces, tag-problem-C, tag-div-2, tag-difficulty-1400, tag-not-pass
# Notes  : dfs and similar, dsu, graphs, greedy, implementation, strings
# ---------------------------------------------------------------------------------------

# ---------------------------------------------------Shared part--------------------------------------------------------
import os
import string
import time
from collections import defaultdict
from sys import stdin, maxsize

inp = lambda: stdin.readline().strip()
iinp = lambda: int(inp())
intl = lambda: list(map(int, inp().split()))
strl = lambda: list(inp().split())
list_to_string = lambda _a: "".join(map(str, _a))
list_to_string_List = lambda _a: " ".join(map(str, _a))
_dp = lambda default_value: defaultdict(lambda: default_value)

MOD = 10 ** 9 + 7
INF = maxsize


# -------------------------------------------------------Solution-------------------------------------------------------

def solve():
    n = iinp()
    s = inp()
    s = list(map(ord, list(s)))

    result = []
    letters = {ord(i): -1 for i in list(string.ascii_lowercase)}

    for i in range(n):
        if letters[s[i]] != -1:
            result.append(chr(letters[s[i]]))
            continue

        already_taken_letters = letters.values()

        for c in letters.keys():
            if letters not in already_taken_letters:
                print(c)

    # # dictionary = _dp(-1)
    #
    # # len_dictionary = 1
    # candidate_letter = letters[0]
    #
    #
    #     if
    # dictionary[s[i]] != -1: \
    #     result.append(chr(dictionary[s[i]]))
    # continue
    #
    # if s[i] == candidate_letter:
    #     dictionary[s[i]] = letters[1]
    #     letters.remove(letters[1])
    #     candidate_letter = letters[1]
    # else:
    #     dictionary[s[i]] = candidate_letter
    #     letters.remove(candidate_letter)
    #     candidate_letter = letters[0]

    # if len(letters) > 1:
    #     candidate_letter = letters[1]
    # elif len(letters) == 1:
    #     candidate_letter = letters[0]

    # if len_dictionary == 26:
    #     candidate_letter = ord("a")
    #
    # if candidate_letter > ord("z"):
    #     candidate_letter = ord("a")

    # max_letter = max(dictionary.values())
    #
    # if max_letter == -1:
    #     if ord(s[i]) == candidate_letter:
    #         dictionary[s[i]] = candidate_letter + 1
    #     else:
    #         dictionary[s[i]] = candidate_letter
    #         candidate_letter += 1
    # else:
    #     if ord(s[i]) == candidate_letter:
    #         dictionary[s[i]] = max_letter + 1
    #     else:
    #         dictionary[s[i]] = candidate_letter
    #         candidate_letter = max_letter + 1
    # result.append(chr(dictionary[s[i]]))

    return list_to_string(result)


def run():
    t = iinp()

    for _ in range(t):
        print(solve())


if __name__ == "__main__":
    if os.environ.get("DEBUG_CODEFORCES"):
        stdin = open("../../input.txt", "r")
        start_time = time.time()
        run()
        print("\n--- %s seconds ---\n" % (time.time() - start_time))
    else:
        run()
