# -----------------------------------------------------------
# URL    : https://www.codewars.com/kata/59b44d00bf10a439dd00006f
# Notes  : tag-codewars, tag-kyu-7
# -----------------------------------------------------------

def add(l):
    return [sum(l[:i+1]) for i in range(len(l))]