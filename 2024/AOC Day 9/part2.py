# https://adventofcode.com/2024/day/9#part2

with open("input.txt") as f:
    input_data = f.read().strip()
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


def move_file(disk_map, file_id):
    idxs = [i for i, x in enumerate(disk_map) if x == file_id]
    if not idxs:
        return
    start, length = idxs[0], len(idxs)
    dest = None
    i = 0
    while i < start:
        if disk_map[i] == ".":
            j = i
            while j < start and disk_map[j] == ".":
                j += 1
            if j - i >= length:
                dest = i
                break
            i = j
        else:
            i += 1
    if dest is not None:
        for i in idxs:
            disk_map[i] = "."
        for i in range(dest, dest + length):
            disk_map[i] = file_id


max_file = max(x for x in disk_map if x != ".")
for fid in range(max_file, -1, -1):
    move_file(disk_map, fid)


checksum = sum(i * int(x) for i, x in enumerate(disk_map) if x != ".")


print(checksum)
