"""
--- Part Two ---
Now that you know what the best paths look like, you can figure out the best spot to sit.

Every non-wall tile (S, ., or E) is equipped with places to sit along the edges of the tile. While determining which of these tiles would be the best spot to sit depends on a whole bunch of factors (how comfortable the seats are, how far away the bathrooms are, whether there's a pillar blocking your view, etc.), the most important factor is whether the tile is on one of the best paths through the maze. If you sit somewhere else, you'd miss all the action!

So, you'll need to determine which tiles are part of any best path through the maze, including the S and E tiles.

In the first example, there are 45 tiles (marked O) that are part of at least one of the various best paths through the maze:

###############
#.......#....O#
#.#.###.#.###O#
#.....#.#...#O#
#.###.#####.#O#
#.#.#.......#O#
#.#.#####.###O#
#..OOOOOOOOO#O#
###O#O#####O#O#
#OOO#O....#O#O#
#O#O#O###.#O#O#
#OOOOO#...#O#O#
#O###.#.#.#O#O#
#O..#.....#OOO#
###############
In the second example, there are 64 tiles that are part of at least one of the best paths:

#################
#...#...#...#..O#
#.#.#.#.#.#.#.#O#
#.#.#.#...#...#O#
#.#.#.#.###.#.#O#
#OOO#.#.#.....#O#
#O#O#.#.#.#####O#
#O#O..#.#.#OOOOO#
#O#O#####.#O###O#
#O#O#..OOOOO#OOO#
#O#O###O#####O###
#O#O#OOO#..OOO#.#
#O#O#O#####O###.#
#O#O#OOOOOOO..#.#
#O#O#O#########.#
#O#OOO..........#
#################
Analyze your map further. How many tiles are part of at least one of the best paths through the maze?
"""

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
