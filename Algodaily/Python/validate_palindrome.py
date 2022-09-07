# https://algodaily.com/challenge_slides/validate-palindrome

def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]


# ##################################################################################################################
# Algodaily solutions
# ##################################################################################################################
import re

ALPHA_NUMERIC = re.compile("[^a-zA-Z0-9]")


def is_palindrome(s):
    if not s or s == "":
        return True
    else:
        left = 0
        right = len(s) - 1

        while left < right:
            left_char = s[left].lower()
            right_char = s[right].lower()

            if is_alpha_num(left_char) and is_alpha_num(right_char):
                if left_char == right_char:
                    left += 1
                    right -= 1
                else:
                    return False
            else:
                if not is_alpha_num(left_char):
                    left += 1
                if not is_alpha_num(right_char):
                    right -= 1

        return True


def is_alpha_num(c):
    return False if ALPHA_NUMERIC.match(c) else True


# ##################################################################################################################


import unittest


class Test(unittest.TestCase):
    def test_1(self):
        assert is_palindrome("A Santa Lived As a Devil At NASA") == True
        print(
            "PASSED: assert is_palindrome('A Santa Lived As a Devil At NASA') == True"
        )

    def test_2(self):
        assert is_palindrome("gold") == False
        print("PASSED: assert is_palindrome('gold') == False")

    def test_3(self):
        assert is_palindrome("a") == True
        print("PASSED: assert is_palindrome('a') == True")

    def test_4(self):
        assert is_palindrome("racecar") == True
        print("PASSED: assert is_palindrome('racecar') == True")


if __name__ == "__main__":
    unittest.main(verbosity=2)
    print("Nice job, 4/4 tests passed!")
