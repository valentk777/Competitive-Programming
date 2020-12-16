from typing import List

from utils import read_lines

input_data = read_lines()


def find_solution(data: List[int], number_of_iterations: int) -> int:
    n = len(data)
    d = {data[number - 1]: number for number in range(1, n)}

    current = data[-1]
    count = n
    while count != number_of_iterations:
        if current not in d.keys():
            d[current] = count
            current = 0
        else:
            new_current = count - d[current]
            d[current] = count
            current = new_current
        count += 1
    return current


def solve_1(data: List[int]):
    result = find_solution(data, 2020)
    print(result)


def solve_2(data: List[int]):
    result = find_solution(data, 30000000)
    print(result)


input_data = list(map(int, input_data[0].split(',')))

solve_1(input_data)
solve_2(input_data)
