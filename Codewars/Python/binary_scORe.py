# -----------------------------------------------------------
# URL    : https://www.codewars.com/kata/56cafdabc8cfcc3ad4000a2b
# Notes  : tag-codewars
# -----------------------------------------------------------

def score(n):
    if n < 2:
        return n

    return 2 ** (len(bin(n).replace("0b", ""))) - 1
