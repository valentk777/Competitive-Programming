# -----------------------------------------------------------
# URL    : https://www.codewars.com/kata/57096af70dad013aa200007b
# Notes  : tag-codewars, tag-kyu-8
# -----------------------------------------------------------

def logical_calc(array, op):
    if op == "AND":
        result = array[0]

        for i in array[1:]:
            result &= i
        return result

    if op == "OR":
        result = array[0]

        for i in array[1:]:
            result |= i
        return result

    if op == "XOR":
        result = array[0]

        for i in array[1:]:
            result ^= i
        return result
