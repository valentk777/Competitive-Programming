# -----------------------------------------------------------
# URL    : https://www.codewars.com/kata/57fae964d80daa229d000126
# Notes  : tag-codewars, tag-kyu-8
# -----------------------------------------------------------

def remove(s):
    if len(s) > 0:
        if s[-1] == "!":
            return s[:-1] 
    return s