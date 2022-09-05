# -----------------------------------------------------------
# URL    : https://www.codewars.com/kata/55035eb47451fb61c0000288
# Notes  : tag-codewars
# -----------------------------------------------------------

def okkOokOo(s):
    def split_by(text, symbol):
        return list(filter(lambda x: len(x) > 0, map(lambda x: x.strip(), text.split(symbol))))

    def converter(letter):
        converted = ''.join(split_by(letter, ',')).lower().replace("o", "0").replace("k", "1")
        return chr(int(converted, 2))

    result = ""

    split_by_word = split_by(s, '!')

    for word in split_by_word:
        split_by_letter = split_by(word, '?')
        result = ''.join(map(converter, split_by_letter)) + " "

    return result.strip(" ")
