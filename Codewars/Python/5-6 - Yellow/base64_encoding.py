# -----------------------------------------------------------
# URL    : https://www.codewars.com/kata/5270f22f862516c686000161
# Notes  : tag-codewars, tag-kyu-5
# -----------------------------------------------------------

def get_base64_letter(x: int):
    # A - Z
    if x < 26:
        return chr(ord("A") + x)

    # a - z
    if x < 52:
        return chr(ord("a") + x - 26)

    # 0 - 9
    if x < 62:
        return chr(ord("0") + x - 52)

    if x == 62:
        return "+"

    if x == 63:
        return "/"


def get_base64_number(x: str):
    # A - Z
    if "A" <= x <= "Z":
        return ord(x) - ord("A")

    # a - z
    if "a" <= x <= "z":
        return ord(x) - ord("a") + 26

    # 0 - 9
    if "0" <= x <= "9":
        return ord(x) - ord("0") + 52

    if x == "+":
        return 62

    if x == "/":
        return 63


def to_base_64(string):
    binary = "".join(map(lambda x: '{0:08b}'.format(ord(x)), string))

    len_binary = len(binary)

    if len_binary % 6 != 0:
        len_binary += 6 - (len_binary % 6)
        binary += "0" * (6 - (len_binary % 6))

    ans = ""

    for i in range(0, len_binary, 6):
        ans += get_base64_letter(int(binary[i:i + 6], 2))

    return ans


def from_base_64(string):
    binary = "".join(map(lambda x: '{0:06b}'.format(x), map(get_base64_number, string)))

    ans = ""
    len_binary = len(binary)

    if len_binary % 8 != 0:
        len_binary -= len_binary % 8
        binary = binary[:len_binary]

    for i in range(0, len(binary), 8):
        ans += chr(int(binary[i:i + 8], 2))

    return ans


# MangNguyen solution
CODES = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


def to_base_64(string):
    padding = 3 - len(string) % 3 if len(string) % 3 else 0
    binary = ''.join(format(ord(i), '08b') for i in string) + '00' * padding
    return ''.join(CODES[int(binary[i:i + 6], 2)] for i in range(0, len(binary), 6))


def from_base_64(string):
    binary = ''.join(format(CODES.find(i), '06b') for i in string)
    return ''.join(chr(int(binary[i:i + 8], 2)) for i in range(0, len(binary), 8)).rstrip('\x00')
