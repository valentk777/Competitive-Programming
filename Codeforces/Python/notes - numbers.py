import math
from collections import Counter
from fractions import Fraction

from template import memodict


# region - NUMBERS DIVISORS

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


@memodict
def get_divisors(n):
    i = 1
    divisors = []
    _sqrt = math.sqrt(n)

    while i <= _sqrt:
        if n % i == 0:
            if n / i != i:
                divisors.append(n // i)

            divisors.append(i)

        i = i + 1

    return divisors


# endregion

# region - NUMBERS PRIMES

def is_square_of_prime(k):
    if k == 1:
        return False

    n = int(math.sqrt(k))

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


@memodict
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

    return get_prime_factors(function) + get_prime_factors(n // function)


@memodict
def get_prime_factors(n):
    factors = []

    while n % 2 == 0:
        factors.append(2)
        n = n // 2

    # n became odd
    _sqrt = int(math.sqrt(n))
    for i in range(3, _sqrt + 1, 2):

        while n % i == 0:
            factors.append(i)
            n = n // i

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


# endregion

# region - NUMBERS MISK

def factorial(n, end):
    ans = 1

    for i in range(end, n + 1):
        ans *= i

    return ans


# for division, use Franction (instead of /), because it works with bigger numbers
Fraction(5, 6)  # -> 5 / 6


# (x ^ y) % p in O(log y)
def power_mod_m(x, y, m):
    res = 1

    # Update x if it is more than or equal to p
    x = x % m

    if x == 0:
        return 0

    while y > 0:

        # If y is odd, multiply x with result
        if (y & 1) == 1:
            res = (res * x) % m

        # y must be even now
        y = y >> 1  # y = y/2
        x = (x * x) % m

    return res

# endregion
