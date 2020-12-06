from utils import read_lines

input_data = read_lines()


def get_tree_count_for_slope(right: int, down: int) -> int:
    line_max = len(input_data)
    column_max = len(input_data[0])
    line = 0
    column = 0
    count_tree = 0
    while line < line_max:
        if input_data[line][column] == '#':
            count_tree += 1
        line += down
        column = (column + right) % column_max
    return count_tree


def solve_1() -> None:
    result = get_tree_count_for_slope(3, 1)
    print(result)


def solve_2() -> None:
    result = (get_tree_count_for_slope(1, 1)
              * get_tree_count_for_slope(3, 1)
              * get_tree_count_for_slope(5, 1)
              * get_tree_count_for_slope(7, 1)
              * get_tree_count_for_slope(1, 2))
    print(result)


solve_1()
solve_2()
