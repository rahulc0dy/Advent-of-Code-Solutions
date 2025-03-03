"""
--- Part Two ---
As you go to win the first prize, you discover that the claw is nowhere near where you expected it would be. Due to a unit conversion error in your measurements, the position of every prize is actually 10000000000000 higher on both the X and Y axis!

Add 10000000000000 to the X and Y position of every prize. After making this change, the example above would now look like this:

Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=10000000008400, Y=10000000005400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=10000000012748, Y=10000000012176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=10000000007870, Y=10000000006450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=10000000018641, Y=10000000010279
Now, it is only possible to win a prize on the second and fourth claw machines. Unfortunately, it will take many more than 100 presses to do so.

Using the corrected prize coordinates, figure out how to win as many prizes as possible. What is the fewest tokens you would have to spend to win all possible prizes?
"""

import re

with open("input.txt", "r") as f:
    blocks = f.read().strip().split("\n\n")

offset = 10_000_000_000_000


def solve_machine(machine_text):
    numbers = list(map(int, re.findall(r"\d+", machine_text)))
    if len(numbers) != 6:
        return 0
    ax, ay, bx, by, px, py = numbers
    px += offset
    py += offset
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
