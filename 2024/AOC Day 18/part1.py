# https://adventofcode.com/2024/day/18

from collections import deque


def read_input(filename="input.txt"):
    with open(filename, "r") as f:
        lines = f.read().splitlines()
    coords = []
    for line in lines:
        if line.strip():
            x_str, y_str = line.strip().split(",")
            coords.append((int(x_str), int(y_str)))
    return coords


def bfs(start, end, corrupted, max_val=70):
    queue = deque([(start[0], start[1], 0)])
    visited = {start}
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while queue:
        x, y, steps = queue.popleft()
        if (x, y) == end:
            return steps
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx <= max_val and 0 <= ny <= max_val:
                if (nx, ny) in corrupted:
                    continue
                if (nx, ny) in visited:
                    continue
                visited.add((nx, ny))
                queue.append((nx, ny, steps + 1))
    return None


coords = read_input("input.txt")
first_1024 = coords[:1024]
corrupted = set(first_1024)
start = (0, 0)
end = (70, 70)
if start in corrupted or end in corrupted:
    print("No path exists: start or end is corrupted.")
else:
    steps = bfs(start, end, corrupted)
    if steps is None:
        print("No valid path found.")
    else:
        print(steps)
