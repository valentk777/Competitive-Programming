# -----------------------------------------------------------
# URL    : https://www.codewars.com/kata/596d34df24a04ee1e3000a25
# Notes  : tag-codewars
# -----------------------------------------------------------

def count_ones_slow(left, right):
    def get_sum(n):
        _sum = 0
        i = 0

        # iterate bit positions 2^0, 2^1, 2^2, 2^3, 2^4 ...
        while (1 << i) <= n:
            change = 1 << i
            k = 0

            print(f"1 << i = {change}")

            for j in range(n + 1):
                print(f"k = {k}")
                print(f"change = {change}")

                _sum += k

                if change == 1:
                    k = not k
                    change = 1 << i
                else:
                    change -= 1
            i += 1

        return _sum

    return get_sum(right) - get_sum(left - 1)


# fast
def _get_largest_power(n):
    x = 0

    while (1 << x) <= n:
        x += 1

    return x - 1


def get_largest_power(n):
    return len(bin(n)) - 3


def count_ones_fast(left, right):
    def get_sum(n):
        if n == 1:
            return 1

        if n <= 0:
            return 0

        largest_power = get_largest_power(n)

        #  is the sum of all "1" in numbers from 1 to 2^x-1
        count_until_largest_power = largest_power * pow(2, (largest_power - 1))

        #  is the sum of leading "1" in numbers from 2^x to n which is not considered in the recursive call
        count_only_left_first_ones = n - pow(2, largest_power) + 1

        # numbers left
        count_until_left_largest_power = get_sum(n - pow(2, largest_power))

        return count_until_largest_power + count_only_left_first_ones + count_until_left_largest_power

    return get_sum(right) - get_sum(left - 1)


# Blind4Basics solution
def count_up_to(n):
    s = 0

    while n:
        p = n.bit_length() - 1
        p2 = 1 << p
        s += p * (p2 >> 1) + n - p2 + 1
        n &= ~p2

        print(n)

    return s


def count_ones(left, right): return count_up_to(right) - count_up_to(left - 1)


result = count_ones(1, 100)
print(result)
