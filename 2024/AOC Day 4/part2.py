# https://adventofcode.com/2024/day/4#part2

import numpy as np


def read_grid_from_file(filename):
    with open(filename, "r") as f:
        grid = [list(line.strip()) for line in f.readlines()]
    return np.array(grid)


def count_xmas_x_shapes(grid):
    count = 0
    rows, cols = grid.shape

    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            if grid[r, c] == "A":
                diag1 = [grid[r - 1, c - 1], grid[r + 1, c + 1]]
                diag2 = [grid[r - 1, c + 1], grid[r + 1, c - 1]]

                if (diag1 == ["M", "S"] or diag1 == ["S", "M"]) and (
                    diag2 == ["S", "M"] or diag2 == ["M", "S"]
                ):
                    count += 1
    return count


grid = read_grid_from_file("input.txt")

print("Part 2: Number of 'X-MAS' occurrences:", count_xmas_x_shapes(grid))
