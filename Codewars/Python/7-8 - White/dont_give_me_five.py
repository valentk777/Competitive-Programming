# -----------------------------------------------------------
# URL    : https://www.codewars.com/kata/5813d19765d81c592200001a
# Notes  : tag-codewars, tag-kyu-7
# -----------------------------------------------------------

def dont_give_me_five(start, end):
    ans = 0

    for i in range(start, end + 1):
        if '5' not in str(i):
            ans += 1

    return ans
