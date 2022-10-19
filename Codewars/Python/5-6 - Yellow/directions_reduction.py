# -----------------------------------------------------------
# URL    : https://www.codewars.com/kata/550f22f4d758534c1100025a
# Notes  : tag-codewars, tag-kyu-5
# -----------------------------------------------------------

def clean(arr):
    arr2 = []
    i = 1
    while i < len(arr):
        dest = arr[i - 1] + arr[i]
        if dest == "NORTHSOUTH" or dest == "SOUTHNORTH" or dest == "WESTEAST" or dest == "EASTWEST":
            i += 1
        else:
            arr2.append(arr[i - 1])

        if i + 1 == len(arr):
            arr2.append(arr[len(arr) - 1])

        i += 1
    return arr2
