# -----------------------------------------------------------
# URL    : https://www.codewars.com/kata/5541f58a944b85ce6d00006a
# Notes  : tag-codewars
# -----------------------------------------------------------

def productFib(prod):
    f1, f2 = 0, 1
    prod_fib = f1 * f2
    while prod_fib < prod:
        f3 = f1 + f2
        f1 = f2
        f2 = f3
        prod_fib = f1 * f2

    return [f1, f2, prod_fib == prod]
