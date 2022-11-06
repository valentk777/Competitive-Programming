# -----------------------------------------------------------
# URL    : https://www.codewars.com/kata/57fb3c839610ce39f7000023
# Notes  : tag-codewars, tag-kyu-6
# -----------------------------------------------------------

def find(s):
    n = len(s)

    if n == 0:
        return ""

    left = 0
    _first = s[0]
    _second = None
    _max = 0
    ans = ""

    for i in range(n):
        if s[i] == _first and _second is not None:
            while s[left] == _first:
                left += 1
            _first = _second
            _second = s[i]
            continue

        if s[i] != _first and _second is None:
            _second = s[i]

        if i - left + 1 > _max:
            _max = i - left + 1
            ans = s[left:i + 1]

    if _second is None:
        return ""
    else:
        return ans
