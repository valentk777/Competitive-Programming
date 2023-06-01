# ---------------------------------------------------------------------------------------
# URL    : https://leetcode.com/problems/two-sum/
# Title  : 1. Two Sum
# Tags   : tag-leetcode, tag-difficulty-easy
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
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # store all numbers and their positions
        _count = defaultdict(lambda: [])

        for idx, num in enumerate(nums):
            _count[num].append(idx)

            candidate = target - num
            is_same_number = candidate == num

            if is_same_number:
                if len(_count[candidate]) > 1:
                    return _count[candidate]
            else:
                if len(_count[candidate]) > 0:
                    return [idx, _count[candidate][0]]

    def twoSum_v2(self, nums: List[int], target: int) -> List[int]:
        # it is enaught to store only last index
        _count = {}

        for idx, num in enumerate(nums):
            candidate = target - num

            if candidate in _count:
                return [_count[candidate], idx]

            _count[num] = idx


if __name__ == "__main__":
    solution = Solution()
    start_time = time.time()
    problem_answer = solution.twoSum(nums=[-3, 4, 3, 90], target=0)

    print(problem_answer)
    print("\n--- %s seconds ---\n" % (time.time() - start_time))
