"""
--- Part Two ---
The reindeer spends a few minutes reviewing your hiking trail map before realizing something, disappearing for a few minutes, and finally returning with yet another slightly-charred piece of paper.

The paper describes a second way to measure a trailhead called its rating. A trailhead's rating is the number of distinct hiking trails which begin at that trailhead. For example:

.....0.
..4321.
..5..2.
..6543.
..7..4.
..8765.
..9....
The above map has a single trailhead; its rating is 3 because there are exactly three distinct hiking trails which begin at that position:

.....0.   .....0.   .....0.
..4321.   .....1.   .....1.
..5....   .....2.   .....2.
..6....   ..6543.   .....3.
..7....   ..7....   .....4.
..8....   ..8....   ..8765.
..9....   ..9....   ..9....
Here is a map containing a single trailhead with rating 13:

..90..9
...1.98
...2..7
6543456
765.987
876....
987....
This map contains a single trailhead with rating 227 (because there are 121 distinct hiking trails that lead to the 9 on the right edge and 106 that lead to the 9 on the bottom edge):

012345
123456
234567
345678
4.6789
56789.
Here's the larger example from before:

89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
Considering its trailheads in reading order, they have ratings of 20, 24, 10, 4, 1, 4, 5, 8, and 5. The sum of all trailhead ratings in this larger example topographic map is 81.

You're not sure how, but the reindeer seems to have crafted some tiny flags out of toothpicks and bits of paper and is using them to mark trailheads on your topographic map. What is the sum of the ratings of all trailheads?
"""

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
