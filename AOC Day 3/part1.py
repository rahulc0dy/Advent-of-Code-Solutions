import re

with open("input.txt", "r") as file:
    data = file.read()

pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

matches = re.findall(pattern, data)

total = 0

for x_str, y_str in matches:
    total += int(x_str) * int(y_str)

print(total)
