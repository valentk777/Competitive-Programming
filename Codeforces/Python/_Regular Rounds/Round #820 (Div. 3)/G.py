# -----------------------------------------------------------
# URL    : https://codeforces.com/contest/1729/problem/G
# Title  : Cut Substrings
# Notes  : tag-codeforces, tag-problem-G, tag-div-3
# -----------------------------------------------------------

MODULO = 10 ** 9 + 7


def solve():
    s = input()
    t = input()
    len_s = len(s)
    len_t = len(t)

    s_split = [s[i - 1:i - 1 + len_t] for i in range(1, len_s - len_t + 2)]

    # index of all t appearance in s
    p = [-500] + [i for i in range(len(s_split)) if s_split[i] == t] + [len_s + len_t - 1]
    len_p = len(p)

    dp_min = [10 ** 9 for _ in range(len_p)]
    dp_variations = [0 for _ in range(len_p)]

    dp_min[0] = 0
    dp_variations[0] = 1

    for i in range(len_p - 1):
        j = i + 1

        # find last intersecting index
        while j < len_p and p[j] < p[i] + len_t:
            j += 1

        k = j

        # check current and future intersections from that index if we remove this one
        while k < len_p and p[k] < p[j] + len_t:
            # if we do not fill that value before
            if dp_min[i] + 1 < dp_min[k]:
                # save number of removes needed
                # if we remove this, we need to fill values for future impacted indexes as well
                dp_min[k] = dp_min[i] + 1
                dp_variations[k] = dp_variations[i]
            elif dp_min[i] + 1 == dp_min[k]:
                dp_variations[k] = (dp_variations[k] + dp_variations[i]) % MODULO

            k += 1

    return f"{dp_min[len_p - 1] - 1} {dp_variations[len_p - 1]}"


if __name__ == "__main__":
    q = int(input())

    for _ in range(q):
        print(solve())
