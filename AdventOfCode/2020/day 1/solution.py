# -----------------------------------------------------------
# Notes  : tag-adventOfCode
# -----------------------------------------------------------


from utils import read_lines, to_int

input_data = to_int(read_lines())
n = len(input_data)


def solve_1():
    for i in range(n):
        for j in range(i + 1, n):
            if input_data[i] + input_data[j] == 2020:
                print(input_data[i] * input_data[j])


def solve_2():
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if input_data[i] + input_data[j] + input_data[k] == 2020:
                    print(input_data[i] * input_data[j] * input_data[k])


solve_1()
solve_2()
