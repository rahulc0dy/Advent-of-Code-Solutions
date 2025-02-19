'''
--- Part One ---
"Looks like the Chief's not here. Next!" One of The Historians pulls out a device and pushes the only button on it. After a brief flash, you recognize the interior of the Ceres monitoring station!

As the search for the Chief continues, a small Elf who lives on the station tugs on your shirt; she'd like to know if you could help her with her word search (your puzzle input). She only has to find one word: XMAS.

This word search allows words to be horizontal, vertical, diagonal, written backwards, or even overlapping other words. It's a little unusual, though, as you don't merely need to find one instance of XMAS - you need to find all of them. Here are a few ways XMAS might appear, where irrelevant characters have been replaced with .:


..X...
.SAMX.
.A..A.
XMAS.S
.X....
The actual word search will be full of letters instead. For example:

MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
In this word search, XMAS occurs a total of 18 times; here's the same word search again, but where letters not involved in any XMAS have been replaced with .:

....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX
Take a look at the little Elf's word search. How many times does XMAS appear?
'''

import numpy as np

def read_grid_from_file(filename):
    with open(filename, 'r') as f:
        grid = [list(line.strip()) for line in f.readlines()]
    return np.array(grid)

def count_xmas_occurrences(grid):
    word = "XMAS"
    word_len = len(word)
    count = 0
    rows, cols = grid.shape

    directions = [
        (0, 1),   # Right
        (1, 0),   # Down
        (0, -1),  # Left
        (-1, 0),  # Up
        (1, 1),   # Down-Right
        (1, -1),  # Down-Left
        (-1, 1),  # Up-Right
        (-1, -1)  # Up-Left
    ]

    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                if 0 <= r + (word_len - 1) * dr < rows and 0 <= c + (word_len - 1) * dc < cols:
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
