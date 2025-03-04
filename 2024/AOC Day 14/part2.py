"""
--- Part Two ---
During the bathroom break, someone notices that these robots seem awfully similar to ones built and used at the North Pole. If they're the same type of robots, they should have a hard-coded Easter egg: very rarely, most of the robots should arrange themselves into a picture of a Christmas tree.

What is the fewest number of seconds that must elapse for the robots to display the Easter egg?
"""

# width = 101
# height = 103
# iterations = 2
# robot_map: list[tuple[int, int, int, int]] = []

# with open("input.txt", "r") as file:
#     for line in file:
#         pos, vel = line.strip().split()
#         x, y = pos.split("=")[1].split(",")
#         vel_x, vel_y = vel.split("=")[1].split(",")
#         robot_map.append((int(x), int(y), int(vel_x), int(vel_y)))

# space: list[list[int]] = [[0 for _ in range(width)] for _ in range(height)]
# first = second = third = fourth = 0

# for pos_x, pos_y, x_vel, y_vel in robot_map:
#     final_x = (pos_x + iterations * x_vel) % width
#     final_y = (pos_y + iterations * y_vel) % height
#     if final_x < 0:
#         final_x += width
#     if final_y < 0:
#         final_y += height

#     space[final_y][final_x] += 1

# for row in space:
#     print("".join(map(str, row)))

import re

width = 101
height = 103
robot_map: list[tuple[int, int, int, int]] = []
with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        if not line:
            continue
        m = re.match(r"p=(-?\d+),(-?\d+)\s+v=(-?\d+),(-?\d+)", line)
        if m:
            x, y, vx, vy = map(int, m.groups())
            robot_map.append((x, y, vx, vy))

tree_pattern = {
    (49, 51),
    (50, 51),
    (51, 51),
    (48, 52),
    (49, 52),
    (50, 52),
    (51, 52),
    (52, 52),
}


def simulate(t: int) -> set[tuple[int, int]]:
    positions = set()
    for pos_x, pos_y, x_vel, y_vel in robot_map:
        final_x = (pos_x + t * x_vel) % width
        final_y = (pos_y + t * y_vel) % height
        positions.add((final_x, final_y))
    return positions


t = 0
while True:
    t += 1
    positions = simulate(t)
    if tree_pattern.issubset(positions):
        print("Christmas tree appears at t =", t)
        break

space: list[list[str]] = [["." for _ in range(width)] for _ in range(height)]
for x, y in positions:
    space[y][x] = "#"

grid_str = "\n".join("".join(row) for row in space)
print(grid_str)
