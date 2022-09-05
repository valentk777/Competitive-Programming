# https://algodaily.com/challenge_slides/array-intersection/info-screen-AK8SJ+tNOe8


def intersection(nums1, nums2):
    nums1 = set(nums1)
    print(nums1)
    nums2 = set(nums2)
    print(nums2)

    def get_result(small_arr, big_arr):
        results = []

        for element in small_arr:
            if element in big_arr:
                results.append(element)

        return results

    if len(nums1) > len(nums2):
        return get_result(nums2, nums1)
    else:
        return get_result(nums1, nums2)


# ##################################################################################################################
# Algodaily solutions
# ##################################################################################################################

def intersection(nums1, nums2):
    nums1 = set(nums1)
    nums2 = set(nums2)

    return list(nums1.intersection(nums2))


# ##################################################################################################################

import unittest


class Test(unittest.TestCase):
    def test_1(self):
        assert intersection([6, 0, 12, 10, 16], [3, 15, 18, 20, 15]) == []
        print("PASSED: `intersection([6,0,12,10,16],[3,15,18,20,15])` should return `[]`")

    def test_2(self):
        assert intersection([1, 5, 2, 12, 6], [13, 10, 9, 5, 8]) == [5]
        print("PASSED: `intersection([1,5,2,12,6],[13,10,9,5,8])` should return `[5]`")

    def test_3(self):
        assert intersection([3], [15]) == []
        print("PASSED: `intersection([3],[15])` should return `[]`")

    def test_4(self):
        assert intersection([2, 16, 8, 9], [14, 15, 2, 20]) == [2]
        print("PASSED: `intersection([2,16,8,9],[14,15,2,20])` should return `[2]`")


if __name__ == "__main__":
    unittest.main(verbosity=2)
    print("Nice job, 4/4 tests passed!")
