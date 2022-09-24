# -----------------------------------------------------------
# URL    : https://codeforces.com/contest/894/problem/A
# Title  : QAQ
# Notes  : tag-codeforces, tag-problem-A, tag-div-2
# -----------------------------------------------------------


def solve_slow():
    n = input()
    nn = list(filter(lambda l: l == "Q" or l == "A", list(n)))
    n_len = len(nn)
    _sum = 0

    for i in range(n_len - 2):
        for j in range(i + 1, n_len - 1):
            for k in range(j + 1, n_len):
                if (nn[i] == "Q") and (nn[j] == "A") and (nn[k] == "Q"):
                    _sum += 1

    return _sum


if __name__ == "__main__":
    print(solve_slow())
