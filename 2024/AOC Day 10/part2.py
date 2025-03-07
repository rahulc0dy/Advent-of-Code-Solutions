# https://adventofcode.com/2024/day/10#part2

with open("input.txt", "r") as file:
    topographic_map = [list(map(int, line.strip())) for line in file]


def count_trails(x: int, y: int, cache: dict[tuple[int, int], int]) -> int:
    if (x, y) in cache:
        return cache[(x, y)]
    if topographic_map[x][y] == 9:
        return 1
    total = 0
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(topographic_map) and 0 <= ny < len(topographic_map[0]):
            if topographic_map[nx][ny] == topographic_map[x][y] + 1:
                total += count_trails(nx, ny, cache)
    cache[(x, y)] = total
    return total


total_rating = 0
cache: dict[tuple[int, int], int] = {}
for i in range(len(topographic_map)):
    for j in range(len(topographic_map[0])):
        if topographic_map[i][j] == 0:
            total_rating += count_trails(i, j, cache)

print(total_rating)
