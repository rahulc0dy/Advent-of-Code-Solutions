# https://adventofcode.com/2024/day/13

import re

with open("input.txt", "r") as f:
    blocks = f.read().strip().split("\n\n")


def solve_machine(machine_text):
    numbers = list(map(int, re.findall(r"\d+", machine_text)))
    if len(numbers) != 6:
        return 0
    ax, ay, bx, by, px, py = numbers
    det = ax * by - ay * bx
    if det == 0:
        return 0
    detA = px * by - py * bx
    detB = ax * py - ay * px
    if detA % det != 0 or detB % det != 0:
        return 0
    A = detA // det
    B = detB // det
    if A * ax + B * bx != px or A * ay + B * by != py:
        return 0
    return A * 3 + B


print(sum(solve_machine(block) for block in blocks))
