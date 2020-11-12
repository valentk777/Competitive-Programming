# -----------------------------------------------------------
# URL    : https://www.codewars.com/kata/5296bc77afba8baa690002d7
# Notes  : tag-codewars
# -----------------------------------------------------------

def get_line(board, line):
    return board[line]


def get_columns(board, column):
    return list(zip(*board))[column]


def get_box(board, line, column):
    line -= line % 3
    column -= column % 3
    return board[line][column:column + 3] + board[line + 1][column:column + 3] + board[line + 2][column:column + 3]


def get_options(board, line, column):
    options = [p for p in range(1, 10) if p not in get_line(board, line) and p not in get_columns(board, column)
               and p not in get_box(board, line, column)]
    return options[0] if len(options) == 1 else 0


def validate(puzzle):
    changes = False
    for i in range(0, 9):
        for j in range(0, 9):
            if puzzle[i][j] == 0:
                option = get_options(puzzle, i, j)
                if option != 0:
                    puzzle[i][j] = option
                    changes = True
    return puzzle, changes


def sudoku(puzzle):
    changes = True
    while changes:
        puzzle, changes = validate(puzzle)

    return puzzle
