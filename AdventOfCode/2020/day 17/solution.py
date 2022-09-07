# -----------------------------------------------------------
# Notes  : tag-adventOfCode
# -----------------------------------------------------------


from typing import List

from utils import read_lines

input_data = read_lines()


def check_status(point, count, grid):
    return (point in grid and 3 <= count <= 4) or (point not in grid and count == 3)


def get_neighbours(x: int, y: int, z: int, w: int = None):
    for _x in range(x - 1, x + 2):
        for _y in range(y - 1, y + 2):
            for _z in range(z - 1, z + 2):
                if w is not None:
                    for _w in range(w - 1, w + 2):
                        yield _x, _y, _z, _w
                else:
                    yield _x, _y, _z


def get_grid(data: List[str], dimension: int):
    if dimension == 3:
        return set((x, y, 0)
                   for y, line in enumerate(data)
                   for x, value in enumerate(line)
                   if value == '#')
    elif dimension == 4:
        return set((x, y, 0, 0)
                   for y, line in enumerate(data)
                   for x, value in enumerate(line)
                   if value == '#')


def generate_coordinates(cycle: int, width: int, iteration: int):
    for z in range(-cycle, cycle + 1):
        for y in range(-cycle, width + cycle + 1):
            for x in range(-cycle, width + cycle + 1):
                if iteration == 3:
                    yield x, y, z
                else:
                    for w in range(-cycle, cycle + 1):
                        yield x, y, z, w


def filter_based_on_status(grid):
    def step(data):
        count = sum(1 for point in get_neighbours(*data) if point in grid)
        return check_status(data, count, grid)

    return step


def solve_1(grid, width: int):
    for cycle in range(1, 7):
        grid = set(filter(filter_based_on_status(grid), generate_coordinates(cycle, width, 3)))

    print(len(grid))


def solve_2(grid, width: int):
    for cycle in range(1, 7):
        grid = set(filter(filter_based_on_status(grid), generate_coordinates(cycle, width, 4)))

    print(len(grid))


solve_1(get_grid(input_data, 3), len(input_data))
solve_2(get_grid(input_data, 4), len(input_data))
