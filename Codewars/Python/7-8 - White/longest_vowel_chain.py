# -----------------------------------------------------------
# URL    : https://www.codewars.com/kata/59c5f4e9d751df43cf000035
# Notes  : tag-codewars, tag-kyu-7
# -----------------------------------------------------------

def solve(s):
    vowels = list("aeiou")
    n = len(s)

    _max = 0
    _current = 0

    for i in range(n):
        if s[i] in vowels:
            _current += 1
        else:
            _max = max(_max, _current)
            _current = 0

    return _max
