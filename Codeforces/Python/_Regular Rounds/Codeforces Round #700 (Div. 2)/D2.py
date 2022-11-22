# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/1480/problem/D2
# Title  : Painting the Array II
# Tags   : tag-codeforces, tag-problem-D, tag-div-2, tag-not-pass
# ---------------------------------------------------------------------------------------


import itertools
from typing import Iterable


def remove_adjacent(data: Iterable[int]):
    return (k for k, v in itertools.groupby(data))


def solve():
    n = int(input())
    a = map(int, input().split())
    a = list(remove_adjacent(a))
    most = max(set(a), key=a.count)
    new = filter(lambda x: x != most, a)
    new = remove_adjacent(new)

    print(1 + len(list(new)))


if __name__ == "__main__":
    solve()
