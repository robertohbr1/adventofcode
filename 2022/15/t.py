from rich import print

# cal = open('input2.txt', 'r', encoding='utf-8').read().strip().split('\n')
# nY = 10
# nTurn2_Range = 20
cal = open('input.txt', 'r', encoding='utf-8').read().strip().split('\n')
nY = 2000000
nTurn2_Range = 4000000

nTurn2_Mult = 4000000


def RetInt(txt):
    return int(txt.replace('x=', '').replace('y=', '')[:-1])


def manhattan(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)


vPos = []

mx, nx = 0, 0
for txt in cal:
    _, _, sx, sy, _, _, _, _, bx, by = txt.split(' ')
    sx = RetInt(sx)
    sy = RetInt(sy)
    bx = RetInt(bx)
    by = RetInt(by + ':')
    vPos.append([sx, sy, bx, by, manhattan(sx, sy, bx, by)])
    mx = max(mx, max(bx, sx))
    nx = min(nx, min(bx, sx))

nx = nx * -1


def Fatia(nY):
    fatia = [' ' for x in range(mx + nx)]

    for txt in vPos:
        sx, sy, bx, by, d = txt
        sx += nx
        bx += nx

        if sy - d <= nY and sy + d >= nY:
            i = d - abs(sy - nY) + 1

            while sx + i > len(fatia):
                fatia.append(' ')

            for x in range(sx - i + 1, sx + i):
                if fatia[x] == ' ':
                    fatia[x] = '#'

        if by == nY:
            fatia[bx] = 'B'

    return ''.join(x for x in fatia)


txt = Fatia(nY)
txt = txt.replace(' ', '').replace('B', '')
print('Turn 1', len(txt))  # 4919281


def Busca2():
    for x in range(nTurn2_Range):
        y = 0
        while y < nTurn2_Range:
            dSum = 0
            for txt in vPos:
                sx, sy, _, _, dist = txt
                if manhattan(sx, sy, x, y) <= dist:
                    dSum = max(dSum, dist - abs(sx - x) + sy)
            if dSum == 0:
                return x, y
            y = dSum + 1

    return 0, 0


x, y = Busca2()
print('Turn 2', x, y, x * nTurn2_Mult + y)  # 12630143363767
