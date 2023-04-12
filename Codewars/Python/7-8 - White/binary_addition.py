# -----------------------------------------------------------
# URL    : https://www.codewars.com/kata/551f37452ff852b7bd000139
# Notes  : tag-codewars, tag-kyu-7
# -----------------------------------------------------------

def add_binary(a, b):
    return bin(a + b).replace("0b", "")


# machine level logic
# we can iterate from last character until first one and make a sum by making XOR operation for current value
# and AND operations for carry (+1) value. then use carry and repeat operation.
# Half adders and full adders
def add_binary_v2(a, b):
    max_len = max(len(bin(a)), len(bin(b))) - 2
    a = bin(a).replace("0b", "").zfill(max_len)
    b = bin(b).replace("0b", "").zfill(max_len)

    ans = ""
    carry = 0

    for i in range(1, max_len + 1):
        ha1s = int(a[-i]) ^ int(b[-i])
        ha1c_out = int(a[-i]) & int(b[-i])
        ha2s = carry ^ ha1s
        ha2c_out = carry & ha1s
        carry = ha1c_out | ha2c_out
        ans = str(ha2s) + ans

    if carry:
        ans = "1" + ans

    return ans
