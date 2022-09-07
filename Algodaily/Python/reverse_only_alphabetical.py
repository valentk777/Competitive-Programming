# -----------------------------------------------------------
# URL    : https://algodaily.com/challenge_slides/reverse-only-alphabetical
# Notes  : tag-algodaily
# -----------------------------------------------------------


def reverse_only_alpha(s):
    arr = list(s)
    start, end = 0, len(arr) - 1

    while start < end:
        if arr[start].isalpha() and arr[end].isalpha():
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

        if not arr[start].isalpha():
            start += 1

        if not arr[end].isalpha():
            end -= 1

    return "".join(arr)


# ##################################################################################################################
# Algodaily solutions
# ##################################################################################################################
# Method 1
import re


def reverse_only_alpha(s):
    alpha_chars = []
    s = list(s)
    new_s = ""

    r = re.compile("[a-zA-Z]")

    for char in s:
        if r.match(char):
            alpha_chars.append(char)

    reversed_alpha = reverse_array(alpha_chars)

    idx_ra = 0
    for i in range(len(s)):
        if r.match(s[i]):
            new_s += reversed_alpha[idx_ra]
            idx_ra += 1
        else:
            new_s += s[i]

    return new_s


def reverse_array(arr):
    return arr[::-1]


# Method 2
def reverse_only_alpha_with_maps(s):
    alpha_only = list(filter(lambda x: x.isalpha(), list(s)))

    print(alpha_only)
    result = []

    for letter in list(s):
        if not letter.isalpha():
            result.append(letter)
            continue

        result.append(alpha_only[len(alpha_only) - 1])
        alpha_only = alpha_only[:-1]

    return "".join(result)


# ##################################################################################################################

def reverse_array(arr):
    return arr[::-1]


import unittest


class Test(unittest.TestCase):
    def test_1(self):
        assert callable(reverse_only_alpha_with_maps) == True
        print("PASSED: Expect reverse_only_alpha is a function")

    def test_2(self):
        assert reverse_only_alpha_with_maps("sea!$hells3") == "sll!$ehaes3"
        print("PASSED: Expect reverse_only_alpha('sea!$hells3') to return 'sll!$ehaes3'")

    def test_3(self):
        assert reverse_only_alpha_with_maps("1kas90jda3") == "1adj90sak3"
        print("PASSED: Expect reverse_only_alpha('1kas90jda3') to return '1adj90sak3'")


if __name__ == "__main__":
    unittest.main(verbosity=2)
    print("Nice job, 3/3 tests passed!")
