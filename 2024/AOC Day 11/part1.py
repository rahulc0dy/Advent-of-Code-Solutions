# https://adventofcode.com/2024/day/11

with open("input.txt", "r") as file:
    stones = list(map(int, file.read().strip().split()))

for i in range(25):
    new_stones = []
    for number in stones:
        if number == 0:
            new_stones.append(1)
        elif len(str(number)) % 2 == 0:
            new_stones.extend(
                [
                    int(str(number)[: len(str(number)) // 2]),
                    int(str(number)[len(str(number)) // 2 :]),
                ]
            )
        else:
            new_stones.append(number * 2024)

    stones = new_stones

print("Number of Stones: ", len(stones))
