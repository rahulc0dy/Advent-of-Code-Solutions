# https://adventofcode.com/2024/day/20


from collections import deque

with open("input.txt", "r") as file:
    track_map = [list(line.strip()) for line in file if line.strip()]

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

reachable_from_S = []
reachable_from_E = []
for i in range(rows):
    for j in range(cols):
        if track_map[i][j] != "#" and distS[i][j] is not None:
            reachable_from_S.append((i, j))
        if track_map[i][j] != "#" and distE[i][j] is not None:
            reachable_from_E.append((i, j))

cheats = set()

max_cheat = 20

for cs in reachable_from_S:
    for ce in reachable_from_E:
        if cs == ce:
            continue
        d = abs(cs[0] - ce[0]) + abs(cs[1] - ce[1])
        if d < 1 or d > max_cheat:
            continue
        cheat_time = distS[cs[0]][cs[1]] + d + distE[ce[0]][ce[1]]
        saving = base_time - cheat_time
        if saving >= 100:
            cheats.add((cs, ce))

print(len(cheats))
