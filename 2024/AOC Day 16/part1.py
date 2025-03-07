# https://adventofcode.com/2024/day/16

import heapq


def solve_maze(maze):
    start = end = None
    for i, x_pos in enumerate(maze):
        for j, cell in enumerate(x_pos):
            if cell == "S":
                start = (i, j)
            elif cell == "E":
                end = (i, j)
    if start is None or end is None:
        raise ValueError("No start or end found.")

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    init_direction = 1

    start_state = (start[0], start[1], init_direction)

    height = len(maze)
    width = len(maze[0])

    heap = [(0, start_state[0], start_state[1], start_state[2])]

    best_cost = {}
    best_cost[start_state] = 0

    while heap:
        cost, x_pos, y_pos, direction = heapq.heappop(heap)

        if cost > best_cost.get((x_pos, y_pos, direction), float("inf")):
            continue

        if (x_pos, y_pos) == end:
            return cost

        dy, dx = directions[direction]
        new_y, new_x = x_pos + dy, y_pos + dx
        if 0 <= new_y < height and 0 <= new_x < width and maze[new_y][new_x] != "#":
            next_state = (new_y, new_x, direction)
            new_cost = cost + 1
            if new_cost < best_cost.get(next_state, float("inf")):
                best_cost[next_state] = new_cost
                heapq.heappush(heap, (new_cost, new_y, new_x, direction))

        left_d = (direction - 1) % 4
        next_state = (x_pos, y_pos, left_d)
        new_cost = cost + 1000
        if new_cost < best_cost.get(next_state, float("inf")):
            best_cost[next_state] = new_cost
            heapq.heappush(heap, (new_cost, x_pos, y_pos, left_d))

        right_d = (direction + 1) % 4
        next_state = (x_pos, y_pos, right_d)
        new_cost = cost + 1000
        if new_cost < best_cost.get(next_state, float("inf")):
            best_cost[next_state] = new_cost
            heapq.heappush(heap, (new_cost, x_pos, y_pos, right_d))

    return None


maze = []
with open("input.txt", "r") as file:
    for line in file:
        maze.append(list(line.strip()))

lowest_score = solve_maze(maze)
print(f"{ lowest_score = }")
