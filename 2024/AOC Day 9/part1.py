# https://adventofcode.com/2024/day/9

with open("input.txt") as file:
    input_data = file.read().strip()
    disk_map = []
    is_file = True
    file_id = 0
    for data in input_data:
        n = int(data)
        if is_file:
            disk_map.extend([file_id] * n)
            file_id += 1
        else:
            disk_map.extend(["."] * n)
        is_file = not is_file

    while True:
        try:
            free_idx = disk_map.index(".")
        except ValueError:
            break
        file_idx = None
        for i in range(len(disk_map) - 1, free_idx, -1):
            if disk_map[i] != ".":
                file_idx = i
                break
        if file_idx is None or file_idx <= free_idx:
            break
        disk_map[free_idx] = disk_map[file_idx]
        disk_map[file_idx] = "."

checksum = sum(i * int(x) for i, x in enumerate(disk_map) if x != ".")

print(checksum)
