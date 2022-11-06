# -----------------------------------------------------------
# URL    : https://www.codewars.com/kata/55bc0c54147a98798f00003e
# Notes  : tag-codewars, tag-kyu-6
# -----------------------------------------------------------
from collections import defaultdict


def substring(s):
    n = len(s)

    if n == 0:
        return ""

    left = 0
    right = 1

    _max = 1
    longest = [left, right]
    _counts = defaultdict(int)
    _counts[s[0]] += 1
    char_1 = s[0]
    char_2 = None

    while left < n and right < n:
        _current = right - left + 1

        if s[right] == char_1 or s[right] == char_2:
            if _current > _max:
                _max = _current
                longest = [left, right]

            _counts[s[right]] += 1
            right += 1
            continue

        if char_2 is None:
            char_2 = s[right]
            if _current > _max:
                _max = _current
                longest = [left, right]

            _counts[s[right]] += 1
            right += 1
            continue

        while _counts[char_1] != 0 and _counts[char_2] != 0:
            _counts[s[left]] -= 1
            left += 1

        if _counts[char_1] == 0:
            char_1 = s[right]
        else:
            char_2 = s[right]

    return s[longest[0]: longest[1] + 1]
