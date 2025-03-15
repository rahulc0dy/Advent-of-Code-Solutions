# https://adventofcode.com/2024/day/25


def compute_lock_heights(block):
    H = len(block)
    W = len(block[0])
    heights = []
    for j in range(W):
        count = 0
        for i in range(1, H):
            if block[i][j] == "#":
                count += 1
            else:
                break
        heights.append(count)
    return heights


def compute_key_heights(block):
    H = len(block)
    W = len(block[0])
    heights = []
    for j in range(W):
        for i in range(H):
            if block[i][j] == "#":
                heights.append((H - 1) - i)
                break
    return heights


def parse_input(filename):
    with open(filename, "r") as f:
        content = f.read().strip()

    blocks = [block.splitlines() for block in content.split("\n\n") if block.strip()]

    locks = []
    keys = []
    for block in blocks:
        if all(ch == "#" for ch in block[0]) and all(ch == "." for ch in block[-1]):
            locks.append(compute_lock_heights(block))
        elif all(ch == "." for ch in block[0]) and all(ch == "#" for ch in block[-1]):
            keys.append(compute_key_heights(block))
        else:

            pass
    return locks, keys, len(blocks[0])


locks, keys, num_rows = parse_input("input.txt")

available = num_rows - 2

count = 0
for lock in locks:
    for key in keys:
        if all(l + k <= available for l, k in zip(lock, key)):
            count += 1
print(count)
