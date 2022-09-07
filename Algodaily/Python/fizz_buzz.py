# https://algodaily.com/challenge_slides/fizz-buzz


def fizz_buzz(n):
    result = ""

    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result += "fizzbuzz"
        elif i % 3 == 0:
            result += "fizz"
        elif i % 5 == 0:
            result += "buzz"
        else:
            result += str(i)

    return result


import unittest


class Test(unittest.TestCase):
    def test_1(self):
        assert fizz_buzz(0) == ""
        print("PASSED: Expect fizz_buzz(0) to equal ''")

    def test_2(self):
        assert fizz_buzz(1) == "1"
        print("PASSED: Expect fizz_buzz(1) to equal '1'")

    def test_3(self):
        assert fizz_buzz(15) == "12fizz4buzzfizz78fizzbuzz11fizz1314fizzbuzz"
        print("PASSED: Expect fizz_buzz(15) to equal '12fizz4buzzfizz78fizzbuzz11fizz1314fizzbuzz'")


if __name__ == "__main__":
    unittest.main(verbosity=2)
    print("Nice job, 3/3 tests passed!")
