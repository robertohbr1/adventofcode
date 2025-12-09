from functools import cache
import time

time_start = time.perf_counter()

cal = open("input.txt", "r", encoding="utf-8").read().split("\n")

total1 = total2 = 0

mat = []

for lin in cal:
    mat.append(list(lin))

h = len(mat)
w = len(mat[0])

visited = set()

@cache
def Busca(y, x, c):
    global vBusca, vSet
    if y < 0 or x < 0 or y >= h or x >= w:
        return 0, 0
    if (y, x) in visited:
        return 0, 0
    if mat[y][x] != c:
        return 0, 0
    
    visited.add((y, x))
    vSet.add((y, x))
    Busca(y, x + 1, c)
    Busca(y + 1, x, c)
    Busca(y, x - 1, c)
    Busca(y - 1, x, c)
    return 



for y in range(h):
    for x in range(w):
        if (y, x) not in visited:
            vSet = set()
            Busca(y, x, mat[y][x])
            t = len(vSet)
            s = len(vSet) * 4
            a = 0
            for vy, vx in vSet:
                nx, ny = 0, -1
                for d in range(4):
                    if (vy + ny, vx + nx) in vSet:
                        s -= 1
                    else: # So, there is no neighbor
# if there is no neighbor (upper or lower), and
# if there is no left neighbor or
# if there is a left neighbor and there is a left neighbor + (upper or lower as first comparison)
                        if ny != 0 and ((vy, vx - 1) not in vSet or ((vy, vx - 1) in vSet and (vy + ny, vx - 1) in vSet)): 
                            a += 1

# if there is no neighbor (left or right), and
# if there is no upper neighbor or
# if there is an upper neighbor and there is an upper neighbor + (left or right as first comparison)
                        elif nx != 0 and ((vy - 1, vx) not in vSet or ((vy - 1, vx) in vSet and (vy - 1, vx + nx) in vSet)): 
                            a += 1
                    nx, ny = -ny, nx
                
            print(mat[y][x], t, s, t * s, a, t * a)
            total1 += t * s
            total2 += t * a

print('Answer 1: ', total1) # 1489582
print('Answer 2: ', total2) # 914966

print(f'Total Time: {time.perf_counter() - time_start}')
