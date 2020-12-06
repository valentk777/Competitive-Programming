from utils import read_lines

input_data = read_lines()


class BoardingPass:
    def __init__(self, information: str):
        self.row_data = information[:7]
        self.column_data = information[7:]
        self.row = self.__find_row()
        self.column = self.__find_column()
        self.seat_id = self.__seat_id()

    def __str__(self):
        return f"{self.row_data} {self.column_data} " \
               f"{self.row}; {self.column}; {self.seat_id}"

    def __find_column(self) -> int:
        return BoardingPass.__binary_search(self.column_data, end=7, lower_letter="L")

    def __find_row(self) -> int:
        return BoardingPass.__binary_search(self.row_data, end=127, lower_letter="F")

    def __seat_id(self) -> int:
        return self.row * 8 + self.column

    @staticmethod
    def __binary_search(text: str, end: int, lower_letter: str) -> int:
        start = 0

        for letter in text:
            if letter == lower_letter:
                end = ((start + end + 1) // 2) - 1
            else:
                start = ((start + end + 1) // 2)

        return start


def solve_1():
    print(boarding_passes[0].seat_id)


def solve_2():
    all_seat_ids = [x.seat_id for x in boarding_passes]
    my_seat = 0
    for i in range(1, len(all_seat_ids)):
        if all_seat_ids[i - 1] - all_seat_ids[i] != 1:
            my_seat = all_seat_ids[i - 1] - 1
            break

    print(my_seat)


boarding_passes = list(map(BoardingPass, input_data))
boarding_passes.sort(reverse=True, key=lambda x: x.column_data)
boarding_passes.sort(key=lambda x: x.row_data)

solve_1()
solve_2()
