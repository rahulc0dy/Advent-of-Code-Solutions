import re

with open("input.txt", "r") as file:
    data = file.read()

pattern = r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)"

total = 0
enabled = True

for match in re.finditer(pattern, data):
    token = match.group(0)
    if token == "do()":
        enabled = True
    elif token == "don't()":
        enabled = False
    elif token.startswith("mul("):
        if enabled:
            x = int(match.group(1))
            y = int(match.group(2))
            total += x * y

print(total)
