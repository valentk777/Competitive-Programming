# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/540/problem/B
# Title  : School Marks
# Tags   : tag-codeforces, tag-problem-B, tag-div-2
# ---------------------------------------------------------------------------------------


def get_median(_a):
    len_a = len(_a)

    if len_a == 0:
        return 0

    _a.sort()

    if len_a % 2 == 1:
        return _a[(len_a + 1) // 2 - 1]
    else:
        return (_a[len_a // 2 - 1] + _a[len_a // 2]) / 2


def list_to_string(_a):
    return " ".join(map(str, _a))


def solve():
    n, k, p, x, y = list(map(int, input().split()))
    a = []

    # note: read list only we already have any marks
    if k != 0:
        a = list(map(int, input().split(" ")))

    # if we have all marks - do nothing
    if n == k:
        return ""

    # if expected median bigger then sum
    if y > x:
        return -1

    sum_marks = sum(a)
    missing_marks_count = n - k
    missing_marks_sum = x - sum_marks

    # if only 1-s already pass possible sum
    if missing_marks_count > missing_marks_sum:
        return -1

    result = []

    # take only medians if we can
    if missing_marks_sum >= missing_marks_count * y:
        result = [y for _ in range(missing_marks_count)]
    else:
        median_marks = get_median(a)

        for _ in range(missing_marks_count):
            if y <= median_marks:
                result.append(1)
                median_marks = get_median(a + result)
            else:
                result.append(y)
                median_marks = get_median(a + result)

    if y <= get_median(a + result) and sum(a + result) <= x:
        return list_to_string(result)
    else:
        return -1


if __name__ == "__main__":
    print(solve())
