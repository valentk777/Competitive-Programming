# -----------------------------------------------------------
# URL    : https://algodaily.com/challenge_slides/max-rectangle-in-a-histogram
# Notes  : tag-algodaily
# -----------------------------------------------------------


def max_rect_in_hist(hist_arr):
    n = len(hist_arr)
    candidates = hist_arr

    for i in range(n):
        for j in range(i + 1, n + 1):
            candidates.append((j - i) * min(hist_arr[i:j]))

    return 0 if len(candidates) == 0 else max(candidates)


import unittest


class Test(unittest.TestCase):
    def test_1(self):
        assert max_rect_in_hist([3, 1, 4, 2, 2, 1]) == 6
        print("PASSED: assert maxRectInHist([3, 1, 4, 2, 2, 1]) == 6")

    def test_2(self):
        assert max_rect_in_hist([]) == 0
        print("PASSED: assert maxRectInHist([]) == 0")

    def test_3(self):
        assert max_rect_in_hist([1, 2, 3, 4]) == 6
        print("PASSED: assert maxRectInHist([1, 2, 3, 4]) == 6")


if __name__ == "__main__":
    unittest.main(verbosity=2)
    print("Nice job, 3/3 tests passed!")
