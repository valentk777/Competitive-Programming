# -----------------------------------------------------------
# URL    : https://www.codewars.com/kata/57ff9d3b8f7dda23130015f
# Notes  : tag-codewars, tag-not-pass
# -----------------------------------------------------------

from typing import List


class Square:
    def __init__(self, row, column, value):
        self.row = row
        self.column = column
        self.value = value

    def __str__(self):
        return f"row = {self.row}; column = {self.column}; value = {self.value}; "


class Map:
    def __init__(self, _map, mines):
        self.total_mines: int = mines
        self.mines_left: int = mines
        self.map: str = _map
        # [row][column]
        self.grid: List[List[Square]] = [[Square(i, j, e) for j, e in enumerate(line.split(" "))] for i, line in
                                         enumerate(_map.split("\n"))]
        self.row_length = len(self.grid[0])
        self.column_length = len(self.grid)
        self.current: Square = self.find_zero()

    def find_zero(self) -> Square:
        for row in self.grid:
            for element in row:
                if element.value == '0':
                    return element

    # def uncover_right(self):
    #     if self.current.row + 1 <
    #
    # def uncover_all_around(self):
    #     if self.current.row + 1 <


    def __str__(self):
        result = ""

        for row in self.grid:
            for element in row:
                result += f"{element.value} "

            result = result.strip()
            result += "\n"

        return result


def solve_mine(_map, n):
    game_map = Map(_map, n)

    while True:
        if game_map.current.value == '0':
            game_map.uncover_all_around()

    print(game_map)
    print(game_map.current)
    # while True:
    #     open(0, 0)
    #     print(open(0, 0))
    #     print()
    #     break
    return '?'


gamemap = """
? ? ? ? ? ?
? ? ? ? ? ?
? ? ? 0 ? ?
? ? ? ? ? ?
? ? ? ? ? ?
0 0 0 ? ? ?
""".strip()

solve_mine(gamemap, 4)
