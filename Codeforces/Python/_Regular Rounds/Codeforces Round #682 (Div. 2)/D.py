# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/1438/problem/D
# Title  : Powerful Ksenia
# Tags   : tag-codeforces, tag-problem-D, tag-div-2, tag-difficulty-2200
# Notes  : bitmasks, constructive algorithms, math
# ---------------------------------------------------------------------------------------


def solve():
    n = int(input())
    a = list(map(int, input().split()))

    if n % 2 == 1:
        number_of_operations, moves, _ = change_bits(a, n)

        print_correct(moves, number_of_operations)
    else:
        number_of_operations, moves, a[:-1] = change_bits(a[:-1], n - 1)
        if a[0] == a[-1]:
            print_correct(moves, number_of_operations)
        else:
            print("NO")


def print_correct(moves, number_of_operations):
    print("YES")
    print(number_of_operations)
    for move in moves:
        print(move)


def change_bits(a, n):
    number_of_operations = 0
    moves = []

    for i in range(2, n, 2):
        number_of_operations += 1
        bitwise = a[i - 2] ^ a[i - 1] ^ a[i]
        a[i - 2] = bitwise
        a[i - 1] = bitwise
        a[i] = bitwise
        moves.append(f"{i - 1} {i} {i + 1}")
    for i in range(1, n - 1, 2):
        number_of_operations += 1
        bitwise = a[i - 1] ^ a[i] ^ a[n - 1]
        a[i - 1] = bitwise
        a[i] = bitwise
        moves.append(f"{i} {i + 1} {n}")
    return number_of_operations, moves, a


if __name__ == "__main__":
    solve()
