# -----------------------------------------------------------
# URL    : https://codeforces.com/contest/1566/problem/B
# Title  : MIN-MEX Cut
# Notes  : tag-codeforces, tag-problem-B
# -----------------------------------------------------------


def solve_using_list():
    s = input()
    zeros = list(filter(lambda x: x != "", s.split("1")))
    zeros_len = len(zeros)

    if zeros_len == 0:
        return 0

    if zeros_len == 1:
        return 1

    return 2


def solve_using_iteration():
    s = input()
    n = len(s)
    result = 0

    for i in range(0, n - 1):
        if s[i] != s[i + 1]:
            if s[i] == "0":
                result += 1

        if result > 1:
            return 2

    if s[n - 1] == "0":
        result += 1

    return min(2, result)


if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        print(solve_using_iteration())
