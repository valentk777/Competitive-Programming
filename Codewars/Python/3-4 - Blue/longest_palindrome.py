# -----------------------------------------------------------
# URL    : https://www.codewars.com/kata/5dcde0b9fcb0d100349cb5c0
# Notes  : tag-codewars, tag-kyu-4
# -----------------------------------------------------------

'''
    Write a function that returns the longest contiguous palindromic substring in s.
    In the event that there are multiple longest palindromic substrings, return the
    first to occur.
'''


def longest_palindrome(s):
    T = '#'.join('^{}$'.format(s))
    n = len(T)
    largest_palindromes = [0] * n
    left = 0
    right = 0

    for i in range(1, n - 1):
        largest_palindromes[i] = (right > i) and min(right - i, largest_palindromes[2 * left - i])

        while T[i + 1 + largest_palindromes[i]] == T[i - 1 - largest_palindromes[i]]:
            largest_palindromes[i] += 1

        if i + largest_palindromes[i] > right:
            left, right = i, i + largest_palindromes[i]

    # first largest

    max_len = 0
    center_index = 0

    for i, n in enumerate(largest_palindromes):
        if n > max_len:
            max_len = n
            center_index = i

    if max_len > 0:
        return T[center_index - max_len:center_index + max_len + 1].replace("#", "")
    else:
        return ""
