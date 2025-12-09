from functools import cache
import time
from collections import deque, defaultdict

time_start = time.perf_counter()

Sample = False
if Sample:
    minDist = 1
    file = "inputsample.txt"
else:
    minDist = 100
    file = "input.txt"

cal = open(file, "r", encoding="utf-8").read().split("\n")

total1 = total2 = 0

mat = []
for i in cal:
    mat.append(list(i))

# find S  in mat and return their position
for i in range(len(mat)):
    for j in range(len(mat[i])):
        if mat[i][j] == 'S':
            y, x = i, j
            break

dists = {}
n = 0
while True:
    dists[(y, x)] = n
    if mat[y][x] == "E":
        break
    for ndr, ndc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if (y + ndr, x + ndc) not in dists and mat[y + ndr][x + ndc] != "#":
            y += ndr
            x += ndc
            n += 1
            break

#cache
def Calc(calcDist):
    dif = defaultdict(int)
    for pos in dists:
        y, x = pos
        n = dists[pos]
        for len_cheat in range(2, calcDist + 1):
            for dy in range(len_cheat + 1):
                dx = len_cheat - dy
                for y2, x2 in set(
                        [
                            (y + dy, x + dx),
                            (y + dy, x - dx),
                            (y - dy, x + dx),
                            (y - dy, x - dx),
                        ]
                    ):        
                    if (y2, x2) in dists:
                        d = dists[(y2, x2)] - n - len_cheat
                        if d >= minDist:
                            dif[d] += 1

    return sum(c for c in dif.values())

total1 = Calc(2)

print('Answer 1: ', total1) # 1389

total2 = Calc(20)

print('Answer 2: ', total2) # 1005068

print(f'Total Time: {time.perf_counter() - time_start}')
