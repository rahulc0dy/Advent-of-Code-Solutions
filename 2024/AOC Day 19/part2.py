# https://adventofcode.com/2024/day/19#part2

designs: list[str] = []

with open("input.txt") as file:
    first_line = file.readline()
    available_patterns = set(list(first_line.strip().split(", ")))
    file.readline()
    for line in file:
        designs.append(line.strip())


def count_design_ways(
    design: str, patterns: set[str], memo: dict[str, int] | None = None
) -> int:
    if memo is None:
        memo = {}
    if design in memo:
        return memo[design]
    if design == "":
        return 1
    ways = 0
    for i in range(1, len(design) + 1):
        prefix = design[:i]
        if prefix in patterns:
            ways += count_design_ways(design[i:], patterns, memo)
    memo[design] = ways
    return ways


total_possible: int = 0

for design in designs:
    total_possible += count_design_ways(design, available_patterns, None)

print(f"{ total_possible = }")
