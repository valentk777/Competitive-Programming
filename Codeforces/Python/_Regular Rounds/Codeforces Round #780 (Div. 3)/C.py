# ---------------------------------------------------------------------------------------
# URL    : https://codeforces.com/contest/1660/problem/C
# Title  : Get an Even String
# Tags   : tag-codeforces, tag-problem-C, tag-div-3, tag-difficulty-1300
# Notes  : dp, greedy, strings
# ---------------------------------------------------------------------------------------

INF = 10 ** 6


def solve():
    s = input()
    n = len(s)

    # letters history
    a = {chr(i): -1 for i in range(ord("a"), ord("z") + 1)}
    a[s[0]] = 0

    dp = [INF for _ in range(n + 1)]
    dp[0] = 0
    dp[1] = 1

    for i in range(1, n):
        # if this letter found first time, it means we need to increase removing letters count
        if a[s[i]] == -1:
            dp[i + 1] = dp[i] + 1

        # if we had this letter before, need to check what is min count letters to delete
        else:
            remove_this_letter = dp[i] + 1

            # last_index_we_find_this_letter_before
            last_idx = a[s[i]]
            number_to_remove_to_join_last_letter_with_this_one = dp[last_idx] + i - last_idx - 1

            dp[i + 1] = min(remove_this_letter, number_to_remove_to_join_last_letter_with_this_one)

        a[s[i]] = i

    return dp[n]


if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        print(solve())
