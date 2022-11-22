# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/1045/problem/I
# Title  : Palindrome Pairs
# Tags   : tag-codeforces, tag-problem-I, tag-div-1
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
list_to_string = lambda _a: "".join(map(str, _a))
list_to_string_list = lambda _a: " ".join(map(str, _a))
_dp = lambda default_value: defaultdict(lambda: default_value)
print_dp = lambda _dict: list(map(lambda item: print(f"{item[0]} = {item[1]}"), _dict.items()))

MOD = 10 ** 9 + 7
INF = maxsize


# -------------------------------------------------------Solution-------------------------------------------------------


def binary_hash(word):
    shift = ord("a")

    hashed = [0 for _ in range(ord("a"), ord("z") + 1)]

    for char in word:
        hashed[ord(char) - shift] = (hashed[ord(char) - shift] + 1) & 1

    return int(list_to_string(hashed), 2)


def binary_hash_faster(word):
    shift = ord("a")
    hashed = 0

    for char in word:
        index = ord(char) - shift
        # flip the binary at the index, XOR if we had 1 before
        hashed ^= (1 << index)

    return hashed


def is_palindrome(int_word):
    s = str(bin(int_word))
    _count = 0

    for c in s:
        if c == "1" and _count < 1:
            _count += 1
        else:
            return False
    return True


def solve_slow():
    n = iinp()

    # store not value, but values and count.
    # in case we will have multiple numbers with same value, we can join them and then get palindrome.
    count_list = _dp(0)

    for i in range(n):
        s = inp()
        count_list[binary_hash_faster(s)] += 1

    ans = 0

    words_in_dict = list(count_list.keys())
    n_words_in_dict = len(words_in_dict)

    # wto for's too slow.
    for i in range(n_words_in_dict):
        ans += count_list[words_in_dict[i]] * (count_list[words_in_dict[i]] - 1) // 2

        for j in range(i + 1, n_words_in_dict):
            if is_palindrome(words_in_dict[i] ^ words_in_dict[j]):
                ans += count_list[words_in_dict[i]] * count_list[words_in_dict[j]]

    return ans


def solve():
    n = iinp()

    # store not value, but values and count.
    # in case we will have multiple numbers with same value, we can join them and then get palindrome.
    count_list = _dp(0)

    for i in range(n):
        s = inp()
        count_list[binary_hash_faster(s)] += 1

    ans = 0

    for key in count_list:
        # all possible combinations with same string
        ans += count_list[key] * (count_list[key] - 1) // 2

        # iterate current bit string and change only one string.
        # If we have this new string in dictionary, we know that join of them will give us palindrome
        # because it would be only one bit 1 and all zeros
        for bit_to_flip in range(26):
            key_flip = key ^ (1 << bit_to_flip)

            # second end needed to do not count (i, j) and (j, i) twice
            if key_flip in count_list and key_flip < key:
                ans += count_list[key] * count_list[key_flip]

    return ans


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
