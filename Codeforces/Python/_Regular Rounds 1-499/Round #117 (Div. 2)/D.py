# -----------------------------------------------------------
# URL    : https://codeforces.com/contest/182/problem/D
# Title  : Common Divisors
# Notes  : tag-codeforces, tag-problem-D, tag-div-2
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

# Time limit exceeded
def solve_slow():
    first_str = inp()
    n_first_str = len(first_str)

    second_str = inp()
    n_second_str = len(second_str)

    if n_first_str > n_second_str:
        first_str, second_str = second_str, first_str
        n_first_str, n_second_str = n_second_str, n_first_str

    _map = _dp(0)
    _map[first_str] = 1

    for step in range(1, n_first_str // 2 + 1):
        temp = first_str[:step]
        stop = False

        for j in range(step, n_first_str, step):
            if j + step > n_first_str:
                stop = True
                break

            if first_str[j:j + step] != temp:
                stop = True
                break

        if not stop:
            _map[temp] += 1

    _count = 0

    for key in _map.keys():
        n_key = len(key)

        stop = False
        for i in range(0, n_second_str, n_key):
            if second_str[i:i + n_key] != key:
                stop = True
                break

        if not stop:
            _count += 1

    return _count


def solve():
    longer_str = inp()
    shorted_str = inp()

    n_longer_str = len(longer_str)
    n_shorted_str = len(shorted_str)

    # take longer
    if n_longer_str < n_shorted_str:
        longer_str, shorted_str = shorted_str, longer_str
        n_longer_str, n_shorted_str = n_shorted_str, n_longer_str

    candidates = []

    for i in range(1, n_longer_str + 1):
        if n_longer_str % i == 0 and n_shorted_str % i == 0:
            candidates.append(i)

    ans = 0

    for idx in candidates:
        substring = longer_str[0:idx]

        if longer_str.count(substring) == n_longer_str / idx and shorted_str.count(substring) == n_shorted_str / idx:
            ans += 1

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
