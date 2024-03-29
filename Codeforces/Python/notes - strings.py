import re
import string
from collections import Counter


# region - STRINGS PALINDROME

# Complexity O(n)
# Manacher algorithm
def longest_palindrome_n(s):
    # Transform S into T.
    # For example, S = "abba", T = "^#a#b#b#a#$".
    # ^ and $ signs are sentinels appended to each end to avoid bounds checking
    T = '#'.join('^{}$'.format(s))
    n = len(T)

    # create temporary array for holding largest palindrome at every point. There are 2*n + 3 such points.
    largest_palindromes = [0] * n
    left = 0
    right = 0

    for i in range(1, n - 1):
        # equals to i' = left - (i-left)
        largest_palindromes[i] = (right > i) and min(right - i, largest_palindromes[2 * left - i])

        # Attempt to expand palindrome centered at i
        while T[i + 1 + largest_palindromes[i]] == T[i - 1 - largest_palindromes[i]]:
            largest_palindromes[i] += 1

        # If palindrome centered at i expand past right, adjust center based on expanded palindrome.
        if i + largest_palindromes[i] > right:
            left, right = i, i + largest_palindromes[i]

    # Find the maximum element in P.
    max_len, center_index = max((n, i) for i, n in enumerate(largest_palindromes))

    # return max len
    return max_len

    # return string value
    return T[center_index - max_len:center_index + max_len + 1].replace("#", "")


# endregion

# region - STRINGS HASH

A = 911382323
M = 9999999999879998


def polynomial_hash(s):
    _hash = 0
    _pow = 1

    for c in s:
        _hash = (_hash + ord(c) * _pow) % M
        _pow = (_pow * A) % M

    return _hash


def str_hash(s):
    _hash = 0
    _pow = 1

    for c in s:
        _hash = (_hash + ord(c) * _pow) % M
        _pow = (_pow * A) % M

    return _hash


# endregion

# region - STRINGS PREFIX/SUFFIX


def prefix_length(s1, s2):
    i = 0
    while i < len(s1) and i < len(s2) and s1[i] == s2[i]:
        i += 1
    return i


def suffix_length(s1, s2):
    i = 0
    while i < len(s1) and i < len(s2) and s1[i - 1] == s2[i - 1]:
        i += 1
    return i


# slow
def get_length_of_longest_prefix_suffix(s):
    return len(re.findall(r'^(\w*).*\1$', s)[0])


def get_length_of_longest_prefix_suffix(s):
    n = len(s)
    lps = [0] * n  # lps[0] is always 0
    length_of_prev_longest_prefix = 0

    i = 1

    while i < n:
        if s[i] == s[length_of_prev_longest_prefix]:
            length_of_prev_longest_prefix = length_of_prev_longest_prefix + 1
            lps[i] = length_of_prev_longest_prefix
            i = i + 1

        else:
            # (pat[i] != pat[len])
            # This is tricky. Consider
            # the example. AAACAAAA
            # and i = 7. The idea is
            # similar to search step.

            if length_of_prev_longest_prefix != 0:
                length_of_prev_longest_prefix = lps[length_of_prev_longest_prefix - 1]

                # Also, note that we do
                # not increment i here

            else:

                # if (len == 0)
                lps[i] = 0
                i = i + 1

    res = lps[n - 1]

    # Since we are looking for
    # non overlapping parts.
    if res > n / 2:
        return n // 2
    else:
        return res


# endregion

# region - STRINGS MISK


# list of letters
print(string.ascii_lowercase)

# this can be re-written this way
# from
_map = list(string.ascii_lowercase) + (list(map(str, range(10))))
s = "aaabbbxxx"
s = list(s.lower())
s = list(filter(lambda x: x in _map, s))
_count = Counter(s)

# to
s = "aaabbbxxx"
_count = Counter(filter(str.isalnum, s.lower()))


def z_array(_string):
    n = len(_string)
    z = [0 for _ in range(n)]

    # [L,R] make a window which matches with prefix of s
    left, right, k = 0, 0, 0
    for i in range(1, n):

        # if i>R nothing matches, so we will calculate. Z[i] using naive way.
        if i > right:
            left, right = i, i

            # R-L = 0 in starting, so it will start checking from 0'th index. For example,
            # for "ababab" and i = 1, the value of R remains 0 and Z[i] becomes 0. For string
            # "aaaaaa" and i = 1, Z[i] and R become 5
            while right < n and _string[right - left] == _string[right]:
                right += 1

            z[i] = right - left
            right -= 1
        else:

            # k = i-L so k corresponds to number which matches in [L,R] interval.
            k = i - left

            # if Z[k] is less than remaining interval then Z[i] will be equal to Z[k].
            # For example, str = "ababab", i = 3, R = 5 and L = 2
            if z[k] < right - i + 1:
                z[i] = z[k]

            # For example str = "aaaaaa" and i = 2, R is 5, L is 0
            else:

                # else start from R and check manually
                left = i

                while right < n and _string[right - left] == _string[right]:
                    right += 1

                z[i] = right - left
                right -= 1

    return z


def find_positions(a, b):
    la = len(a)
    lb = len(b)
    z = z_array(b + "#" + a)
    z_rev = z_array(b[::-1] + "#" + a[::-1])

    positions = []
    for i in range(la):
        left = min(i, z[lb + 1])
        right = min(lb - i, z_rev[lb + 1])
        if left + right == lb:
            positions.append(str(i + 1))

    return positions


# get count of letters
s = "aaabbbxxx"
xxx = Counter(s)
print(xxx)

# endregion
