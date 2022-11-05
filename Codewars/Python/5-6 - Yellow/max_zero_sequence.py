# -----------------------------------------------------------
# URL    : https://www.codewars.com/kata/52b4d1be990d6a2dac0002ab
# Notes  : tag-codewars, tag-kyu-5
# -----------------------------------------------------------


def max_zero_sequence(arr):
    n = len(arr)
    _max = 0
    ans = []

    for j in range(1, n):
        for i in range(j):
            if sum(arr[i:j]) == 0:
                if len(arr[i:j]) > _max:
                    ans = arr[i:j]
                    _max = len(arr[i:j])

    return ans
