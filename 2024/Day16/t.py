from functools import cache
import time
import heapq

time_start = time.perf_counter()

cal = open("input.txt", "r", encoding="utf-8").read().split("\n")

total1 = total2 = 0

mat = []
for i in cal:
    mat.append(list(i))

# find S  in mat and return their position
for i in range(len(mat)):
    for j in range(len(mat[i])):
        if mat[i][j] == 'S':
            start = (i, j)
            break

queue = [(0, *start, 0, 1, [start])]
seen = {(*start, 0, 1)}
part1 = None
best_cost = float("inf")
points = set()

while queue:
    cost, r, c, dr, dc, path = heapq.heappop(queue)
    seen.add((r, c, dr, dc))
    if mat[r][c] == "E":
        if not total1:
            total1 = cost
        if cost <= best_cost:
            best_cost = cost
            for point in path:
                points.add(point)
        else:
            break
    if mat[r + dr][c + dc] != "#" and (r + dr, c + dc, dr, dc) not in seen:
        heapq.heappush(
            queue, (cost + 1, r + dr, c + dc, dr, dc, path + [(r + dr, c + dc)])
        )
    for ndr, ndc in [(-dc, dr), (dc, -dr)]:
        if (r, c, ndr, ndc) not in seen and mat[r + ndr][c + ndc] != "#":
            heapq.heappush(queue, (cost + 1000, r, c, ndr, ndc, list(path)))
total2 = len(points) 

print('Answer 1: ', total1) # 130536
print('Answer 2: ', total2) # 1024

print(f'Total Time: {time.perf_counter() - time_start}')
