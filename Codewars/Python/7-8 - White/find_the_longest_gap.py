# -----------------------------------------------------------
# URL    : https://www.codewars.com/kata/55b86beb1417eab500000051
# Notes  : tag-codewars, tag-kyu-7
# -----------------------------------------------------------

def gap(num):
    num_list = bin(num).replace("0b", "").split("1")[1:-1]

    if len(num_list) == 0:
        return 0

    return len(max(num_list, key=lambda x: len(x)))
