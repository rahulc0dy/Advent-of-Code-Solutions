"""
--- Part Two ---
Fortunately, the Elves are trying to order so much fence that they qualify for a bulk discount!

Under the bulk discount, instead of using the perimeter to calculate the price, you need to use the number of sides each region has. Each straight section of fence counts as a side, regardless of how long it is.

Consider this example again:

AAAA
BBCD
BBCC
EEEC
The region containing type A plants has 4 sides, as does each of the regions containing plants of type B, D, and E. However, the more complex region containing the plants of type C has 8 sides!

Using the new method of calculating the per-region price by multiplying the region's area by its number of sides, regions A through E have prices 16, 16, 32, 4, and 12, respectively, for a total price of 80.

The second example above (full of type X and O plants) would have a total price of 436.

Here's a map that includes an E-shaped region full of type E plants:

EEEEE
EXXXX
EEEEE
EXXXX
EEEEE
The E-shaped region has an area of 17 and 12 sides for a price of 204. Including the two regions full of type X plants, this map has a total price of 236.

This map has a total price of 368:

AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA
It includes two regions full of type B plants (each with 4 sides) and a single region full of type A plants (with 4 sides on the outside and 8 more sides on the inside, a total of 12 sides). Be especially careful when counting the fence around regions like the one full of type A plants; in particular, each section of fence has an in-side and an out-side, so the fence does not connect across the middle of the region (where the two B regions touch diagonally). (The Elves would have used the Möbius Fencing Company instead, but their contract terms were too one-sided.)

The larger example from before now has the following updated prices:

A region of R plants with price 12 * 10 = 120.
A region of I plants with price 4 * 4 = 16.
A region of C plants with price 14 * 22 = 308.
A region of F plants with price 10 * 12 = 120.
A region of V plants with price 13 * 10 = 130.
A region of J plants with price 11 * 12 = 132.
A region of C plants with price 1 * 4 = 4.
A region of E plants with price 13 * 8 = 104.
A region of I plants with price 14 * 16 = 224.
A region of M plants with price 5 * 6 = 30.
A region of S plants with price 3 * 6 = 18.
Adding these together produces its new total price of 1206.

What is the new total price of fencing all regions on your map?
"""

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
