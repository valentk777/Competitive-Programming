# -----------------------------------------------------------
# URL    : https://codeforces.com/contest/544/problem/A
# Title  : Set of Strings
# Notes  : tag-codeforces, tag-problem-A, tag-div-2
# -----------------------------------------------------------


def solve():
    k = int(input())
    q = input()
    n = len(q)

    if n < k:
        print("NO")
        return

    if k == 1:
        print("YES")
        print(q)
        return

    used_char = [q[0]]
    results = []
    start = 0
    left = k

    for i in range(1, n):
        if q[i] not in used_char:
            results.append(q[start:i])
            start = i
            used_char.append(q[i])
            left -= 1

        if left == 1:
            results.append(q[i:])
            break

    if len(results) == k:
        print("YES")

        for r in results:
            print(r)
    else:
        print("NO")


if __name__ == "__main__":
    solve()
