# -----------------------------------------------------------
# URL    : https://www.codewars.com/kata/546ba103f0cf8f7982000df4
# Notes  : tag-codewars, tag-kyu-7
# -----------------------------------------------------------

def calculate(n1, n2, o):
    n1 = int(n1, 2)
    n2 = int(n2, 2)
    ans = 0

    if o == "add":
        ans = n1 + n2
    if o == "subtract":
        ans = n1 - n2
    if o == "multiply":
        ans = n1 * n2

    return '{0:b}'.format(ans)


print(calculate('1', '1', 'subtract'))
print(calculate('10', '1', 'subtract'))
print(calculate('10', '100', 'subtract'))
print(calculate('10', '10', 'multiply'))
