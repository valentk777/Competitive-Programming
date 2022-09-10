# -----------------------------------------------------------
# URL    : https://codeforces.com/contest/1480/problem/C
# Title  : Searching Local Minimum
# Notes  : tag-codeforces, tag-problem-C, tag-div-2, tag-not-pass
# -----------------------------------------------------------


from sys import stdout


def print_ats(ats: int):
    print(f"! {ats}")
    stdout.flush()


def solve():
    n = int(input())
    n = n if n < 100 else 100

    print(f"? {1}")
    left = int(input())
    first = left

    if n == 1:
        print_ats(1)
        return

    print(f"? {2}")
    middle = int(input())

    if n == 2:
        print_ats(1 if left < middle else 2)
        return

    for i in range(3, n + 1):
        print(f"? {i}")
        right = int(input())

        if middle < min(left, right):
            print_ats(i - 1)
            return

        left, middle = middle, right

    if first < min(left, middle):
        print_ats(1)


if __name__ == "__main__":
    solve()
