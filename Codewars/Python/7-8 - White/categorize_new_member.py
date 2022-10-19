# -----------------------------------------------------------
# URL    : https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa
# Notes  : tag-codewars, tag-kyu-7
# -----------------------------------------------------------

def openOrSenior(data):
    li = []
    for element in data:
        if ((element[0] > 54) & (element[1] > 7)):
            li.append("Senior")
        else:
            li.append("Open")
    return li
