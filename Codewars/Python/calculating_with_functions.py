# -----------------------------------------------------------
#
# https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39
#
# -----------------------------------------------------------

def validate(number: str, func: str = None) -> int:
    if func is not None:
        return int(eval(number + func))
    return int(number)


def zero(func=None):
    return validate("0", func)


def one(func=None):
    return validate("1", func)


def two(func=None):
    return validate("2", func)


def three(func=None):
    return validate("3", func)


def four(func=None):
    return validate("4", func)


def five(func=None):
    return validate("5", func)


def six(func=None):
    return validate("6", func)


def seven(func=None):
    return validate("7", func)


def eight(func=None):
    return validate("8", func)


def nine(func=None):
    return validate("9", func)


def plus(func=None):
    return f"+{func}"


def minus(func):
    return f"-{func}"


def times(func):
    return f"*{func}"


def divided_by(func=None):
    return f"/{func}"
