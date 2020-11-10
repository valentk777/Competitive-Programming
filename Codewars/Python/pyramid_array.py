# -----------------------------------------------------------
#
# https://www.codewars.com/kata/515f51d438015969f7000013
#
# -----------------------------------------------------------

def pyramid(n: int) -> list:
    return [[1 for _ in range(i + 1)] for i in range(n)]
