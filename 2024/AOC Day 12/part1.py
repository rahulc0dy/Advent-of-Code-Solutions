# https://adventofcode.com/2024/day/12


def solve(garden):
    rows = garden.splitlines()
    H, W = len(rows), len(rows[0])
    visited = [[False] * W for _ in range(H)]
    total_price = 0

    def dfs(i, j, letter):
        stack = [(i, j)]
        region = []
        while stack:
            x, y = stack.pop()
            if x < 0 or x >= H or y < 0 or y >= W:
                continue
            if visited[x][y]:
                continue
            if rows[x][y] != letter:
                continue
            visited[x][y] = True
            region.append((x, y))
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                stack.append((x + dx, y + dy))
        return region

    for i in range(H):
        for j in range(W):
            if not visited[i][j]:
                letter = rows[i][j]
                region = dfs(i, j, letter)
                area = len(region)
                perim = 0
                region_set = set(region)
                for x, y in region:
                    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        if (x + dx, y + dy) not in region_set:
                            perim += 1
                total_price += area * perim

    return total_price


with open("input.txt", "r") as file:
    garden_map = file.read()

print(solve(garden_map))
