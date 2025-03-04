"""
--- Part Two ---
During the bathroom break, someone notices that these robots seem awfully similar to ones built and used at the North Pole. If they're the same type of robots, they should have a hard-coded Easter egg: very rarely, most of the robots should arrange themselves into a picture of a Christmas tree.

What is the fewest number of seconds that must elapse for the robots to display the Easter egg?
"""

import numpy as np
import re


def parse_input(filename):
    data = []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            m = re.match(r"p=(-?\d+),(-?\d+)\s+v=(-?\d+),(-?\d+)", line)
            if m:
                data.append(tuple(map(int, m.groups())))
    return np.array(data)


def circular_variance(values, modulus):
    angles = 2 * np.pi * values / modulus
    R = np.sqrt(np.sum(np.cos(angles)) ** 2 + np.sum(np.sin(angles)) ** 2) / len(values)
    return 1 - R


data = parse_input("input.txt")
x0 = data[:, 0]
y0 = data[:, 1]
vx = data[:, 2]
vy = data[:, 3]

width = 101
height = 103

best_t = None
best_metric = float("inf")
best_x = None
best_y = None

for t in range(10403):
    x = (x0 + vx * t) % width
    y = (y0 + vy * t) % height
    metric = circular_variance(x, width) + circular_variance(y, height)
    if metric < best_metric:
        best_metric = metric
        best_t = t
        best_x = x.copy()
        best_y = y.copy()

print("Christmas tree appears at t =", best_t)

grid = np.full((height, width), ".", dtype="<U1")
for xi, yi in zip(best_x, best_y):
    grid[int(yi), int(xi)] = "#"
print("\n".join("".join(row) for row in grid))
