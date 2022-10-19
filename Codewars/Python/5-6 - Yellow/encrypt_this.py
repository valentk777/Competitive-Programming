# -----------------------------------------------------------
# URL    : https://www.codewars.com/kata/5848565e273af816fb000449
# Notes  : tag-codewars, tag-kyu-6
# -----------------------------------------------------------

def encrypt_this(text):
    z = []
    for w in text.split():
        if len(w) == 2:
            z.append(str(ord(w[0])) + w[1])
        elif len(w) > 2:
            z.append(str(ord(w[0])) + w[-1] + w[2:-1] + w[1])
        else:
            z.append(str(ord(w[0])))
    return " ".join(z)
