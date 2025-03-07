# https://adventofcode.com/2024/day/8

grid = []


def parse_input(grid):
    antennas = {}
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell != ".":
                if cell not in antennas:
                    antennas[cell] = []
                antennas[cell].append((x, y))
    return antennas


def find_antinodes(antennas, width, height):
    antinodes = set()

    for freq, locations in antennas.items():
        n = len(locations)

        for i in range(n):
            x1, y1 = locations[i]
            for j in range(i + 1, n):
                x2, y2 = locations[j]

                dx, dy = x2 - x1, y2 - y1

                x3a, y3a = x1 - dx, y1 - dy
                x3b, y3b = x2 + dx, y2 + dy

                if 0 <= x3a < width and 0 <= y3a < height:
                    antinodes.add((x3a, y3a))
                if 0 <= x3b < width and 0 <= y3b < height:
                    antinodes.add((x3b, y3b))

    return antinodes


with open("input.txt", "r") as file:
    for line in file:
        grid.append(line.strip())

antennas = parse_input(grid)
width, height = len(grid[0]), len(grid)
antinodes = find_antinodes(antennas, width, height)
print("Total unique antinode locations:", len(antinodes))
