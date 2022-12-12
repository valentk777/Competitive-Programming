# ---------------------------------------------------------------------------------------
# URL    : https://adventofcode.com/2022/day/12
# Title  : Hill Climbing Algorithm
# Tags   : tag-adventofcode, tag-not-pass
# ---------------------------------------------------------------------------------------

# region --------------------------------------------Shared part--------------------------------------------------------
import copy
import math
import sys
from collections import defaultdict, Counter

from utils import read_lines

list_to_string = lambda _a: "".join(map(str, _a))
list_to_string_list = lambda _a: " ".join(map(str, _a))
_dp = lambda default_value: defaultdict(lambda: default_value)
fact = lambda number: math.factorial(number)
cnt = lambda _a: Counter(_a)


def lcm(a, b):
    return a * b // math.gcd(a, b)


def print_dp(_dict):
    for item in _dict.items():
        print(f"{item[0]} = {item[1]}")


MOD = 10 ** 9 + 7
INF = sys.maxsize
A = 911382323
M = 9999999999879998


# endregion

# -------------------------------------------------------Solution-------------------------------------------------------

class Node:
    def __init__(self, x, y, distance, value):
        self.x = x
        self.y = y
        self.distance_from_source = distance
        self.value = value

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.distance_from_source == other.distance_from_source

    def __str__(self):
        return f"x = {self.x}, y= {self.y}, dist={self.distance_from_source}, value = {self.value}"


def find_start_end_node_v1(data):
    start_node = Node(0, 0, 0, 0)
    end_node = Node(0, 0, 0, 0)

    for i in range(len(data)):
        line = data[i]

        for j in range(len(line)):
            element = line[j]

            if element == ord("S"):
                start_node = Node(i, j, 0, ord("a") - 1)
                data[i][j] = ord("a") - 1

            if element == ord("E"):
                end_node = Node(i, j, 0, ord("z") + 1)
                data[i][j] = ord("z") + 1

    return data, start_node, end_node


def find_only_end_node(data):
    end_node = Node(0, 0, 0, 0)

    for i in range(len(data)):
        line = data[i]

        for j in range(len(line)):
            element = line[j]

            if element == ord("S"):
                data[i][j] = ord("a")

            if element == ord("E"):
                end_node = Node(i, j, 0, ord("z") + 1)
                data[i][j] = ord("z") + 1

    return data, end_node


def add_neighbours(node, data, num_of_rows, num_of_columns):
    neighbours = []

    if (0 <= node.x - 1 < num_of_rows) and data[node.x - 1][node.y] - node.value <= 1:
        neighbours.append(Node(node.x - 1, node.y, node.distance_from_source + 1, data[node.x - 1][node.y]))
    if (0 <= node.x + 1 < num_of_rows) and data[node.x + 1][node.y] - node.value <= 1:
        neighbours.append(Node(node.x + 1, node.y, node.distance_from_source + 1, data[node.x + 1][node.y]))
    if (0 <= node.y - 1 < num_of_columns) and data[node.x][node.y - 1] - node.value <= 1:
        neighbours.append(Node(node.x, node.y - 1, node.distance_from_source + 1, data[node.x][node.y - 1]))
    if (0 <= node.y + 1 < num_of_columns) and data[node.x][node.y + 1] - node.value <= 1:
        neighbours.append(Node(node.x, node.y + 1, node.distance_from_source + 1, data[node.x][node.y + 1]))

    return neighbours


def get_all_start_nodes(data):
    start_nodes = []

    for i in range(len(data)):
        line = data[i]

        for j in range(len(line)):
            element = line[j]

            if element == ord("a"):
                start_nodes.append(Node(i, j, 0, element))

    return start_nodes


def solve_1(data) -> None:
    data, start_node, end_node = find_start_end_node_v1(data)
    num_of_rows = len(data)
    num_of_columns = len(data[0])
    queue = [start_node]

    while queue != []:
        node = queue[0]
        queue.remove(node)

        if data[node.x][node.y] == end_node.value:
            print(node.distance_from_source)
            return node.distance_from_source

        data[node.x][node.y] = 0

        if node.distance_from_source > num_of_rows * num_of_columns + 5:
            continue

        neighbours = add_neighbours(node, data, num_of_rows, num_of_columns)

        for n in neighbours:
            if n not in queue and n.value != 0:
                queue.append(n)

    print("End")


def solve_2(data) -> None:
    data, end_node = find_only_end_node(data)
    num_of_rows = len(data)
    num_of_columns = len(data[0])
    start_nodes = get_all_start_nodes(data)
    candidates = []

    for start_node in start_nodes:
        new_data = copy.deepcopy(data)
        queue = [start_node]

        while queue != []:
            node = queue[0]
            queue.remove(node)

            if new_data[node.x][node.y] == end_node.value:
                candidates.append(node.distance_from_source)
                break

            new_data[node.x][node.y] = 0

            if node.distance_from_source > num_of_rows * num_of_columns + 5:
                continue

            neighbours = add_neighbours(node, new_data, num_of_rows, num_of_columns)

            for n in neighbours:
                if n not in queue and n.value != 0:
                    queue.append(n)

        candidates = [min(candidates)]

    print(min(candidates))


if __name__ == "__main__":
    input_data = read_lines()

    solve_1(list(map(lambda x: list(map(lambda y: ord(y), x)), input_data)))
    solve_2(list(map(lambda x: list(map(lambda y: ord(y), x)), input_data)))
