# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/1688/problem/A
# Title  : Cirno's Perfect Bitmasks Classroom
# Tags   : tag-codeforces, tag-problem-A, tag-div-2, tag-difficulty-800
# Notes  : bitmasks, brute force
# ---------------------------------------------------------------------------------------


def solve():
    x = int(input())

    if x == 1:
        return 3

    # this will take set all bits to zero except the bit. 11100100 -> 00000100
    result = x & -x

    # if x bigger than result, it means there are a few 1's left
    if x > result:
        return result

    # if this is the same number, then add 1 bit at the end will be enough
    return result + 1


if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        print(solve())
