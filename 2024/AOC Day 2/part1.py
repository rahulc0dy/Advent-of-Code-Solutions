# https://adventofcode.com/2024/day/2

file = open("input.txt", "r")

safeData = 0


def check_safe_data(items_list) -> bool:
    numbers = list(map(int, items_list))
    for i in range(len(numbers) - 1):
        if (
            abs(int(numbers[i]) - int(numbers[i + 1])) > 3
            or abs(int(numbers[i]) - int(numbers[i + 1])) < 1
        ):
            return False

    if int(numbers[0]) > int(numbers[1]):
        for i in range(len(numbers) - 1):
            if int(numbers[i]) < int(numbers[i + 1]):
                return False
    else:
        for i in range(len(numbers) - 1):
            if int(numbers[i]) > int(numbers[i + 1]):
                return False

    return True


for line in file:
    dataList = line.strip().split(" ")

    if check_safe_data(dataList):
        safeData += 1

print(safeData)
