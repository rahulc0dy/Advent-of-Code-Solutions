# https://adventofcode.com/2024/day/8#part2

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

        if n > 1:
            antinodes.update(locations)

        for i in range(n):
            x1, y1 = locations[i]
            for j in range(i + 1, n):
                x2, y2 = locations[j]

                dx, dy = x2 - x1, y2 - y1

                k = -1
                while True:
                    x_next, y_next = x1 + k * dx, y1 + k * dy
                    if 0 <= x_next < width and 0 <= y_next < height:
                        antinodes.add((x_next, y_next))
                    else:
                        break
                    k -= 1

                k = 1
                while True:
                    x_next, y_next = x2 + k * dx, y2 + k * dy
                    if 0 <= x_next < width and 0 <= y_next < height:
                        antinodes.add((x_next, y_next))
                    else:
                        break
                    k += 1

    return antinodes


with open("input.txt", "r") as file:
    for line in file:
        grid.append(line.strip())

antennas = parse_input(grid)
width, height = len(grid[0]), len(grid)
antinodes = find_antinodes(antennas, width, height)
print("Total unique antinode locations:", len(antinodes))
