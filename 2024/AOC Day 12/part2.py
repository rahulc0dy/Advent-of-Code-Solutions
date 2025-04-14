# https://adventofcode.com/2024/day/12#part2

# ! DOES NOT WORK


def read_grid(filename):
    with open(filename, "r") as f:
        return [line.rstrip("\n") for line in f if line.rstrip("\n")]


def get_neighbors(r, c, nrows, ncols):
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < nrows and 0 <= nc < ncols:
            yield nr, nc


def flood_fill(grid, start_r, start_c, visited):
    nrows, ncols = len(grid), len(grid[0])
    letter = grid[start_r][start_c]
    region = set()
    stack = [(start_r, start_c)]
    while stack:
        r, c = stack.pop()
        if (r, c) in visited:
            continue
        visited.add((r, c))
        region.add((r, c))
        for nr, nc in get_neighbors(r, c, nrows, ncols):
            if grid[nr][nc] == letter and (nr, nc) not in visited:
                stack.append((nr, nc))
    return region


def count_sides(region):
    cells_by_row = {}
    cells_by_col = {}

    for r, c in region:
        cells_by_row.setdefault(r, []).append(c)
        cells_by_col.setdefault(c, []).append(r)

    horizontal_sides = 0
    for r, cols in cells_by_row.items():
        cols.sort()

        groups = []
        current_group = [cols[0]]

        for c in cols[1:]:
            if c == current_group[-1] + 1:
                current_group.append(c)
            else:
                groups.append(current_group)
                current_group = [c]

        groups.append(current_group)

        horizontal_sides += len(groups) * 2

    vertical_sides = 0
    for c, rows in cells_by_col.items():
        rows.sort()

        groups = []
        current_group = [rows[0]]

        for r in rows[1:]:
            if r == current_group[-1] + 1:
                current_group.append(r)
            else:
                groups.append(current_group)
                current_group = [r]

        groups.append(current_group)

        vertical_sides += len(groups) * 2

    return (horizontal_sides + vertical_sides) // 2


def bulk_fence_price(region):
    area = len(region)
    sides = count_sides(region)
    return area * sides


def solve_bulk_fence_price(filename):
    grid = read_grid(filename)
    nrows, ncols = len(grid), len(grid[0])
    visited = set()
    total_price = 0
    for r in range(nrows):
        for c in range(ncols):
            if (r, c) in visited:
                continue
            region = flood_fill(grid, r, c, visited)
            total_price += bulk_fence_price(region)
    return total_price


answer = solve_bulk_fence_price("input.txt")
print("The new total price of fencing all regions is:", answer)
