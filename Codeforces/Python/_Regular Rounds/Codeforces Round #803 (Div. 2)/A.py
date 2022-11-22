# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/1698/problem/A
# Title  : XOR Mixup
# Tags   : tag-codeforces, tag-problem-A, tag-div-2
# ---------------------------------------------------------------------------------------


def get_xor_sum(a, n):
    result = a[0]

    for i in range(1, n):
        result ^= a[i]

    return result


def solve():
    n = int(input())
    a = list(map(int, input().split()))

    for i in range(n):
        current = a[i]
        new_list = a[:i]

        if i + 1 < n:
            new_list += a[i + 1:]

        if get_xor_sum(new_list, n - 1) == current:
            return current


if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        print(solve())
