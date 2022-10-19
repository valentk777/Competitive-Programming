# -----------------------------------------------------------
# URL    : https://www.codewars.com/kata/5729c30961cecadc4f001878
# Notes  : tag-codewars, tag-kyu-7
# -----------------------------------------------------------

def unite_unique(*args):
    l = []
    for a in args:
        for b in a:
            if b not in l:
                l.append(b)
    return l