# https://adventofcode.com/2024/day/15

with open("input.txt", "r") as f:
    lines = f.read().splitlines()
    grid_lines = []
    moves_lines = []
    reading_moves = False
    for line in lines:
        if line.strip() == "":
            reading_moves = True
            continue
        if not reading_moves:
            grid_lines.append(line)
        else:
            moves_lines.append(line)


grid = [list(line) for line in grid_lines]
moves = "".join(moves_lines)


def find_robot(grid):
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == "@":
                return i, j
    return None


def simulate_moves(grid, moves, robot):
    direction = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}
    r, c = robot
    rows = len(grid)
    cols = len(grid[0])

    for move in moves:
        if move not in direction:
            continue
        dx, dy = direction[move]
        new_r, new_c = r + dx, c + dy

        if grid[new_r][new_c] == "#":
            continue

        if grid[new_r][new_c] == ".":
            grid[r][c] = "."
            grid[new_r][new_c] = "@"
            r, c = new_r, new_c
            continue

        if grid[new_r][new_c] == "O":
            chain = []
            cur_r, cur_c = new_r, new_c
            while grid[cur_r][cur_c] == "O":
                chain.append((cur_r, cur_c))
                cur_r += dx
                cur_c += dy
            if grid[cur_r][cur_c] == "#" or not (
                0 <= cur_r < rows and 0 <= cur_c < cols
            ):
                continue
            for box_r, box_c in reversed(chain):
                grid[box_r + dx][box_c + dy] = "O"
                grid[box_r][box_c] = "."
            grid[r][c] = "."
            grid[new_r][new_c] = "@"
            r, c = new_r, new_c
    return (r, c)


def compute_gps_sum(grid):
    total = 0
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == "O":
                total += 100 * i + j
    return total


robot = find_robot(grid)
if robot is None:
    print("No robot found in the grid.")
simulate_moves(grid, moves, robot)
result = compute_gps_sum(grid)
print(result)
