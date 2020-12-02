from utils import read


class PassObject:
    def __init__(self, data):
        numbers, letter, password = data.split()
        number1, number2 = numbers.split('-')
        self.first_number: int = int(number1)
        self.second_number: int = int(number2)
        self.letter: str = letter[0]
        self.password: str = password


input_data = read().split('\n')

pass_data = list(map(PassObject, input_data))
n = len(pass_data)


def compare_letters(letter: str):
    def step(data):
        return data == letter

    return step


def validate_password_1(data: PassObject) -> bool:
    return data.first_number <= len(list(filter(compare_letters(data.letter), data.password))) <= data.second_number


def validate_password_2(data: PassObject) -> bool:
    return (data.password[data.first_number - 1] == data.letter
            and data.password[data.second_number - 1] != data.letter
            or data.password[data.first_number - 1] != data.letter
            and data.password[data.second_number - 1] == data.letter)


def solve_1():
    print(sum(map(validate_password_1, pass_data)))


def solve_2():
    print(sum(map(validate_password_2, pass_data)))


solve_1()
solve_2()
