# https://adventofcode.com/2024/day/19

designs: list[str] = []

with open("input.txt") as file:
    first_line = file.readline()
    available_patterns = set(list(first_line.strip().split(", ")))
    file.readline()
    for line in file:
        designs.append(line.strip())


def is_design_possible(design: str, patterns: set[str]) -> bool:
    if not design:
        return True
    for i in range(1, len(design) + 1):
        if design[:i] in patterns and is_design_possible(design[i:], patterns):
            return True
    return False


total_possible: int = 0

for design in designs:
    if is_design_possible(design, available_patterns):
        total_possible += 1

print(f"{ total_possible = }")
