# -----------------------------------------------------------
# URL    : https://codeforces.com/contest/1480/problem/C
# Title  : Searching Local Minimum
# Notes  : tag-codeforces, tag-problem-C, tag-div-2
# -----------------------------------------------------------

def solve():
    a, b, n = list(map(int, input().split()))
    a_i = list(map(int, input().split()))
    b_i = list(map(int, input().split()))

    monsters = []
    for i in range(len(a_i)):
        monsters.append([a_i[i], b_i[i]])

    monsters.sort(key=lambda x: x[0])

    for m in monsters:
        while m[1] > 0:
            if b > 0:
                m[1] -= a
                b -= m[0]
            else:
                print("NO")
                return

    print("YES")


if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        solve()
