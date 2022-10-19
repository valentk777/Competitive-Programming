# -----------------------------------------------------------
# URL    : https://www.codewars.com/kata/529bf0e9bdf7657179000008
# Notes  : tag-codewars, tag-kyu-4
# -----------------------------------------------------------

def valid_solution(board):
    for line in board:
        if sum(line) != 45:
            return False

    for x in range(1, 9, 3):
        lines = board[x - 1:x + 2]
        for y in range(1, 9, 3):
            if sum(lines[0][y - 1:y + 2] + lines[1][y - 1:y + 2] + lines[2][y - 1:y + 2]) != 45:
                return False

    for c in range(0, 9):
        if sum(x[c] for x in board) != 45:
            return False

    return True
