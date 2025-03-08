from collections import deque


def read_input(filename="input.txt"):
    with open(filename, "r") as f:
        return [
            (int(x), int(y))
            for line in f.read().splitlines()
            if line.strip()
            for x, y in [line.split(",")]
        ]


def bfs(start, end, corrupted, max_val=70):
    if start in corrupted or end in corrupted:
        return None
    q = deque([start])
    visited = {start}
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while q:
        x, y = q.popleft()
        if (x, y) == end:
            return True
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if (
                0 <= nx <= max_val
                and 0 <= ny <= max_val
                and (nx, ny) not in corrupted
                and (nx, ny) not in visited
            ):
                visited.add((nx, ny))
                q.append((nx, ny))
    return None


coords = read_input("input.txt")
corrupted = set()
for coord in coords:
    corrupted.add(coord)
    if bfs((0, 0), (70, 70), corrupted) is None:
        print(f"{coord[0]},{coord[1]}")
        break
