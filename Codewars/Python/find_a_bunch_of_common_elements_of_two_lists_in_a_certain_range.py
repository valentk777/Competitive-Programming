# -----------------------------------------------------------
#
# https://www.codewars.com/kata/58161c5ac7e37d17fc00002f
#
# -----------------------------------------------------------

def filter_array(arrX, odd, _from, _to):
    duplicates_in_X = set()

    for i in range(1, len(arrX)):
        if _from > arrX[i] or arrX[i] > _to:
            continue
        if arrX[i] % 2 != odd:
            continue
        if arrX[i - 1] == arrX[i]:
            duplicates_in_X.add(arrX[i])
            i += 1
    return duplicates_in_X


def find_arr(arrA, arrB, rng, wanted):
    arrA.sort()
    arrB.sort()

    if wanted == "odd":
        duplicates_in_A = filter_array(arrA, 1, rng[0], rng[1])
        duplicates_in_B = filter_array(arrB, 1, rng[0], rng[1])

    else:
        duplicates_in_A = filter_array(arrA, 0, rng[0], rng[1])
        duplicates_in_B = filter_array(arrB, 0, rng[0], rng[1])

    result = list(duplicates_in_A & duplicates_in_B)
    result.sort()
    return result
