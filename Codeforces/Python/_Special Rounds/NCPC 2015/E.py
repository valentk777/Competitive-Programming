# -----------------------------------------------------------
# URL    : https://codeforces.com/gym/100781
# Title  : Entertainment Box
# Notes  : tag-codeforces, tag-problem-E, tag-not-pass
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
list_to_string = lambda _a: " ".join(map(str, _a))
_dp = lambda default_value: defaultdict(lambda: default_value)

MOD = 10 ** 9 + 7
INF = maxsize


# -------------------------------------------------------Solution-------------------------------------------------------

def solve():
    n, k = intl()

    events = []
    _count = 0

    for i in range(n):
        x, y = intl()
        events.append([x, y])

    events = sorted(events, key=lambda q: q[1])
    new_events = []

    for _ in range(k):
        finish = 0

        for event in events:
            if finish <= event[0]:
                finish = event[1]
                _count += 1
            else:
                new_events.append(event)

        events = new_events
        new_events = []

    return _count


def run():
    print(solve())


if __name__ == "__main__":
    if os.environ.get("DEBUG_CODEFORCES"):
        stdin = open("../../input.txt", "r")
        start_time = time.time()
        run()
        print("\n--- %s seconds ---\n" % (time.time() - start_time))
    else:
        run()
