# ---------------------------------------------------------------------------------------
# URL    : https://leetcode.com/problems/top-k-frequent-elements/
# Title  : 347. Top K Frequent Elements
# Tags   : tag-leetcode, tag-difficulty-medium
# ---------------------------------------------------------------------------------------

# region --------------------------------------------Shared part--------------------------------------------------------

import math
import sys
import time
from collections import defaultdict, Counter

from typing import List

inp = lambda: sys.stdin.readline().strip().rstrip("\r\n")
iinp = lambda: int(inp())
intl = lambda: list(map(int, inp().split()))
strl = lambda: list(inp().split())
list_to_string = lambda _a: "".join(map(str, _a))
list_to_string_list = lambda _a: " ".join(map(str, _a))
_dp = lambda default_value: defaultdict(lambda: default_value)
flush = lambda: sys.stdout.flush()
print_flush = lambda _text: (print(_text), flush())
fact = lambda number: math.factorial(number)
_cnt = lambda _a: Counter(_a)


def lcm(a, b):
    return a * b // math.gcd(a, b)


def print_dp(_dict):
    for item in _dict.items():
        print(f"{item[0]} = {item[1]}")


def memodict(f):
    """memoization decorator for a function taking a single argument"""

    class memodict(dict):
        def __missing__(self, key):
            ret = self[key] = f(key)
            return ret

    return memodict().__getitem__


MOD = 10 ** 9 + 7
INF = sys.maxsize
A = 911382323
M = 9999999999879998
yes = "YES"
no = "NO"


# endregion

# -------------------------------------------------------Solution-------------------------------------------------------

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        _count = Counter(nums)
        _count = dict(sorted(_count.items(), key=lambda x: x[1], reverse=True))
        return list(_count.keys())[:k]


if __name__ == "__main__":
    solution = Solution()
    start_time = time.time()
    problem_answer = solution.topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2)

    print(problem_answer)
    print("\n--- %s seconds ---\n" % (time.time() - start_time))
