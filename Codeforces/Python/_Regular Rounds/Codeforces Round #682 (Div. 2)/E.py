# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/1438/problem/E
# Title  : Yurii Can Do Everything
# Tags   : tag-codeforces, tag-problem-E, tag-div-2, tag-difficulty-2500, tag-not-pass
# Notes  : binary search, bitmasks, brute force, constructive algorithms, divide and conquer, two pointers
# ---------------------------------------------------------------------------------------


# slow
def solve_1():
    def is_bitwise_equal_sum(_a, _i, _j):
        base_bitwise = _a[_i] ^ _a[_j]
        mid_sum = sum(_a[_i + 1:_j])
        return base_bitwise == mid_sum

    n = int(input())
    a = list(map(int, input().split()))
    count = 0

    for i in range(n - 2):
        for j in range(i + 2, n):
            if is_bitwise_equal_sum(a, i, j):
                count += 1
    print(count)


# slow
def solve_2():
    n = int(input())
    a = list(map(int, input().split()))
    count = 0

    for i in range(n - 2):
        sums = {i + 1: a[i + 1]}

        for j in range(i + 2, n):
            sums[j] = sums[j - 1] + a[j]

            if a[i] ^ a[j] == sums[j - 1]:
                count += 1

    print(count)


# dont work
def solve():
    n = int(input())
    a = list(map(int, input().split()))
    s = [0 for _ in range(n)]
    count = 0
    st = []

    for i in range(n):
        s[i] = s[i - 1] + a[i]

    for l in range(1, n):
        M = 1

        while M <= a[l]:
            for r in range(l + 2, M + 1):
                if (r <= n) and (s[r - 1] - s[l] <= M):
                    if (a[l] ^ a[r]) == s[r - 1] - s[l]:
                        st.append({l, r})
                else:
                    break
            M <<= 1

    reversed(a)

    for i in range(n):
        s[i] = s[i - 1] + a[i]

    for l in range(1, n):
        M = 1

        while M <= a[l]:
            for r in range(l + 2, M + 1):
                if (r <= n) and (s[r - 1] - s[l] <= M):
                    if (a[l] ^ a[r]) == s[r - 1] - s[l]:
                        st.append({n - r + 1, n - l + 1})
                else:
                    break
            M <<= 1

    print(len(st))


if __name__ == "__main__":
    solve()
