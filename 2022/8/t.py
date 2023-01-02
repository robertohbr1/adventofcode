cal = open('input.txt', 'r', encoding='utf-8').read().strip().split('\n')

size = 99


def RetLin(L, C, i, f):
    for x in range(i, f):
        if cal[L][x] >= cal[L][C]:
            return False
    return True


def RetCol(L, C, i, f):
    for x in range(i, f):
        if cal[x][C] >= cal[L][C]:
            return False
    return True


def Ret(L, C):
    if RetLin(L, C, 0, C):
        return 1
    if RetLin(L, C, C + 1, size):
        return 1
    if RetCol(L, C, 0, L):
        return 1
    if RetCol(L, C, L + 1, size):
        return 1
    return 0


t = 0
for x in range(size):
    if x == 0 or x == size - 1:
        t += size
    else:
        for y in range(size):
            if y == 0 or y == size - 1:
                t += 1
            else:
                t += Ret(x, y)

print('Resposta 1: ', t)


def RetLinM(L, C, i, f, st):
    s = 0
    for x in range(i, f, st):
        s += 1
        if cal[L][x] >= cal[L][C]:
            break
    return s


def RetColM(L, C, i, f, st):
    s = 0
    for x in range(i, f, st):
        s += 1
        if cal[x][C] >= cal[L][C]:
            break
    return s


def RetMult(L, C):
    return RetLinM(L, C, C - 1, -1, -1) * RetLinM(L, C, C + 1, size, 1) * RetColM(L, C, L - 1, -1, -1) * RetColM(L, C, L + 1, size, 1)


t = 0
for x in range(1, size - 1):
    for y in range(1, size - 1):
        t = max(t, RetMult(x, y))

print('Resposta 2: ', t)
