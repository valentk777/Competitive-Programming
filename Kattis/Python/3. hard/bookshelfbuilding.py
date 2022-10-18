# -----------------------------------------------------------
# URL    : https://open.kattis.com/problems/bookshelfbuilding
# Title  : Bookshelf Building
# Notes  : tag-kattis, tag-hard, tag-not-pass
# -----------------------------------------------------------

# ---------------------------------------------------Shared part--------------------------------------------------------
import os
import time
from collections import defaultdict
from sys import stdin, maxsize

inp = lambda: stdin.readline().strip()
iinp = lambda: int(inp())
intl = lambda: list(map(int, inp().split()))
strl = lambda: list(inp().split())
list_to_string = lambda _a: "".join(map(str, _a))
list_to_string_list = lambda _a: " ".join(map(str, _a))
_dp = lambda default_value: defaultdict(lambda: default_value)
print_dp = lambda _dict: list(map(lambda item: print(f"{item[0]} = {item[1]}"), _dict.items()))
list_from_inp = lambda n: [inp() for _ in range(n)]

MOD = 10 ** 9 + 7
INF = maxsize


# -------------------------------------------------------Solution-------------------------------------------------------

def solve():
    # x - width, y = height
    n, x, y = intl()

    books = []
    for i in range(n):
        w, h = intl()
        books.append((w, h, w * h))

    books = sorted(books, key=lambda book: (book[1], book[2]), reverse=True)

    board = books[0][1]

    x_up = x
    x_down = x
    y_up = y - board

    for i in range(n):
        if books[i][1] > y:
            return "impossible"

        if x_down - books[i][0] >= 0:
            x_down -= books[i][0]
        elif y_up >= books[i][1]:
            if x_up - books[i][0] >= 0:
                x_up -= books[i][0]
            else:
                return "impossible"
        else:
            return "impossible"

    if board == y:
        return -1

    return board


def run():
    print(solve())


if __name__ == "__main__":
    if os.environ.get("DEBUG_CODEFORCES"):
        stdin = open("../input.txt", "r")
        start_time = time.time()
        run()
        print("\n--- %s seconds ---\n" % (time.time() - start_time))
    else:
        run()
