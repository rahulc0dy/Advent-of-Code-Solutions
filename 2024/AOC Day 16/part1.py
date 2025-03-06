"""--- Day 16: Reindeer Maze ---
It's time again for the Reindeer Olympics! This year, the big event is the Reindeer Maze, where the Reindeer compete for the lowest score.

You and The Historians arrive to search for the Chief right as the event is about to start. It wouldn't hurt to watch a little, right?

The Reindeer start on the Start Tile (marked S) facing East and need to reach the End Tile (marked E). They can move forward one tile at a time (increasing their score by 1 point), but never into a wall (#). They can also rotate clockwise or counterclockwise 90 degrees at a time (increasing their score by 1000 points).

To figure out the best place to sit, you start by grabbing a map (your puzzle input) from a nearby kiosk. For example:

###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############
There are many paths through this maze, but taking any of the best paths would incur a score of only 7036. This can be achieved by taking a total of 36 steps forward and turning 90 degrees a total of 7 times:


###############
#.......#....E#
#.#.###.#.###^#
#.....#.#...#^#
#.###.#####.#^#
#.#.#.......#^#
#.#.#####.###^#
#..>>>>>>>>v#^#
###^#.#####v#^#
#>>^#.....#v#^#
#^#.#.###.#v#^#
#^....#...#v#^#
#^###.#.#.#v#^#
#S..#.....#>>^#
###############
Here's a second example:

#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################
In this maze, the best paths cost 11048 points; following one such path would look like this:

#################
#...#...#...#..E#
#.#.#.#.#.#.#.#^#
#.#.#.#...#...#^#
#.#.#.#.###.#.#^#
#>>v#.#.#.....#^#
#^#v#.#.#.#####^#
#^#v..#.#.#>>>>^#
#^#v#####.#^###.#
#^#v#..>>>>^#...#
#^#v###^#####.###
#^#v#>>^#.....#.#
#^#v#^#####.###.#
#^#v#^........#.#
#^#v#^#########.#
#S#>>^..........#
#################
Note that the path shown above includes one 90 degree turn as the very first move, rotating the Reindeer from facing East to facing North.

Analyze your map carefully. What is the lowest score a Reindeer could possibly get?"""

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
