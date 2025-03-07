# https://adventofcode.com/2024/day/4

import numpy as np


def read_grid_from_file(filename):
    with open(filename, "r") as f:
        grid = [list(line.strip()) for line in f.readlines()]
    return np.array(grid)


def count_xmas_occurrences(grid):
    word = "XMAS"
    word_len = len(word)
    count = 0
    rows, cols = grid.shape

    directions = [
        (0, 1),  # Right
        (1, 0),  # Down
        (0, -1),  # Left
        (-1, 0),  # Up
        (1, 1),  # Down-Right
        (1, -1),  # Down-Left
        (-1, 1),  # Up-Right
        (-1, -1),  # Up-Left
    ]

    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                if (
                    0 <= r + (word_len - 1) * dr < rows
                    and 0 <= c + (word_len - 1) * dc < cols
                ):
                    match = True
                    for i in range(word_len):
                        if grid[r + i * dr, c + i * dc] != word[i]:
                            match = False
                            break
                    if match:
                        count += 1
    return count


grid = read_grid_from_file("input.txt")

print("Part 1: Number of 'XMAS' occurrences:", count_xmas_occurrences(grid))
