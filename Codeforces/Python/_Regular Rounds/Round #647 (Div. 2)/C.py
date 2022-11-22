# -----------------------------------------------------------
# URL    : https://codeforces.com/contest/1362/problem/C
# Title  : Johnny and Another Rating Drop
# Notes  : tag-codeforces, tag-problem-C, tag-div-2
# -----------------------------------------------------------


def solve():
    n = int(input())

    _sum = 0

    # we can calculate number of bits from last till first one.
    # Last bit changed every time, so it will be n changes, then second bit change every 2**1 bits
    # then every 2**k bits until first one
    for i in range(n.bit_length()):
        _sum += n // (1 << i)

    return _sum


if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        print(solve())
