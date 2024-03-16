# ---------------------------------------------------------------------------------------
# URL    : https://programavimas.vgtu.lt/contests/54/problems/2101/
# Title  : Kalnagūbriai
# Tags   : tag-LSPO, tag-vgtu, tag-problem-D
# Notes  :
# ---------------------------------------------------------------------------------------

# region --------------------------------------------Shared part--------------------------------------------------------
import math
import sys
from collections import defaultdict, Counter

inp = lambda: sys.stdin.readline().strip().rstrip("\r\n")
iinp = lambda: int(inp())
intl = lambda: list(map(int, inp().split()))
strl = lambda: list(inp().split())
list_to_string = lambda _a: "".join(map(str, _a))
list_to_string_list = lambda _a: " ".join(map(str, _a))
_dp = lambda default_value: defaultdict(lambda: default_value)
flush = lambda: sys.stdout.flush()
print_flush = lambda _text: (print(_text), flush())
fact = lambda number: math.factorial(number)
cnt = lambda _a: Counter(_a)


def lcm(a, b):
    return a * b // math.gcd(a, b)


def print_dp(_dict):
    for item in _dict.items():
        print(f"{item[0]} = {item[1]}")


MOD = 10 ** 9 + 7
INF = sys.maxsize
A = 911382323
M = 9999999999879998


# endregion
# -------------------------------------------------------Solution-------------------------------------------------------

def print_picture(matrix):
    for line in matrix:
        print("".join(line))

def solve():
    n = iinp()
    a = intl()

    _current = 0
    _min = 0
    _max = 0
    for i, e in enumerate(a):
        if i % 2 == 0:
            _current += e
        else:
            _current -= e
        
        if _min > _current:
            _min = _current

        if _max < _current:
            _max = _current

    # my current position is 0
    # min position _min
    # max position _max - 1
    # total columns sum
    # total rows
    h = _max - _min
    w = sum(a)

    matrix = []

    for i in range(h):
        matrix.append(["."] * w)

    start = h + _min
    _position = 0

    for i, e in enumerate(a):
        if i % 2 == 0:
            start -= 1

            for j in range(e):
                matrix[start][_position] = "/"
                start -= 1
                _position +=1
        else:
            start += 1

            for j in range(e):
                matrix[start][_position] = "\\"
                start += 1
                _position +=1

    print_picture(matrix)

def run():
    solve()


if __name__ == "__main__":
    run()
