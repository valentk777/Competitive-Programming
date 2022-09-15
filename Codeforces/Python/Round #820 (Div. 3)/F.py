# -----------------------------------------------------------
# URL    : https://codeforces.com/contest/1729/problem/F
# Title  : Title
# Notes  : tag-codeforces, tag-problem-F, tag-div-3, tag-not-pass
# -----------------------------------------------------------


def solve():
    s = input()
    n = len(s)
    w, m = list(map(int, input().split()))  # length of substring, queries

    found = 0
    options = {_i: [] for _i in range(0, 9)}

    for _i in range(1, n - w + 2):
        if found == 9 * 2:
            break

        r = int(s[_i - 1:_i + w - 1]) % 9

        if len(options[r]) < 2:
            options[r].append(_i)
            found += 1

    for i in range(m):
        l, r, k = list(map(int, input().split()))
        vv = int(s[l - 1:r]) % 9

        results = set()

        for mod1 in range(0, 9):
            for mod2 in range(0, 9):
                if (mod1 * vv + mod2) % 9 == k and len(options[mod1]) > 0 and len(options[mod2]) > 0:
                    if mod1 == mod2 and len(options[mod1]) == 2:
                        results.add((options[mod1][0], options[mod1][1]))
                    else:
                        L1 = min(options[mod1])
                        L2 = min(options[mod2])

                        if L1 == L2:
                            continue

                        results.add((L1, L2))

        if len(results) > 0:
            results = sorted(results, key=lambda x: (x[0], x[1]))
            print(f"{results[0][0]} {results[0][1]}")
        else:
            print("-1 -1")


if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        solve()
