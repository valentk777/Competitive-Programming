# -----------------------------------------------------------
# URL    : https://www.codewars.com/kata/511f11d355fe575d2c000001
# Notes  : tag-codewars, tag-kyu-7
# -----------------------------------------------------------

def two_oldest_ages(ages):
    oldest = []
    maxim = max(ages)
    oldest.append(maxim)
    ages.remove(maxim)
    oldest.append(max(ages))
    return sorted(oldest)