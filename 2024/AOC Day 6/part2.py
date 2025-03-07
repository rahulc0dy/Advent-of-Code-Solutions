# https://adventofcode.com/2024/day/6#part2


def simulate(candidate, grid, start, initial_dir):
    R, C = len(grid), len(grid[0])
    pos = start
    d = initial_dir
    visited = set()
    while True:
        state = (pos, d)
        if state in visited:
            return True
        visited.add(state)
        next_i = pos[0] + d[0]
        next_j = pos[1] + d[1]
        next_pos = (next_i, next_j)
        if not (0 <= next_i < R and 0 <= next_j < C):
            return False
        if grid[next_i][next_j] == "#" or next_pos == candidate:
            d = (d[1], -d[0])
        else:
            pos = next_pos


with open("input.txt", "r") as f:
    grid = [list(line.rstrip("\n")) for line in f]

guard_start = None
for i, row in enumerate(grid):
    for j, ch in enumerate(row):
        if ch == "^":
            guard_start = (i, j)
            grid[i][j] = "."
            break
    if guard_start is not None:
        break

initial_dir = (-1, 0)
R, C = len(grid), len(grid[0])
valid_count = 0
for i in range(R):
    for j in range(C):
        if grid[i][j] == "." and (i, j) != guard_start:
            if simulate((i, j), grid, guard_start, initial_dir):
                valid_count += 1

print(valid_count)
