# -----------------------------------------------------------
# URL    : https://www.codewars.com/kata/54bb6f887e5a80180900046b
# Notes  : tag-codewars, tag-kyu-6
# -----------------------------------------------------------

# Complexity O(n*n)
def longest_palindrome_n_2(s):
    n = len(s)

    if n == 0:
        return 0

    dp = [[0 for _ in range(n)] for _ in range(n)]

    ans = 1

    for i in range(n):
        dp[i][i] = 1

    for start_idx in range(n - 1):
        if s[start_idx] == s[start_idx + 1]:
            dp[start_idx][start_idx + 1] = 1
            ans = 2

    for len_of_substring in range(3, n + 1):
        for start_idx in range(n - len_of_substring + 1):
            end_idx = start_idx + len_of_substring - 1

            # if palindrome
            if dp[start_idx + 1][end_idx - 1] == 1 and s[start_idx] == s[end_idx]:
                dp[start_idx][end_idx] = 1

                if len_of_substring > ans:
                    ans = len_of_substring

    return ans


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

    return max_len


print(longest_palindrome_n("baablkj12345432133d"), 9)
