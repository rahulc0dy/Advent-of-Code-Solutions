# https://adventofcode.com/2024/day/21


def bfs_path(start, target, keypad):
    pos_to_key = {v: k for k, v in keypad.items()}
    start_pos = keypad[start]
    target_pos = keypad[target]

    allowed = set(pos_to_key.keys())

    from collections import deque

    queue = deque()
    queue.append((start_pos, ""))
    visited = {start_pos: ""}

    moves = [("^", (-1, 0)), ("<", (0, -1)), (">", (0, 1)), ("v", (1, 0))]

    while queue:
        pos, path = queue.popleft()
        if pos == target_pos:
            return path
        for move_sym, (dr, dc) in moves:
            new_pos = (pos[0] + dr, pos[1] + dc)
            if new_pos in allowed:
                new_path = path + move_sym
                if new_pos not in visited or new_path < visited[new_pos]:
                    visited[new_pos] = new_path
                    queue.append((new_pos, new_path))
    return None


def cost_and_sequence(target_seq, keypad, initial):
    seq = ""
    current = initial
    for ch in target_seq:
        path = bfs_path(current, ch, keypad)
        seq += path + "A"
        current = ch
    return seq, len(seq)


num_keypad = {
    "7": (0, 0),
    "8": (0, 1),
    "9": (0, 2),
    "4": (1, 0),
    "5": (1, 1),
    "6": (1, 2),
    "1": (2, 0),
    "2": (2, 1),
    "3": (2, 2),
    "0": (3, 1),
    "A": (3, 2),
}

dir_keypad = {"^": (0, 1), "A": (0, 2), "<": (1, 0), "v": (1, 1), ">": (1, 2)}


def overall_cost_for_code(code):
    numeric_part = int(code[:-1])
    # Level 1: type door code on numeric keypad (starting at A)
    S1, L1 = cost_and_sequence(code, num_keypad, "A")
    # Level 2: type S1 on directional keypad (starting at A)
    S2, L2 = cost_and_sequence(S1, dir_keypad, "A")
    # Level 3: type S2 on directional keypad (starting at A)
    S3, L3 = cost_and_sequence(S2, dir_keypad, "A")
    return L3 * numeric_part, (L1, L2, L3, S1, S2, S3)


total_complexity = 0

with open("input.txt", "r") as file:
    codes: list[str] = file.read().splitlines()
print(codes)

for code in codes:
    comp, _ = overall_cost_for_code(code)
    total_complexity += comp

print(f"{ total_complexity = }")
