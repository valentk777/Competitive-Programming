# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/1419/problem/D2
# Title  : D2. Sage's Birthday (hard version)
# Tags   : tag-codeforces, tag-problem-D, tag-div-2, tag-not-pass
# ---------------------------------------------------------------------------------------

# ---------------------------------------------------Shared part--------------------------------------------------------
import os
import time
from collections import defaultdict, Counter
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

def solve():
    n = iinp()
    a = intl()

    _counts = Counter(a)

    # print_dp(_counts)

    keys = sorted(list(_counts.keys()))
    keys_n = len(keys)

    # print(keys)

    ans_count = 0
    ans = [keys[keys_n - 1]]
    _counts[keys[keys_n - 1]] -= 1

    if _counts[keys[keys_n - 1]] == 0:
        keys.remove(keys[keys_n - 1])

    i = keys_n - 2

    while i >= 0:
        _max = max(_counts, key=_counts.get)

        if i > -1:
            if _max < keys[i]:
                ans.append(_max)
                ans.append(keys[i])

                ans_count += 1
                _counts[_max] -= 1

                if _counts[_max] == 0:
                    keys.remove(_max)
                    i -= 1

                _counts[keys[i]] -= 1

                if _counts[keys[i]] == 0:
                    keys.remove(keys[i])
                    i -= 1
            else:
                t = i - 1

                if t > -1:
                    if _max > keys[t]:
                        ans.append(keys[t])
                        ans.append(_max)

                        ans_count += 1
                        _counts[_max] -= 1

                        if _counts[_max] == 0:
                            keys.remove(_max)
                            i -= 1

                        _counts[keys[t]] -= 1

                        if _counts[keys[t]] == 0:
                            keys.remove(keys[t])
                            i -= 1

                else:
                    ans.append(keys[i])
                    keys.remove(keys[i])
                    _counts[keys[i]] -= 1
                # while t > -1 and _max > keys[t]:
                #     t -= 1
                #
                # if t > -1:
                #     ans.append(keys[t])
                #     ans.append(_max)
                #
                #     ans_count += 1
                #     _counts[_max] -= 1
                #
                #     if _counts[_max] == 0:
                #         keys.remove(_max)
                #         i -= 1
                #
                #     _counts[keys[i]] -= 1
                #
                #     if _counts[keys[t]] == 0:
                #         keys.remove(keys[t])
                #         i -= 1
                # else:
                #     print("cia")
                #     break
        #
        # if i > -1:
        #     ans.append(keys[i])

        # i -= 2

    for k, v in _counts.items():
        ans.extend([k] * v)

    print(ans_count)
    return list_to_string_list(ans)


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
