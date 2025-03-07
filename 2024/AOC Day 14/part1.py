# https://adventofcode.com/2024/day/14

width = 101
height = 103
robot_map: list[tuple[int, int, int, int]] = []

with open("input.txt", "r") as file:
    for line in file:
        pos, vel = line.strip().split()
        x, y = pos.split("=")[1].split(",")
        vel_x, vel_y = vel.split("=")[1].split(",")
        robot_map.append((int(x), int(y), int(vel_x), int(vel_y)))

first = second = third = fourth = 0

for pos_x, pos_y, x_vel, y_vel in robot_map:
    final_x = (pos_x + 100 * x_vel) % width
    final_y = (pos_y + 100 * y_vel) % height
    if final_x < 0:
        final_x += width
    if final_y < 0:
        final_y += height
    if final_x < width // 2 and final_y < height // 2:
        first += 1
    elif final_x > width // 2 and final_y < height // 2:
        second += 1
    elif final_x < width // 2 and final_y > height // 2:
        third += 1
    elif final_x > width // 2 and final_y > height // 2:
        fourth += 1


print(first * second * third * fourth)
