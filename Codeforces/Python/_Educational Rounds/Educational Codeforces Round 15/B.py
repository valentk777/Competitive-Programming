# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/702/problem/B
# Title  : Powers of Two
# Tags   : tag-codeforces, tag-problem-B
# ---------------------------------------------------------------------------------------


def is_power_of_two(x):
    return (x != 0) and ((x & (x - 1)) == 0)


def solve_slow():
    n = int(input())
    a = list(map(int, input().split()))
    pair_count = 0

    for i in range(n - 1):
        for j in range(i + 1, n):
            if is_power_of_two(a[i] + a[j]):
                pair_count += 1

    return pair_count


# idea: use dictionary to store previous values and count of them. this gives us possibility avoid another iteration
def solve_fast():
    n = int(input())
    a = list(map(int, input().split()))
    pairs = {i: 0 for i in a}
    pair_count = 0

    # save power of two numbers
    powers = [1 << _pow for _pow in range(32)]

    for i in range(n):
        for _pow in range(32):
            diff = powers[_pow] - a[i]
            if diff in pairs.keys():
                pair_count += pairs[diff]

        pairs[a[i]] += 1

    return pair_count


if __name__ == "__main__":
    print(solve_fast())
