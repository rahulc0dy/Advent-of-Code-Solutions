# https://adventofcode.com/2024/day/20

from collections import deque

with open("input.txt", "r") as file:
    track_map = [list(line.rstrip("\n")) for line in file]

rows = len(track_map)
cols = len(track_map[0]) if rows > 0 else 0

S = None
E = None
for i in range(rows):
    for j in range(cols):
        if track_map[i][j] == "S":
            S = (i, j)
        elif track_map[i][j] == "E":
            E = (i, j)

if S is None or E is None:
    raise ValueError("Could not find start (S) or end (E) in the input.")


def bfs(start):
    dist = [[None] * cols for _ in range(rows)]
    queue = deque()
    si, sj = start
    dist[si][sj] = 0
    queue.append((si, sj))
    while queue:
        i, j = queue.popleft()
        for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < rows and 0 <= nj < cols:
                if track_map[ni][nj] != "#" and dist[ni][nj] is None:
                    dist[ni][nj] = dist[i][j] + 1
                    queue.append((ni, nj))
    return dist


distS = bfs(S)
distE = bfs(E)

if distS[E[0]][E[1]] is None:
    raise ValueError("E is not reachable from S by normal means.")

base_time = distS[E[0]][E[1]]

cheats = set()

for i in range(rows):
    for j in range(cols):
        if track_map[i][j] == "#" or distS[i][j] is None:
            continue
        start_time = distS[i][j]
        for d1 in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            inter_i = i + d1[0]
            inter_j = j + d1[1]
            if not (0 <= inter_i < rows and 0 <= inter_j < cols):
                continue
            for d2 in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                cheat_end_i = inter_i + d2[0]
                cheat_end_j = inter_j + d2[1]
                if not (0 <= cheat_end_i < rows and 0 <= cheat_end_j < cols):
                    continue
                if track_map[cheat_end_i][cheat_end_j] == "#":
                    continue
                if distE[cheat_end_i][cheat_end_j] is None:
                    continue

                cheat_time = start_time + 2 + distE[cheat_end_i][cheat_end_j]
                saving = base_time - cheat_time
                if saving >= 100:
                    cheats.add(((i, j), (cheat_end_i, cheat_end_j)))

print(len(cheats))
