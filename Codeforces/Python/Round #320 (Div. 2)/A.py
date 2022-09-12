# -----------------------------------------------------------
# URL    : https://codeforces.com/contest/579/problem/A
# Title  : Raising Bacteria
# Notes  : tag-codeforces, tag-problem-A, tag-div-2
# -----------------------------------------------------------


def solve():
    n = int(input())

    _count = 1
    closes_power_of_two = 1 << (n.bit_length() - 1)
    diff = n - closes_power_of_two

    while diff > 0:
        closes_power_of_two = 1 << (diff.bit_length() - 1)
        diff -= closes_power_of_two
        _count += 1

    return _count


if __name__ == "__main__":
    print(solve())
