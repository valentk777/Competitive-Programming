# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/1527/problem/A
# Title  : And Then There Were K
# Tags   : tag-codeforces, tag-problem-A, tag-div-2, tag-difficulty-800
# Notes  : bitmasks
# ---------------------------------------------------------------------------------------


def solve():
    n = int(input())

    # when we get number, using & we need to remove firs bit,
    # so the biggest number without bit in first location will be 2**k - 1
    # before this will be 2**k with value 100000000... So all other bits will be removed (excluding first one)
    # and second value 2**k - 1 will be 01111111... and remove first bit.
    return (1 << (n.bit_length() - 1)) - 1


if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        print(solve())
