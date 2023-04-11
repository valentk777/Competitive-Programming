# -----------------------------------------------------------
# URL    : https://www.codewars.com/kata/541a354c39c5efa5fa001372
# Notes  : tag-codewars, tag-kyu-6
# -----------------------------------------------------------

def ip_to_num(ip):
    return int("".join(map(lambda x: '{0:08b}'.format(int(x)), ip.split("."))), 2)


def num_to_ip(num):
    num = bin(num).replace("0b", "").zfill(32)
    ans = str(int(num[:8], 2))

    for i in range(8, 32, 8):
        ans += "." + str(int(num[i:i + 8], 2))

    return ans
