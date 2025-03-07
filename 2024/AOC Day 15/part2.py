# https://adventofcode.com/2024/day/15#part2

with open("input.txt") as f:
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
moves = "".join(moves_lines)
grid = []
for line in grid_lines:
    new_line = ""
    for ch in line:
        if ch == "#":
            new_line += "##"
        elif ch == "O":
            new_line += "[]"
        elif ch == ".":
            new_line += ".."
        elif ch == "@":
            new_line += "@."
        else:
            new_line += ch
    grid.append(list(new_line))
R = len(grid)
C = len(grid[0])
robot = None
for i in range(R):
    for j in range(0, C, 2):
        if grid[i][j] == "@":
            robot = (i, j)
            break
    if robot is not None:
        break
dirs = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}
for m in moves:
    if m not in dirs:
        continue
    dr, dc = dirs[m]
    r, c = robot
    if dc != 0:
        nr, nc = r, c + 2 * dc
    else:
        nr, nc = r + dr, c
    if not (0 <= nr < R and 0 <= nc < C):
        continue
    dcell = grid[nr][nc]
    if dcell == "#":
        continue
    if dcell == ".":
        grid[r][c] = "."
        grid[r][c + 1] = "."
        grid[nr][nc] = "@"
        grid[nr][nc + 1] = "."
        robot = (nr, nc)
        continue
    if dcell in "[]":
        if dcell == "[":
            box_left = nc
        else:
            box_left = nc - 1
        chain = []
        if dr == 0:
            cur = box_left
            while (
                cur >= 0
                and cur + 1 < C
                and grid[nr][cur] == "["
                and grid[nr][cur + 1] == "]"
            ):
                chain.append((nr, cur))
                cur += 2 * dc
        else:
            rcur = nr
            while (
                0 <= rcur < R
                and grid[rcur][box_left] == "["
                and grid[rcur][box_left + 1] == "]"
            ):
                chain.append((rcur, box_left))
                rcur += dr
        if not chain:
            continue
        can_push = True
        if dr == 0:
            far_r, far_c = chain[-1]
            dest_c = far_c + 2 * dc
            if (
                dest_c < 0
                or dest_c + 1 >= C
                or grid[far_r][dest_c] != "."
                or grid[far_r][dest_c + 1] != "."
            ):
                can_push = False
        else:
            far_r, far_c = chain[-1]
            dest_r = far_r + dr
            if (
                dest_r < 0
                or dest_r >= R
                or grid[dest_r][far_c] != "."
                or grid[dest_r][far_c + 1] != "."
            ):
                can_push = False
        if not can_push:
            continue
        newpos = [None] * len(chain)
        if dr == 0:
            far_r, far_c = chain[-1]
            newpos[-1] = (far_r, far_c + 2 * dc)
            for i in range(len(chain) - 2, -1, -1):
                newpos[i] = chain[i + 1]
        else:
            far_r, far_c = chain[-1]
            newpos[-1] = (far_r + dr, far_c)
            for i in range(len(chain) - 2, -1, -1):
                newpos[i] = chain[i + 1]
        for br, bc in chain:
            grid[br][bc] = "."
            grid[br][bc + 1] = "."
        for old_box, new_box in zip(chain, newpos):
            rr, cc = new_box
            grid[rr][cc] = "["
            grid[rr][cc + 1] = "]"
        grid[r][c] = "."
        grid[r][c + 1] = "."
        target_tile = chain[0][1]
        grid[nr][target_tile] = "@"
        grid[nr][target_tile + 1] = "."
        robot = (nr, target_tile)
s = 0
for i in range(R):
    j = 0
    while j < C - 1:
        if grid[i][j] == "[" and grid[i][j + 1] == "]":
            s += 100 * i + j
            j += 2
        else:
            j += 1
print(s)
