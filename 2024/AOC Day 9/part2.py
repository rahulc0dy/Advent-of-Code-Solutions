"""
--- Part Two ---
Upon completion, two things immediately become clear. First, the disk definitely has a lot more contiguous free space, just like the amphipod hoped. Second, the computer is running much more slowly! Maybe introducing all of that file system fragmentation was a bad idea?

The eager amphipod already has a new plan: rather than move individual blocks, he'd like to try compacting the files on his disk by moving whole files instead.

This time, attempt to move whole files to the leftmost span of free space blocks that could fit the file. Attempt to move each file exactly once in order of decreasing file ID number starting with the file with the highest file ID number. If there is no span of free space to the left of a file that is large enough to fit the file, the file does not move.

The first example from above now proceeds differently:

00...111...2...333.44.5555.6666.777.888899
0099.111...2...333.44.5555.6666.777.8888..
0099.1117772...333.44.5555.6666.....8888..
0099.111777244.333....5555.6666.....8888..
00992111777.44.333....5555.6666.....8888..
The process of updating the filesystem checksum is the same; now, this example's checksum would be 2858.

Start over, now compacting the amphipod's hard drive using this new method instead. What is the resulting filesystem checksum?
"""

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
