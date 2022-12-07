# ---------------------------------------------------------------------------------------
# URL    : https://adventofcode.com/2022/day/7
# Title  : No Space Left On Device
# Tags   : tag-adventofcode, tag-not-pass
# ---------------------------------------------------------------------------------------

# region --------------------------------------------Shared part--------------------------------------------------------

import math
import sys
from collections import defaultdict, Counter

from bigtree import Node, findall, tree_to_dict, print_tree

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

def get_all_dir_sizes(data):
    tree_dict = tree_to_dict(data, all_attrs=True)
    all_dirs_sizes = []
    for name, value in tree_dict.items():
        if "dir_" in name.split("/")[-1]:
            all_dirs_sizes.append(value["size"])
    return all_dirs_sizes


def get_file_graph(data):
    c_cd = "$ cd "
    c_ls = "$ ls"

    root = Node("dir_base", size=0)
    current_node = root
    n = len(data)
    i = 0

    while i < n:
        line = data[i]

        if c_cd in line:
            dir_name = line.replace(c_cd, "")

            if dir_name == "/":
                current_node = root
            elif dir_name == "..":
                current_node = current_node.parent
            else:
                nodes = findall(current_node, lambda _node: _node.name == f"dir_{dir_name}")

                if len(nodes) == 1:
                    current_node = nodes[0]
                else:
                    for node in nodes:
                        if node.parent == current_node:
                            current_node = node
                            break

        elif "$" not in line:
            indicator, name = line.split()

            if indicator == "dir":
                size = 0
                name = f"dir_{name}"
            else:
                size = int(indicator)

            Node(name, size=size, parent=current_node)
            current_node.size += size

            parent = current_node.parent

            while parent is not None:
                parent.size += size
                parent = parent.parent

        elif c_ls == line:
            pass

        i += 1

    return root


def solve_1(data) -> None:
    all_dirs_sizes = get_all_dir_sizes(data)
    all_dirs_sizes = filter(lambda x: x <= 100000, all_dirs_sizes)
    print(sum(all_dirs_sizes))


def solve_2(data) -> None:
    all_dirs_sizes = sorted(get_all_dir_sizes(data))
    used = all_dirs_sizes[-1]
    unused = 70000000 - used
    missing = 30000000 - unused

    all_dirs_sizes = list(filter(lambda x: x >= missing, all_dirs_sizes))
    print(all_dirs_sizes[0])


if __name__ == "__main__":
    input_data = read_lines()
    input_data = get_file_graph(input_data)
    print_tree(input_data, attr_list=["size"])

    solve_1(input_data.copy())
    solve_2(input_data.copy())
