# -----------------------------------------------------------
# URL    : https://codeforces.com/gym/100781
# Title  : Adjoin the Networks
# Notes  : tag-codeforces, tag-problem-A, tag-not-pass
# -----------------------------------------------------------

# ---------------------------------------------------Shared part--------------------------------------------------------
import collections
import os
import time
from collections import defaultdict
from sys import stdin, maxsize

inp = lambda: stdin.readline().strip()
iinp = lambda: int(inp())
intl = lambda: list(map(int, inp().split()))
strl = lambda: list(inp().split())
list_to_string = lambda _a: " ".join(map(str, _a))
_dp = lambda default_value: defaultdict(lambda: default_value)

MOD = 10 ** 9 + 7
INF = maxsize


# -------------------------------------------------------Solution-------------------------------------------------------

def connected_components(edges):
    # build the graph
    neighbors = collections.defaultdict(set)

    for u, v in edges:
        neighbors[u].add(v)
        neighbors[v].add(u)

    # traverse the graph
    sizes = []
    visited = set()
    graphs = []

    for u in neighbors.keys():
        graph = []

        if u in visited:
            continue

        # visit the component that includes u
        size = 0
        agenda = {u}

        while agenda:
            v = agenda.pop()
            visited.add(v)
            graph.append(v)
            size += 1
            agenda.update(neighbors[v] - visited)
        sizes.append(size)
        graphs.append(graph)

    return graphs, sizes


def bfs(graph, root):
    maxdepth = 0
    visited = []
    queue = []
    visited.append(root)
    queue.append((root, 1))
    while queue:
        x, depth = queue.pop(0)
        maxdepth = max(maxdepth, depth)
        # print(x)
        for child in graph[x]:
            if child not in visited:
                visited.append(child)
                queue.append((child, depth + 1))
    return maxdepth


def solve():
    c, l = intl()
    original_graph = {i: [] for i in range(c)}
    edges = [[i, i] for i in range(c)]

    for i in range(l):
        a, b = intl()
        edges.append([a, b])
        original_graph[a].append(b)
        original_graph[b].append(a)

    graphs, sizes = connected_components(edges)

    _mins = []
    _maxs = []

    for graph in graphs:
        _min = INF
        _max = -INF

        for node in graph:
            result = bfs(original_graph, node)

            if result < _min:
                _min = result

            if result > _max:
                _max = result

        _mins.append(_min - 1)
        _maxs.append(_max - 1)

    _main = max(_maxs)
    _maxs.remove(_main)

    if max(_maxs) + 1 > _main:
        return _main + 1
    else:
        return _main


def run():
    print(solve())


if __name__ == "__main__":
    if os.environ.get("DEBUG_CODEFORCES"):
        stdin = open("../../input.txt", "r")
        start_time = time.time()
        run()
        print("\n--- %s seconds ---\n" % (time.time() - start_time))
    else:
        run()
