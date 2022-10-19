# -----------------------------------------------------------
# URL    : https://www.codewars.com/kata/59887207635904314100007b
# Notes  : tag-codewars, tag-kyu-7
# -----------------------------------------------------------

def closest(lst):
    value = min(set([abs(x) for x in lst]))
    if value in lst and value != 0:
        return None if -1 * value in lst else value
    else:
        return -1 * value
