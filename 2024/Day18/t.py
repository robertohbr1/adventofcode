from functools import cache
import time
from collections import deque

time_start = time.perf_counter()

Sample = False
if Sample:
    h = w = xs = ys = 6
    limit = 12
    sFile = "inputsample.txt"
else:
    h = w = xs = ys = 70
    limit = 1024
    sFile = "input.txt"

cal = open(sFile, "r", encoding="utf-8").read().split("\n")

total1 = total2 = 0

vErr = []
for c in cal:
    x, y = map(int, c.split(','))
    vErr.append((y, x))

def Busca(limit):
    queue = deque([(0, 0, 0)])
    v = set()
    while queue:
        y, x, cost = queue.popleft()
        if (y, x) in v:
            continue
        v.add((y, x))
        if x == xs and y == ys:
            return cost
        for ny, nx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if 0 <= y + ny <= h and 0 <= x + nx <= w and (y + ny, x + nx) not in v and (y + ny, x + nx) not in vErr[:limit]:
                queue.append((y + ny, x + nx, cost + 1))
    return -1
            
total1 = Busca(limit)

lo, hi = limit + 1, len(vErr) - 1
while lo < hi:
    mid = (lo + hi) // 2
    if Busca(mid + 1) != -1:
        lo = mid + 1
    else:
        hi = mid
total2 = f'{vErr[lo][1]},{vErr[lo][0]}'

print('Answer 1: ', total1) # 298
print('Answer 2: ', total2) # 52,32

print(f'Total Time: {time.perf_counter() - time_start}')
