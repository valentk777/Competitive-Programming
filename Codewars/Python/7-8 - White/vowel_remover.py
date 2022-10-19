# -----------------------------------------------------------
# URL    : https://www.codewars.com/kata/5547929140907378f9000039
# Notes  : tag-codewars, tag-kyu-8
# -----------------------------------------------------------

def shortcut( s ):
    res = ""
    for i in s:
        if i not in ['a', 'e', 'i', 'o', 'u']:
            res += i
    return res