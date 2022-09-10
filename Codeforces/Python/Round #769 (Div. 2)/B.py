# -----------------------------------------------------------
# URL    : https://codeforces.com/contest/1632/problem/B
# Title  : Roof Construction
# Notes  : tag-codeforces, tag-problem-B, tag-div-2
# -----------------------------------------------------------


def list_to_string(_a):
    return " ".join(map(str, _a))


def solve_max():
    def invert_bits(x):
        # construct mask with only ones
        mask = 2 ** x.bit_length() - 1

        # alternative way to get a mask
        # mask = x
        #
        # for i in range(x.bit_length()):
        #     mask |= mask >> (2 ** i)

        return x ^ mask

    def invert_bits_v2(x):
        # alternative way to get a mask
        mask = x

        for i in range(x.bit_length()):
            mask |= mask >> (2 ** i)

        return x ^ mask

    n = int(input())

    # max number will be a number, when all possible places in max element will be filled with 1
    # we take n - 1 (max element), find with changed bit's and group them as pair
    inverted = invert_bits(n - 1)

    result = list(range(n))
    result.remove(inverted)
    result += [inverted]

    return list_to_string(result)


def solve_min():
    n = int(input())

    max_sum = 1 << ((n - 1).bit_length() - 1)

    # all values before should be less than max_sum in order to do not produce bigger XOR
    # max_sum should be close to 0 in order to produce max_sum
    # all others number, bigger than max_sum should be in right part and do not produce bigger XOR than max_sum

    # this will be the same if we iterate from the beginning:
    # 1, 2, 3, ..., 0, max_sum, max_sum + 1, .... n - 1, for n > 3
    result = list(range(max_sum - 1, -1, -1)) + list(range(max_sum, n))
    return list_to_string(result)


if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        print(solve_min())
