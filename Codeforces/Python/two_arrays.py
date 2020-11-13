# -----------------------------------------------------------
# URL    : https://codeforces.com/contest/1417/problem/B
# Notes  : tag-codeforces, tag-problem-B, tag-div-2
# -----------------------------------------------------------

def solve():
    n, t_critical = map(int, input().split())
    a = list(map(int, input().split()))

    t_half = t_critical // 2
    t_mod2 = t_critical % 2 == 0
    was_0 = False

    for element in a:
        if element > t_half:
            print(0, end=" ")
        elif t_mod2 and element == t_half:
            print(int(was_0), end=" ")
            was_0 = not was_0
        else:
            print(1, end=" ")
    print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()
