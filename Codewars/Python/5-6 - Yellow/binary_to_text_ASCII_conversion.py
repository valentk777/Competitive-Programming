# -----------------------------------------------------------
# URL    : https://www.codewars.com/kata/5583d268479559400d000064
# Notes  : tag-codewars, tag-kyu-6
# -----------------------------------------------------------

def binary_to_string(binary):
    ans = ""

    for i in range(0, len(binary), 8):
        ans += chr(int(binary[i: i + 8], 2))

    return ans
