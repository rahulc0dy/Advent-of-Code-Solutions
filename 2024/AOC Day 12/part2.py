# https://adventofcode.com/2024/day/12#part2

from collections import deque, defaultdict


def solve_full(input_lines):
    grid = [list(line.rstrip()) for line in input_lines if line.strip()]
    R, C = len(grid), len(grid[0])
    visited = [[False] * C for _ in range(R)]
    regions = []

    for r in range(R):
        for c in range(C):
            if not visited[r][c]:
                ch = grid[r][c]
                region = set()
                q = deque([(r, c)])
                visited[r][c] = True
                while q:
                    i, j = q.popleft()
                    region.add((i, j))
                    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        ni, nj = i + dr, j + dc
                        if (
                            0 <= ni < R
                            and 0 <= nj < C
                            and not visited[ni][nj]
                            and grid[ni][nj] == ch
                        ):
                            visited[ni][nj] = True
                            q.append((ni, nj))
                regions.append(region)

    total = 0
    for region in regions:
        area = len(region)
        edges = []
        for r, c in region:
            if (r - 1, c) not in region:
                edges.append(((r, c), (r, c + 1)))
            if (r + 1, c) not in region:
                edges.append(((r + 1, c), (r + 1, c + 1)))
            if (r, c - 1) not in region:
                edges.append(((r, c), (r + 1, c)))
            if (r, c + 1) not in region:
                edges.append(((r, c + 1), (r + 1, c + 1)))

        horiz = defaultdict(list)
        vert = defaultdict(list)
        for p1, p2 in edges:
            (r1, c1), (r2, c2) = p1, p2
            if r1 == r2:
                start, end = sorted([c1, c2])
                horiz[r1].append((start, end))
            elif c1 == c2:
                start, end = sorted([r1, r2])
                vert[c1].append((start, end))

        def merge_intervals(intervals):
            if not intervals:
                return 0
            intervals.sort()
            merged = []
            cur_start, cur_end = intervals[0]
            for s, e in intervals[1:]:
                if s <= cur_end:
                    cur_end = max(cur_end, e)
                else:
                    merged.append((cur_start, cur_end))
                    cur_start, cur_end = s, e
            merged.append((cur_start, cur_end))
            return len(merged)

        sides = 0
        for row, segs in horiz.items():
            sides += merge_intervals(segs)
        for col, segs in vert.items():
            sides += merge_intervals(segs)

        total += area * sides
    return total


if __name__ == "__main__":
    import sys

    with open("input.txt", "r") as f:
        lines = f.readlines()
    answer = solve_full(lines)
    print(answer)
