# -----------------------------------------------------------
# URL    : https://codeforces.com/contest/546/problem/A
# Notes  : tag-codeforces, tag-problem-A, tag-div-2
# -----------------------------------------------------------


def solve():
    k, n, w = list(map(int, input().split()))

    t_sum = 0
    for i in range(w + 1):
        t_sum += k * i

    pin = n - t_sum
    print(0) if pin >= 0 else print(-pin)


if __name__ == "__main__":
    solve()
