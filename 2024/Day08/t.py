import time

time_start = time.perf_counter()

cal = open("input.txt", "r", encoding="utf-8").read().split("\n")

total1 = total2 = 0

mat = []
for lin in cal:    
    mat.append(list(lin))

h = len(mat)
w = len(mat[0])

ant1 = set()
ant2 = set()

def antAdd(ant, y, x):
    if 0 <= x < w and 0 <= y < w:
        ant.add((y, x))
        return True
    return False

def antAddRecur(ant, y, x, ny, nx):
    if antAdd(ant, y, x):
        antAddRecur(ant, y + ny, x + nx, ny, nx)

def CountPos(vL, vet):
    if len(vet) == 0:
        return
    for vR in vet:
        nx = vL[0] - vR[0]
        ny = vL[1] - vR[1]

        antAdd(ant1, vL[1] + ny, vL[0] + nx)
        antAdd(ant1, vR[1] - ny, vR[0] - nx)

        antAddRecur(ant2, vL[1], vL[0], ny, nx)
        antAddRecur(ant2, vR[1], vR[0], -ny, -nx)
    
    CountPos(vet[0], vet[1:])


pos = []
for y, vet in enumerate(mat):
    for x, c in enumerate(vet):
        if c != '.':
            for k, v in enumerate(pos):
                if v[0] == c:
                    break
            else:
                k = len(pos)
                pos.append([c, []])

            pos[k][1].append([x, y])

for vet in pos:
    CountPos(vet[1][0], vet[1][1:])

total1 = len(ant1)
print('Answer 1: ', total1) # 278

total2 = len(ant2)
print('Answer 2: ', total2) # 1067

print(f'Total Time: {time.perf_counter() - time_start}')
