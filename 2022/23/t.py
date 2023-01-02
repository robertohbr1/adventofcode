import time

time_start = time.perf_counter()

cal = open('input.txt', 'r', encoding='utf-8').read().splitlines()

N, S, W, E = 0, 1, 2, 3
nDir = 0

vArena = []
vDir = []
nMult = 60
for txt in cal:
    txt = '.' * nMult + txt + '.' * nMult
    vArena.append([t for t in txt])
    vDir.append([-1 for _ in txt])

txt = '.' * len(vArena[0])
for x in range(nMult):
    vArena.insert(0, [t for t in txt])
    vDir.insert(0, [-1 for _ in txt])
    vArena.append([t for t in txt])
    vDir.append([-1 for _ in txt])


vDest = {}


def Clear():
    global vDest
    vDest = {}
    for y in range(len(vDir)):
        for x in range(len(vDir[y])):
            vDir[y][x] = -1


def TestNeighbor(y, x):
    for xd in range(-1, 2):
        for yd in range(-1, 2):
            if xd == 0 and yd == 0:
                continue
            if y + yd >= 0 and y + yd < len(vArena) and x + xd >= 0 and x + xd < len(vArena[0]):
                if vArena[y + yd][x + xd] == '#':
                    return True
    return False


def Test(y, x, n):
    global vDir, vDest
    yd1, yd2, yd3, xd1, xd2, xd3 = y, y, y, x, x, x
    if n == N:
        if yd2 == 0:
            return False
        yd1, yd2, yd3 = y - 1, y - 1, y - 1
        xd1, xd2, xd3 = x - 1, x, x + 1
    if n == S:
        if yd2 == len(vArena):
            return False
        yd1, yd2, yd3 = y + 1, y + 1, y + 1
        xd1, xd2, xd3 = x - 1, x, x + 1
    if n == W:
        if xd2 == 0:
            return False
        yd1, yd2, yd3 = y - 1, y, y + 1
        xd1, xd2, xd3 = x - 1, x - 1, x - 1
    if n == E:
        if xd2 == len(vArena[0]):
            return False
        yd1, yd2, yd3 = y - 1, y, y + 1
        xd1, xd2, xd3 = x + 1, x + 1, x + 1
    if vArena[yd1][xd1] == '#' or vArena[yd2][xd2] == '#' or vArena[yd3][xd3] == '#':
        return False
    vSame = vDest.get((yd2, xd2))
    if vSame:
        vDir[vSame[0]][vSame[1]] = -1
        vDest.pop((yd2, xd2))
        return True
    vDir[y][x] = n
    vDest[(yd2, xd2)] = (y, x)
    return True


def Move():
    global vArena
    for x in vDest.keys():
        vArena[x[0]][x[1]] = '#'
        vArena[vDest[x][0]][vDest[x][1]] = '.'


def CountEmpty():
    global vArena
    xI, yI, xA, yA = 1000, 1000, 0, 0
    for y in range(len(vArena)):
        for x in range(len(vArena[y])):
            if vArena[y][x] == '#':
                xI = min(xI, x)
                xA = max(xA, x)
                yI = min(yI, y)
                yA = max(yA, y)

    nRet = 0
    for y in range(yI, yA + 1):
        for x in range(xI, xA + 1):
            if vArena[y][x] == '.':
                nRet += 1
    return nRet


nCount = 0
bExiste = True
while bExiste:
    nCount += 1
    bExiste = False
    Clear()
    for y in range(len(vArena)):
        for x in range(len(vArena[y])):
            if vArena[y][x] == '#':
                if TestNeighbor(y, x):
                    for z in range(4):
                        if Test(y, x, (nDir + z) % 4):
                            bExiste = True
                            break

    if not bExiste:
        break
    Move()
    nDir = (nDir + 1) % 4
    if nCount == 10:
        print('Round 1:', CountEmpty())  # 4195

print('Round 2:', nCount)  # 1069

print(f'Total Time: {time.perf_counter() - time_start}')
