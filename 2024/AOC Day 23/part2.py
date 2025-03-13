# https://adventofcode.com/2024/day/23#part2


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


def bron_kerbosch(R, P, X, graph, cliques):
    if not P and not X:
        cliques.append(R)
        return
    for v in list(P):
        bron_kerbosch(
            R.union({v}),
            P.intersection(graph[v]),
            X.intersection(graph[v]),
            graph,
            cliques,
        )
        P.remove(v)
        X.add(v)


def find_maximum_clique(graph):
    cliques = []
    nodes = set(graph.keys())
    bron_kerbosch(set(), nodes, set(), graph, cliques)
    max_clique = max(cliques, key=len) if cliques else set()
    return max_clique


graph = read_graph("input.txt")

max_clique = find_maximum_clique(graph)

password = ",".join(sorted(max_clique))

print(f"{ password }")
