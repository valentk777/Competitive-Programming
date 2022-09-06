# -----------------------------------------------------------
# URL    : https://www.codewars.com/kata/52bef5e3588c56132c0003bc
# Notes  : tag-codewars
# -----------------------------------------------------------

class Node:
    def __init__(self, left, right, value):
        self.left = left
        self.right = right
        self.value = value


def tree_by_levels(node: Node):
    def find(_node: Node, level: str):
        if _node.left is not None and _node.right is not None:
            return find(_node.left, level + "L") + find(_node.right, level + "R") + [(_node.value, level)]

        elif _node.left is not None:
            return find(_node.left, level + "L") + [(_node.value, level)]

        elif _node.right is not None:
            return find(_node.right, level + "R") + [(_node.value, level)]
        else:
            return [(_node.value, level)]

    if node is None:
        return []

    nodes_l = []
    nodes_r = []

    if node.left is not None:
        nodes_l = find(node.left, "L")

    if node.right is not None:
        nodes_r = find(node.right, "R")

    result = [(node.value, "B")] + nodes_l + nodes_r
    result = sorted(result, key=lambda tup: (len(tup[1]), tup[1]))
    result = list(map(lambda x: x[0], result))
    print(result)
    return result


# samuel.vieyra@bbva.com solution
def tree_by_levels(node):
    p, q = [], [node]

    while q:
        v = q.pop(0)

        if v is not None:
            p.append(v.value)
            q += [v.left, v.right]

    return p if not node is None else []


# suic solution
from collections import deque


def tree_by_levels(node):
    if not node:
        return []

    res, queue = [], deque([node, ])

    while queue:
        n = queue.popleft()
        res.append(n.value)

        if n.left is not None:
            queue.append(n.left)

        if n.right is not None:
            queue.append(n.right)

    return res
