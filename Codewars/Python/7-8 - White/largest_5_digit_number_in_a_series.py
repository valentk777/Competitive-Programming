# -----------------------------------------------------------
# URL    : https://www.codewars.com/kata/51675d17e0c1bed195000001
# Notes  : tag-codewars, tag-kyu-7
# -----------------------------------------------------------

def solution(digits: str) -> int:
    max_value = 0
    
    for i in range(len(digits) - 4):
        if max_value < int(digits[i:i + 5]):
            max_value = int(digits[i:i + 5])

    return max_value