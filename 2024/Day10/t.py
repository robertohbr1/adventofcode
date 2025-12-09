import time

time_start = time.perf_counter()

cal = open("input.txt", "r", encoding="utf-8").read().split("\n")

total1 = total2 = 0

pos9 = set()
visited = set()
h = len(cal) + 2
w = len(cal[0]) + 2

mat = [[-1] * w]
for lin in cal:
    mat.append([*map(int, [-1] + list(lin) + [-1])])
mat.append([-1] * w)

def Conta(y, x, n, isType1, sPath):
    global visited, pos9
    if isType1:
        if (y, x, n) in visited:
            return
        visited.add((y, x, n))
    sx, sy = -1, 0
    for z in range(4):
        if mat[y + sy][x + sx] == n:
            if n == 9:
                if isType1:
                    pos9.add((y + sy, x + sx))
                else:
                    pos9.add(sPath + f'/{y + sy}:{x + sx}')
            else:
                Conta(y + sy, x + sx, n + 1, isType1, sPath + f'/{y + sy}:{x + sx}')
        sx, sy = -sy, sx
    return

def Busca(y, x, isType1):
    global visited, pos9
    pos9 = set()
    visited = set()
    Conta(y, x, 1, isType1, '')
    return len(pos9)

for y in range(1, h - 1):
    for x in range(1, w - 1):
        if mat[y][x] == 0:
            total1 += Busca(y, x, True)
            # print(y, x, len(pos9))
            total2 += Busca(y, x, False)
            # print(y, x, len(pos9))

print('Answer 1: ', total1) # 593
print('Answer 2: ', total2) # 1192

print(f'Total Time: {time.perf_counter() - time_start}')
