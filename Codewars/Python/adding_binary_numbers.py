# -----------------------------------------------------------
# URL    : https://www.codewars.com/kata/55c11989e13716e35f000013
# Notes  : tag-codewars
# -----------------------------------------------------------

def bit_merge(x, y):
    if x + y == "00":
        return "0"
    elif x + y == "01" or x + y == "10":
        return "1"
    else:
        return "2"


def add(a, b):
    max_len = max(len(a), len(b))

    a = ("0" + a.zfill(max_len))[::-1]
    b = ("0" + b.zfill(max_len))[::-1]

    memory = "0"
    result = ""

    for i in range(max_len):
        merged = bit_merge(a[i], b[i])

        if merged == "2":
            if memory == "1":
                result = "1" + result
            else:
                memory = "1"
                result = "0" + result
        else:
            final = bit_merge(merged, memory)

            if final == "2":
                result = "0" + result
                memory = "1"
            else:
                result = final + result
                memory = "0"

    if memory == "1":
        result = memory + result

    result = result.lstrip("0")

    if len(result) == 0:
        return "0"

    return result


# brianpck solution
def binary_string_to_int(string):
    return sum((d == '1') * 2**i for i, d in enumerate(string[::-1]))

def add(a, b):
    return '{:b}'.format(binary_string_to_int(a) + binary_string_to_int(b))
