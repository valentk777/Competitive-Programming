# -----------------------------------------------------------
# URL    : https://www.codewars.com/kata/5a0178f66f793bc5b0001728
# Notes  : tag-codewars, tag-kyu-6
# -----------------------------------------------------------

from collections import Counter


def longest_palindrome(s):
    _count = Counter(filter(str.isalnum, s.lower()))

    ans = 0
    add_one = False

    for key, value in _count.items():
        if value > 1:
            ans += (value // 2) * 2

            if value & 1 == 1:
                add_one = True

        else:
            add_one = True

    if add_one:
        return ans + 1
    else:
        return ans
