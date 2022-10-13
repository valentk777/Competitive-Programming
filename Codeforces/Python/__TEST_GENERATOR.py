from random import randint

import pyperclip

list_to_string = lambda _a: "".join(map(str, _a))
list_to_string_list = lambda _a: " ".join(map(str, _a))
list_to_cases = lambda _a: "\n".join(map(str, _a))


def generate_numbers_single_line(_n, _min, _max):
    _numbers = []

    for i in range(_n):
        _numbers.append(randint(_min, _max))

    _result = list_to_string_list(_numbers)

    print()
    print(_result)
    print()
    pyperclip.copy(_result)

    return _result


def generate_single_random_string(_n, _min, _max):
    def step():
        _numbers = []

        for i in range(_n):
            _numbers.append(chr(randint(ord("a"), ord("z"))))

        _result = list_to_string(_numbers)
        print(_result)
        # pyperclip.copy(_result)

        return _result

    return step


def generate_multiple_random_strings(_number_of_test_cases, generator):
    strings = []

    for i in range(_number_of_test_cases):
        strings.append(generator())

    _result = list_to_cases(strings)
    pyperclip.copy(_result)
    return _result


number_of_symbols_in_single_line = 40
number_of_test_cases = 30000
min_number_value = 2
# max_number_value = 2 * 10 ** 5
max_number_value = 2

# generate_numbers(number_of_symbols_in_single_line, min_number_value, max_number_value)
# generate_single_random_string(number_of_symbols_in_single_line, min_number_value, max_number_value)
string_generator = generate_single_random_string(number_of_symbols_in_single_line, min_number_value, max_number_value)

generate_multiple_random_strings(number_of_test_cases, string_generator)
