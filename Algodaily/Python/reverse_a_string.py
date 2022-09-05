# https://algodaily.com/challenge_slides/reverse-a-string


def reverse_string_old(str1):
    def reverse_x(str2, x):
        if x > 1:
            return str2[x] + reverse_x(str2[:x], x - 1)
        elif x == 1:
            return str2[x] + str2[0]
        else:
            return str2

    return reverse_x(str1, len(str1) - 1)


def reverse_string(str1):
    arr = list(str1)
    j = len(arr)

    for i in range(j // 2):
        j -= 1
        arr[i], arr[j] = arr[j], arr[i]

    return "".join(arr)


# ##################################################################################################################
# Algodaily solutions
# ##################################################################################################################
# Method 1
def reverse_str(s):
    str_arr = list(s)
    start, end = 0, len(str_arr) - 1
    while start < end:
        str_arr[start], str_arr[end] = str_arr[end], str_arr[start]
        start += 1
        end -= 1
    return "".join(str_arr)


print(reverse_str("jake"))


# Method 2
def reverse_string(s):
    if len(s) <= 1:
        return s

    return reverse_string(s[1:]) + s[0]


# Method 3
def reverse_string(s):
    tmp = ""
    for char in s:
        tmp = char + tmp
    return tmp


# ##################################################################################################################


import unittest


class Test(unittest.TestCase):
    def test_1(self):
        assert reverse_string("njnschnjkdasn j32 uida") == "adiu 23j nsadkjnhcsnjn"
        print("PASSED: reverse_string('njnschnjkdasn j32 uida') should return 'adiu 23j nsadkjnhcsnjn'")

    def test_2(self):
        assert reverse_string("timbuktu12") == "21utkubmit"
        print("PASSED: reverse_string('timbuktu12') should return '21utkubmit'")

    def test_3(self):
        assert reverse_string("") == ""
        print("PASSED: reverse_string('') should return ''")

    def test_4(self):
        assert reverse_string("reverseastring") == "gnirtsaesrever"
        print("PASSED: reverse_string('reverseastring') should return 'gnirtsaesrever'")


if __name__ == "__main__":
    unittest.main(verbosity=2)
    print("Nice job, 4/4 tests passed!")
