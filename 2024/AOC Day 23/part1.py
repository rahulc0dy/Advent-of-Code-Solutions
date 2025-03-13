# https://adventofcode.com/2024/day/23

import itertools


def read_graph(file_path):
    graph = {}
    with open(file_path, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            a, b = line.split("-")
            if a not in graph:
                graph[a] = set()
            if b not in graph:
                graph[b] = set()
            graph[a].add(b)
            graph[b].add(a)
    return graph


def count_triangles_with_t(graph):
    nodes = list(graph.keys())
    count = 0
    triangles_with_t = []
    for combo in itertools.combinations(nodes, 3):
        a, b, c = combo
        if b in graph[a] and c in graph[a] and c in graph[b]:
            if any(node.startswith("t") for node in combo):
                count += 1
                triangles_with_t.append(combo)
    return count, triangles_with_t


file_path = "input.txt"
try:
    graph = read_graph(file_path)
except FileNotFoundError:
    print(f"Error: {file_path} not found.")

triangle_count, triangles = count_triangles_with_t(graph)
print(f"{ triangle_count = }")
