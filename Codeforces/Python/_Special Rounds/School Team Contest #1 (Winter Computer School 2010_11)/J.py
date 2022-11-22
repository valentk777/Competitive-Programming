# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/39/problem/J
# Title  : Spelling Check
# Tags   : tag-codeforces, tag-problem-J, tag-difficulty-1500
# Notes  : hashing, implementation, strings
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
flush = lambda: stdout.flush()
print_flush = lambda _text: (print(_text), flush())


def print_dp(_dict):
    for item in _dict.items():
        print(f"{item[0]} = {item[1]}")


MOD = 10 ** 9 + 7
INF = maxsize
A = 911382323
M = 9999999999879998


# -------------------------------------------------------Solution-------------------------------------------------------


def prefix_length(s1, s2):
    i = 0
    while i < len(s1) and i < len(s2) and s1[i] == s2[i]:
        i += 1
    return i


def suffix_length(s1, s2):
    i = 0
    while i < len(s1) and i < len(s2) and s1[- 1 - i] == s2[- 1 - i]:
        i += 1
    return i


def solve_prefix_suffix():
    a = inp()
    b = inp()

    n_a = len(a)

    # count length of equals at the beginning
    prefix = prefix_length(a, b)

    # count length of equals at the end
    suffix = suffix_length(a, b)

    if prefix + 1 < n_a - suffix:
        print(0)
        return

    ans = list(range(max(n_a - suffix, 1), min(prefix + 1, n_a) + 1))
    print(len(ans))
    print(*ans)


def z_array(_string):
    n = len(_string)
    z = [0 for _ in range(n)]

    # [L,R] make a window which matches with prefix of s
    left, right, k = 0, 0, 0

    for i in range(1, n):

        # if i>R nothing matches, so we will calculate. Z[i] using naive way.
        if i > right:
            left, right = i, i

            # R-L = 0 in starting, so it will start checking from 0'th index. For example,
            # for "ababab" and i = 1, the value of R remains 0 and Z[i] becomes 0. For string
            # "aaaaaa" and i = 1, Z[i] and R become 5
            while right < n and _string[right - left] == _string[right]:
                right += 1

            z[i] = right - left
            right -= 1
        else:

            # k = i-L so k corresponds to number which matches in [L,R] interval.
            k = i - left

            # if Z[k] is less than remaining interval then Z[i] will be equal to Z[k].
            # For example, str = "ababab", i = 3, R = 5 and L = 2
            if z[k] < right - i + 1:
                z[i] = z[k]

            # For example str = "aaaaaa" and i = 2, R is 5, L is 0
            else:

                # else start from R and check manually
                left = i

                while right < n and _string[right - left] == _string[right]:
                    right += 1

                z[i] = right - left
                right -= 1

    return z


def solve_z_array():
    a = inp()
    b = inp()

    n_a = len(a)
    n_b = len(b)

    z = z_array(b + "#" + a)
    z_rev = z_array(b[::-1] + "#" + a[::-1])

    print(z)
    print(z_rev)

    positions = []

    for i in range(n_a):
        left = min(i, z[n_b + 1])
        right = min(n_b - i, z_rev[n_b + 1])

        if left + right == n_b:
            positions.append(str(i + 1))

    n_positions = len(positions)

    if n_positions > 0:
        print(n_positions)
        print(*positions)
    else:
        print(0)


def run():
    # solve_prefix_suffix()
    solve_z_array()


if __name__ == "__main__":
    if os.environ.get("DEBUG_CODEFORCES"):
        stdin = open("../../input.txt", "r")
        start_time = time.time()
        run()
        print("\n--- %s seconds ---\n" % (time.time() - start_time))
    else:
        run()
