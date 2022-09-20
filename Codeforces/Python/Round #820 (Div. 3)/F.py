# -----------------------------------------------------------
# URL    : https://codeforces.com/contest/1729/problem/F
# Title  : Kirei and the Linear Function
# Notes  : tag-codeforces, tag-problem-F, tag-div-3
# -----------------------------------------------------------

INF = 10 ** 5


def solve():
    s = input()
    w, m = list(map(int, input().split()))  # length of substring, queries

    partial_sums = [0]

    for char in s:
        partial_sums.append((partial_sums[-1] + int(char)) % 9)

    mods_1 = [-1 for _ in range(9)]
    mods_2 = [-1 for _ in range(9)]

    # iterate from end and leave only last best mod
    for i in range(len(s) - w, -1, -1):
        mod = (partial_sums[i + w] - partial_sums[i] + 9) % 9
        mods_2[mod] = mods_1[mod]
        mods_1[mod] = i

    for _ in range(m):
        l, r, k = list(map(int, input().split()))
        min_1, min_2 = INF, INF
        mod_lr = (partial_sums[r] - partial_sums[l - 1] + 9) % 9

        for i in range(9):
            # only if mod exist and L smaller than we already have
            if -1 < mods_1[i] < min_1:
                mod_rm2 = (k - i * mod_lr + 81) % 9

                # if mod1 == mod2
                if mod_rm2 == i:

                    # if mod2 exist
                    if mods_2[mod_rm2] > -1:
                        min_1, min_2 = mods_1[i], mods_2[i]
                else:
                    if mods_1[mod_rm2] > -1:
                        min_1, min_2 = mods_1[i], mods_1[mod_rm2]

        if min_1 == INF:
            print("-1 -1")
        else:
            print(f"{min_1 + 1} {min_2 + 1}")


if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        solve()
