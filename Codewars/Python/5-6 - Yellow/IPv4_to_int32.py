# -----------------------------------------------------------
# URL    : https://www.codewars.com/kata/52ea928a1ef5cfec800003ee
# Notes  : tag-codewars, tag-kyu-6
# -----------------------------------------------------------

def ip_to_int32(ip):
    return int("".join(map(lambda x: '{0:08b}'.format(int(x)), ip.split("."))), 2)
