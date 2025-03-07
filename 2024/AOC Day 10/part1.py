# https://adventofcode.com/2024/day/10

with open("input.txt", "r") as file:
    topographic_map = [list(map(int, line.strip())) for line in file]


def trace_trail(x: int, y: int) -> set[tuple[int, int]]:
    if topographic_map[x][y] == 9:
        return {(x, y)}

    endpoints = set()
    for direction_x, direction_y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_x, new_y = x + direction_x, y + direction_y
        if 0 <= new_x < len(topographic_map) and 0 <= new_y < len(topographic_map[0]):
            if topographic_map[new_x][new_y] == topographic_map[x][y] + 1:
                endpoints |= trace_trail(new_x, new_y)
    return endpoints


total = 0
for i in range(len(topographic_map)):
    for j in range(len(topographic_map[0])):
        if topographic_map[i][j] == 0:
            endpoints = trace_trail(i, j)
            total += len(endpoints)

print(f"Total Score: {total}")
