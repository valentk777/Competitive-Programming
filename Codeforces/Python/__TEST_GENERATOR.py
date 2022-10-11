from random import randint

import pyperclip

list_to_string = lambda _a: "".join(map(str, _a))
list_to_string_list = lambda _a: " ".join(map(str, _a))


def generate_numbers(_n, _min, _max):
    _numbers = []

    for i in range(_n):
        _numbers.append(randint(_min, _max))

    _result = list_to_string_list(_numbers)

    print()
    print(_result)
    print()
    pyperclip.copy(_result)


def generate_random_string(_n, _min, _max):
    _numbers = []

    for i in range(_n):
        _numbers.append(chr(randint(ord("a"), ord("z"))))

    _result = list_to_string(_numbers)

    print()
    print(_result)
    print()
    pyperclip.copy(_result)


number_of_test_cases = 10 ** 5
min_number_value = 1
max_number_value = 2 * 10 ** 5

# generate_numbers(number_of_test_cases, min_number_value, max_number_value)
generate_random_string(number_of_test_cases, min_number_value, max_number_value)
