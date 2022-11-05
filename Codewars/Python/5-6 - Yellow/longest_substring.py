# -----------------------------------------------------------
# URL    : https://www.codewars.com/kata/5bcd90808f9726d0f6000091
# Notes  : tag-codewars, tag-kyu-6
# -----------------------------------------------------------
from collections import defaultdict


def longest_substring(s: str) -> int:
    n = len(s)

    if n == 0:
        return 0

    left = 0
    right = 1

    _letter = defaultdict(int)
    _letter[s[left]] += 1
    _max = 1
    _current = 1

    while left < n and right < n:
        _current = right - left + 1

        if _letter[s[right]] == 0:
            _letter[s[right]] += 1
            _max = max(_max, _current)
            right += 1
        else:
            _letter[s[left]] -= 1
            left += 1

    return _max
