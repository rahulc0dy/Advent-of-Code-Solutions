'''
--- Part Two ---
The Elf looks quizzically at you. Did you misunderstand the assignment?

Looking for the instructions, you flip over the word search to find that this isn't actually an XMAS puzzle; it's an X-MAS puzzle in which you're supposed to find two MAS in the shape of an X. One way to achieve that is like this:

M.S
.A.
M.S
Irrelevant characters have again been replaced with . in the above diagram. Within the X, each MAS can be written forwards or backwards.

Here's the same example from before, but this time all of the X-MASes have been kept instead:

.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........
In this example, an X-MAS appears 9 times.

Flip the word search from the instructions back over to the word search side and try again. How many times does an X-MAS appear?
'''

import numpy as np

def read_grid_from_file(filename):
    with open(filename, 'r') as f:
        grid = [list(line.strip()) for line in f.readlines()]
    return np.array(grid)

def count_xmas_x_shapes(grid):
    count = 0
    rows, cols = grid.shape

    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            if grid[r, c] == 'A':
                diag1 = [grid[r - 1, c - 1], grid[r + 1, c + 1]] 
                diag2 = [grid[r - 1, c + 1], grid[r + 1, c - 1]]

                if (diag1 == ['M', 'S'] or diag1 == ['S', 'M']) and (diag2 == ['S', 'M'] or diag2 == ['M', 'S']):
                    count += 1
    return count

grid = read_grid_from_file("input.txt")

print("Part 2: Number of 'X-MAS' occurrences:", count_xmas_x_shapes(grid))
