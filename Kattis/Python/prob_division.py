# -----------------------------------------------------------
# URL    : https://open.kattis.com/problems/division
# Title  : Division
# Notes  : tag-kattis, tag-not-pass
# -----------------------------------------------------------

# ---------------------------------------------------Shared part--------------------------------------------------------
import os
import time
from math import ceil, floor
from sys import stdin, maxsize

inp = lambda: stdin.readline().strip()
iinp = lambda: int(inp())
intl = lambda: list(map(int, inp().split()))
strl = lambda: list(inp().split())

MOD = 10 ** 9 + 7
INF = maxsize
const = 10 ** 100 - 1


# -------------------------------------------------------Solution-------------------------------------------------------
def my_power(t, a):
    result = t

    for _ in range(2, a + 1):
        result *= t

        if result > const:
            return -1

    return result


# Function to perform a division of two numbers using the
# binary search algorithm
def divide(x, y):
    left = 0.0
    right = x

    # set accuracy of the result
    precision = 0.0000000000001

    before = INF

    while True:
        # calculate mid
        mid = left + (right - left) / 2

        # if `y×mid` is almost equal to `x`, return `mid`
        if abs(y * mid - x) == 0:
            return mid

        # if `y×mid` is less than `x`, update `left` to `mid`
        if y * mid < x:
            left = mid
        else:
            # if `y×mid` is more than `x`, update `right` to `mid`
            right = mid

        if mid == before:
            return -1

        before = mid


def get_number(t, a, b):
    if a == b:
        return 1

    if a < b:
        return -1

    # ta_b = my_power(t ** (a - b)
    # if ta_b > const:
    #     return -1

    t_b = my_power(t, b)

    if t_b == -1:
        return -1

    ta_b = my_power(t, (a - b))

    if ta_b == -1:
        return -1

    # t_a = my_power(t, a)
    #
    # if (t_a - 1) % (t_b - 1) != 0:
    #     return -1
    #
    # return (t_a - 1) // (t_b - 1)

    # qq, ee = div_algo_pos_a( my_power(t, a) - 1, t_b - 1)
    # if ee == 0:
    #     return qq
    # else:
    #     return -1

    result = divide(my_power(t, a) - 1, t_b - 1)

    if result == -1:
        return -1

    return int(result)

    # k = (((1 - ta_b) % t_b) - ta_b)
    #
    # # k = ta_b
    # q = (1 - k) // t_b
    #
    # while k <= const:
    #
    #     if ta_b - k == q:
    #         return k
    #
    #     for r in range(1, t_b - 1):
    #         if ta_b - k == q + r:
    #             return -1
    #
    #     k += t_b
    #     q -= 1
    #
    #
    # return -1

    #
    # print(maybe)
    #
    # # if len(str(t)) > 100:
    # #     return -1
    #
    # # for i in range()
    #
    # # if t < 1000:
    # ta = t ** a - 1
    # tb = t ** b - 1
    #
    # if ta % tb != 0:
    #     return -1
    #
    # result = ta // tb
    #
    # if len(str(result)) > 100:
    #     return -1
    #
    # return result

    #
    # diffta = ta - 1
    # diffba = tb - 1
    #
    # if diffba != 0:
    #     return -1
    #
    # result = diffta // diffba
    #
    # if len(str(result)) > 100:
    #     return -1
    #
    # return result


def solve():
    t, a, b = intl()

    ats = get_number(t, a, b)

    if ats != -1:
        return f"({t}^{a}-1)/({t}^{b}-1) {ats}"
    else:
        return f"({t}^{a}-1)/({t}^{b}-1) is not an integer with less than 100 digits."


def run():
    try:
        while True:
            print(solve())
    except:
        pass


if __name__ == "__main__":
    if os.environ.get("DEBUG_CODEFORCES"):
        stdin = open("input.txt", "r")
        start_time = time.time()
        run()
        print("\n--- %s seconds ---\n" % (time.time() - start_time))
    else:
        run()
