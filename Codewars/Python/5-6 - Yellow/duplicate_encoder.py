# -----------------------------------------------------------
# URL    : https://www.codewars.com/kata/54b42f9314d9229fd6000d9c
# Notes  : tag-codewars, tag-kyu-6
# -----------------------------------------------------------

def duplicate_encode(word):
    new_word = ""
    word = word.lower()
    for letter in word:
        if word.count(letter) > 1:
            new_word += ")"
        else:
            new_word += "("

    return new_word
