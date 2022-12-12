from random import randint

import pyperclip

list_to_string = lambda _a: "".join(map(str, _a))
list_to_string_list = lambda _a: " ".join(map(str, _a))
list_to_cases = lambda _a: "\n".join(map(str, _a))


class NumberGenerators:
    def __init__(self, number_of_symbols_in_single_line, number_of_test_cases, min_number_value, max_number_value):
        self.number_of_symbols_in_single_line = number_of_symbols_in_single_line
        self.number_of_test_cases = number_of_test_cases
        self.min_number_value = min_number_value
        self.max_number_value = max_number_value

    def generate_sequence_until_n(self):
        _numbers = [i for i in range(1, self.number_of_symbols_in_single_line + 1)]
        _result = list_to_string_list(_numbers)

        print(_result)

        pyperclip.copy(_result)

        return _result

    def generate_numbers_single_line(self):
        return self._generate_numbers_single_line(True)()

    def _generate_numbers_single_line(self, copy):
        def step():
            _numbers = []

            for i in range(self.number_of_symbols_in_single_line):
                _numbers.append(randint(self.min_number_value, self.max_number_value))

            _result = list_to_string_list(_numbers)

            print(_result)

            if copy:
                pyperclip.copy(_result)

            return _result

        return step

    def generate_multiple_random_numbers(self, generator=None):
        if generator is None:
            generator = self._generate_numbers_single_line(False)

        strings = []

        for i in range(self.number_of_test_cases):
            strings.append(generator())

        _result = list_to_cases(strings)
        pyperclip.copy(_result)

        return _result


class StringGenerators:
    def __init__(self, number_of_symbols_in_single_line, number_of_test_cases, min_char=ord("a"), max_char=ord("z")):
        self.number_of_symbols_in_single_line = number_of_symbols_in_single_line
        self.number_of_test_cases = number_of_test_cases
        self.min_char = min_char
        self.max_char = max_char

    def _generate_single_random_string(self, copy):
        def step():
            _numbers = []

            for i in range(self.number_of_symbols_in_single_line):
                _numbers.append(chr(randint(self.min_char, self.max_char)))

            _result = list_to_string(_numbers)
            print(_result)

            if copy:
                pyperclip.copy(_result)

            return _result

        return step

    def generate_single_random_string(self):
        return self._generate_single_random_string(True)()

    def generate_multiple_random_strings(self, generator=None):
        if generator is None:
            generator = self._generate_single_random_string(False)

        strings = []

        for i in range(self.number_of_test_cases):
            strings.append(generator())

        _result = list_to_cases(strings)
        pyperclip.copy(_result)

        return _result


N = NumberGenerators(
    number_of_symbols_in_single_line=100000,
    number_of_test_cases=2000000,
    min_number_value=1,
    max_number_value=1000000000,
)

S = StringGenerators(
    number_of_symbols_in_single_line=100000,
    number_of_test_cases=30000,
    min_char=1,
    max_char=1000000000,
)

# N.generate_numbers_single_line(number_of_symbols_in_single_line, min_number_value, max_number_value)
# S.generate_single_random_string(number_of_symbols_in_single_line, min_number_value, max_number_value)
# generator = S.generate_single_random_string(number_of_symbols_in_single_line, min_number_value, max_number_value)
# S.generate_multiple_random_strings(number_of_test_cases, generator)

# N.generate_sequence_until_n()
# N.generate_numbers_single_line()
N.generate_numbers_single_line()
