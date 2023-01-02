from rich import print

cal = open('input.txt', 'r', encoding='utf-8').read().strip().split('\n')

mat = []
mov = []
for txt in cal:
    mat.append([])
    mov.append([])
    y = len(mat) - 1
    for l in txt:
        mat[y].append(ord(l) - ord('a') + 1)
        mov[y].append(-1)
        x = len(mat[y]) - 1
        if l == 'S':
            mat[y][x] = 1
            sx = x
            sy = y
        elif l == 'E':
            mat[y][x] = 26  # ord('z') - ord('a') + 1
            ex = x
            ey = y

x, y = sx, sy
w = len(mat[0]) - 1
h = len(mat) - 1


def teste(x, y, x1, y1):
    global t, alter
    if x1 < 0 or y1 < 0 or x1 > w or y1 > h:
        return

    if mov[y1][x1] != -1:
        return

    if mat[y1][x1] <= mat[y][x] + 1:
        mov[y1][x1] = t + 1
        vLast.append([x1, y1])
    return


def teste4(x, y):
    teste(x, y, x - 1, y)
    teste(x, y, x + 1, y)
    teste(x, y, x, y - 1)
    teste(x, y, x, y + 1)


def Executa():
    global alter, t, vLast
    while mov[ey][ex] == -1:
        vBusca = []
        for v in vLast:
            vBusca.append(v)
        vLast = []
        for v in vBusca:
            teste4(v[0], v[1])
        t += 1
    print(t - 1)


t = 1
mov[sy][sx] = t
vLast = []
vLast.append([sx, sy])

Executa()  # 481

vLast = []
for x in range(w + 1):
    for y in range(h + 1):
        if mat[y][x] == 1:
            mov[y][x] = 1
            vLast.append([x, y])
        else:
            mov[y][x] = -1

t = 1
Executa()  # 480
