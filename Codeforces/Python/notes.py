import math
import re
import string
from collections import Counter, defaultdict
from fractions import Fraction
from math import sqrt


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


# get count of letters
s = "aaabbbxxx"
xxx = Counter(s)
print(xxx)

A = 911382323
M = 9999999999879998


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


# return you number of 2 divisors in provided x (slow)
def count_number_of_n_divisors(x, n):
    return 0 if x % n else count_number_of_n_divisors(x // n, n) + 1


# fast
def count_number_of_2_divisors(x):
    ans = 0

    while x & 1 == 0:
        ans += 1
        x //= 2

    return ans


print(count_number_of_n_divisors(10, 2) == 1)
print(count_number_of_n_divisors(8, 2) == 3)


def get_divisors(n):
    i = 1
    divisors = []
    _sqrt = sqrt(n)

    while i <= _sqrt:
        if n % i == 0:
            if n / i != i:
                divisors.append(n // i)

            divisors.append(i)

        i = i + 1

    return divisors


def is_square_of_prime(k):
    if k == 1:
        return False

    n = int(sqrt(k))

    if n * n != k:
        return False

    i = 2

    while i * i <= n:
        if n / i == n // i:
            return False
        i += 1

    return True


def get_all_prime_squares(max_value):
    a = [1] * max_value
    s = set()

    for i in range(2, max_value):
        if a[i]:
            s.add(i * i)

            for j in range(i * i, max_value, i):
                a[j] = 0

    return s


# @memodict
def get_prime_factors(n):
    """returns a Counter of the prime factorization of n"""

    def pollard_rho(_n):
        """pollard_rho - return a random factor of n; O(sqrt of lpf[n])"""
        if _n & 1 == 0:
            return 2

        if _n % 3 == 0:
            return 3

        s = ((_n - 1) & (1 - _n)).bit_length() - 1
        d = _n >> s

        for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
            p = pow(a, d, _n)
            if p == 1 or p == _n - 1 or a % _n == 0:
                continue

            for _ in range(s):
                prev = p
                p = (p * p) % _n

                if p == 1:
                    return math.gcd(prev - 1, _n)
                if p == _n - 1:
                    break
            else:
                for i in range(2, _n):
                    x, y = i, (i * i + 1) % _n
                    f = math.gcd(abs(x - y), _n)

                    while f == 1:
                        x, y = (x * x + 1) % _n, (y * y + 1) % _n
                        y = (y * y + 1) % _n
                        f = math.gcd(abs(x - y), _n)

                    if f != _n:
                        return f

        return _n

    if n <= 1:
        return Counter()

    function = pollard_rho(n)

    if function == n:
        return Counter([n])

    return prime_factors(function) + prime_factors(n // function)


def get_prime_factors(n):
    factors = []

    while n % 2 == 0:
        factors.append(2)
        n = n / 2

    # n became odd
    _sqrt = int(math.sqrt(n))
    for i in range(3, _sqrt + 1, 2):

        while n % i == 0:
            factors.append(i)
            n = n / i

    if n > 2:
        factors.append(n)

    return factors


def get_prime_range(n):
    history = [True] * n
    p = []

    for i in range(2, n):
        if history[i]:
            p.append(i)

            for j in range(i * i, n, i):
                history[j] = False
    return p


def number_of_prime_factors(n):
    number = 0

    while n % 2 == 0:
        number += 1
        n = n / 2

    # n became odd
    _sqrt = int(math.sqrt(n))
    for i in range(3, _sqrt + 1, 2):

        while n % i == 0:
            number += 1
            n = n / i

    if n > 2:
        number += 1

    return number


def is_prime(n):
    if n == 2:
        return True

    if (n % 2 == 0 and n != 2) or n < 2:
        return False

    i = 3
    while i * i <= n:
        if n % i == 0:
            return False

        i += 2

    return True


def factorial(n, end):
    ans = 1

    for i in range(end, n + 1):
        ans *= i

    return ans


# for division, use Franction (insted of /), because it works with bigger numbers
Fraction(5, 6)  # -> 5 / 6

# for binary search
from bisect import bisect_left, bisect_right

a = [1, 5, 5, 9]
print(bisect_left(a, 4))
print(bisect_right(a, 4))

# list of letters
print(string.ascii_lowercase)

# this can be re-written this way
# from
_map = list(string.ascii_lowercase) + (list(map(str, range(10))))
s = list(s.lower())
s = list(filter(lambda x: x in _map, s))
_count = Counter(s)

# to
_count = Counter(filter(str.isalnum, s.lower()))


# LIS (the longest increasing subsequence)
def find_lis(a, n):
    # max value where elements are smaller than current value
    dp = defaultdict(int)

    for i in range(n):
        dp[i] = 1

        for j in range(i):
            if a[j] < a[i] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1


# LIS (the longest increasing subsequence) + sequence itself
def find_lis_with_sequence(a, n):
    # if we want sequence itself, we can store array as well
    dp = defaultdict(list)

    for i in range(n):
        for j in range(i):
            if a[j] < a[i] and (len(dp[i]) < len(dp[j]) + 1):
                dp[i] = dp[j].copy()

        dp[i].append(i)

    _max = []

    for lis in dp.values():
        if len(lis) > len(_max):
            _max = lis

    return len(_max), _max


def find_lis_with_sequence_fast(a, n):
    _idx = []  # index of last element for each length of LIS
    _values = []  # value of last element for each length of LIS
    _predecessor = [-1] * n  # index of predecessor for LIS ending here

    for i, e in enumerate(a):
        j = bisect_left(_values, e)

        if j == len(_values):
            _values.append(e)
            _idx.append(i)
        else:
            _values[j] = e
            _idx[j] = i
        if j > 0:
            _predecessor[i] = _idx[j - 1]

    i = _idx[-1]

    for j in range(len(_values) - 1, -1, -1):
        _values[j] = i
        i = _predecessor[i]

    return _values


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


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return -1


def dfs(v, graph, used, k):
    ans = k
    used.add(v)

    for u in graph[v]:
        if u not in used:
            ans = max(ans, dfs(u, graph, used | {u}, k + 1))

    return ans
