# https://adventofcode.com/2024/day/17#part2

import heapq
from collections import defaultdict

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

TURN_COST = 1000
FORWARD_COST = 1


def read_maze(filename):
    with open(filename, "r") as f:
        grid = [line.rstrip("\n") for line in f if line.strip()]
    start = end = None
    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch == "S":
                start = (r, c)
            elif ch == "E":
                end = (r, c)
    return grid, start, end


def dijkstra(grid, start, end):
    R, C = len(grid), len(grid[0])
    start_state = (start[0], start[1], 1)

    dist = defaultdict(lambda: float("inf"))
    dist[start_state] = 0
    pred = defaultdict(list)

    heap = [(0, start_state)]

    while heap:
        cost, (r, c, d) = heapq.heappop(heap)
        if cost != dist[(r, c, d)]:
            continue
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] != "#":
            nstate = (nr, nc, d)
            new_cost = cost + FORWARD_COST
            if new_cost < dist[nstate]:
                dist[nstate] = new_cost
                pred[nstate] = [(r, c, d)]
                heapq.heappush(heap, (new_cost, nstate))
            elif new_cost == dist[nstate]:
                pred[nstate].append((r, c, d))
        for nd in [(d - 1) % 4, (d + 1) % 4]:
            nstate = (r, c, nd)
            new_cost = cost + TURN_COST
            if new_cost < dist[nstate]:
                dist[nstate] = new_cost
                pred[nstate] = [(r, c, d)]
                heapq.heappush(heap, (new_cost, nstate))
            elif new_cost == dist[nstate]:
                pred[nstate].append((r, c, d))

    best = float("inf")
    goal_states = []
    for (r, c, d), cst in dist.items():
        if grid[r][c] == "E":
            if cst < best:
                best = cst
                goal_states = [(r, c, d)]
            elif cst == best:
                goal_states.append((r, c, d))
    return pred, goal_states


def collect_optimal_tiles(pred, goal_states):
    visited = set()
    stack = list(goal_states)
    while stack:
        state = stack.pop()
        if state in visited:
            continue
        visited.add(state)
        for pstate in pred.get(state, []):
            if pstate not in visited:
                stack.append(pstate)
    tiles = {(r, c) for (r, c, d) in visited}
    return tiles


grid, start, end = read_maze("input.txt")
pred, goal_states = dijkstra(grid, start, end)
opt_tiles = collect_optimal_tiles(pred, goal_states)
print("Number of tiles that are part of at least one best path:", len(opt_tiles))
