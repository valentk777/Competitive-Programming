# -----------------------------------------------------------
# URL    : https://www.codewars.com/kata/546dba39fa8da224e8000467
# Notes  : tag-codewars, tag-kyu-6
# -----------------------------------------------------------

def run_length_encoding(s):
    if s == "":
        return []

    result = []
    p, c = s[0], 1
    for l in s[1:]:
        if l == p:
            c += 1
        else:
            result.append([c, p])
            c, p = 1, l

    result.append([c, p])
    return result
