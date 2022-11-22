# -----------------------------------------------------------
# URL    : https://codeforces.com/contest/1138/problem/D
# Title  : Camp Schedule
# Notes  : tag-codeforces, tag-problem-D, tag-div-2
# -----------------------------------------------------------

# ---------------------------------------------------Shared part--------------------------------------------------------
import os
import time
from collections import defaultdict, Counter
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


def get_length_of_longest_prefix_suffix(s):
    n = len(s)
    lps = [0] * n  # lps[0] is always 0
    length_of_prev_longest_prefix = 0

    i = 1

    while i < n:
        if s[i] == s[length_of_prev_longest_prefix]:
            length_of_prev_longest_prefix = length_of_prev_longest_prefix + 1
            lps[i] = length_of_prev_longest_prefix
            i = i + 1

        else:
            # (pat[i] != pat[len])
            # This is tricky. Consider the example. AAACAAAA and i = 7. The idea is similar to search step.
            if length_of_prev_longest_prefix != 0:
                length_of_prev_longest_prefix = lps[length_of_prev_longest_prefix - 1]

                # Also, note that we do not increment i here

            else:

                # if (len == 0)
                lps[i] = 0
                i = i + 1

    res = lps[n - 1]

    # Since we are looking for
    # non overlapping parts.
    if res > n / 2:
        return n // 2
    else:
        return res


def solve():
    s = inp()
    t = inp()

    count_s = Counter(s)
    count_t = Counter(t)

    if count_s["0"] < count_t["0"] or count_s["1"] < count_t["1"]:
        return s

    # we need to create this string because normally only half of string should be added
    # when calculating prefix and suffix. We want to find at best n-1 long string (not n // 2).
    # to cover a case where 1111 -> 111 (not 11). so we need only 1 "1" at the end
    n_prefix = get_length_of_longest_prefix_suffix(t + "#" + t[1:])
    ans = ""

    # create first pattern
    if count_s["0"] - count_t["0"] >= 0 and count_s["1"] - count_t["1"] >= 0:
        count_s["0"] -= count_t["0"]
        count_s["1"] -= count_t["1"]
        ans += t

    # we know that t could be generated from previous t.
    # so we will modify t by removing prefix also as suffix and continue
    if n_prefix != 0:
        t = t[n_prefix:]
        count_t = Counter(t)

    while count_s["0"] - count_t["0"] >= 0 and count_s["1"] - count_t["1"] >= 0:
        _min = INF

        if count_t["0"] > 0:
            _min = min(count_s["0"] // count_t["0"], _min)
        if count_t["1"] > 0:
            _min = min(count_s["1"] // count_t["1"], _min)

        ans += t * _min
        count_s["0"] -= _min * count_t["0"]
        count_s["1"] -= _min * count_t["1"]
        break

    ans += count_s["0"] * "0" + count_s["1"] * "1"

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
