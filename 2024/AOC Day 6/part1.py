# https://adventofcode.com/2024/day/6

mapArea = []

with open("input.txt", "r") as file:
    for i, line in enumerate(file):
        row = list(line.strip())
        mapArea.append(row)

        if "^" in row:
            guardPos = (i, row.index("^"))

dir = (-1, 0)

visited = set()
visited.add(guardPos)

while True:
    new_i = guardPos[0] + dir[0]
    new_j = guardPos[1] + dir[1]

    if not (0 <= new_i < len(mapArea) and 0 <= new_j < len(mapArea[0])):
        break

    if mapArea[new_i][new_j] == "#":
        dir = (dir[1], -dir[0])
    else:
        mapArea[guardPos[0]][guardPos[1]] = "X"
        guardPos = (new_i, new_j)
        visited.add(guardPos)

total = len(visited)

print(f"{total = }")
