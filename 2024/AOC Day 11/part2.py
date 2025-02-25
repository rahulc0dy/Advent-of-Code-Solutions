"""
--- Part Two ---
The Historians sure are taking a long time. To be fair, the infinite corridors are very large.

How many stones would you have after blinking a total of 75 times?
"""

from collections import Counter

with open("input.txt", "r") as file:
    stones = list(map(int, file.read().strip().split()))

stone_counts = Counter(stones)

for i in range(75):
    new_stone_counts: Counter = Counter()

    for number, count in stone_counts.items():
        if number == 0:
            new_stone_counts[1] += count
        else:
            str_number = str(number)
            length = len(str_number)

            if length % 2 == 0:
                mid = length // 2
                left_part = int(str_number[:mid])
                right_part = int(str_number[mid:])
                new_stone_counts[left_part] += count
                new_stone_counts[right_part] += count
            else:
                new_stone_counts[number * 2024] += count

    stone_counts = new_stone_counts

total_stones = sum(stone_counts.values())
print("Number of Stones:", total_stones)
